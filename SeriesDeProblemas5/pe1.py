"""
pe1.py
26/08/2021
"""

import os
import platform
import sys
#1.a)
def f1():
    f = open("home.txt", "w")
    f.write(str(os.environ))
    f.close()
#f1()

#1.b)
def f2():

    s = str(os.name) + "\n"
    s += str(platform.system()) + "\n"  # e.g. Windows, Linux, Darwin
    s += str(platform.architecture()) + "\n"  # e.g. 64-bit
    s += str(platform.machine()) + "\n"  # e.g. x86_64
    s += str(platform.node()) + "\n"  # Hostname
    s += str(platform.processor()) + "\n"  # e.g. i386
    s += str(sys.platform)
    f = open("sistema.txt", "w")
    f.write(s)
f2()

#1.c)
def f3(file_name):
    try : 
        open(file_name)

    except OSError as error : 
        print(error) 
        print("File descriptor is not associated with any terminal device") 
#f3("home.txt")
#f3("lala.txt")

#1.d)
def f4():
    print("Diretoria da execução do script: ", os.path.dirname(os.path.abspath(__file__)))
    print("Diretoria atual: ", os.path.abspath(os.getcwd()))
    print("Id do processo do script: ", os.getpid())
    #print("Id do utilizador atual: ", os.getuid()) # disponivel apenas em so linux
f4()

