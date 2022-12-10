f = open('write_something.txt',"a")
lines = ["hi\n","this is python"]
f.writelines(lines)
f.close()
