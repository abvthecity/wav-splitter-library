# Wav Splitter API

is a python library for splitting wav files into intervals, and a library for combining wav files.

# How to use

```Python
from splitterkit import readwave, writewave, split, combine

src = 'res/samples/f_disgust.wav'
dest = 'res/output/somefile.wav'

data = readwave(src)
# data = (meta, [data])
splitted = split(data, 1)
# splitted = [(meta, [wav,data,intervals]), (metamod, [datamod])]

combined = combine(splitted + [data])
# combined = (meta, [data])
writewave(dest, combined)
```
