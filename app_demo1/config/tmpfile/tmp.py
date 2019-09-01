import datetime,time,re,random,_ctypes
str1 = "abc"
xx=re.match("^ab",str1)
print(xx)

str2 = "<_dd>+<nam12>"
str3 = "dff"
# yy = re.match("^<(\S*)>$",str2).group(1)
# zz = re.match("^(<na).*>$",str2)
# print(yy)
# print(zz)
pattern=re.compile(r'<[_a-zA-Z0-9]+>')
result1 = pattern.findall(str3)
print(11111111111)
print(result1)

for i in result1:
	print(i.replace('<','').replace('>',''))
tt1 ="<random.randint(1,10)>"
#pattern = re.compile(r'<[()_,\.a-zA-Z0-9]+>')
pattern = re.compile(r'<[^\s<>]+>')
result1 = pattern.findall(tt1)
print(222222222)
print(result1)


