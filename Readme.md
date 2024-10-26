# 这是一个用于将B站缓存的视频导出为mp4或mp3的python脚本


[BilibiliTransDownFromClient](https://github.com/unmenyo/BilibiliTransDownFromClient)

---
---

## 1.使用该脚本的前提

[~~没有安装python的点我这里~~](https://www.python.org/)

该脚本使用了 ffmpeg，请将 ffmpeg 路径添加到环境变量中，或将文件 ffmpeg.exe 放入脚本文件根目录下

[下载ffmpeg请点击此处](https://ffmpeg.org/)

---

## 2.使用

Transform.py用于导出视频
OnlyAudio.py用于仅导出音频，且将视频的第一帧作为封面（在b站听歌听的）

bilibili电脑端：将缓存的视频所在文件夹bilibili直接拖入 Transform.py或OnlyAudio.py（后文将统称脚本），这将使所有缓存的视频导出，也可进入bilibili文件夹，自行选择想要导出的单个视频的文件夹拖入脚本。

### 就像这样:

![](https://picx.zhimg.com/v2-885a966c1ae3b85fe540ce58992a751f_r.jpg)

### 或是这样：

![](https://pic4.zhimg.com/v2-95cc6ea80717bf58c8a4dfa625ca69a7_r.jpg)

bilibili手机端：手机端缓存的视频通常都在这个路径下 

    /storage/emulated/0/Android/data/tv.danmaku.bili/download

同上，使用时将 download 文件夹直接拖入脚本中，这将使所有缓存的视频导出，也可进入 download 文件夹，自行选择想要导出的单个视频的文件夹拖入脚本。

---

## 3.其实导出只需要同一个文件夹有这三个缓存下来的文件
电脑端：

>xxxxxxxxx.m4s
>xxxxxxxxx.m4s
>videoInfo.json

手机端：

>video.m4s
>audio.m4s
>entry.json

只需要这三个文件放在同一个文件夹，并将这个文件夹拖入脚本中就能导出