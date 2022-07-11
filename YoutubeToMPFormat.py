import os
import FunctionsMP3MP4 as FunctModule

#test link
#https://www.youtube.com/watch?v=6riDJMI-Y8U

configf = open("_Config.ini","r")
lines = configf.readlines()
savepath = lines[1]
configf.close()


while True:
    vidlink = input("Enter link: ")
    
    if(vidlink == ""):
        break

    print(" ")
    print("---------YOUTUBE DOWNLOADER---------")
    print(" ")
    print("(1) - Youtube Video to MP4")
    print("(2) - Youtube Video to MP3")
    print(" ")

    ch = int(input("Enter Choice: "))

    if(ch == 1):
        FunctModule.DownloadMP4(vidlink,AudioOnly = False)

    elif(ch == 2):
        FunctModule.DownloadMP4(vidlink,AudioOnly = True)
        FunctModule.WriteToMP3(FunctModule.mp4file,"DownloadedFile")
        os.remove(FunctModule.mp4file)
        NewName = input("Enter New File-Name (Including .mp3 Extension): ")
        os.rename("DownloadedFile.mp3",NewName)



    