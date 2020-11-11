import subprocess
from ffmpeg_install import ffmpeg_install


def main():
    print("Installing Libraries...")
    subprocess.call(["pip3 install --user -r requirements.txt"], shell=True)
    print("Libraries installed, now installing FFMPEG")
    ffmpeg_install()
    print("Done!")
        
    
    
if __name__ == "__main__":
    main()