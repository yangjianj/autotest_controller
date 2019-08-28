# 自动化测试平台后台代码     
app_demo1 接口测试   
app_demo2 ui测试   

功能：    
1.用户管理：登录控制，增删改查，角色权限控制    (session cookie，装饰器)    
2.测试执行：接口功能测试，性能测试，时间记录             (request，多线程，装饰器)    
3.测试结果展现                               （echarts）    
4.各版本测试数据统计，图标展示                 (mysql,sqlite3,echarts)         
5.失败重试    
6.异步任务执行，定时任务                      （rabbitmq,apscheduler）      
7.缓存                                      （redis）     
8.文件上传+富文本     
9.短信/邮件    

django 命令：
python manage.py runserver 0.0.0.0:8090
python manage.py migrate

ui自动化实现说明：   
1.用例管理：execl写用例 : 一个testsuit对象对应excel表格的一个sheet   
2.yaml记录页面元素信息：页面>元素标志>元素属性（type,value,name,timeout）  
3.testsuit>testcase>teststep = action element page value   
4.关键字驱动：用例中包含不同的关键字，框架需根据关键字匹配对应的执行动作，特点：每个元素操作需要重新封装   
取数据》划分不同case》case区块划分（前置，操作，验证，后置）》操作步骤匹配    
5.数据驱动：一套固定动作（前置，操作，验证，后置）封装成一个unittest case,excel用例中包含每个步骤的数据与预期结果（例如登录框的不同数据验证）   
6.测试用例结构：（setup(开浏览器)-content（测试流程）--teardown（截图，关浏览器））    
7.结果输出：输出测试结果到excel（步骤执行结果，步骤执行信息，case执行时间，suite执行时间）   
8.疑点：步骤取值供下一个步骤使用+suite/case级变量，for循环，if-then-else    
优点：   
1.页面元素信息由yml管理，方便维护    
2.用例中使用元素名在执行后log分析中更直观，不会不理解每个步骤对应哪个元素操作    


api自动化实现说明：   
1.用例管理：excel写用例    
2.执行=》结果校验=》记录存储到数据库

编码原则：  
1.异常处理在函数内部处理，不在多个函数组合时使用   
