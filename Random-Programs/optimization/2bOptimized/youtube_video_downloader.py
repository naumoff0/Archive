import subprocess
import os
from pafy import *
from clear_screen import clearScreen
from input_sanitizer import accepted_inputs


def main():
    directory = os.path.dirname(os.path.realpath(__file__)) + "/downloaded_videos"
    
    # ensure log folder exists
    if not os.path.exists(directory):
        os.mkdir(directory)

    
    amount = None
    
    # ensure user gives correct number
    while True:
        try:
            clearScreen()
            
            # round input incase user tries to be sneaky and gives a decimal
            amount = round(int(input("Number of videos to download: ")))
            print("Asking user for amount")
            
            if amount < 1:
                print("Invalid amount")
                continue
            
        except ValueError:
            print("Invalid amount!")
        else:
            break
        
    # TODO add import from file feature
    links = []
    fileFormats = []
    
    applyExtensionToAll = False
    formatForLink = None
    
    for i in range(amount):
        clearScreen()
        link = input("URL for Video {}: ".format(i+1))
        
        # get file format
        if applyExtensionToAll == False:
            option = input("File format: ")
            
            # note that tons of file formats are available so make a pull request if you want more
            option = accepted_inputs(["mp3", "mp4"], option)
            formatForLink = option
            
            
        # ask user if they want to apply the file extension to all further downloads
        if i == 0 and amount > 1 and applyExtensionToAll == False:
            choice = input("Apply this to all further videos (y/n): ")        
            choice = accepted_inputs(["y", "n"], choice)
            
            if choice == "y":                
                applyExtensionToAll = True
            

        # add link and requested format
        links.append(link)
        fileFormats.append(formatForLink)
    
    totalLinks = len(links)

    for i in range(totalLinks):

        video = new(links[i])
        
        if not video:
            print("Invalid URL! Continuing to next URL...")
            continue
        
        print("Downloading...")
    
        # set video prefrences for downloading
        if fileFormats[i] == "mp3":
            bestAudio = video.getbestaudio()
            bestAudio.download(filepath=directory)
        else:
            bestVideo = video.getbest(preftype="mp4")
            bestVideo.resolution, bestVideo.extension
            
            # download video
            bestVideo.download(quiet=False, filepath=directory)
    
    # open downloaded videos folder
    subprocess.call(["cd", directory], shell=True)
        
    # source: http://bytefreaks.net/gnulinux/bash/ffmpeg-extract-audio-from-webm-to-mp3
    # The following command will find all webm files that are in the current directory and in all sub-folders and extract the audio to mp3 format.
    subprocess.call(["find . -type f -iname \"*.webm\" -exec bash -c 'FILE=\"$1\"; ffmpeg -i \"${FILE}\" -vn -ab 128k -ar 44100 -y \"${FILE%.webm}.mp3\";' _ '{}' \;"], shell=True)
        
    # delete webm file
    subprocess.call(["find . -name \"*.webm\" -type f -delete"], shell=True)
    print("\n\n___________________\nAll Done!")
    
    
    
if __name__ == "__main__":
    main()