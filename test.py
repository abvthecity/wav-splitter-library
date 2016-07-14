import os, sys, binascii, splitter

src = 'samples/f_disgust.wav'
data = splitter.split_ascii(src, 1)
print data[1]
