import os


def DirSearch(path):
    global ListName
    global ListPath
    ListName = []
    ListPath = []
    with os.scandir(path) as files:
        for entry in files:
            #print(entry.path)
            if entry.is_dir():
                ListPath.append('{([([{ ' + str(entry.path))
                ListName.append('{([([{ ' + str(entry)[11:-2])#提示文件夹，好丑陋的[11:-2]

                IntoDir(entry)#进第二个一样的函数，因为用第一个函数来递归会导致列表变空，我技术不好

                ListPath.append('}])])} ' + str(entry.path))
                ListName.append('}])])} ' + str(entry)[11:-2])

            else:
                ListPath.append(str(entry.path))
                ListName.append(str(entry)[11:-2])

    return ListName , ListPath

def IntoDir(path):
    with os.scandir(path) as files:
        for entry in files:
            #print(entry.path)
            if entry.is_dir():
                ListPath.append('{([([{ ' + str(entry.path))
                ListName.append('{([([{ ' + str(entry)[11:-2])
                IntoDir(entry)
                ListPath.append('}])])} ' + str(entry.path))
                ListName.append('}])])} ' + str(entry)[11:-2])
            else:
                ListPath.append(str(entry.path))
                ListName.append(str(entry)[11:-2])



def PrintOnPath(InputPath,ListPath,ListName,DisplayName,DisplayPath):
    str = ''

    if DisplayName == 1:
        print('--------------------------------')
        print(InputPath)

    a = '|-'
    for i in ListName:
        if i[0:6] == '{([([{':
            a = a + '--------'

        if DisplayName == 1:
            print(a + i)

        if i[0:6] == '}])])}':
            a = a + '\b\b\b\b\b\b\b\b'

    if DisplayName == 1:
        print('--------------------------------\n')
#--------------------------------------------------------------------------------------
    if DisplayPath == 1:
        print('--------------------------------')
        print(InputPath)
    str = str + '--------------------------------\n' + InputPath + '\n'

    a = '|-'
    
    for i in ListPath:
        if i[0:6] == '{([([{':
            a = a + '--------'

        if DisplayName == 1:
            print(a + i)
        str = str + i + '\n'

        if i[0:6] == '}])])}':
            a = a + '\b\b\b\b\b\b\b\b'
    if DisplayPath == 1:
        print('--------------------------------\n')
    str = str + '--------------------------------\n'

    return str

"""

"""
