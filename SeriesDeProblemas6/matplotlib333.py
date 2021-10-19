"""
Paulo Luis 17359
pf3.py pf4.py e pf5.py
29/08/2021
"""
import matplotlib.pyplot as plt
import numpy as np
import math

#3)
def f1():
    y = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    plt.plot(y, color='green', marker="x")
    plt.title("potencias de 2", fontsize=20)
    plt.ylabel("2**n", fontsize=15)
    plt.xlabel("n", fontsize=15)
    plt.savefig("grafico3.pdf")
    plt.show()
f1()

#4)
def f2():
    div = 4*math.pi / 100
    i = 0
    xl = []
    yl = []
    cosyl = []
    cossenyl = []
    for _ in range(100):
        yl.append(math.sin(i))
        cosyl.append(math.cos(i))
        cossenyl.append(math.sin(i) * math.sin(i))
        xl.append(i)
        i += div
    plt.plot(xl,yl)
    plt.plot(xl, cosyl, color='red')
    plt.plot(xl, cossenyl, color='yellow')
    plt.xlabel('x values from 0 to 4pi')
    plt.ylabel('sin(x)')
    plt.title('Plot of sin from 0 to 4pi')
    plt.legend(['sin(x)', 'cos(x)', 'cos(x) * sin(x)']) 
    plt.savefig("sen.pdf")
    plt.show()
f2()


def f2_numpy():
    x = np.arange(0, 4*np.pi, 0.1)   # start,stop,step
    y = np.sin(x)
    z = np.cos(x)
    plt.plot(x,y,x,z, 4, 1)
    plt.xlabel('x values from 0 to 4pi')
    plt.ylabel('sin(x) and cos(x)')
    plt.title('Plot of sin and cos from 0 to 4pi')
    plt.legend(['sin(x)', 'cos(x)']) 
    plt.savefig("sen2.pdf")
    plt.show()
f2_numpy()

#5)
def f3():
    xl= [x for x in range(-30, 30)]
    yl= [x**2 - 2*x - 2 for x in range(-30, 30)]
    
    plt.plot(xl,yl)
    plt.axis(xmin=-10, xmax=10, ymin=-10, ymax=50)
    plt.axhline(2, color='orange',linestyle='--',linewidth=1)
    plt.plot([-20,20], resolvente(2, -2, -2), "r")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Plot of f(x)=x**2 - 2*x - 2')
    plt.legend(['f(x)', 'reta', 'zeros']) 
    #plt.savefig("fcc.pdf")
    plt.show()


def resolvente(a, b, c):
    root = (b*b)-(4*a*c)
    if root < 0:
	    return []
    total = []
    total.append((-b+math.sqrt(root))/(2*a))
    total.append((-b-math.sqrt(root))/(2*a))
    total.sort()
    return total
f3()

#6)
def f4():
    div = math.pi * 4 / 100
    x = - 2 * math.pi

    xl = []
    cosyl = []
    sinyl = []
    cossinyl = []
    for _ in range(100):
        xl.append(x)
        cosyl.append(math.cos(x))
        sinyl.append(math.sin(x))
        cossinyl.append(math.cos(x) * math.sin(x))
        x+=div

    fig, axs = plt.subplots(3)
    fig.suptitle('Cos and Sin relation')
    axs[0].plot(xl, cosyl, 'tab:green')
    axs[0].set_title("Cos")
    axs[0].set(xlabel='x', ylabel='cos(x)')

    axs[1].plot(xl, sinyl, 'tab:red')
    axs[1].set_title("Sin")
    axs[1].set(xlabel='x', ylabel='sin(x)')

    axs[2].plot(xl, cossinyl, 'tab:brown')
    axs[2].set_title("Cos * Sin")
    axs[2].set(xlabel='x', ylabel='cos(x) * sin(x)')

    for ax in axs.flat:
        ax.label_outer()
    #plt.savefig("subaba.pdf")
    plt.show()
f4()