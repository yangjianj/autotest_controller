import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE = os.path.join(BASE_DIR,'db.sqlite3')
LOGFILE = os.path.join(BASE_DIR,'app_demo1\\log\\test.log')
Interface_Time_Out = 500

#图灵apikey,userid
tuling_apikey="81a0447221504656bff04b47d1a8c868"
tuling_userid="363282"
tuling_api="http://openapi.tuling123.com/openapi/api/v2"
headers = {}
headers['Content-Type'] = 'application/json; charset=UTF-8'
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
        "apiKey": "81a0447221504656bff04b47d1a8c868",
        "userId": "363282"
    }
}