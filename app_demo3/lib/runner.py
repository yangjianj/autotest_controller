import os
import unittest
from HtmlTestRunner import HTMLTestRunner
import app_demo1.config.config as config
import app_demo3.testcases
from app_demo1.lib.log_man import LogManager
#测试结果信息收集：
class Runner():
    def __init__(self):
        #self.logger = LogManager("system")
        pass

    #根据文件名匹配case
    def run_by_pattern(self,casedir,testplan):
        workdir = os.path.join(config.BASE_DIR,"app_demo3")
        casedir = os.path.join(config.BASE_DIR,"app_demo3\\testcases")
        discover = unittest.defaultTestLoader.discover(casedir, pattern="ui_lianjia*.py", top_level_dir=None)
        reportfile = os.path.join(workdir, 'report','htmltestrunner.html')
        with open(reportfile,'wb') as f:
            runner = HTMLTestRunner(stream=f,
                                    verbosity=2,
                                    title='my report',
                                    description='generated by htmltestrunner')
            all_result=runner.run(discover)

        return all_result

    #根据case名匹配case
    def run_by_casename(self,caselist):
        workdir = os.path.join(config.BASE_DIR,"app_demo3")
        caselist = ['lianjia.ui_lianjia_test_001.Base_t1.test_run3','lianjia.ui_lianjia_test_001.Base_t1.test_run']
        discover = unittest.TestLoader().loadTestsFromNames(caselist,module=None)
        reportfile = os.path.join(workdir, 'report','htmltestrunner.html')
        with open(reportfile,'wb') as f:
            runner = HTMLTestRunner(stream=f,
                                    verbosity=2,
                                    title='my report',
                                    description='generated by htmltestrunner')
            all_result=runner.run(discover)

        return all_result

if __name__ == '__main__':
    runner = Runner()
    all_result = runner.run_by_pattern(1,2)
    #all_result = runner.run_by_casename(1)
    #结果编号：0-passed;1-failed;2-error
    for item in all_result.result:
        print(item)