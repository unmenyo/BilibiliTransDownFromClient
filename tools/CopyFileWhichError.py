import shutil
import os

def ErrorCopy(name,path):
    if not os.path.exists('./ErrorCopy'):
        os.makedirs('./ErrorCopy')
    shutil.copyfile(path,"./ErrorCopy/"+name)