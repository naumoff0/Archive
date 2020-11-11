import subprocess
import os
import shutil

def ffmpeg_install():
    # Download and extract the latest archive:
    subprocess.call(["wget https://johnvansickle.com/ffmpeg/builds/ffmpeg-git-64bit-static.tar.xz"], shell=True)
    subprocess.call(["tar xvf ffmpeg-git-*.tar.xz"], shell=True)
    
    # Place the ffmpeg and other binaries into /usr/local/bin 
    subprocess.call(["cd ./ffmpeg-git-*"], shell=True)
    subprocess.call(["sudo cp ff* qt-faststart /usr/local/bin/"], shell=True)
    
    # Delete uneeded files
    os.remove("ffmpeg-git-64bit-static.tar.xz")
    shutil.rmtree("ffmpeg-git-20171231-64bit-static")
