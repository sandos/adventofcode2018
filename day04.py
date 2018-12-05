from __future__ import print_function

f = open("adventofcode2018\\day04.input", "r")

lines = f.readlines()

events = []

for l in lines:
    d = l.split()
    print(d[0][1:], end=' ')
    dates = d[0][1:].split('-')

    print(d[1][:-1], end=' ')
    print(" ".join(d[2:]))

    res = []
    res.append(dates)
    # res.append(d[0][1:])
    res.append(d[1][0:2])
    res.append(d[1][3:-1])
    res.append(" ".join(d[2:]))
    # print(res)
    events.append(res)

for x in sorted(events, key=lambda x : x[0][0] + x[0][1] + x[0][2] + x[1] + x[2]):
    print(x)