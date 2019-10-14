import hashlib,time,datetime
from django.contrib.auth.models import User
from app_demo1.lib.database_model import CommentSerializer

class UserManager():
    #token过期时间管理使用redis
    def __init__(self):
        pass

    def login(self,user,password):
        pass

    def logout(self):  #服务端需要保存

        pass

    def create_user(self,username,password,role):
        pass

    def set_password(self):
        pass

    def change_password(self):
        pass

    def _generate_token(self,user,time):
        salt = 'auto'
        tokenstr = user+time+salt
        x = hashlib.sha256()
        x.update(tokenstr.encode())
        return x.hexdigest()

    def get_token(self,user,password):
        timestamp = (datetime.datetime.now() + datetime.timedelta(days=7)).strftime("%Y-%m-%d-%H-%M-%S")
        userobj = User.objects.filter(username=user)
        userjson = CommentSerializer(instance=userobj, many=True)
        if password == userjson["password"]:
            token = self._generate_token(user, timestamp)
            return token, timestamp
        else:
            return None

    def auth_token(self,user,token,dietime):
        dtime = datetime.datetime.strptime(dietime, "%Y-%m-%d-%H-%M-%S")
        timenow = datetime.datetime.now()
        if dtime<timenow:     #token已过期
            return 'token die'
        else:
            if token == self._generate_token(user, dietime):
                return True
            else:
                return 'auth failed'
