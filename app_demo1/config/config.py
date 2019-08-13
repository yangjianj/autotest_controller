import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASE = os.path.join(BASE_DIR, '../../db.sqlite3')
LOGFILE={"api": os.path.join(BASE_DIR, 'app_demo1\\log\\../log/api_test_log.log'),
         "ui": os.path.join(BASE_DIR, 'app_demo1\\log\\../log/ui_test_log.log')}
Interface_Time_Out = 500

WEBSITE ={"baidu":"http://www.baidu.com","weibo":"https://www.weibo.com/login.php"}
PAGEFILE={"baidu":os.path.join(BASE_DIR, 'app_demo2\\common\\../../app_demo2/common/web_test.yaml'),
"xinlang":os.path.join(BASE_DIR,'app_demo2\\common\\page.yaml'),
}



headers = {}
headers['Content-Type'] = 'application/json; charset=UTF-8'

#图灵apikey,userid81a0447221504656bff04b47d1a8c868
tuling_apikey="81a0447221504656bff04b47d1a8c868"
tuling_userid="363282"
tuling_api="http://openapi.tuling123.com/openapi/api/v2"

tuling_request_data={
    "reqType":0,
    "perception": {
        "inputText": {
            "text": "深圳天气"
        },
        "inputImage": {
            "url": "imageUrl"
        },
        "selfInfo": {
            "location": {
                "city": "深圳",
                "province": "深圳",
                "street": "坂田街道"
            }
        }
    },
    "userInfo": {
        "apiKey": "31532114329044d2a2d8b61203f21a77",
        #"apiKey": "81a0447221504656bff04b47d1a8c868",
        "userId": "1234"
    }
}


#淘宝接口
taobao_url = "http://suggest.taobao.com/sug"
taobao_querystring = {"code":"utf-8","q":"%E9%9E%8B","callback":"cb"}

#物流接口
wl_url="http://www.kuaidi100.com/query"
wl_querystring = {"type":"yunda","postid":"3835494398576"}

method_mapping={'点击':'click',
}