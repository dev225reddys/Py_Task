import os
from os import path
import sys
import subprocess as sp
import re

def get_HCI(props):
    keys = []
    if len(sys.argv) <=1:
        for line in range(len(props)):
            print("\nHCI Information from svn:externals:\n" + "*" * 50 + "\n")
            # hciSeen = []
            f_hci = re.findall('^#HCI_+\w+',props[line])
            if(f_hci):
                print(props[line])
            f_keys = re.findall('^#HCI_+\w+',props[line])
            if f_keys:
                f_k1 = f_keys.split('_')
                keys.append(f_k1)
        print("*" * 50 + "\n")
        print("The following HCI keywords were found: " +[keys[key] for key in range(len(keys))]+ "\n\n")
        print("Invoke script with ALL to check out all HCI element directories.\n")
        print("Invoke script with RESET to delete all HCI element directories.\n")
        print("Invoke script with UPDATE to svn update all HCI element directories.\n\n")

    elif len(sys.argv) > 1:
        # print('Arg Passed : ',sys.argv[1])
        # if sys.argv
        if(sys.argv[1] == 'RESET'):
            print("Removing all HCI element directories. \n")
            for line in range(len(props)):
                propline = props[line]
                f_keys_r = re.findall('^#HCI_+\w+',propline)
                if f_keys_r:
                    undef, svnUrl, dir = propline.split('\t')
                    if path.exists(dir):
                        print(" Found HCI Directory : {0} - removing it\n".format(dir))
                        taskRemDir = os.remove(dir)
                        if taskRemDir:
                            print('Removed Successfully.')
                        else:
                            print("Couldn't Remove it.\t Try Again!")
        elif(sys.argv=='UPDATE'):
            print("Updating all HCI element Directories. \n")
            for line in range(len(props)):
                propline = props[line]
                f_keys_r = re.findall('^#HCI_+\w+',propline)
                if f_keys_r:
                    undef, svnUrl, dir = propline.split('\t')
                    if path.exists(dir):
                        print(" Found HCI Directory : {0} - Updating\n".format(dir))
                        taskUpdDir = sp.getoutput('svn update '+dir)
                        if taskUpdDir:
                            print(taskUpdDir)
                        else:
                            print("Couldn't Update.\t Please Try again!")
        else:
            for arg in sys.argv:
                # if arg!='ALL' and if re.findall('#HCI_'+arg,[props[line] for line in range(len(props))):
                    # print("Sorry, couldn't find an HCI element named {0}\n".format(arg))
                if arg!='ALL':
                    print("Run this command without arguments to display valid elements.\n")
                for line in range(len(props)):
                    propline = props[line]
                    if(arg=="ALL") and (re.findall('^#HCI_+\w+',propline)) or (re.findall('^#HCI_'+arg,propline)):
                    # if(arg=="ALL") and if(re.findall('^#HCI_+\w+',propline)) or if(re.findall('^#HCI_'+arg+,propline)):
                        lbl,svnUrl,dir = propline.split('\t')
                        split_lbl = lbl.split('_')
                        split_lbl = split_lbl[1]
                        if path.exists(dir):
                            print("{0} -> {1}".format(lbl,dir))
                            print("\n Path already Exists, Skipping\n")
                        else:
                            print("{0} -> {1}".format(lbl,dir))
                            print("\nChecking Out...\n")
                            svnCo = sp.getoutput("svn co "+svnUrl+" "+dir)
                            print(svnCo)

if __name__ == "__main__":
    propRaw = sp.getoutput('svn propget svn:externals .')
    props = propRaw.split('\n')
    get_HCI(props)
