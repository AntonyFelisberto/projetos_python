import os

file = open("myfile.txt","c") #c(create), r(read),a(append), w(write)
print(file.read())
file.write("Happy learning!!")
os.remove(filename)
file.close()