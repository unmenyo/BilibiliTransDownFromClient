import sys
import os
from tools import GetPath
from tools import FileSelect
from tools import InputFFmpeg
from tools import Fixm4s
from pprint import pprint
line = '\n--------------------------------\n'

InputPath = sys.argv[1]


try:
    ListName , ListPath = GetPath.DirSearch(InputPath)
    targets = FileSelect.av_m4s_select(ListName,ListPath)


    for i in range(len(targets)):
        if targets[i][3]==1:
            targets[i][1] = Fixm4s.fix(targets[i][1])
            targets[i][2] = Fixm4s.fix(targets[i][2])



    a = InputFFmpeg.ffoutmp4(targets,"./outputmp4/")

    if targets[i][3]==1:
        TempFileName,TempFilePath = GetPath.DirSearch('./temp')

        print(line)
        for i in range(len(TempFilePath)):
            os.remove(TempFilePath[i])
            print('Delete:    ' + TempFilePath[i])
        os.rmdir("./Temp")
        print('Delete:    ./Temp')
        print(line)

    print(line)
    print(a)
    print(line)


except:
    print("Error from Transform.py")





input()