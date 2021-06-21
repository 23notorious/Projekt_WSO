import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg

historia_pozycji0 = [line.split() for line in open('pozycje0.txt')]  
historia_pozycji1 = [line.split() for line in open('pozycje1.txt')]  
historia_pozycji2 = [line.split() for line in open('pozycje2.txt')]  
historia_pozycji3 = [line.split() for line in open('pozycje3.txt')]  


def Pierwsza(x):
    return [item[0] for item in x]
def Druga(y):
    return [item[1] for item in y]


def rysuj(pozycja):
    y = []

    for i in enumerate(pozycja):
##        print("Pozycja w chwili",i[0],"to",i[1])
        y.append(i[0])
        
    x = Pierwsza(pozycja)
    y = Druga(pozycja)
    return [x, y]

while True:
    print("""
        Podaj liczbę:
        0 - pierwszy skyfall
        1 - drogi skyfall
        2 - trzeci skyfall
        3 - czwarty skyfall
        4 - wszystkie
        enter - exit
    """)

    txt = int(input())
    if txt == 0:
        plt.plot((rysuj(historia_pozycji0))[0], (rysuj(historia_pozycji0))[1])
        for i in range(0, len((rysuj(historia_pozycji0))[0])):
            plt.annotate(i, ((rysuj(historia_pozycji0))[0][i], (rysuj(historia_pozycji0))[1][i]))
        plt.scatter((rysuj(historia_pozycji0))[0], (rysuj(historia_pozycji0))[1])

    if txt == 1:
        
        plt.plot((rysuj(historia_pozycji1))[0], (rysuj(historia_pozycji1))[1])
        for i in range(0, len((rysuj(historia_pozycji1))[0])):
            plt.annotate(i, ((rysuj(historia_pozycji1))[0][i], (rysuj(historia_pozycji1))[1][i]))
        plt.scatter((rysuj(historia_pozycji1))[0], (rysuj(historia_pozycji1))[1])

    if txt == 2:
        
        plt.plot((rysuj(historia_pozycji2))[0], (rysuj(historia_pozycji2))[1])
        for i in range(0, len((rysuj(historia_pozycji2))[0])):
            plt.annotate(i, ((rysuj(historia_pozycji2))[0][i], (rysuj(historia_pozycji2))[1][i]))
        plt.scatter((rysuj(historia_pozycji2))[0], (rysuj(historia_pozycji2))[1])

    if txt == 3:

        plt.plot((rysuj(historia_pozycji3))[0], (rysuj(historia_pozycji3))[1])
        for i in range(0, len((rysuj(historia_pozycji3))[0])):
            plt.annotate(i, ((rysuj(historia_pozycji3))[0][i], (rysuj(historia_pozycji3))[1][i]))
        plt.scatter((rysuj(historia_pozycji3))[0], (rysuj(historia_pozycji3))[1])

    if txt == 4:
        plt.plot((rysuj(historia_pozycji0))[0], (rysuj(historia_pozycji0))[1])
        for i in range(0, len((rysuj(historia_pozycji0))[0])):
            plt.annotate(i, ((rysuj(historia_pozycji0))[0][i], (rysuj(historia_pozycji0))[1][i]))
        plt.scatter((rysuj(historia_pozycji0))[0], (rysuj(historia_pozycji0))[1])

        plt.plot((rysuj(historia_pozycji1))[0], (rysuj(historia_pozycji1))[1])
        for i in range(0, len((rysuj(historia_pozycji1))[0])):
            plt.annotate(i, ((rysuj(historia_pozycji1))[0][i], (rysuj(historia_pozycji1))[1][i]))
        plt.scatter((rysuj(historia_pozycji1))[0], (rysuj(historia_pozycji1))[1])

        plt.plot((rysuj(historia_pozycji2))[0], (rysuj(historia_pozycji2))[1])
        for i in range(0, len((rysuj(historia_pozycji2))[0])):
            plt.annotate(i, ((rysuj(historia_pozycji2))[0][i], (rysuj(historia_pozycji2))[1][i]))
        plt.scatter((rysuj(historia_pozycji2))[0], (rysuj(historia_pozycji2))[1])

        plt.plot((rysuj(historia_pozycji3))[0], (rysuj(historia_pozycji3))[1])
        for i in range(0, len((rysuj(historia_pozycji3))[0])):
            plt.annotate(i, ((rysuj(historia_pozycji3))[0][i], (rysuj(historia_pozycji3))[1][i]))
        plt.scatter((rysuj(historia_pozycji3))[0], (rysuj(historia_pozycji3))[1])


    img = mpimg.imread('mapapro1.png')
    plt.imshow(img, extent=[-32, 32.0, -32.0, 32.0])

    plt.show()
    del txt
