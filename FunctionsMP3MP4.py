from pytube import YouTube
from moviepy.editor import *

def DownloadMP4(_vidlink = None,AudioOnly = False):
    #Downloads MP4 File from Youtube URL and outputs it as an MP4 w/wo Audio (For Easy Conversion purposes).
    global mp4file
    global mp4filename

    yt = YouTube(_vidlink)

    if AudioOnly == False:
        print("Downloading Video File......")
        stream = yt.streams.filter(progressive = True,file_extension = 'mp4').first()
        stream.download()
        print("Downloaded Video File Successfully!......")
    elif AudioOnly == True:
        print("Downloading Video File......")
        stream = yt.streams.filter(only_audio = True, only_video= False).first()
        mp4filename = stream.title
        mp4file = stream.download()
        print("Downloaded Video File (w/o Video Content) Successfully!......")



def WriteToMP3(_mp4file,newfilename):
    #Converts an MP4 file to an MP3
    audioclip = AudioFileClip(_mp4file)
    audioclip.write_audiofile(newfilename + ".mp3")
    audioclip.close()
    print("MP3 File Creation Successful!......")