# Authored by Andrew Jiang
# BCG digital Ventures
import wave, math
from collections import namedtuple

metatuple = namedtuple('metatuple', ['nchannels', 'sampwidth', 'framerate', 'nframes', 'comptype', 'compname'])
datatuple = namedtuple('datatuple', ['meta', 'data'])

def readwave(src):
    read = wave.open(src, 'rb')
    meta = read.getparams()
    # turn params into named tuple
    meta = metatuple(meta[0], meta[1], meta[2], meta[3], meta[4], meta[5])
    data = read.readframes(meta.nframes)
    read.close()
    return datatuple(meta, [data])

def writewave(dest, data):
    files = []
    data = split_list(data)
    for i in range(len(data)):
        destfile = dest + `i` + '.wav'
        write = wave.open(destfile, 'wb')
        write.setparams(data[i].meta)
        write.writeframes(data[i].data)
        write.close()
        files.append(destfile)
    return files

def split(data, start, end):
    data = merge(data) # insurance
    meta = data.meta
    start *= meta.sampwidth
    end *= meta.sampwidth
    spliced = data.data[0][start:end]
    nf = len(spliced) / meta.sampwidth
    meta = meta._replace(nframes=nf)
    return datatuple(meta, [spliced])

def split_s(data, start, end):
    fr = data.meta.framerate
    newdata = split(data, start*fr, end*fr)
    return newdata

def splitInterval(data, interval=None, overlap=None):
    data = merge(data) # insurance
    if(interval == None):
        interval = data.meta.framerate # 1s
    if(overlap == None):
        overlap = interval
    if(interval < 1 or overlap < 1):
        raise ValueError('cannot iterate')
    iterations = int(math.ceil(1.0 * data.meta.nframes / interval))
    canned = []
    for i in range(iterations):
        start = i * interval
        end = start + overlap
        canned.append(split(data, start, end))
    newdata = combine_list(canned)
    return newdata

def splitInterval_s(data, interval=None, overlap=None):
    if(interval != None):
        interval = interval * data.meta.framerate
    if(overlap != None):
        overlap = overlap * data.meta.overlap
    newdata = splitInterval(data, interval, overlap)
    return newdata

def split_list(data):
    newdata = []
    nframes = data.meta.nframes
    ndata = len(data.data)
    for i in range(ndata):
        nf = len(data.data[i]) / data.meta.sampwidth
        meta = data.meta._replace(nframes=nf)
        newdata.append(datatuple(meta, data.data[i]))
    return newdata

def combine_list(data):
    newdata = []
    meta = data[0].meta
    for i in range(len(data)):
        newdata += data[i].data
    nf = len(''.join(newdata)) / meta.sampwidth
    meta = meta._replace(nframes=nf)
    return datatuple(meta, newdata)

def merge(data):
    meta = data.meta
    newdata = ''.join(data.data)
    return datatuple(meta, [newdata])
