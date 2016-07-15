from splitterkit import readwave, writewave, split, combine

src = 'res/samples/f_disgust.wav'
dest = 'res/output/somefile.wav'

data = readwave(src)
print len(data[1][0])
splitted = split(data, 1)
print splitted[0][0][3], splitted[1][0][3]

combined = combine(splitted + [data])
print len(combined[1][0])
writewave(dest, combined)

for i in range(len(splitted)):
    for j in range(len(splitted[i][1])):
        destination = 'res/output/file-'+`i`+'-'+`j`+'.wav'
        writewave(destination, (splitted[i][0],[splitted[i][1][j]]))
