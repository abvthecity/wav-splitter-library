from splitterkit import readwave, writewave, split, combine

# this function is designed to split a wav file
# into a series of wav files, with a buffer and an overlap
def split_overlap(src, dest, buf, overlap):
    data = readwave(src) # wav data
    splitted = split(data, 1) # split into 1s intervals
    files = []
    for i in range(len(splitted[1]) / buf):
        j = i * buf # actual iterator
        r = j + overlap
        combined = combine([(splitted[0], splitted[1][j:r])])
        destfile = dest + `i` + '.wav'
        writewave(destfile, combined)
        files.append(destfile)
    return files
