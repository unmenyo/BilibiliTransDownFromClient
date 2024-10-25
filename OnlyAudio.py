import sys
import os
from tools import GetPath
from tools import FileSelect
from tools import InputFFmpeg
from tools import Fixm4s
from tools import CopyFileWhichError
from pprint import pprint
line = '\n--------------------------------\n'

def Transform(Path):#如果只是想从视频中抽取音频而非从b站缓存抽取，可以把这个方法、(1)下方的判断、(2)临时文件夹相关的代码删了
    try:
        ListName , ListPath = GetPath.DirSearch(Path)
        targets = FileSelect.av_m4s_select(ListName,ListPath)


        for i in range(len(targets)):
            if targets[i][3]==1:
                targets[i][1] = Fixm4s.fix(targets[i][1])
                targets[i][2] = Fixm4s.fix(targets[i][2])



        a = InputFFmpeg.ffoutmp4(targets,"./mp4Temp/")

        if targets[i][3]==1:
            TempFileName,TempFilePath = GetPath.DirSearch('./temp')

            print(line)
            for i in range(len(TempFilePath)):
                os.remove(TempFilePath[i])
                print('Delete:    ' + TempFilePath[i])
            os.rmdir("./Temp")
            print('Delete:    ./Temp')
            print(line)


    except:
        print("Not run Transform.py")
        return "Error"



Path = sys.argv[1]
try:
    source_isbili = Transform(Path)

    if source_isbili == "Error":#(1)判断是从b站缓存文件夹来的还是自己不知道从哪拿来的mp4
        dirpath = Path
    else:
        dirpath = "./mp4Temp/"
        
    
    ListName , ListPath = GetPath.DirSearch(dirpath)
    targets = []
    
    for i in range(len(ListName)):
        targets.append([ListName[i][:-4],ListPath[i]])
    print(targets)
    for i in range(len(targets)):
        pngPath = InputFFmpeg.PullFirstFrame(targets[i])#抽取视频第一帧作为封面
        a = InputFFmpeg.ffoutmp3(targets[i],pngPath)#抽音频
        if (pngPath or a) == 'Error':
            CopyFileWhichError.ErrorCopy(targets[i][0],targets[i][1])

        
    print(line)

    TempFileName,TempFilePath = GetPath.DirSearch("./mp4Temp/")#(2)删除临时文件
    for i in range(len(TempFilePath)):
        os.remove(TempFilePath[i])
        print('Delete:    ' + TempFilePath[i])
    os.rmdir("./mp4Temp")
    print('Delete:    ./mp4Temp')

    TempFileName,TempFilePath = GetPath.DirSearch("./mp3Temp/")
    for i in range(len(TempFilePath)):
        os.remove(TempFilePath[i])
        print('Delete:    ' + TempFilePath[i])
    os.rmdir("./mp3Temp")
    print('Delete:    ./mp3Temp')

    TempFileName,TempFilePath = GetPath.DirSearch("./pngTemp/")
    for i in range(len(TempFilePath)):
        os.remove(TempFilePath[i])
        print('Delete:    ' + TempFilePath[i])
    os.rmdir("./pngTemp")
    print('Delete:    ./pngTemp')

    print(line)


    print(line)
    print("Done")
    print(line)
        

except:
    print("Error form OnlyAudio.py")




input()