# yt2mp3

Simple python script to download and convert youtube videos to mp3.

You can copy and paste the full youtube link and set your output folder in the script.

Features:
* Downloads and inserts Coverartwork
* Downloads and inserts Metadata (eg. Artist, Title, Albumtitle, Year)

Uses the following dependancies, which have to be installed:

$ brew install youtube_dl
$ brew install ffmpeg

***Tipp on Mac OS***

 To have the script as an executable file on your desktop in order to speed things up,
 rename:
 > yt2mp3.py to yt2mp3.command
 
 then open your terminal and make the file 
 executable by setting admin rights to it: cd to Desktop and type: 
 
 > chmod +x yt2mp3.command
 
 Now you can double click on the command file and it will start the script.
