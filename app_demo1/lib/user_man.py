import hashlib,time,datetime
from app_demo1.models import User,PermissionMap
from app_demo1.lib.app_serializers import CommentSerializer
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect

class UserManager():
    def __init__(self):
        self.name=0

    def create_user(self,userobj):
        try:
            user=User(username=userobj["username"],password=userobj["password"],userid=userobj["userid"])
            user.save()
            userdict = dict(username=userobj["username"],password=userobj["password"],userid=userobj["userid"])
            return dict(result=True,message=userdict)
        except Exception as e:
            return dict(result=False, message=str(e))

    def change_password(self,username,password,newpwd):
        try:
            user = User.objects.get(username=username)
            if user.password == password:
                user.password = newpwd
                user.save()
                return True
            else:
                return {"re":False,"message":"password error"}
        except Exception as e:
            return {"re":False,"message":str(e)}


    def check_password(self,username,password):
        try:
            userlist = User.objects.filter(username=username)
            if userlist[0].password == password:
                return True
            else:
                return False
        except Exception as e:
            return False

    def delete_user(self,userlist):
        for user in userlist:
            User.objects.filter(username=user["username"]).delete()

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

def check_permission(func):
    # 权限控制
    def inner(*args):
        user_request = args[0]
        request_function = user_request.path.split('/')[1]
        roleid = Permission_map.objects.get(function = request_function).roleid
        username = user_request.session["username"]
        userobj = User.objects.get(username=username)
        if userobj.roleid > roleid:
            result = {"status":"error","message":"permission delay"}
            return JsonResponse(result)
        else:
            result = func(*args)
            return result
    return inner