from django.db import models

'''
Create your models here.
create cmd : 通过模型类在数据库中创建表
python manage.py makemigrations  
python manage.py migrate  
'''
#定义模型--数据库中的表
class Player(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    position = models.CharField(max_length=10)
    number = models.IntegerField()
    email = models.EmailField()
    worktime = models.FloatField()
    flag = models.BooleanField()
    content = models.TextField(max_length=300)


class Test(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    position = models.CharField(max_length=10)
    number = models.IntegerField()
    email = models.EmailField(verbose_name='邮件')
    number1 = models.IntegerField(blank=True, null=True)
    number2 = models.IntegerField(blank=True, null=True)

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=255)
    userid = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    project = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    roleid = models.IntegerField()

class Yang(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

class PermissionMap(models.Model):
    id = models.IntegerField(primary_key=True)
    function = models.CharField(max_length=255)
    roleid = models.IntegerField()

class Slave(models.Model):
    label = models.CharField(max_length=255)
    ip = models.CharField(primary_key=True,max_length=255)
    bindqueue = models.CharField(max_length=255)
    updatetime = models.DateTimeField()

class Task(models.Model):
    version = models.CharField(max_length=255)
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=255)
    data = models.CharField(max_length=255)
    
class ApiTestcase(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    project_name = models.CharField(max_length=255)
    module_name = models.CharField(max_length=255)
    api_name = models.CharField(max_length=255)
    protocol = models.CharField(max_length=255)
    header = models.CharField(max_length=255)
    expected = models.CharField(max_length=255)
    api_link = models.TextField()
    request_data = models.TextField()


class UiTaskCaseTable(models.Model):
    id = models.IntegerField(primary_key=True)
    taskid = models.CharField(max_length=50)
    caseid = models.CharField(max_length=50)
    caseresult = models.CharField(max_length=50)
    result_message = models.CharField(max_length=50)
    output = models.CharField(max_length=255)
    product_function = models.CharField(max_length=50)
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    elapsedtime = models.CharField(max_length=50)
    worker = models.CharField(max_length=50) #未分配worker则表示可以在任意worker上执行
    status = models.CharField(max_length=50) #wait,running/finished