import wave
from src.splitterkit import split_ascii

src = 'res/samples/f_disgust.wav'
wavData = wave.open(src, mode='rb')
data = split_ascii(wavData, 1)
print data[1]
