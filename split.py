f = open('data.txt')
for line in f.readlines():
    print(line)
    splitData = line.split(',')
    print(splitData)
    print("------")
f.close()