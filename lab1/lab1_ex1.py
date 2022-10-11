import sounddevice as sd
from sounddevice import *
import numpy as np
import time 
from scipy.io.wavfile import write
import argparse as ap
import os

parser = ap.ArgumentParser()
parser.add_argument("--resolition", type = str, default="int32")
args = parser.parse_args()

ts = time.time()
i = 1
store_audio = True

def callback(data, frames, callback_time, status):
    global store_audio
    if store_audio == True: 
        write(f'{ts}.wav', 48000, data = data)
        in_byte = os.path.getsize(f'{ts}.wav')
        in_byte = in_byte/1024
        print(f'size: {in_byte} KB')

with InputStream(device=0, channels=1, samplerate=48000, dtype = args.resolution, callback=callback, blocksize=48000):
    while True:
        a = input()
        if a == "q":
            break
        if a == "p":
            store_audio = not store_audio





