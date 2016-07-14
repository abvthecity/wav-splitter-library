# Wav Splitter API

is a python library for splitting wav files into intervals, and a library for combining wav files.

# How to use

```Python
import wave
from splitterkit import split, split_ascii, combine, combine_ascii

wavData = wave.open('path/to/file.wav', mode='rb')

splitted = split(wavData, 1) # split wav into 1s intervals
# splitted: (meta, [data,for,each,interval])
# meta: (nchannels, sampwidth, framerate, nframes, comptype, compname)
# split_ascii converts each data into ascii base64

wavData.close()

wavData = wav.open('path/to/writefile.wav', mode='wb')

toCombine = [(meta, [data]), (meta, [data,wav]), splitted]

combined = combine(toCombine, wavData) # combine array of wav data
# combined: (meta, [data])
# combined_ascii converts from ascii
# saves directly to file

wavData.close()
```
