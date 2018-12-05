from __future__ import print_function
import gc

f = open("adventofcode2018\\day05.input", "r")

lines = f.readlines()

w = list(lines[0][0:-1])

updated = True

while updated:
    updated = False
    # print(len(w))
    for index in range(len(w)-1):
        if w[index].lower() == w[index+1].lower():
            if w[index] != w[index+1]:
                #print(w[index-5:index+5], index)
                #w = w[0:index-1] + w[index+2:]
                del w[index]
                del w[index]
                updated = True
                #w = filter(lambda x : x != ' ', w)
                # print(w[index-5:index+5], index)
                break

print(len(w))