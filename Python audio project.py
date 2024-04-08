import subprocess

def play_audio(file_name, audio_device=None):
    command = ['ffplay', '-nodisp', '-autoexit', file_name]
    
    subprocess.call(command)

if __name__ == "__main__":
    file_name = "/home/pi/Downloads/y2mate.com - Can I Have More Of You - Copy.mp3"  # Change this to the path of your audio file
    audio_device = "card 1: Device [USB PnP Sound Device], device 0: USB Audio [USB Audio]"  # Change this to the audio device ID if using USB audio adaptor

    play_audio(file_name, audio_device)
