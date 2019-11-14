import shutil
import pysvn
import subprocess as sp
import os
from os import path
import getpass
from . config import Config

class scm():
    def __init__(self, pData):
        self.pData = pData
        # self.option = option
        # Class Variables
        self.scm_type = pData["scm_type"]
        self.key = pData["key"]
        self.local = pData["local"]
        self.remote = pData["remote"]
    # def callMethods(self):
    #     funcs = {
    #         "svn":svn,
    #         "git":git
    #     }
    #     print(self.remote)
    #     scm_type = str(self.scm_type)
    #     # print(scm_type)
    #     option = self.option
    #     scm_cl = funcs[scm_type](self.key, self.local, self.remote)
    #     scm_cl.option()
    #     # scm_obj = (funcs[self.scm_type])
    #     # print(scm_obj)
    #     # call_scm = scm_obj.(self.option)(self.url,self.path)

class git(scm):
    def checkout(self):
        pass
    def update(self):
        pass

class svn(scm):
    def checkout(self):
        if path.isdir(self.local):
            print("Path {0} -> {1} already exists. Skipping..".format(self.key, self.local))
        else:
            call_svn = Config.client.checkout(self.remote, self.local)
            print(call_svn)
    def update(self):
        if path.isdir(self.local):
            call_svn = Config.client.update(self.local)
            print(call_svn)
        else:
            print("It's not a Directory (or Can't find an HCI Directory with ", self.local)
    def reset(self):
        def del_evenReadonly(action, name, exc):
            os.chmod(name, stat.S_IWRITE)
            os.remove(name)
        if path.isdir(self.local):
            print("Found HCI Directory.\nRemoving..")            
            shutil.rmtree(self.local, onerror=del_evenReadonly)
            print('Directory -> {0} has been removed Succesfully.'.format(self.local))
        else: 
            print("It's not a Directory (or) Can't Find an HCI Directory with : ",self.local)
