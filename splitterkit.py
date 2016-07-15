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
    mod = nframes % iframes
    # split data
    newData = []
    newDataMod = []
    for i in range(0, limit):
        f = i * iframes * sw
        t = (i + 1) * iframes * sw
        content_raw = data[1][0][f:t]
        newData.append(content_raw)
    if mod > 0:
        f = limit * iframes * sw
        t = (limit + 1) * iframes * sw
        content_raw = data[1][0][f:t]
        newDataMod.append(content_raw)
    #  save new data
    newMeta = list(data[0])
    newMetaMod = list(data[0])
    newMeta[3] = iframes
    newMetaMod[3] = mod
    container = []
    container.append((newMeta, newData))
    if mod > 0:
        container.append((newMetaMod, newDataMod))
    print 'ran SPLIT'
    return container

def combine(data):
    meta = data[0][0]
    totalframes = 0
    newdata = ''
    for i in range(len(data)):
        newdata += ''.join(data[i][1])
        totalframes += data[i][0][3]*len(data[i][1])
    meta[3] = totalframes
    print 'ran COMBINE'
    return (meta, [newdata])
