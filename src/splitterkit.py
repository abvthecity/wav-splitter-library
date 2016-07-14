import binascii

def split(wave, interval):
    # read wav
    frameRate = wave.getframerate()
    nframes = wave.getnframes()
    iframes = interval * frameRate
    limit = nframes / iframes
    print '------', nframes % iframes
    # split data
    data = []
    for i in range(0, limit):
        content_raw = wave.readframes(interval * frameRate)
        data.append(content_raw)
    # return
    metalist = list(wave.getparams())
    metalist[3] = interval * frameRate
    meta = tuple(metalist)
    return (meta, data)

def split_ascii(src, interval):
    wav = split(src, interval)
    data = []
    for i in range(len(wav[1])):
        content_ascii = binascii.b2a_base64(wav[1][i])
        data.append(content_ascii)
    return (wav[0], data)
