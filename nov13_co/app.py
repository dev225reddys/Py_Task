from modules.scm import scm, git, svn
from modules.rjson import *
from modules.argp import *
import pysvn

class scm_ops():
    def formatData(option, data):
        data = data["module"]
        # print(len(data))
        for k in data.keys():
            # print(data[k])
            for p in range(len(data[k]["path"])):
                pData = {
                    "key":k,
                    "local": data[k]["path"][p]["local_path"],
                    "remote": data[k]["path"][p]["remote_path"],
                    "scm_type": data[k]["path"][p]["scm_type"]
                }
                a = funcs[data[k]["path"][p]["scm_type"]](pData)
                getattr(a, option)()
            
    def initMethods():
        if args.update:
            scm_ops.formatData("update", rd)
        elif args.checkout:
            scm_ops.formatData("checkout",rd)
        elif args.reset:
            scm_ops.formatData("reset", rd)
        else:
            pass

        
if __name__ == "__main__":
    funcs = {
        "svn":svn,
        "git":git
    }
    rd = readJson(args.json_file)
    scm_ops.initMethods()
