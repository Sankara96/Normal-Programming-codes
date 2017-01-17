import subprocess

def textToWav(text,file_name):
   subprocess.call(["espeak", "-w hey.wav", text])

textToWav('hello world','hello')