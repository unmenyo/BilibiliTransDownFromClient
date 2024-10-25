import subprocess
import os
def ffoutmp4(targets,dir):#targets=[ [名字,音视频,音视频] , [名字,音视频,音视频] , ………… ]
    try:
        if not os.path.exists(dir):
            os.makedirs(dir)
        for i in range(len(targets)):
            try:
                subprocess.Popen('"./ffmpeg/ffmpeg.exe"' + ' -i ' + targets[i][1] + ' -i ' + targets[i][2] + ' -codec copy ' + dir + 'tmptmp.mp4',shell=True).wait()
            except:
                subprocess.Popen('"ffmpeg"' + ' -i ' + targets[i][1] + ' -i ' + targets[i][2] + ' -codec copy ' + dir + 'tmptmp.mp4',shell=True).wait()
            
            os.rename(dir + "tmptmp.mp4", dir + targets[i][0] + ".mp4")

        return 'Done'

    except:
        print('ffmpeg.exe不见了?')
        return 'Error'


def ffoutmp3(target,png):#targets=[名字,视频]
    try:
        if not os.path.exists('./mp3Temp'):
            os.makedirs('./mp3Temp')
        try:#抽音频
            subprocess.Popen('"./ffmpeg/ffmpeg.exe"'+' -i '+'"'+ target[1] +'"'+ " -vn -c:a mp3 " +'"'+'./mp3Temp/'+ target[0] +'.mp3"',shell=True).wait()
        except:
            subprocess.Popen('"ffmpeg"'+' -i '+'"'+ target[1] +'"'+ " -vn -c:a mp3 " +'"'+'./mp3Temp/'+ target[0] +'.mp3"',shell=True).wait()

        if not os.path.exists('./outputmp3'):
            os.makedirs('./outputmp3')
        a = './mp3Temp/'+ target[0] +'.mp3' #临时音频的路径
        try:#加封面
            subprocess.Popen('"./ffmpeg/ffmpeg.exe"'+  ' -i '+'"'+ a +'"'  +  ' -i '+'"'+ png +'"'+ " -map 0:a -map 1:v -map_metadata 0 -id3v2_version 3 -c:a copy -c:v copy " +'"'+'./outputmp3/'+ target[0] +'.mp3"',shell=True).wait()
        except:
            subprocess.Popen('"ffmpeg"'+  ' -i '+'"'+ a +'"'  +  ' -i '+'"'+ png +'"'+ " -map 0:a -map 1:v -map_metadata 0 -id3v2_version 3 -c:a copy -c:v copy " +'"'+'./outputmp3/'+ target[0] +'.mp3"',shell=True).wait()

        return 'Done'

    except:
        print('ffmpeg.exe不见了?')
        return 'Error'


def PullFirstFrame(target):#targets=[名字,视频]
    try:
        if not os.path.exists('./pngTemp'):
            os.makedirs('./pngTemp') 
        try:
            subprocess.Popen('"./ffmpeg/ffmpeg.exe"'+' -i '+'"'+ target[1] +'"'+' -frames:v 1 '+'"'+'./pngTemp/'+ target[0] +'.png"',shell=True).wait()
        except:
            subprocess.Popen('"ffmpeg"'+' -i '+'"'+ target[1] +'"'+' -frames:v 1 '+'"'+'./pngTemp/'+ target[0] +'.png"',shell=True).wait()

        return "./pngTemp/"+ target[0] +".png"

    except:
        print('ffmpeg.exe不见了?')
        return 'Error'