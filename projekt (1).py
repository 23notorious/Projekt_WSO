from os import lseek
import random

j = random.randint(-10,10)
k = random.randint(-10,10)
pozycja = [j,k]
historia_pozycji = []

# print(pozycja)
licznik = 0
y = []
g = []
while(licznik < 100):
    przesuwak = random.choice([-1, 0, 1])
    kierunek = random.choice([0, 1])

    ostatnio = list(pozycja)
    if (kierunek == 0):
        pozycja[0] += przesuwak
    elif (kierunek == 1):
        pozycja[1] += przesuwak

    if(ostatnio == pozycja):
        continue

    licznik += 1
    historia_pozycji.append(list(pozycja))



with open("pozycje.txt",'w') as output:
    for element in historia_pozycji:
        x = ' '.join(map(str, element)) + ' \n'
        output.write(str(x))
    
    # print(historia_pozycji)
    