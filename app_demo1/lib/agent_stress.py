import argparse
import hashlib
import hmac
import json
import random
import requests
import threading
import time
import paho.mqtt.client as mqtt
import logging
import queue
from collections import defaultdict

shadow_set_reply = queue.Queue()
subdev_login_reply = queue.Queue()
property_post_reply = queue.Queue()
topology_add_reply = queue.Queue()

msg_cnt = queue.Queue()
start_time = 0
agent_msg_cnt = defaultdict(int)

logger = logging.getLogger(__file__)
formatter = logging.Formatter('%(funcName)s-%(lineno)d-%(asctime)s-%(threadName)s-%(levelname)s: %(message)s')
logger.setLevel(level=logging.DEBUG)
filename = "agents_log_" + time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime()) + ".log"
file_handler = logging.FileHandler(filename)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

console_handler = logging.StreamHandler()  # 设置StreamHandler
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.INFO)  # 设置StreamHandler的消息等级
logger.addHandler(console_handler)  # 添加StreamHandler


class BasicDevice(object):
    """
       设备的基类：包含设备基础的三元组属性：productKey，deviceName，deviceSecret

    """

    def __init__(self, productkey, devicename, devicesecret, signmethod="HmacSHA256"):
        """
        设备基类的初始化
        :param productkey: str
        :param devicename: str
        :param devicesecret: str
        """
        self.productKey = productkey
        self.deviceName = devicename
        self.deviceSecret = devicesecret
        self.signMethod = signmethod
        self.authdata = None
        self.msgId = 0
        self.msg_ver = 0

    def mqtt_auth_data(self):
        """通过三元组"""

        authdata = {
            "productKey": self.productKey,
            "deviceName": self.deviceName,
            "clientId": self.productKey + self.deviceName,
            "signmethod": self.signMethod,
            "timestamp": str(int(round(time.time() * 1000)))
        }

        sign_keys = list(authdata.keys())  # Add the sign dict
        sign_keys.sort(
            key=lambda item: item.lower())  # the keys is ordered by first alphabet, and compose the sign content
        sign_content = ""
        for i in sign_keys:
            if i == "signmethod":
                continue
            sign_content += i + str(authdata[i])
        logger.debug(sign_content)
        sign_content = sign_content.encode("utf-8")

        authdata["sign"] = self.sign(sign_content)
        self.authdata = authdata
        return authdata

    def sign(self, content):
        # make signature
        secret_key = bytes.fromhex(self.deviceSecret)
        # logger.debug("BaseDevice->sign" + secret_key.hex())
        if self.signMethod == "HmacSHA1":
            signature = hmac.new(secret_key, content, hashlib.sha1).hexdigest()
        elif self.signMethod == "HmacMD5":
            signature = hmac.new(secret_key, content, hashlib.md5).hexdigest()
        else:
            signature = hmac.new(secret_key, content, hashlib.sha256).hexdigest()
        return signature


