from scipy.io import wavfile
from scipy.fftpack import fft
import numpy as np

def pavan():
    sampFreq, snd = wavfile.read('440_sine.wav')
    #fft_output = fft(snd)
    norm = 2.**(int(str(snd.dtype)[-2:]) - 1) # normalize between -1 and 1
    snd = snd / norm
    #print(snd.shape, snd)
    s1 = snd[:,0]
    print(s1.shape, s1)
    n = len(s1)
    p = fft(s1)
    nUniquePts = int(ceil((n + 1)/2.0))
    p = abs(p[0:nUniquePts]) #absolute value provides magnitude



pavan()
#print(norm)
#a = snd.dtype
#print(a)
#print(sampFreq)
#print(snd)
