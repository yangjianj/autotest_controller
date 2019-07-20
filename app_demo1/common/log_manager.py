import logging,time
import app_demo1.config as config

class LogManager():
	
	def __init__(self,name,logfile):
		self.mylogger = logging.getLogger(name)  #logger 名默认为root
		self.mylogger.setLevel(level=logging.INFO)  # 设置消息等级为INFO
		handler = logging.FileHandler(config.LOGFILE)  # FileHandler:日志输出到文件
		handler.setLevel(logging.INFO)  
		formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s: %(message)s')
		handler.setFormatter(formatter)  #设置消息格式
		self.mylogger.addHandler(handler)  #添加处理器

		#logger.info("Start print log")
		#logger.debug("Do something")
		#logger.warning("Something maybe fail.")
		#logger.info("Finish")

	def write(self,info):
		self.mylogger.info(info)

if __name__ == '__main__':
	loger = LogManager('loger1','logger1.log')
	loger.write('234567890-')