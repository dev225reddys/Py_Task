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

def svn_update(dire):
    if path.isdir(dire):
        print("Found HCI Directory.\n Updating it..")
        callSVN = sp.getoutput('svn update '+dire)
        print(callSVN)
    else:
        print("It's not a Directory (or) Can't Find an HCI Directory with : ",dire)

def svn_delete(dire):
    if path.isdir(dire):
            print("Found HCI Directory.\nRemoving..")
            shutil.rmtree(dire)
            print('Directory -> {0} has been removed Succesfully.'.format(dire))
    else:
        print("It's not a Directory (or) Can't Find an HCI Directory with : ",dire)

def getDirs(jsonData,keyList):
    Dirs = {}
    for keyi in range(len(keyList)):
        key = keyList[keyi]
        Dirs[key] = []
        if len(jsonData['module'][key]['path']) > 1:
            for dir in range(len(jsonData['module'][key]['path'])):
                Dirs[key].append(jsonData['module'][key]['path'][dir]['local_path'])
                # Dirs.append(jsonData['module'][key]['path'][dir]['local_path'])
        else:
            Dirs[key].append(jsonData['module'][key]['path'][0]['local_path'])
    return Dirs

def getAllDat(jsonData,keyList):
    AllDat = {}
    for keyi in range(len(keyList)):
        key = keyList[keyi]
        if len(AllDat) ==0 or key not in AllDat.keys():
            AllDat[key] = {}
            if "local_path" not in AllDat[key].keys() or len(AllDat[key]) <=1:
                AllDat[key]["local_path"] = []
            if "remote_path" not in AllDat[key].keys():
                AllDat[key]["remote_path"] = []
        if len(jsonData['module'][key]['path']) > 1:
            for dir in range(len(jsonData['module'][key]['path'])):
                AllDat[key]["local_path"].append(jsonData['module'][key]['path'][dir]['local_path'])
                AllDat[key]["remote_path"].append(jsonData['module'][key]['path'][dir]['remote_path'])
                # Dirs.append(jsonData['module'][key]['path'][dir]['local_path'])
        else:
            AllDat[key]["local_path"].append(jsonData['module'][key]['path'][0]['local_path'])
            AllDat[key]["remote_path"].append(jsonData['module'][key]['path'][0]['remote_path'])
    return AllDat

def getkeyData(jsonData,PasskeyV):
    keyDat = {}
    key = PasskeyV
    if len(keyDat) ==0 or key not in keyDat.keys():
        keyDat[key] = {}
        if "local_path" not in keyDat[key].keys() or len(keyDat[key]) <=1:
            keyDat[key]["local_path"] = []
        if "remote_path" not in keyDat[key].keys():
            keyDat[key]["remote_path"] = []
    if len(jsonData['module'][key]['path']) > 1:
        for dir in range(len(jsonData['module'][key]['path'])):
            keyDat[key]["local_path"].append(jsonData['module'][key]['path'][dir]['local_path'])
            keyDat[key]["remote_path"].append(jsonData['module'][key]['path'][dir]['remote_path'])
            # Dirs.append(jsonData['module'][key]['path'][dir]['local_path'])
    else:
        keyDat[key]["local_path"].append(jsonData['module'][key]['path'][0]['local_path'])
        keyDat[key]["remote_path"].append(jsonData['module'][key]['path'][0]['remote_path'])
    return keyDat

def getDirUrlLbl(jsonData,keyList):
    Dirs = {}
    url = {}
    # keyName = []
    for keyi in range(len(keyList)):
        key = keyList[keyi]
        Dirs.append(jsonData[0]['module'][key]['path'][0]['local_path'])
        url.append(jsonData[0]['module'][key]['path'][0]['remote_path'])
        # keyName.append(jsonData[obj]['key'][0]['name'])
    return Dirs,url

def getURL():
    url = []
    for obj in range(len(jsonData)):
        url.append(jsonData[obj]['key'][0]['url'])
    return url

