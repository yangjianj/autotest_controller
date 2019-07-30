# -*-coding:UTF-8 -*-
import os
import sqlite3
import app_demo1.config as config

class DataManager():
    def __init__(self):
        dbpath=config.DATABASE
        self._conn = sqlite3.connect(dbpath,check_same_thread=False)
        self._cc = self._conn.cursor()

    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,"_instance"):
            cls._instance = super().__new__(cls,*args,**kwargs)
        return cls._instance

    def exec_by_sql(self,sql):
        self._cc.execute(sql)
        self._conn.commit()
        return True

    def close_conn(self):
        self._conn.close()

    def query_users(self):
        table=self._cc.execute("select * from Users")
        self._conn.commit()
        return table

    def update_user(self,name,workid,role,project,telephone):
        try:
            table=self._cc.execute("update Users set workid='%s', role='%s',project='%s',telephone='%s'  \
            where name='%s'"%(workid,role,project,telephone,name))
            self._conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def add_user(self,name,workid,role,project,telephone):
        pass

    def delete_user(self,name):
        pass

    def save_api_case(self):

        print(11111)

    def save_api_result(self):
        pass



if __name__ == '__main__':
    dd=DataManager()
    re=dd.query_Users()
    for i in re:
        print(i)
