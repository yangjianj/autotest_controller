# -*- coding: utf-8 -*-
from flask import Flask
import requests,time,datetime
import threading
import config

app= Flask(__name__)

@app.route("/")
def index():
    return '<h1> hello flask !</h1>'

@app.route("/get_json")
def get_json():
    return '{"code": 0,"payload": [{"省份": "湖南省","时间": "2019-07-10",}, {"省份": "湖北省","时间": "2019-07-15", },' \
           '{"省份": "深圳市","时间": "2019-08-02", }, {  "省份": "广东省", "时间": "2019-08-15", }],"errmsg": ""}'

def heartbeat():  #slave心跳
    while(1):
        url = config.master_url
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        data = {'ip':config.ip,'time':timestamp}
        headers = {
            'content-type': "application/json",
        }
        response = requests.request("POST",url,data=data,headers = headers)
        if  response["status"] == "ok":
            pass
        else:
            break
        time.sleep(config.sycle)

def run_cmd():
    pass


if __name__=="__main__":
    threading.Thread(target = heartbeat,args = ()).start()
    app.run(host='0.0.0.0', port=8080, debug=True)