# Authored by Andrew Jiang
# — BCG digital Ventures
import wave, math

def readwave(src):
    read = wave.open(src, 'rb')
    meta = list(read.getparams())
    data = read.readframes(meta.nframes)
    read.close()
    return (meta, [data])

def writewav(dest, data):
    files = []
    data = split_list(data)
    for i in range(len(data)):
        destfile = dest + `i` + '.wav'
        write = wave.open(destfile, 'wb')
        write.setparams(data[i][0])
        write.writeframes(data[i][1])
        write.close()
        files.append(destfile)
    return files

def split(data, start, end):
    data = merge(data) # insurance
    meta = data[0]
    start *= meta.sampwidth
    end *= meta.sampwidth
    spliced = data[1][0][start:end]
    nf = len(spliced) / meta.sampwidth
    meta = meta._replace(nframes=nf)
    return (meta, [spliced])

def split_s(data, start, end):
    fr = data[0].framerate
    newdata = split(data, start*fr, end*fr)
    return newdata

def splitInterval(data, interval=None, overlap=None):
    data = merge(data) # insurance
    if(interval == None):
        interval = data[0].framerate # 1s
    if(overlap == None):
        overlap = interval
    if(interval < 1 || overlap < 1):
        raise ValueError('cannot iterate')
    iterations = math.ceil(1.0 * data[0].nframes / interval)
    canned = []
    for i in range(iterations):
        start = i * interval
        end = start + overlap
        canned.append(split(data, start, end))
    newdata = combine_list(canned)
    return newdata

def splitInterval_s(data, interval=None, overlap=None):
    if(interval != None):
        interval = interval * data[0].framerate
    if(overlap != None):
        overlap = overlap * data[0].overlap
    newdata = splitInterval(data, interval, overlap)
    return newdata

def split_list(data):
    newdata = []
    nframes = data[0].nframes
    ndata = len(data[1])
    for i in range(ndata):
        nf = len(data[1][i]) / data[0].sampwidth
        meta = data[0]._replace(nframes=nf)
        newdata.append((meta, data[1][i]))
        write.close()
    return newdata

def combine_list(data):
    newdata = []
    meta = data[0][0]
    for i in range(len(data)):
        newlist += data[i][1]
    nf = len(''.join(newlist)) / meta.sampwidth
    meta = meta._replace(nframes=nf)
    return (meta, newdata)

def merge(data):
    meta = data[0]
    newdata = ''.join(data[1])
    return (meta, [newdata])
