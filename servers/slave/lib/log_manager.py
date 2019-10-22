import logging
import config

class LogManager():
	
	def __init__(self,name):
		self.mylogger = logging.getLogger(name)  #logger 名默认为root
		#self.mylogger.setLevel(level=logging.INFO)  # 设置消息等级为INFO
		self.handler = logging.FileHandler(config.LOGFILE[name],encoding='utf-8')  # FileHandler:日志输出到文件

		formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s: %(message)s')
		self.handler.setFormatter(formatter)  #设置消息格式
		self.mylogger.addHandler(self.handler)  #添加处理器

		#logger.info("Start print log")
		#logger.debug("Do something")
		#logger.warning("Something maybe fail.")
		#logger.info("Finish")
	def _setlevel(self,level):
		pass

	def info(self,info):
		self.handler.setLevel(logging.INFO)
		self.mylogger.info(info)

	def error(self,error):
		self.handler.setLevel(logging.ERROR)
		self.mylogger.error(error)



if __name__ == '__main__':
	loger = LogManager('api')
	loger.info('message 234567890-')
	loger.error('message 234567890-')