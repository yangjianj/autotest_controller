#-*- coding: utf-8 -*-
import requests,json
from requests import exceptions
import app_demo1.config as config
class Reques():
    def get(self, url,headers,parms):#get消息
        result={}
        try:
            self.r = requests.get(url, headers=headers,params=parms,timeout=config.Interface_Time_Out)
            self.r.encoding = 'UTF-8'
            spend=self.r.elapsed.total_seconds()
            #json_response = json.loads(self.r.text)
            #return (json_response,spend)      #返回响应与总时长（s）
            result["response"] = self.r.text
            result["spend"] = spend
            return (result)
        except exceptions.Timeout :
            return {'get请求出错': "请求超时" }
        except exceptions.InvalidURL:
            return {'get请求出错': "非法url"}
        except exceptions.HTTPError:
            return {'get请求出错': "http请求错误"}
        except Exception as e:
            return {'get请求出错':"错误原因:%s"%e}
    def post(self, url, payload,qstring,headers):#post消息
        #payload(string);qstring(dict)
        result={}
        try:
            self.r =requests.post(url,data=payload,params=qstring,headers=headers,timeout=config.Interface_Time_Out)
            spend = self.r.elapsed.total_seconds()
            #json_response = json.loads(self.r.text)
            result["response"]=self.r.text
            result["spend"]=spend
            return result
        except exceptions.Timeout :
            return {'post请求出错': "请求超时" }
        except exceptions.InvalidURL:
            return {'post请求出错': "非法url"}
        except exceptions.HTTPError:
            return {'post请求出错': "http请求错误"}
        except Exception as e:
            return {'post请求出错': "错误原因:%s" % e}
    def delfile(self,url,params,headers):#删除的请求
        try:
            self.rdel_word=requests.delete(url,data=params,headers=headers,timeout=config.Interface_Time_Out)
            json_response=json.loads(self.rdel_word.text)
            spend=self.rdel_word.elapsed.total_seconds()
            return (json_response,spend)
        except exceptions.Timeout :
            return {'delete请求出错': "请求超时" }
        except exceptions.InvalidURL:
            return {'delete请求出错': "非法url"}
        except exceptions.HTTPError:
            return {'delete请求出错': "http请求错误"}
        except Exception as e:
            return {'delete请求出错': "错误原因:%s" % e}
    def putfile(self,url,params,headers):#put请求
        try:
            self.rdata=json.dumps(params)
            me=requests.put(url,self.rdata,headers=headers,timeout=config.Interface_Time_Out)
            json_response=json.loads(me.text)
            spend=me.elapsed.total_seconds()
            return (json_response,spend)
        except exceptions.Timeout :
            return {'put请求出错': "请求超时" }
        except exceptions.InvalidURL:
            return {'put请求出错': "非法url"}
        except exceptions.HTTPError:
            return {'put请求出错': "http请求错误"}
        except Exception as e:
            return {'put请求出错': "错误原因:%s" % e}