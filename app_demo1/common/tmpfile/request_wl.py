import requests

url = "http://www.kuaidi100.com/query"

querystring = {"type":"yuantong","postid":"11111111111"}
querystring = {"type":"yunda","postid":"3835494398576"}

payload = "{\r\n    \"userInfo\": {\r\n        \"apiKey\": \"31532114329044d2a2d8b61203f21a77\",\r\n        \"userId\": \"485026\"\r\n    }\r\n}"
headers = {
    'Content-Type': "application/json"
    }

print(type(querystring))
response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)