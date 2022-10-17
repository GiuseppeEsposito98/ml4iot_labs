import sounddevice as sd
from sounddevice import *
import numpy as np
import time 
from scipy.io.wavfile import write
import argparse as ap
import os

parser = ap.ArgumentParser()
parser.add_argument("--resolition", type = str, default="int32")
parser.add_argument("--samplerate", type = str, default="int32")
parser.add_argument("--number_channels", type = str, default="int32")
parser.add_argument("--block_size", type = int, default= 4*48000)

args = parser.parse_args()


store_audio = True

def callback(data, frames, callback_time, status):
    global store_audio
    if store_audio == True: 
        ts = time.time()
        write(f'{ts}.wav', args.samplerate, data = data)
        in_byte = os.path.getsize(f'{ts}.wav')
        in_byte = in_byte/1024
        print(f'size: {in_byte} KB')

with InputStream(device=0, channels=args.number_channels, samplerate=args.samplerate, dtype = args.resolution, callback=callback, blocksize=48000):
    while True:
        a = input()
        if a == "q":
            print("Stop recording")
            break
        if a == "p":
            print("i'm not saving this audio")
            store_audio = not store_audio





