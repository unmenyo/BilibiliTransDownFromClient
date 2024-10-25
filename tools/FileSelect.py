import json
from . import GetPath

def av_m4s_select(ListName,ListPath,):
    TargetPath =[]#临时存放目标文件路径
    targets = []#存入多个列表，每个列表都是一个视频所需要文件的路径

    NumOfList = -1#在列表里是第几个元素
    for i in ListName:
        NumOfList = NumOfList + 1
        NumOfMedia = -1

        if i == 'entry.json':#手机端的，将entry.json所在文件夹中的所有文件列出到FileName，FilePath
            path = str(ListPath[NumOfList][:-10])#entry.json所在文件夹路径
            FileName , FilePath = GetPath.DirSearch(path)
            #GetPath.PrintOnPath(path,FilePath,FileName)

            try:
                with open(ListPath[NumOfList],'r',encoding='utf8') as EntryJson:#读取entry.json
                    EntryJsonData = json.load(EntryJson)
                    if len(EntryJsonData["title"])>len(EntryJsonData["page_data"]["download_subtitle"]):
                        subtitle = EntryJsonData["title"]
                    else:
                        subtitle = EntryJsonData["page_data"]["download_subtitle"]
                    title = subtitle.replace('/','-')#非法字符换成横杠
                    title = title.replace('\\','-')
                    title = title.replace(':','-')
                    title = title.replace('*','-')
                    title = title.replace('?','-')
                    title = title.replace('"','-')
                    title = title.replace('<','-')
                    title = title.replace('>','-')
                    title = title.replace('|','-')
                    
                    TargetPath.append(title) #把[文件名，视频路径，音频路径]组合为一个列表输入targets

                    for media in FileName:
                        NumOfMedia = NumOfMedia + 1
                        if media == 'video.m4s':
                            TargetPath.append(FilePath[NumOfMedia])
                        elif media == 'audio.m4s':
                            TargetPath.append(FilePath[NumOfMedia])
                    
                    if TargetPath[1] == 0:#判断视频音频文件
                        raise Exception
                    elif TargetPath[2] == 0:
                        raise Exception
                    elif len(TargetPath) > 4:
                        raise Exception

                    TargetPath.append(0)#标记手机端
                    targets.append(TargetPath)#列表输入targets
                    TargetPath = []#归零

            except Exception:
                print('Error:该目录存在entry.json但缺少video.m4s或audio.m4s文件,或者m4s文件过多导致无法选中')
                print('目录为：' + str(ListPath[NumOfList][:-10]) + '\n')
            except:
                print('Error:有可能是读取json文件失败')
        

        if i == 'videoInfo.json':#电脑端的，我直接抄我自己
            path = str(ListPath[NumOfList][:-14])
            FileName , FilePath = GetPath.DirSearch(path)
            #GetPath.PrintOnPath(path,FilePath,FileName)

            try:
                with open(ListPath[NumOfList],'r',encoding='utf8') as videoInfoJson:#读取entry.json
                    videoInfoJsonData = json.load(videoInfoJson)
                    subtitle = videoInfoJsonData["groupTitle"] + videoInfoJsonData["title"]
                    title = subtitle.replace('/','-')#非法字符换成横杠
                    title = title.replace('\\','-')
                    title = title.replace(':','-')
                    title = title.replace('*','-')
                    title = title.replace('?','-')
                    title = title.replace('"','-')
                    title = title.replace('<','-')
                    title = title.replace('>','-')
                    title = title.replace('|','-')
                    TargetPath.append(title) #把[文件名，视频路径，音频路径，电脑客户端]组合为一个列表输入targets
                    for media in FileName:
                        NumOfMedia = NumOfMedia + 1
                        if media[-4:] == '.m4s':
                            TargetPath.append(FilePath[NumOfMedia])
                        #elif media == 'audio.m4s':
                            #TargetPath.append(FilePath[NumOfMedia])
                    
                    if TargetPath[1] == 0:#判断视频音频文件
                        raise Exception
                    elif TargetPath[2] == 0:
                        raise Exception
                    elif len(TargetPath) > 4:
                        raise Exception
                    
                    TargetPath.append(1)#标记电脑端
                    targets.append(TargetPath)#列表输入targets
                    TargetPath = []#归零

            except Exception:
                print('Error:该目录存在entry.json但缺少video.m4s或audio.m4s文件,或者m4s文件过多导致无法选中')
                print('目录为：' + str(ListPath[NumOfList][:-10]) + '\n')
            except:
                print('Error:有可能是读取json文件失败')
        

    return targets