class Agent(BasicDevice):
    """
    网关的类，继承了设备的基类和线程类
    """

    def __init__(self, productkey, devicename, devicesecret, signmethod="HmacSHA256", device_num=10):
        """
        网关类的初始化
        """
        super().__init__(productkey, devicename, devicesecret, signmethod)
        self.subDevices = []
        self.sendInterval = 1000  # 单位毫秒
        self.attrNum = 10
        self.authServiceUrl = 'https://corepro.api.fiibeacontest.xyz/test/corepro/auth/mqtt/?X-MicroService-Name=beacon-corepro-deviceauth-sqa&X-NameSpace-Code=coreprosqa'
        self.mqBrokerAddr = '134.175.75.199'
        self.mqBrokerPort = 1883
        self.mqUser = 'fe'
        self.mqPwd = ''
        self.mqclient = mqtt.Client()
        self.subDevicesFlag = True
        self.agent_name = ""

    def get_mqtt_usr_pwd(self):
        """
        获取mqtt connect用的帐号密码
        """
        auth_post = self.mqtt_auth_data()
        res = requests.post(self.authServiceUrl, data=auth_post)
        res_json = res.json()
        usr_pwd = res_json.get('payload')[0]
        self.mqUser = usr_pwd.get("iotId")
        self.mqPwd = usr_pwd.get("iotToken")
        return self.mqUser, self.mqPwd

    def addTopo(self):
        """
        网关向proxy中已有的topic发送消息，告诉proxy该网关现在的topo
        :return:
        """
        logger.debug("add topo ....")
        topic = '/{}/{}/topology/add'.format(self.productKey, self.deviceName)

        params = []
        for device in self.subDevices:
            res_data = device.mqtt_auth_data()
            params.append(res_data)
            self.subdevice_subs(device.productKey, device.deviceName)

        msg = {
            'id': "",
            'params': params
        }
        self.pubMsg(topic, msg)
        res = topology_add_reply.get(timeout=120)
        if 200 == json.loads(res).get("code"):
            logger.debug("add topo success")
        else:
            logger.error("add topo failed")
            raise Exception("add topo failed")

    def loginDevice(self):
        """
        网关向proxy的子设备登录的topic发送消息，告知proxy 登录的设备
        :return:
        """
        logger.info("login device .....")
        topic_subdev = '/{}/{}/subdev/login'.format(self.productKey, self.deviceName)

        for device in self.subDevices:
            res_data = device.mqtt_auth_data()
            msg = {
                'id': "",
                "params": res_data
            }
            logger.debug('login device for [{}/{} ]'.format(device.productKey, device.deviceName))
            self.pubMsg(topic_subdev, msg)
            res = subdev_login_reply.get(timeout=600)
            if 200 == json.loads(res).get("code"):
                logger.debug("subdev/login success")
            else:
                logger.error("subdev/login failed")
                raise Exception("subdev/login failed")
            time.sleep(0.2)
            # clear devide shadow
            subdev_shadow_topic, msg = device.clear_shadow()
            self.pubMsg(subdev_shadow_topic, msg)
            time.sleep(0.2)
            # res = shadow_set_reply.get(timeout=600)
            # if 200 == json.loads(res).get("code"):
            #     logger.debug("shadow_set success")
            # else:
            #     logger.error("shadow_set failed")
            #     raise Exception("shadow_set failed")

        logger.info('login device end')

    def logout_sub_device(self):
        """
        网关向proxy的子设备登录的topic发送消息，告知proxy 登录的设备
        :return:
        """
        logger.info("logout device .....")
        topic_subdev = '/{}/{}/subdev/logout'.format(self.productKey, self.deviceName)

        for device in self.subDevices:
            msg = {
                'id': "",
                "params": {
                    "productKey": device.productKey,
                    "deviceName": device.deviceName
                }
            }
            logger.debug('login device for [{}/{} ]'.format(device.productKey, device.deviceName))
            self.pubMsg(topic_subdev, msg)

        logger.info('logout device end')

    def startSubDevices(self):
        """
        开启子设备的线程，运行device 类的run方法
        :return:
        """
        while self.subDevicesFlag:
            for device in self.subDevices:
                topic, msg = device.property()
                self.pubMsg(topic, msg)
            time.sleep(1)

    def mqtt_on_connect(self):
        def on_connect(client, userdata, flags, rc):
            """
            mqtt 的连接状态
            :param client: mqtt client的客户端
            :param userdata: mqtt 连接需要的用户名和密码信息
            :param flags:
            :param rc: int , 连接的返回值
            :return:
            """
            logger.info("mqtt connected with result code :{}".format(str(rc)))
            client.subscribe("/{}/{}/topology/add/reply".format(self.productKey, self.deviceName))
            client.subscribe('/{}/{}/subdev/login/reply'.format(self.productKey, self.deviceName))
            client.subscribe('/{}/{}/subdev/logout/reply'.format(self.productKey, self.deviceName))

        return on_connect

    @staticmethod
    def mqtt_on_message():
        def on_message(client, userdata, msg):
            res = msg.topic.split("/", 3)[-1]
            if res == "shadow/set/reply":
                logger.debug("********shadow/set/reply" + msg.payload.decode())
                # shadow_set_reply.put(msg.payload.decode())
            elif res == "topology/add/reply":
                topology_add_reply.put(msg.payload.decode())
            elif res == "property/post/reply":
                logger.debug("********property/post/reply" + msg.payload.decode())
                # property_post_reply.put(msg.payload.decode())
            elif res == "subdev/login/reply":
                subdev_login_reply.put(msg.payload.decode())

        return on_message

    def run(self, agent_num, devices_cnt, device_pd_key, device_secure):
        """
        :return:
        """

        logger.debug("start threading")
        while True:
            logger.info("get mqtt username & password")
            try:
                self.get_mqtt_usr_pwd()
                break
            except Exception as e:
                logger.error("get mqtt username & password{}".format(e))
                time.sleep(1)

        self.mqclient = mqtt.Client(client_id=self.productKey + self.deviceName)
        self.mqclient.on_connect = self.mqtt_on_connect()
        self.mqclient.on_message = self.mqtt_on_message()
        self.mqclient.username_pw_set(self.mqUser, self.mqPwd)
        while True:
            try:
                logger.info("connecting mqtt broker")
                self.mqclient.connect(host=self.mqBrokerAddr, port=self.mqBrokerPort)
                break
            except Exception as e:
                logger.error("mqtt connect error")
                time.sleep(1)
        self.mqclient.loop_start()
        # 初始化mqtt client 结束
        start = (agent_num - 1) * devices_cnt + 1
        end = start + devices_cnt
        devices_configs = [(device_pd_key, "DeviceForTest{:04}".format(x), device_secure) for x in
                           range(start, end)]
        for config in devices_configs:
            device = Device(*config)
            self.subDevices.append(device)
        while True:
            try:
                logger.info("addTopo")
                time.sleep(1)
                self.addTopo()
            except Exception as e:
                logger.error("Exception happend: ", str(e))
                time.sleep(1)
                continue
            try:
                logger.info("loginDevice")
                time.sleep(1)
                self.loginDevice()
            except Exception as e:
                logger.error("Exception happend: ", str(e))
                time.sleep(1)
                continue
            try:
                logger.info("startSubDevices")
                time.sleep(1)
                self.startSubDevices()
                self.logout_sub_device()
            except Exception as e:
                logger.error("Exception happend: ", str(e))
                self.logout_sub_device()
                time.sleep(1)

    def pubMsg(self, topic, msg):
        """
        mqtt 发送消息
        :param topic: str，消息送达的topic
        :param msg: json ，需要发送的消息
        :return:
        """
        self.msgId += 1
        try:
            msg["id"] = str(self.msgId)
            logger.debug('pub msg: topic :{} msg:{} '.format(topic, msg))
            # //TODO:发送mqtt 信息
            self.mqclient.publish(topic=topic, payload=json.dumps(msg))
            msg_cnt.put(threading.current_thread().name)
            return self.msgId
        except Exception as e:
            self.msgId -= 1
            logger.error('pub msg failed: {}'.format(str(e)))

    def subdevice_subs(self, productKey, deviceName):
        self.mqclient.subscribe('/{}/{}/shadow/set/reply'.format(productKey, deviceName))
        self.mqclient.subscribe('/{}/{}/shadow/get/reply'.format(productKey, deviceName))
        logger.debug("subscribe shadow get set {}/{}".format(productKey, deviceName))


