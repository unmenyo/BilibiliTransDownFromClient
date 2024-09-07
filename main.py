import sys
import os
from tools import GetPath
from tools import FileSelect
from tools import InputFFmpeg
from tools import Fixm4s
from pprint import pprint


InputPath = sys.argv[1]
ListName , ListPath = GetPath.DirSearch(InputPath)
targets = FileSelect.select(ListName,ListPath)


for i in range(len(targets)):
    if targets[i][3]:
        targets[i][1] = Fixm4s.fix(targets[i][1])
        targets[i][2] = Fixm4s.fix(targets[i][2])



a = InputFFmpeg.ffout(targets)

TempFileName,TempFilePath = GetPath.DirSearch('./temp')

line = '\n--------------------------------\n'

print(line)
for i in range(len(TempFilePath)):
    os.remove(TempFilePath[i])
    print('Delete:    ' + TempFilePath[i])
os.rmdir('./temp')
print('Delete:    ./temp')
print(line)

print(line)
print(a)
print(line)

input()
