
# # class scm():
# #     def __init__(self, url, path, option):
# #         self.url = url
# #         self.path = path
# #         self.option = option
# #     def Git(self, **kwargs):
# #         print(self.url)
# #         print("called Git")
# #     def svn(self, **kwargs):
# #         print(remote_url)
# #         print(self.url)
# #         print("Called SVN")

# # class scm_type():
# #     def __init__(self, scm_type):
# #         self.scm_type = scm_type
# #         actions = {
# #             "checkout":scm("scm_type").checkout("remote_url", "local_url")
# #         }

# # # t = "svn"
# # # a = scm("SomeURL", "SomePath", "someOption")
# # # ClBindings = {"svn":a.SVN,"git":a.Git}
# # # ClBindings[t]

# # # scm.Git()
# # scm_type(svn)



# # # class scm():
# # #     def __init__(self, scm_type, url, path):
# # #         self.scm_type = scm_type
# # #         self.url = url
# # #         self.path = path
# # #         # self.option = optionx 
# # #         print("init")
# # #         (self.scm_type)(url, path)
# # #     def Git(self):
# # #         print(self.url)
# # #         print("called Git")
# # #     def svn(self):
# # #         print(self.url)
# # #         print("Called SVN")

# # # scm("svn", "SomeURL", "SomePath")


# # class scm():
# #     def __init__(self):
# #         pass
# #     def checkout():
# #         pass
# #     def update():
# #         pass

# class git(scm):
#     def __init__(self):
#         self.url = scm.url
#         self.path = scm.path
#         self.option = scm.option
#         print("git",self.url)
# class svn(scm):
#     # def __init__(self, key, local, remote):
#     #     # self.key = key
#     #     # self.local = local
#     #     # self.remote = remote
#     #     # # self.option = None
#     #     # print("svn", self.url)
#     #     scm.__init__(pData, option)
#     def update(self, rem_url, local_path):
#         # self.rem_url = rem_url
#         # self.local_path = local_path
#         print("test")
#         print(self.local)
#     def checkout(self, rem_url, local_path):
#         self.rem_url = rem_url
#         self.local_path = local_path

# # class scm():
# #     def __init__(self, scm_type, url, path, option):
# #         self.url = url
# #         self.path = path
# #         self.option = option
# #         funcs = {
# #             "svn":svn,
# #             "git":git
# #         }
# #         scm_obj = (funcs[scm_type])
# #         # call_scm = scm_obj.(self.option)(self.url,self.path)

# class scm():
#     def __init__(self, pData, option):
#         #Passed Args
#         self.pData = pData
#         self.option = option
#         # Class Variables
#         self.scm_type = pData["scm_type"]
#         self.key = pData["key"]
#         self.local = pData["local"]
#         self.remote = pData["remote"]
#     def callMethods(self):
#         funcs = {
#             "svn":svn,
#             "git":git
#         }
#         print(self.remote)
#         scm_type = str(self.scm_type)
#         # print(scm_type)
#         option = self.option
#         scm_cl = funcs[scm_type](self.key, self.local, self.remote)
#         scm_cl.option()
#         # scm_obj = (funcs[self.scm_type])
#         # print(scm_obj)
#         # call_scm = scm_obj.(self.option)(self.url,self.path)


# # scm("svn", "someR", "somep", "update")

import shutil
import pysvn
import subprocess as sp
import os
from os import path
import getpass
from . import config

class scm():
    def __init__(self, pData, option):
        self.pData = pData
        self.option = option
        # Class Variables
        self.scm_type = pData["scm_type"]
        self.key = pData["key"]
        self.local = pData["local"]
        self.remote = pData["remote"]
    def callMethods(self):
        funcs = {
            "svn":svn,
            "git":git
        }
        print(self.remote)
        scm_type = str(self.scm_type)
        # print(scm_type)
        option = self.option
        scm_cl = funcs[scm_type](self.key, self.local, self.remote)
        scm_cl.option()
        # scm_obj = (funcs[self.scm_type])
        # print(scm_obj)
        # call_scm = scm_obj.(self.option)(self.url,self.path)

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
            call_svn = client.checkout(self.remote, self.local)
            print(call_svn)
    def update(self):
        if path.isdir(self.local):
            call_svn = client.update(self.local)
            print(call_svn)
        else:
            print("It's not a Directory (or Can't find an HCI Directory with ", self.local)
    def reset(self):
        if path.isdir(self.local):
            print("Found HCI Directory.\nRemoving..")            
            shutil.rmtree(dire, onerror=del_evenReadonly)
            print('Directory -> {0} has been removed Succesfully.'.format(dire))
        else: 
            print("It's not a Directory (or) Can't Find an HCI Directory with : ",dire)
