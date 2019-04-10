

import os

path1 = "C:\\Users\\Schui\\Desktop\\project\\" # first part of the path

path2 = "Python\\" # second part of the path

path = os.path.join(path1, path2) # concatenating the two parts of the path

for file in os.listdir(path):
    if file.endswith(".txt"):
        print (os.path.join(path, file))

 


mTime = os.path.getmtime("C:\\Users\\Schui\\Desktop\\project\\Python\\pythonAssignment.txt")
fText1 = ("pythonAssignment.txt")
print("{} has been created {} seconds ago".format(fText1, mTime))


mTime1 = os.path.getmtime("C:\\Users\\Schui\\Desktop\\project\\Python\\pythonAssignment2.txt")
fText2 = ("pythonAssignment2.txt")
print("{} has been created {} seconds ago".format(fText2, mTime1))