class Device(BasicDevice):
    """
    设备类
    """

    def __init__(self, productkey, devicename, devicesecret, signmethod="HmacSHA256"):
        """
        设备类的初始化
        """
        super().__init__(productkey, devicename, devicesecret, signmethod)
        self.msgVersion = 0

    def property(self):
        """
        网关向proxy 的设备属性的topic 发送消息，告知proxy现在的设备属性
        :return:
        """
        topic = '/{}/{}/property/post'.format(self.productKey, self.deviceName)
        params = {}
        attrArray = ["light{:02}".format(num) for num in range(1, 51)]
        for s in attrArray:
            params[s] = 120 + random.randint(0, 99)
        self.msgVersion += 1
        msg = {
            'id': "",
            'msg_ver': self.msgVersion,
            'params': params
        }
        return topic, msg

    def clear_shadow(self):
        """
        清除影子设备
        :return:
        """
        topic = "/{}/{}/shadow/set".format(self.productKey, self.deviceName)
        msg = {
            "id": "",
            "params": {}
        }
        return topic, msg


def main():
    """
    proxy 服务器的压测流程
    :return:
    """
    parser = argparse.ArgumentParser(description="123")
    parser.add_argument('--agent_cnt', default=r"2", help="666")
    parser.add_argument('--agent_with_n_devices', default=r"2", help="666")
    parser.add_argument('--productkey_device', default=r"6491013971442184481", help="666")
    parser.add_argument('--securekey_device', default=r"ba37137528b1aeeb5d20098a6372235a25b07da15f2dbe52f1a0d02c838b84f1", help="666")
    args = parser.parse_args()
    print(args)
    agent_cnt = int(args.agent_cnt)
    agent_with_n_devices = int(args.agent_with_n_devices)
    productkey_device = args.productkey_device
    securekey_device = args.securekey_device
    rawdata = ["6491014024004213449", '6491013971442184481',
               'ba37137528b1aeeb5d20098a6372235a25b07da15f2dbe52f1a0d02c838b84f1']
    agents_configs = [(rawdata[0], "GWForTest{:04}".format(x), rawdata[2]) for x in range(1, 101)]
    agents = [Agent(*x) for x in agents_configs]

    mythreads = []
    for i, agent in enumerate(agents[:agent_cnt]):
        i += 1
        t = threading.Thread(target=agent.run, args=(i, agent_with_n_devices, productkey_device, securekey_device),
                             name="GWForTest{:04}".format(i))
        mythreads.append(t)
        # agent.run()
    for myth in mythreads:
        myth.start()
        time.sleep(0.5)

    global start_time
    start_time = time.time()
    ccc = threading.Thread(target=cntmsg)
    ccc.start()
    while True:
        agent_name = msg_cnt.get()
        # logger.info(agent_name)
        agent_msg_cnt[agent_name] = agent_msg_cnt[agent_name] + 1


def cntmsg():
    global start_time
    global agent_msg_cnt
    preview_data = agent_msg_cnt.copy()
    total = 0
    while True:
        time_now = time.time()
        time_diff = time_now - start_time
        if time_diff >= 60:
            start_time = time_now
            logger.info(preview_data)
            for key in preview_data.keys():
                msg_diff = agent_msg_cnt[key] - preview_data[key]
                logger.info("{}: {}/60s,avg {}/1s".format(key, msg_diff, msg_diff / time_diff))
                total += msg_diff
            logger.info("all agents {}/60s,avg {}/1s".format(total, total / time_diff))
            preview_data = agent_msg_cnt.copy()
            total = 0


if __name__ == "__main__":
    main()
