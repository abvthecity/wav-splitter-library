# Wav Splitter API (aka Splitterkit)

Splitterkit is a simple python library for splitting and merging **wave** files.

This library is written for an internal project at BCG Digital Ventures. Its purpose is simple: split an audio track into a dozen tracks, or splice a segment out of a track. But I've written this library in a way that can be re-used for any wav-splitting purposes.

## How to use

### Example

```Python
from splitterkit import readwave, writewave, split, merge, combine

src = 'res/money.wav'
dest = 'res/output-'

# extract data from wav file
data = readwave(src)

# split file into equal 1-second intervals
splitted = split(data)

# save each 1-second interval to output as individual files
ex1 = writewave(dest + 'ex1-', splitted)
print ex1 # ['res/file-ex1-0.wav', 'res/file-ex1-1.wav', ...]

# here's a weird application of merging audio
# which will output original sound looped twice.
merged = merge(combine([splitted, data]))
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
* `slicewave(data, start, end)`
  * data: `(meta, [data])`
  * start: frame#
  * end: frame#
  * returns: `(meta, [sliced_data])`
* `slicewave_s(data, start_seconds, end_seconds)`
  * same as `split()` but using seconds
* `split(data, interval, [overlap])`
  * data: `(meta, [data])`
  * interval: # of frames you want to iterate over (>0)
  * overlap: # of frames to cover per iteration (=interval, >0)
  * returns: `(meta, [mult, data, pts, ...])`
* `split_s(data, interval_seconds, [overlap_seconds])`
  * same as `splitInterval()` but using seconds
* `separate(data)`:
  * data: `(meta, [data, data2, data3, ...])`
  * returns: `[(meta, [data]), (meta2, [data2, data3]), ...]`
* `combine(data)`
  * data: `[(meta, [data]), (meta2, [data2, data3]), ...]`
  * returns: `(meta, [data, data2, data3, ...])`
  * *note: Meta data will be inherited from the first wav data included in the array. Make sure `channels`, `samplewidth`, `framerate` are all the same.*
* `merge(data)`
  * data: `(meta, [data, data2, data3, ...])`
  * returns: `(meta, [data])`

## Conclusion

This is a single-file library that can be imported into any project your heart desires, including a node.js server using `python-shell`. Good luck! :)

Authored by Andrew Jiang
