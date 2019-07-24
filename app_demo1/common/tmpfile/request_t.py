import requests

url = "http://suggest.taobao.com/sug"
querystring = {"code":"utf-8","q":"%E8%A1%A3%E6%9C%8D","callback":"cb"}

payload = "{\r\n    \"userInfo\": {\r\n        \"apiKey\": \"31532114329044d2a2d8b61203f21a77\",\r\n        \"userId\": \"485026\"\r\n    }\r\n}"
headers = {
    'Content-Type': "application/json",
    'Host': "suggest.taobao.com",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "113",
    'Connection': "keep-alive"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
print(response.text)