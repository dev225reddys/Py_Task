from modules.scm import scm, git, svn
from modules.rjson import *
from modules.argp import *
import pysvn


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
            a = svn(pData, option)
            a.update()
        
def initMethods():
    if args.update:
        formatData("update", rd)
    elif args.checkout:
        formatData("checkout",rd)
    elif args.reset:
        formatData("reset", rd)
    else:
        pass

        
if __name__ == "__main__":
    rd = readJson(args.json_file)
    initMethods()
