from __future__ import print_function

f = open("adventofcode2018\\day03.input", "r")

lines = f.readlines()

world = []

for i in range(1000):
    world.append([])
    for x in range(1000):
        world[i].append(0)

for l in lines:
    ss = l.split()

    coords = ss[2].split(',')
    sx = int(coords[0])
    sy = int(coords[1][0:-1])

    endcoords = ss[3].split('x')

    w = int(endcoords[0])
    h = int(endcoords[1])

    for x in range(sx, sx+w):
        for y in range(sy, sy+h):
            world[x][y] += 1

count = 0

for x in range(1000):
    for y in range(1000):
        if world[x][y] > 1:
            count += 1

print(count)

for l in lines:
    ss = l.split()

    coords = ss[2].split(',')
    sx = int(coords[0])
    sy = int(coords[1][0:-1])

    endcoords = ss[3].split('x')

    w = int(endcoords[0])
    h = int(endcoords[1])

    overlap = False

    for x in range(sx, sx+w):
        for y in range(sy, sy+h):
            if world[x][y] != 1:
                overlap = True

    if not overlap:
        print("Non-overlap: ", l)
