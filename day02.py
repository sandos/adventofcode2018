f = open("adventofcode2018\\day02.input", "r")

lines = f.readlines()

numOf2 = 0
numOf3 = 0

for l in lines:
    histogram = {}
    for c in l:
        if histogram.has_key(c):
            histogram[c] += 1
        else:
            histogram[c] = 1

    add3 = False
    add2 = False

    for key, value in histogram.iteritems():
        if value == 2:
            add2 = True
        if value == 3:
            add3 = True

    if add2:
        numOf2 += 1
    if add3:
        numOf3 += 1

print numOf2 * numOf3