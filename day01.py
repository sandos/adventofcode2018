f = open("adventofcode2018\\day01.input", "r")

lines = f.readlines()

sum = 0
visited = {}

done = False

while not done:
    for l in lines:
        sum += int(l)
        if visited.has_key(sum):
            print("found loop {}", sum)
            done = True
            break
        else:
            visited[sum] = 1

#print sum