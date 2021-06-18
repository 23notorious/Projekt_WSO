import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg

historia_pozycji = [line.split() for line in open('pozycje.txt')]  # opens the text file and calls .split() on every line, effectively splitting on every space, creating a list of numbers.

# print(lines)

# pozycje = open("pozycje.txt","r")
# historia_pozycji = list(pozycje.read().splitlines())
# print(historia_pozycji)

def Pierwsza(x):
    return [item[0] for item in x]
def Druga(y):
    return [item[1] for item in y]
y = []
g = []
for i in enumerate(historia_pozycji):
    print("Pozycja w chwili",i[0],"to",i[1])
   
    y.append(i[0])
    
x = Pierwsza(historia_pozycji)
y = Druga(historia_pozycji)
print(Pierwsza(historia_pozycji))
print(Druga(historia_pozycji))

plt.plot(x,y)
for i in range(0, len(historia_pozycji)):
    plt.annotate(i, (x[i], y[i]))
plt.scatter(x, y)

img = mpimg.imread('D:\Python\mapapro1.png')
plt.imshow(img, extent=[-33, 33.0, -33.0, 33.0])

plt.show()
