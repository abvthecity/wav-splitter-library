# Wav Splitter API

is a python library for splitting wav files into equal intervals, as well as combine wav files.

# How to use

```Python
from splitterkit import readwave, writewave, split, combine

src = 'res/input/somefile.wav'
dest = 'res/output/somefile.wav'

data = readwave(src)
# data = (meta, [data])
splitted = split(data, 1) # into 1 second intervals
# splitted = [(meta, [wav,data,intervals]), (metamod, [datamod])]

for i in range(len(splitted)):
    for j in range(len(splitted[i][1])):
        destination = 'res/output/file-'+`i`+'-'+`j`+'.wav'
        writewave(destination, (splitted[i][0],[splitted[i][1][j]]))
# saves each 1-second interval to output as individual files

combined = combine(splitted + [data])
# combined = (meta, [data])
# essentially loops 2 times.
writewave(dest, combined)
```

# Requirements

1. This api is obviously written for wav files. Please don't try any other filetypes.
2. Please equalize channels, samplewidth, and framerate if you want to perform combine functions. These metadata will be inherited from the first wav data included in the array.
