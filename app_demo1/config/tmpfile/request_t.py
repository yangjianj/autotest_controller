from jsonschema import validate
import json
schema = {
 "type" : "object",
 "properties" :
     {  "price" :
            {"type" : "number"},
         "name" :
             {"type" : "string"},
     },
         }

s=validate(instance={"name" : '1234', "price" : 34.99}, schema=schema)
print(s)

try:
    1/0
except Exception as e:
    result = e
    print(result)


print(1111111111)

json.loads('{"ss":112}')
#json.loads("wwwwwww")

#json.loads({"ss":111})
ss='{"type" : "object","properties" :{"price" :{"type" : "number"},"name" :{"type" : "string"}}}'
json.loads(ss)