import wave, binascii

def split(src, interval):
    # read wav
    read = wave.open(src, mode='rb')
    frameRate = read.getframerate()
    nframes = read.getnframes()
    limit = nframes / (interval * frameRate)
    # split data
    data = []
    for i in range(0, limit):
        content_raw = read.readframes(interval * frameRate)
        data.append(content_raw)
    # get meta, close, return
    meta = read.getparams()
    read.close()
    return (meta, data)

def split_ascii(src, interval):
    wav = split(src, interval)
    data = []
    for i in range(len(wav[1])):
        content_ascii = binascii.b2a_base64(wav[1][i])
        data.append(content_ascii)
    return (wav[0], data)
