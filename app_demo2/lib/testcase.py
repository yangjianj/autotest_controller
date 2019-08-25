# -*- coding: utf-8 -*-
from app_demo1.lib.tool import *

class Testcase():
	def __init__(self,steps,operate):
		self.steps = steps
		self.name = steps[0][0]
		self.result = {"result":"passed","steps":[]}
		self.operate = operate
		self.report_dir = ''

	@record_time
	def run(self):
		self.setup()
		self.runstep()
		self.teardown()
		return self.result

	def runstep(self):
		for step in self.steps:
			msg={"action":step[3],"page":step[4],"element":step[5]}
			if step[6] != '':
				msg.update(json.loads(step[6]))
			result = self.operate.execute(msg)
			self._record_result(step,result)

	def setup(self):
		pass

	def teardown(self):
		msg = {}
		msg["filepath"] =os.path.join(self.report_dir, self.name+"_ending_screen.png")
		self.operate.handler.get_screenshot_as_file(msg)

	def log(self):
		pass

	def _record_result(self,step,result):
		if "passed" in result:
			step[8]="passed"
			step[9]=str(result["passed"])
		else:
			step[8]="failed"
			step[9]=str(result["failed"])
			self.result["result"]="failed"
		self.result["steps"].append(step)