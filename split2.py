f = open('data.txt')
for line in f.readlines():
    print(line)
    splitData = line.split(',')
    print(splitData)
    final = []
    for data in splitData:
        final.append( data.strip())
    print(final)
    print("------")
f.close()