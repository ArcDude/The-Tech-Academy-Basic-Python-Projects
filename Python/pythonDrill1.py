@@ -0,0 +1,21 @@

import os

path1 = "C:\\Users\\Schui\\Desktop\\project\\" # first part of the path

path2 = "Python\\" # second part of the path

path = os.path.join(path1, path2) # concatenating the two parts of the path

print(os.listdir(path)) # printing all files and folders in the Python folder
                        # in the project folder on the desktop


mTime = os.path.getmtime("C:\\python_projects\\pythonAssignment.txt")
fText1 = ("pythonAssignment.txt")
print("{} has been created {} seconds ago".format(fText1, mTime))


mTime1 = os.path.getmtime("C:\\python_projects\\pythonAssignment2.txt")
fText2 = ("pythonAssignment2.txt")
print("{} has been created {} seconds ago".format(fText2, mTime1))

