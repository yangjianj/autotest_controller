import datetime,time,re
str1 = "abc"
xx=re.match("^ab",str1)
print(xx)

str2 = "<nam12>"
yy = re.match("^<(\S*)>$",str2).group(1)
zz = re.match("^(<na).*>$",str2)
print(yy)
print(zz)

m ="3"
print(eval("3+2"))
print(eval(m))