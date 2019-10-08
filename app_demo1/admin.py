from django.contrib import admin
from app_demo1.models import Test,Player,User,Yang

def change_up(modeladmin, request, queryset):  #定义动作
    queryset.update(position='1')
    print(queryset)                #包含所选数据行的列表
    print(1111111111111)
change_up.short_description = "up" #重写动作显示名称

def change_down(modeladmin, request, queryset):
    queryset.update(position='0')
change_down.short_description = "down"



class TestAdmin(admin.ModelAdmin):
    list_display = ("name","age","position","number","email","number1","number2")
    #fields = ["name","age"]  #点进行信息需要显示的项
    search_fields = ["name","age"]  #搜索框输入yj 20
    actions = [change_up,change_down]  #表中加入自定义方法下拉框

class UserAdmin(admin.ModelAdmin):
    list_display = ["id","name","workid","role","project","telephone"]
    search_fields = ["name"]
    actions = []

admin.site.register(Test,TestAdmin)
admin.site.register(Player)
admin.site.register(User,UserAdmin)
admin.site.register(Yang)
# Register your models here.
