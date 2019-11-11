from modules.scm import import scm
from modules import rjson


Git = Git()
SVN = SVN()
class scm_obj():
    def __init__(self, scm_type):
        self.type = scm_type