from splitterkit import split_overlap

src = 'res/samples/money.wav'
dest = 'res/output/files'

print split_overlap(src, dest, 1, 3)
