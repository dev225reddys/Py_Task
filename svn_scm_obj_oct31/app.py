from modules.scm import Git, SVN
from modules import rjson

class scm_obj():
    def __init__(self, scm_type):
        self.type = scm_type