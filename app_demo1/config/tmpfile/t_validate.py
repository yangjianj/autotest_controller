from jsonschema import validate
import json

cc={'status': 200, 're_data': '123456789'}
template={"type":"object",
          "properties":{
				"re_data":{"type":"string"},
          }
      }

validate(instance=cc, schema=template)
cc='"{\'status\': 200, \'re_data\': \'123456789\'}"'
print(type(json.loads(cc)))