def _RESET_(jsonData,keyList):
    Dirs = getDirs(jsonData,keyList)
    for key_value in Dirs.keys():
        if len(Dirs[key_value]) > 1:
            for dire in range(len(Dirs[key_value])):
                svn_delete(Dirs[key_value][dire])
        else:
            svn_delete(Dirs[key_value][0])

def _Update_(jsonData,keyList):
    Dirs = getDirs(jsonData,keyList)
    for key_value in Dirs.keys():
        if len(Dirs[key_value]) > 1:
            for dire in range(len(Dirs[key_value])):
                svn_update(Dirs[key_value][dire])
        else:
            svn_update(Dirs[key_value][0])

def svn_co(keyV, local_path, remote_path):
    if path.isdir(local_path):
        print("Path {0} -> {1} already exists. Skipping..".format(keyV,local_path))
    else:
        print("Checking out :  \t {0} -> {1}: ".format(keyV,local_path))
        callSVN = sp.getoutput('svn co '+remote_path+' '+local_path)
        print(callSVN)

def checkAll(jsonData,keyList):
    getAllDat1 = getAllDat(jsonData,keyList)
    # print(getAllDat1.keys())
    # exit()
    for keyV in getAllDat1.keys():
        if len(getAllDat1[keyV]["local_path"]) > 1:
            for pos in range(len(getAllDat1[keyV]["local_path"])):
                keyData = keyV
                local_path = getAllDat1[keyV]["local_path"][pos]
                remote_path = getAllDat1[keyV]["remote_path"][pos]
                svn_co(keyV,local_path,remote_path)
        else:
            keyData = keyV
            local_path = getAllDat1[keyV]["local_path"][0]
            remote_path = getAllDat1[keyV]["remote_path"][0]
            svn_co(keyV,local_path,remote_path)

    # for dire,eurl,keyv in zip(Dirs,url,keyList):
    #     if path.isdir(dire):
    #         print("Path {0} -> {1} already exists. Skipping..".format(keyv,dire))
    #     else:
    #         print("Checking out :  \t {0} -> {1}: ".format(keyv,dire))
    #         callSVN = sp.getoutput('svn co '+eurl+' '+dire)
    #         print(callSVN)
def checkKey(jsonData,PasskeyV):
    keyData = getkeyData(jsonData,PasskeyV)
    if len(keyData[PasskeyV]["local_path"]) > 1:
        for pos in range(len(keyData[PasskeyV]["local_path"])):
            local_path = keyData[PasskeyV]["local_path"][pos]
            remote_path = keyData[PasskeyV]["remote_path"][pos]
            svn_co(PasskeyV,local_path,remote_path)
    else:
        local_path = keyData[PasskeyV]["local_path"][0]
        remote_path = keyData[PasskeyV]["remote_path"][0]
        svn_co(PasskeyV,local_path,remote_path)
    # if path.isdir(dire):
    #     print("Path {0} -> {1} already exists. Skipping..".format(keyv,dire))
    # else:
    #     print("Checking out :  \t {0} -> {1}: ".format(keyv,dire))
    #     callSVN = sp.getoutput('svn co '+eurl+' '+dire)
    #     print(callSVN)


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
        # keyList = [jsonData[i]['key'][0]['name'] for i in range(len(jsonData))]
        keyList = list(jsonData['module'].keys())
        # print(keyList)
        # print((jsonData['module']['ap3']["path"][1]))
        # exit()
        # print(args.Command)
        if args.Command in updateCommands:
            _Update_(jsonData,keyList)
        elif args.Command in deleteCommands:
            _RESET_(jsonData,keyList)
        elif (args.Command == 'ALL') or (args.Command == 'all'):
            checkAll(jsonData,keyList)
        elif (args.Command in keyList):
            checkKey(jsonData,args.Command)

        else:
            print("Unknown Command. \n pass [-h] along with this filename to find possible commands.")
        # print("Response Json Data : ",jsonData)
        # print("Length of Json Data : ",len(jsonData))
        # print("Found Keys : ",[jsonData[i]['key'][0]['name'] for i in range(len(jsonData))])