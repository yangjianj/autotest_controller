# -*- coding: utf-8 -*-
from app_demo1.lib.tool import *

class Testcase():
	def __init__(self,steps,operate):
		self.steps = steps
		self.id = steps[0][0]
		self.result = {"result":"passed","steps":[]}
		self.operate = operate
		self.suite_dir = ''
		self.case_dir = ''

	@record_time
	def run(self):
		self.case_dir =create_case_dir(self.suite_dir,self.id)
		self.setup()
		self.runstep()
		self.teardown()
		return self.result

	def runstep(self):
		for step in self.steps:
			if self.result["result"] == "failed" :
				block_result = {"result":"block","message":None}
				self._record_step_result(step,block_result)
				continue
			msg={"action":step[3],"page":step[4],"element":step[5]}
			if step[6] != '':
				msg.update(json.loads(step[6]))
			result = self.operate.execute(msg)
			self._record_step_result(step,result)

	def setup(self):
		pass

	def teardown(self):
		msg = {}
		msg["filepath"] =os.path.join(self.case_dir,"ending_screen.png")
		self.operate.handler.get_screenshot_as_file(msg)

	def log(self):
		pass

	def _record_step_result(self,step,result):
		step[8] = result["result"]
		step[9] = str(result["message"])
		if result["result"] == "failed":
			self._error_handler(step[3])
			self.result["result"] = "failed"
		self.result["steps"].append(step)


	def _error_handler(self,curr_action):
		timestr = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
		msg = {}
		msg["filepath"] = os.path.join(self.case_dir,curr_action+timestr+".png")
		self.operate.handler.get_screenshot_as_file(msg)