# -*- coding: utf-8 -*-
import redis,json
import app_demo1.config.config as CONFIG
class Connector():
    def __init__(self):
        self.client = redis.Redis(host=CONFIG.REDIS_HOST,port=CONFIG.REDIS_PORT,db=0)

    def set(self,key,value):
        return self.client.set(key,value)

    def get(self,key):
        return self.client.get(key).decode('utf-8')
    
    def keys(self):
        return self.client.keys()
    
    def hset(self,name,key,value):
        return self.client.hset(name,key,value)
    
    def hget(self,name,key):
        result = self.client.hget(name,key)
        if result:
            return result.decode('utf-8')
        else:
            return None

    def subscribe(self,topic):
        ps = self.client.pubsub()
        ps.subscribe(topic)
        return ps.listen()

    def publish(self,topic,message):
        try:
            self.client.publish(topic,message)
            return True
        except Exception as error:
            print(error)
            return None

if __name__ == '__main__':
    #Connector().set('d1','{"x":100,"y":200}')
    #Connector().hset('car1','target','[200,500]')
    con = Connector()
    #print(re)
    #print(Connector().keys())
   # re = Connector().get('car1').decode('utf-8')
   # print(Connector().hget('car1','target'))

    for item in con.subscribe('topic1'):
        print(item)
        try:
            print(json.loads(item["data"]))
        except Exception as e:
            print(e)


