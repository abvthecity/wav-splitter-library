# author: Andrew Jiang
import wave

def readwave(src):
    read = wave.open(src, 'rb')
    meta = list(read.getparams())
    data = read.readframes(meta[3]) # everything!
    read.close()
    print 'ran READWAVE'
    return (meta, [data])

def writewave(dest, data):
    # data = (meta, [data])
    write = wave.open(dest, 'wb')
    write.setparams(tuple(data[0]))
    write.writeframes(data[1][0])
    write.close()
    print 'ran WRITEWAVE'

def split(data, interval):
    # data = (meta, [data])
    # read wav
    sw = data[0][1] # sample width
    frameRate = data[0][2]
    nframes = data[0][3]
    iframes = interval * frameRate
    limit = nframes / iframes
    if nframes % iframes > 0:
        limit += 1
    # split data
    newData = []
    for i in range(0, limit):
        f = i * iframes * sw
        t = (i + 1) * iframes * sw
        content_raw = data[1][0][f:t]
        newData.append(content_raw)
    #  save new data
    newMeta = list(data[0])
    newMeta[3] = iframes
    print 'ran SPLIT'
    return (newMeta, newData)

def combine(data):
    meta = data[0][0]
    newdata = ''
    for i in range(len(data)):
        newdata += ''.join(data[i][1])
    meta[3] = len(newdata) / meta[1]
    print 'ran COMBINE'
    return (meta, [newdata])

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
