import json
import argparse
import subprocess as sp
import os
from os import path
import shutil

class SmartFormatter(argparse.HelpFormatter): #Customizing the help command
    def _split_lines(self, text, width):
        if text.startswith('* '): #Print everything in new line starting with *
            return text[2:].splitlines()  
        return argparse.HelpFormatter._split_lines(self, text, width)

def read_json(file_name):
    read_file = open(file_name,'r')
    get_json_data = json.load(read_file)
    return get_json_data

def svn_update(dire):
    if path.isdir(dire):
        print("Found HCI Directory.\n Updating it..")
        call_svn = sp.getoutput('svn update '+dire)
        print(call_svn)
    else:
        print("It's not a Directory (or) Can't Find an HCI Directory with : ",dire)

def svn_delete(dire):
    if path.isdir(dire):
            print("Found HCI Directory.\nRemoving..")
            shutil.rmtree(dire) # To remove multiple trees
            print('Directory -> {0} has been removed Succesfully.'.format(dire))
    else:
        print("It's not a Directory (or) Can't Find an HCI Directory with : ",dire)

def get_local_path(json_data): 
    dirs = {} #Creating empty dict. This will contain array of paths
    for module in json_data.keys():
        dirs[module] = []
        for p in json_data[module]['path']:
            dirs[module].append(p['local_path'])
    return dirs

def reset(json_data,key_list):
    dirs = get_local_path(json_data)
    for key_value in dirs.keys():
            for dire in dirs[key_value]:
                svn_delete(dire)
      
def update(json_data,key_list):
    print(key_list)  
    dirs = get_local_path(json_data)
    for key_value in dirs.keys():
            for dire in dirs[key_value]:
                svn_update(dire)

def svn_co(keyV, local_path, remote_path):
    if path.isdir(local_path):
        print("Path {0} -> {1} already exists. Skipping..".format(keyV,local_path))
    else:
        print("Checking out :  \t {0} -> {1}: ".format(keyV,local_path))
        call_svn = sp.getoutput('svn co '+remote_path+' '+local_path)
        print(call_svn)


def check_all(json_data,key_list):
    for k in key_list:
        for path in json_data[k]['path']:
            local = path['local_path']
            remote = path['remote_path']
            svn_co(k, local, remote)
        
def check_key(json_data,pass_key):
    if (pass_key not in json_data.keys()): return
    for path in json_data[pass_key]['path']:
        local = path['local_path']
        remote = path['remote_path']
        svn_co(pass_key, local, remote)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='HCI functional arguments',conflict_handler='resolve',formatter_class=SmartFormatter)
    #Filling the ArpgumentParser object with all the information 
    #add_argument()tell the ArgumentParser how to take the strings on the command line and turn them into objects
    group=parser.add_mutually_exclusive_group(required=True)
    parser.add_argument('--json_file',help='JSON file to be parsed - Eg : fileName.json', default='data1.json')
    #parser.add_argument('--Command',required=True,help='* \nList of SVN Command(s) \ndelete --To DELETE ALL Directories\nupdate --To Update HCI Directories \nALL to Checkout all Keys \n (or) specify keyValue to checkout')                  
    group.add_argument('--update', action='store_true')
    group.add_argument('--reset', action='store_true')
    group.add_argument('--checkout',action='store_true')
    parser.add_argument('--check_opt')
    print(parser.parse_args())
    #Information is stored in args and used when parse_args() is called
    #parse_args() : ArgumentParser parses arguments through the parse_args() method

    args = parser.parse_args()
    # if (args.Command=='' or None) or (args.json_file=='' or None):
    if (args.json_file=='' or None):
        parser.print_help
    else:   
        #Storing the Json File in the filePath, reading the data and storing it in jsonData 
        file_path = args.json_file
        json = read_json(file_path)
        json_data =json['module']
        #Data in jsonData will be in dict format
        # The top level keys of module are stored in keyList. Eg: ap3,medusa and convert that to list fromat from dict format for simplification
        
        key_list = list(json_data.keys())
        if args.update ==True:
            update(json_data,key_list)
        elif args.reset ==True:
            reset(json_data,key_list)
        elif (args.checkout == True):
            if args.check_opt != None:
                if (args.check_opt in key_list):
                    check_key(json_data,args.check_opt)
            else:
                check_all(json_data,key_list)
        else:
            print("Unknown Command. \n pass [-h] along with this filename to find possible commands.")