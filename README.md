# yt2mp3

A python script which downloads and converts a youtube video to mp3.
You can copy and paste the full youtube link and set your output folder in the script.


## Features
* Downloads and inserts Coverartwork
* Downloads and inserts Metadata (eg. Artist, Title, Albumtitle, Year)

## Dependancies
Uses the following dependancies, which have to be installed:
[youtube-dl](https://github.com/ytdl-org/youtube-dl) and [FFmpeg](https://github.com/FFmpeg/FFmpeg)
```shell
$ brew install youtube-dl
$ brew install ffmpeg
```
---

## Tipp on MacOS

 to make the script executable on your desktop,
 rename:
 ```shell
yt2mp3.py to yt2mp3.command
```
 
 then open your terminal and make the file 
 executable by setting admin rights to it: cd to Desktop and type: 
 ```shell
 chmod +x yt2mp3.command
 ```
 
 Now you can double click on the command file and it will start the script.
 
 ---
 
## Disclaimer 
*for educational purpose only. i'm not responsible for your actions or any copyright infringement due the usage of this script*
