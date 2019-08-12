class a():
	def __init__(self,name):
		self.s=name

	def aaa(self,x):
		print(x)
		print(self.s)


if __name__ == '__main__':
	m=a('yyy')
	fun = getattr(m,'aaa')
	fun(1)
