"""
pe1.py
26/08/2021
"""

import os
#2.a)
def make_folder(folder: str):
    path = os.path.join("./", folder)
    os.mkdir(path)

#make_folder("folder1")

#2.b)
def make_file(file: str):
    s = ""
    for i in range(1,1001):
        s += "a"
    with open(file, "w") as f:
        f.write(s)

path = "./folder1/"
file = "ola.txt"
path_file = os.path.join(path, file)
#make_file(path_file)

#2.c)
def f3(file :str):
    fd = os.open(file, os.O_RDWR|os.O_CREAT)
    for i in range(1,1001):
        if i%10 == 0:
            os.lseek(fd, i, 0)
            os.write(fd, str.encode("b"))
#f3(path_file)

#2.d)
def f4(dir: str):
    l = []
    for file in os.listdir(dir):
        f = os.path.join(dir, file)
        fd = os.open(f, os.O_RDWR|os.O_CREAT)
        s = str(os.read(fd, 1))
        s2 = s[2:len(s)-1]
        print("file: ", file, " - s2: ", s2)
        if s2 == "a":
            l.append(f)
        os.close(fd)
    for el in l:
        os.remove(el)
f4("./folder1/")
