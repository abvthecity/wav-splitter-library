# Wav Splitter API

is a python library for splitting wav files into equal intervals, as well as combine wav files.

# How to use

```Python
from splitterkit import readwave, writewave, split, combine

src = 'res/input/somefile.wav'
dest = 'res/somefile.wav'

data = readwave(src)
# data = (meta, [data])
splitted = split(data, 1) # into 1 second intervals
# splitted = (meta, [wav,data,intervals])

for i in range(len(splitted[1])):
    destination = 'res/output/file-'+`i`+'.wav'
    writewave(destination, (splitted[0],[splitted[1][i]]))
# saves each 1-second interval to output as individual files

combined = combine([splitted, data])
# combined = (meta, [data])
# essentially loops 2 times.
writewave(dest, combined)
```
More straight-forward, you can directly split files with a buffer and an overlap, and receive an array of the destinations of these newly split files.
```Python
from splitterkit import split_overlap

src = 'res/input/money.wav'
dest = 'res/output'
# split_overlap(src, dest, buffer, overlap)
print split_overlap(src, dest, 1, 2)
# output: ['res/output-0.wav', 'res/output-1.wav', ...]
# buffer: # of skips per 1s interval (iterator) (>=1)
# overlap: # of overlapping seconds (>=1)
```

# Requirements

1. This api is obviously written for wav files. Please don't try any other filetypes.
2. Please equalize channels, samplewidth, and framerate if you want to perform combine functions. These metadata will be inherited from the first wav data included in the array.
