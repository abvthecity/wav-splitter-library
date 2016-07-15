from splitterkit import readwave, writewave, split, merge, combine

src = 'res/money.wav'
dest = 'res/output-'

# extract data from wav file
data = readwave(src)

# split file into equal 1-second intervals
splitted = split(data)

# save each 1-second interval to output as individual files
ex1 = writewave(dest + '1-', splitted)
print ex1 # ['res/file-ex1-0.wav', 'res/file-ex1-1.wav', ...]

# here's a weird application of merging audio
# which will output original sound looped twice.
merged = merge(combine([splitted, data]))
ex2 = writewave(dest + '2-', merged)
print ex2 # ['res/file-ex2-0.wav']
