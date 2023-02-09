from main import *
import os


class ProjetosBuild(QMainWindow):
    
    def build():
        os.system('aws codebuild start-build --project-name carbon-crm-backend')
        pass
    