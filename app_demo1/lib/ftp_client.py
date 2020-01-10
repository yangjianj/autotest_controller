# -*- coding: utf-8 -*-
import os
from ftplib import FTP
class FtpClient():
    def __init__(self,host,user,passwd):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.client = FTP(host=host,user=user,passwd=passwd)
    
    def upload(self,file,localfile):
        # file: uitest_base/suite_names/output.xml
        # localfile: tmp/test.txt
        fp = open(localfile,'rb')
        self.client.storbinary('STOR %s'%(file), fp)
        fp.close()
        print('upload succeed !')
        return True
    
    def download(self,filelist,localdir='tmp/'):
        # file: uitest_base/suite_names/output.xml
        for file in filelist:
            dirname,filename = os.path.split(file)
            if not os.path.exists(localdir+dirname):
                os.makedirs(localdir+dirname)
            fd = open(localdir+file,'wb')
            self.client.retrbinary('RETR %s'%(file),fd.write)
            fd.close()
        print('download succeed !')
        return True
    
    def delete(self,file):
        self.client.delete(file)
    
    def close(self):
        self.client.close()

    def dir(self,path=None):
        if path == None:
            path = self.client.pwd()
        file_list = []
        self.client.dir(path,file_list.append)
        return file_list

    def path_exist(self,path):
        try:
            self.client.dir(path)
            return True
        except Exception as e:
            return False

    def mkd(self,pathname):
        try:
            self.client.mkd(pathname)
        except Exception as e:
            print(e)
        return True

    def pwd(self):
        return self.client.pwd()

if __name__ == '__main__':
    #ftp = FTP(host="127.0.0.1",user=  "test",passwd="123456")
    client = FtpClient(host="127.0.0.1",user="test",passwd="123456")
    root_list = client.dir('corepro-message-plugin-2.0-SNAPSHOT-jar-with-dependencies-112201.jar')
    for item in root_list:
        print(item)
    print('delete')
    #client.delete('uitest_base/log.html')
    #client.mkd('test/test1/test2')
    #print(client.path_exist('test/test1'))
    #client.download('uitest_base/suite_names/output.xml')
    client.upload('uitest_base/suite_names/output_up.xml','tmp/uitest_base/suite_names/output.xml')
    client.close()