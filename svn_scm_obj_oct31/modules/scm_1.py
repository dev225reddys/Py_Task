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
    def checkout():
        print(self.local)
        pass
    def update():
        pass

class svn(scm):
    def checkout():
        pass
    def update():
        pass

