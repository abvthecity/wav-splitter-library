# Wav Splitter API (aka SplitterKit)

SplitterKit is a simple python library for splitting and merging **wave** files. (Yes: .wav files only).

### What is this for?

This micro-service library is written for an internal project at BCG Digital Ventures. It serves a specific purpose: splice an audio file into a dozen files. But I've written this library in a way that can be re-used for any wav-splitting purposes. :)

## How to use

### Example

```Python
from splitterkit import readwave, writewave, splitInterval, merge, combine_list

src = 'res/input/money.wav'
dest = 'res/file-'

# extract data from wav file
data = readwave(src)

# split file into equal 1-second intervals
splitted = splitInterval(data)

# save each 1-second interval to output as individual files
ex1 = writewave(dest + 'ex1-', splitted)
print ex1 # ['res/file-ex1-0.wav', 'res/file-ex1-1.wav', ...]

# here's a weird application of merging audio
# which will output original sound looped twice.
merged = merge(combine_list([splitted, data]))
ex2 = writewave(dest + 'ex2-', merged)
print ex2 # ['res/file-ex2-0.wav']

# test this out by running test.py
```

### Methods
* `readwave(src)`
  * src: `'path/of/file.wav'`
  * returns: `(meta, [data])`
  * *note: `data` is in a string of bits. `meta` is the `namedtuple` produced by `wave.open(src).getparams()`.*
* `writewave(dest, data)`
  * dest: `'path/of/dir/prefix-'`
  * data: `(meta, [mult, data, pts, ...])`
  * returns: `['path/of/dir/prefix-0.wav', ...]`
* `split(data, start, end)`
  * data: `(meta, [data])`
  * start: frame#
  * end: frame#
  * returns: `(meta, [sliced_data])`
* `split_s(data, start_seconds, end_seconds)`
  * same as `split()` but using seconds
* `splitInterval(data, interval, [overlap])`
  * data: `(meta, [data])`
  * interval: # of frames you want to iterate over (>0)
  * overlap: # of frames to cover per iteration (=interval, >0)
  * returns: `(meta, [mult, data, pts, ...])`
* `splitInterval_s(data, interval_seconds, [overlap_seconds])`
  * same as `splitInterval()` but using seconds
* `split_list(data)`:
  * data: `[(meta, [data, data2, data3, ...])]`
  * returns: `[(meta, [data]), (meta2, [data2, data3]), ...]`
* `combine_list(data)`
  * data: `[(meta, [data]), (meta2, [data2, data3]), ...]`
  * returns: `[(meta, [data, data2, data3, ...])]`
  * *note: Meta data will be inherited from the first wav data included in the array. Make sure `channels`, `samplewidth`, `framerate` are all the same.*
* `merge(data)`
  * data: `(meta, [data, data2, data3, ...])`
  * returns: `(meta, [data])`

## Conclusion

Authored by Andrew Jiang
