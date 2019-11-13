import json
import argparse
parser = argparse.ArgumentParser(description='HCI functional arguments',conflict_handler='resolve')
#Filling the ArpgumentParser object with all the information 
#add_argument()tell the ArgumentParser how to take the strings on the command line and turn them into objects
parser.add_argument('--json_file',help='JSON file to be parsed - Eg : fileName.json', default='data1.json')                 
gtmp = parser.add_argument_group(title='Action', description='One of these options must be chosen.')
group = gtmp.add_mutually_exclusive_group(required=True)
group.add_argument('--update','-u', action='store_true', help="Updates the working copy")
group.add_argument('--reset','-r', action='store_true',help="Remove a file from a working copy")
group.add_argument('--checkout','-c',const='all', help="Check out a working copy from a repository",nargs='?')
print(parser.parse_args())
#Information is stored in args and used when parse_args() is called
#parse_args() : ArgumentParser parses arguments through the parse_args() method

args = parser.parse_args()