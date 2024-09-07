import subprocess
import os
def ffout(targets):
    try:
        if not os.path.exists('output'):
            os.makedirs('output')
        for i in range(len(targets)):
            try:
                p = subprocess.Popen('"ffmpeg"' + ' -i ' + targets[i][1] + ' -i ' + targets[i][2] + ' -codec copy ' + './output/' + targets[i][0] + '.mp4',shell=True).wait()
            except:
                p = subprocess.Popen('"./ffmpeg/ffmpeg.exe"' + ' -i ' + targets[i][1] + ' -i ' + targets[i][2] + ' -codec copy ' + './output/' + targets[i][0] + '.mp4',shell=True).wait()

    except:
        print('ffmpeg.exe不见了?')


    return 'Done'