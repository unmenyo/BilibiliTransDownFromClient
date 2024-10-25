import os
from . import GetPath
def fix(path):#整整电脑端缓存的m4s
    with open(path,"rb") as file:
        header = file.read(16)
        NewHeader = header.replace(b'000000000',b'')#改改头部
        bufsize = int(64*1024*1024)


        if not os.path.exists('temp'):#创临时文件夹
            os.makedirs('temp')
        str = path[path.rfind('\\')+1:]#临时文件的名字
        with open('./temp/'+str,"wb") as temp:
            temp.write(NewHeader)
            raw = file.read(bufsize)
            while raw:
                temp.write(raw)
                raw = file.read(bufsize)

    OutputPath = os.path.abspath('./temp/'+str)
    return OutputPath
                            
"""
        print(file)
        
        
        print(path)
"""