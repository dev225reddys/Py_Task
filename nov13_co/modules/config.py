import pysvn


#Verfies the SVN server trust
def ssl_server_trust_prompt( trust_dict ):
    return True, 10, True

#Prompts the user for password
def get_login(realm, username, may_save):
    username = getpass.getuser()
    password = getpass.getpass()
    return True, username, password, True

client = pysvn.Client()
client.callback_ssl_server_trust_prompt = ssl_server_trust_prompt
client.callback_get_login = get_login