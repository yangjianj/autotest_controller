# 自动化测试平台后台代码     
功能：    
1.用户管理：登录控制，增删改查，角色权限控制    (session cookie)    
2.测试执行：接口功能测试，性能测试             (request，多线程)    
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

