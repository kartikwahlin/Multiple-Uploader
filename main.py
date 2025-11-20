import typer #For taking CLI input
from pathlib import Path#For taking path??
import soundfile as sf
import pyloudnorm as pyln #For reading loudness from files
import subprocess #For adjusting loudness to platform-tuned values

PRESETS = { #Hash Map<String,String>
        "youtube": 'loudnorm=I=-14:TP=-1:LRA=11',
        "tiktok": 'loudnorm=I=-15:TP=-1.5:LRA=7',
        "instagram": 'loudnorm=I=-14:TP=-1.2:LRA=9'
}

def normalizeAll(input, output=None):#Create a folder and put the 3 normalized files in
        if output==None:
                #TODO Set output to same folder as input
                output=""
                
        #Make folder at output
        try:
                subprocess.run(["mkdir", output], check=True)
        except Exception as e:
                print(e)

        #run normalizeTo using input and 3 spots in output
        for key in PRESETS:
                op1 = f"{output}/{key}.mp4"
                normalizeTo(input, op1, key)
        return

def normalizeTo(input, output, preset):
        filter = PRESETS[preset] #has to be exact string
        cmd = f'ffmpeg -i "{input}" -af "{filter}" -c:v copy "{output}"'
        subprocess.run(cmd, shell=True, check=True)
        return

def main(name: str):
        print(f"Hello {name}")

if( __name__ == "__main__"):
        typer.run(main)