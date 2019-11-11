from modules.scm import import scm
from modules import rjson
import pysvn


# Git = Git()
# SVN = SVN()
# class scm_obj():
#     def __init__(self, scm_type):
#         self.type = scm_type

client = pysvn.Client()
client.callback_ssl_server_trust_prompt = ssl_server_trust_prompt
client.callback_get_login = get_login