自动化测试平台后台代码     
---------------------
app_demo1 接口   
app_demo2 ui测试（废弃）   
app_demo3 ui    

功能：    
-----
1.用户管理：登录控制，增删改查，角色权限控制---(session cookie,django中间件,装饰器)(完成)    
2.后台实现接口测试，ui测试，接口性能    
3.页面添加，编辑，执行测试：接口功能测试，性能测试，时间记录---(request，多线程，装饰器)    
4.各版本测试数据统计，图标展示---(mysql,sqlite3,echarts)         
5.失败重试    
6.异步/分布式任务执行，定时任务---（rabbitmq,apscheduler,master-slave）      
slave功能：作为并发测试成员之一执行测试；单独执行部分测试任务    
7.缓存---（redis）     
8.文件上传+富文本     
9.短信/邮件    
10.日志收集与处理    
11.测试结果展现---（echarts）    


### django 命令：  
django-admin startproject HelloWorld    
python manage.py startapp app_name    
python manage.py runserver 0.0.0.0:8090    
python manage.py makemigrations    
python manage.py migrate    

app_demo1   
========    

### api自动化实现说明：   
    
1.用例管理：excel写用例    
2.执行=》结果校验=》记录存储到数据库    
3.csv比较适合存放测试数据，或数据驱动型用例，不适合步骤多的用例

### 用例：        
1.取excel中测试数据库发送http请求并验证结果    
2.执行api性能测试，设置并发数量，提取返回结果     


app_demo2(废弃-通过excel写ui操作用例实现复杂且灵活性没有代码好)
==============       

### ui自动化实现说明：     
1.用例管理：execl写用例 : 一个testsuit对象对应excel表格的一个sheet   
2.yaml记录页面元素信息：页面>元素标志>元素属性（type,value,name,timeout）  
3.testsuit>testcase>teststep = action element page value   
4.关键字驱动：用例中包含不同的关键字，框架需根据关键字匹配对应的执行动作，特点：每个元素操作需要重新封装   
取数据》划分不同case》case区块划分（前置，操作，验证，后置）》操作步骤匹配    
5.数据驱动：一套固定动作（前置，操作，验证，后置）封装成一个unittest case,excel用例中包含每个步骤的数据与预期结果（例如登录框的不同数据验证）   
6.测试用例结构：（setup(开浏览器)-content（测试流程）--teardown（截图，关浏览器））    
7.结果输出：输出测试结果到excel（步骤执行结果，步骤执行信息，case执行时间，suite执行时间）   
8.疑点：步骤取值供下一个步骤使用+suite/case级变量，变量多样引用，for循环，if-then-else,外部数据引用，字符类型支持    
### 使用说明：   
1.变量赋值与引用（赋值:输出框：name=text；引用:value框：<name>）  
2.支持变量的多样引用<random.randint(1,10)> ,type(<val1>),<val1>[1],<val1>+"name1"   
  
### 优点：   
1.页面元素信息由yml管理，方便维护    
2.用例中使用pagename+元素名在执行后log分析中更直观，不会不理解每个步骤对应哪个元素操作    
  
### 缺点：   
1.相比代码书写灵活性差    
2.花太多时间在解析excel内容来达到python脚本的效果   
改进想法：>app-demo3   
1.保留yml管理元素，去除excel书写用例用代码写用例！！   
2.用例写在unittest中      

app_demo3     
=========    
### 设计说明：        
1.保留app_demo2中yml管理元素的方式，去除excel书写用例用python脚本写用例！！   
2.用例写在unittest中，执行按用例命名规则discover组织suite  
3.输出htmltestrunner文件改进输出到html+存储到数据库（数据已提取待对接mysql）    
4.失败重跑:提取失败用例casename加载重跑

### 用例：   
1.打开页面-点击标签-输入城市值-等待元素出现--ok    
2.获取ul元素子元素个数--遍历子元素下某个标签并输出text--ok     
3.csv中多组数据作为同一方法的输入（ddt）    


### 编码相关：  
1.异常处理在函数内部处理，不在多个函数组合时使用   
2.python导入excel的字符类型种类： 0 --empty,1 --string, 2 --number(都是浮点), 3 --date, 4 --boolean, 5 --error   
3.统一接口数据格式：    
成功:{'status':'success','data':{}};失败:{'status':'fail','message':'失败说明'}

### 问题：
1.分布式执行中slave（通过rabbitmq接收任务）状态监控（非jenkins执行）--python脚本实现主机端口监控--已解决（app_demo1/lib/port_monitor.py）

### 执行结果展示：    
1.UI数据驱动    
1.1[数据驱动_脚本](/app_demo3/testcases/ddt_test/ddt_test_001.py)    
1.2数据驱动_数据![数据驱动_数据](/app_demo3/report/数据驱动_数据.JPG)    
1.3数据驱动_结果![数据驱动_结果](/app_demo3/report/数据驱动_结果.JPG)    
2.UI关键字驱动    
2.1[关键字驱动_脚本](/app_demo3/testcases/lianjia/ui_lianjia_test_001.py)     
2.2关键字驱动_结果![关键字驱动_结果](/app_demo3/report/关键字驱动_结果.JPG)      
3.API测试    
3.1[API测试_脚本](/app_demo1/lib/runner.py)     
3.2API测试_CASE![API测试_CASE](/app_demo1/report/API测试用例.JPG)     
3.3API测试_测试结果![API测试_测试结果](/app_demo1/report/API测试结果.JPG)     



使用介绍：
1.ui测试：项目ui元素映射文件，+测试脚本    
2.api测试：按一定格式定义测试所需接口文件    


