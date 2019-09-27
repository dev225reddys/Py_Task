import json
import argparse
import subprocess as sp
import os
from os import path
import shutil

class SmartFormatter(argparse.HelpFormatter):
    def _split_lines(self, text, width):
        if text.startswith('*** '):
            return text[2:].splitlines()  
        return argparse.HelpFormatter._split_lines(self, text, width)

def readJson(fileName):
    readFile = open(fileName,'r')
    getJsonData = json.load(readFile)
    return getJsonData

def getDirs(jsonData):
    Dirs = []
    for obj in range(len(jsonData)):
        Dirs.append(jsonData[obj]['key'][0]['dir'])
    return Dirs
def getDirUrlLbl(jsonData):
    Dirs = []
    url = []
    keyName = []
    for obj in range(len(jsonData)):
        Dirs.append(jsonData[obj]['key'][0]['dir'])
        url.append(jsonData[obj]['key'][0]['url'])
        keyName.append(jsonData[obj]['key'][0]['name'])
    return Dirs,url,keyName

def getURL():
    url = []
    for obj in range(len(jsonData)):
        url.append(jsonData[obj]['key'][0]['url'])
    return url

def _RESET_(jsonData):
    Dirs = getDirs(jsonData)
    for Dire in range(len(Dirs)):
        if path.isdir(Dirs[Dire]):
            print("Found HCI Directory.\nRemoving..")
            shutil.rmtree(Dirs[Dire])
            print('Directory -> {0} has been removed Succesfully.'.format(Dirs[Dire]))
        else:
            print("It's not a Directory (or) Can't Find an HCI Directory with : ",Dirs[Dire])

def _Update_(jsonData):
    Dirs = getDirs(jsonData)
    for Dire in range(len(Dirs)):
        if path.isdir(Dirs[Dire]):
            print("Found HCI Directory.\n Updating it..")
            callSVN = sp.getoutput('svn update '+Dirs[Dire])
            print(callSVN)
        else:
            print("It's not a Directory (or) Can't Find an HCI Directory with : ",Dirs[Dire])
def checkAll(jsonData,keyList):
    Dirs,url,keyName = getDirUrlLbl(jsonData)
    for dire,eurl,keyv in zip(Dirs,url,keyName):
        if path.isdir(dire):
            print("Path {0} -> {1} already exists. Skipping..".format(keyv,dire))
        else:
            print("Checking out :  \t {0} -> {1}: ".format(keyv,dire))
            callSVN = sp.getoutput('svn co '+eurl+' '+dire)
            print(callSVN)
def checkKey(jsonData,PasskeyV):
    Dirs,url,keyName = getDirUrlLbl(jsonData)
    for dire,eurl,keyv in zip(Dirs,url,keyName):
        if keyv == PasskeyV:
            if path.isdir(dire):
                print("Path {0} -> {1} already exists. Skipping..".format(keyv,dire))
            else:
                print("Checking out :  \t {0} -> {1}: ".format(keyv,dire))
                callSVN = sp.getoutput('svn co '+eurl+' '+dire)
                print(callSVN)


if __name__ == "__main__":
    updateCommands = ['update','UPDATE','upd']
    deleteCommands = ['reset','delete','DELETE','RESET','del']
    parser = argparse.ArgumentParser(description='HCI functional arguments',conflict_handler='resolve',formatter_class=SmartFormatter)
    parser.add_argument('Command',
                        help='*** \nList of SVN Command(s) \nRESET --To DELETE ALL Directories\nUPDATE --To Update HCI Directories \nALL to Checkout all Keys \n (or) specify keyValue to checkout')
    parser.add_argument('JsonFile',
                        help='JSON file to be parsed - Eg : fileName.json')

    args = parser.parse_args()
    if (args.Command=='' or None) or (args.JsonFile=='' or None):
        parser.print_help
    else:    
        filePath = args.JsonFile
        jsonData = readJson(filePath)
        keyList = [jsonData[i]['key'][0]['name'] for i in range(len(jsonData))]
        if args.Command in updateCommands:
            _Update_(jsonData)
        elif args.Command in deleteCommands:
            _RESET_(jsonData)
        elif (args.Command == 'ALL') or (args.Command == 'all'):
            checkAll(jsonData,keyList)
        elif (args.Command in keyList):
            checkKey(jsonData,args.Command)

        else:
            print("Unknown Command. \n pass [-h] along with this filename to find possible commands.")