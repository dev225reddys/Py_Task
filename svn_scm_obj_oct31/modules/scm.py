
# class scm():
#     def __init__(self, url, path, option):
#         self.url = url
#         self.path = path
#         self.option = option
#     def Git(self, **kwargs):
#         print(self.url)
#         print("called Git")
#     def svn(self, **kwargs):
#         print(remote_url)
#         print(self.url)
#         print("Called SVN")

# class scm_type():
#     def __init__(self, scm_type):
#         self.scm_type = scm_type
#         actions = {
#             "checkout":scm("scm_type").checkout("remote_url", "local_url")
#         }

# # t = "svn"
# # a = scm("SomeURL", "SomePath", "someOption")
# # ClBindings = {"svn":a.SVN,"git":a.Git}
# # ClBindings[t]

# # scm.Git()
# scm_type(svn)



# # class scm():
# #     def __init__(self, scm_type, url, path):
# #         self.scm_type = scm_type
# #         self.url = url
# #         self.path = path
# #         # self.option = optionx 
# #         print("init")
# #         (self.scm_type)(url, path)
# #     def Git(self):
# #         print(self.url)
# #         print("called Git")
# #     def svn(self):
# #         print(self.url)
# #         print("Called SVN")

# # scm("svn", "SomeURL", "SomePath")


# class scm():
#     def __init__(self):
#         pass
#     def checkout():
#         pass
#     def update():
#         pass

class git():
    def __init__(self):
        self.url = scm.url
        self.path = scm.path
        self.option = scm.option
        print("git",self.url)
class svn():
    def __init__(self):
        self.url = None
        self.path = None
        self.option = None
        print("svn", self.url)
    def update(self, rem_url, local_path):
        self.rem_url = rem_url
        self.local_path = local_path
        print("test")
    def checkout(self, rem_url, local_path):
        self.rem_url = rem_url
        self.local_path = local_path

class scm():
    def __init__(self, scm_type, url, path, option):
        self.url = url
        self.path = path
        self.option = option
        funcs = {
            "svn":svn,
            "git":git
        }
        scm_obj = (funcs[scm_type])
        call_scm = scm_obj.(self.option)(self.url,self.path)

scm("svn", "someR", "somep", "update")