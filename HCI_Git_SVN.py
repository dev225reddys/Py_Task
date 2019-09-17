import subprocess as sp
import os
import sys
import argparse as ap
import re


def git_Commit():
    CommitMsg = str(input('Enter Commit Message'))
    git_c_cmd = 'git commit -m '+CommitMsg
    git_c = sp.call(git_c_cmd)
    if git_c:
        git_push_cmd = 'git push origin master'
        git_push = sp.call(git_push_cmd)
        if(git_push):
            print('Successfully Made Changes!')

def git_HCI(getHCIDirs,cmds):
    HCIDirs = getHCIDirs
    if(cmds=='RESET'):
        for i in range(len(HCIDirs)):
            rmfile = os.remove(HCIDirs[i])
            if rmfile:
                git_Commit()
    if(cmds=='ALL'):
        print('Displaying All Files Starting with HCI')
        for i in range(len(HCIDirs)):
            print(HCIDirs[i])
    else:
        print('No Arguments Passed!')
        
def get_HCI(cmds):
    hciSeen = []
    if cmds != 'ALL' or cmds != 'RESET':
        print("\nHCI Information from svn:externals:\n" + "*" * 50 + "\n")
        for p in range(len(props)):
            if re.search('/^#HCIDoc', props[p]):
                info = p
                print("* ",info,'\n')
            if re.search("/^#HCI_(.*?)", props[p]):
                hciSeen.append(p)
        print("*"*50+"\n")
        print("The following HCI keywords were found: ")
        for i in range(len(hciSeen)):
            print(props[hciSeen[i]],'\n')
        print("Invoke script with \"ALL\" to check out all HCI element directories.\n")
        print("Invoke script with \"RESET\" to delete all HCI element directories.\n")
        print("Invoke script with \"UPDATE\" to \"svn update\" all HCI element directories.\n\n")

    elif cmds == "RESET":

        print("Removing all HCI elemement directories.\n")
        for i in range(len(hciSeen)):
            pArr = props[hciSeen[i]]
            undef,svnUrl,dir = pArr.split('\t')
            os.system("rm -rm "+dir)
    elif cmds == "UPDATE":
        print("Updating all HCI elemement directories.\n")
        for i in range(len(hciSeen)):
            pArr = props[hciSeen[i]]
            undef,svnUrl,dir = pArr.split('\t')
            os.system('svn update '+dir)
    else:
        for hci in sys.argv:
            if hci == "ALL":  
                print( "Sorry, couldn't find an HCI element named \"hci\".\n")
                print( "Run this command without arguments to display valid elements.\n")
            rc = os.system("svn co svnUrl "+dir)
            if rc:
                print("\n ERROR: svn checkout returned \"rc\" aborting\n")


if __name__ == "__main__":

    parser = ap.ArgumentParser(description='Args')
    parser.add_argument('--fn')
    parser.add_argument('--cmd')
    args, leftovers = parser.parse_known_args()
    if args.fn is not None:
        if args.cmd is not None:
            if args.fn == 'git' or args.fn == 'github':
                getHCIDirs = []
                git_URL = 'Specify URL Here'
                git_add_cmd = 'git remote add origin '+git_URL
                git_add = sp.call(git_add_cmd)
                if(git_add):
                    git_pull_cmd = 'git pull origin master'
                    git_pull = sp.call(git_pull_cmd)
                    if(git_pull):
                        CMD = 'dir HCI_*'
                        response = sp.getoutput(CMD)
                        response = response.split(' ')
                        while "" in response:
                            response.remove("")
                        getHCIDirs = response
                        # print(getHCIDirs)
                        git_HCI(getHCIDirs,args.cmd)
            elif args.fn == 'svn' or args.fn == 'SVN':
                propCMD = ('svn propset svn:externals .')
                props = sp.getoutput(propCMD)
                props = props.split('\n')
                get_HCI(args.cmd)
            else:
                print('Invalid Args. \n for Github use `Git` or `Github`.\n for SVN use `SVN` or `svn`.')
        else:
            print('Missing Arguments. \n CMD is not passed')
    else:
        print('Missing Arguments. \n fn is not passed.')