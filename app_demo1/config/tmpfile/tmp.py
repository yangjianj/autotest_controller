import datetime,time,re
str1 = "abc"
xx=re.match("^ab",str1)
print(xx)

str2 = "<nam12>"
yy = re.match("^<(\S*)>$",str2).group(1)
zz = re.match("^(<na).*>$",str2)
print(yy)
print(zz)


def _data_identify(data):
	# type(data) = dict识别输入数据中引用的变量，变量格式<val>
	for item in data:
		try:
			yy = re.match("^<(\S*)>$", data[item]).group(1)
			data[item] = 11
		except Exception as error:
			pass
	return data

ddct = {'name':"<yang>"}
ddct=_data_identify(ddct)
print(ddct)

print(ddct['dd'])