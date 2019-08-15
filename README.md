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
1.用例管理：execl写用例    
2.yaml记录页面元素信息：页面>元素标志>元素属性（type,value,name,timeout）  
3.testsuit>testcase>teststep = action element page value   
4.关键字驱动：用例中包含不同的关键字，框架需根据关键字匹配对应的执行动作，特点：每个元素操作需要重新封装   
取数据》划分不同case》case区块划分（前置，操作，验证，后置）》操作步骤匹配    
5.数据驱动：一套固定动作（前置，操作，验证，后置）封装成一个unittest case,excel用例中包含每个步骤的数据与预期结果（例如登录框的不同数据验证）   


api自动化实现说明：   
1.用例管理：excel写用例    
2.执行=》结果校验=》记录存储到数据库
