# Zadanie 1

lista1 = []

for i in range(1, 11):
    lista1.append(i)

print(lista1)

###

lista2 = []

for i in range(0, 22, 2):
    lista2.append(i)

print(lista2)

###

lista3 = []

for i in range(1, 11):
    lista3.append(i**2)

print(lista3)

###

lista4 = []

for i in range(1, 11):
    lista4.append(0)

print(lista4)

###

lista5 = []

for i in range(0, 11):
    if i % 2 == 0:
        lista5.append(0)
    else:
        lista5.append(1)

print(lista5)

###

lista6 = []

for i in range(0, 5):
    lista6.append(i)

for i in range(0, 5):
    lista6.append(i)

print(lista6)

###

# Zadanie 5

def minmax(a):

    najwieksza = a[0]
    najmniejsza = a[0]

    for i in range(0, len(a)):
        if a[i] < najmniejsza:
            najmniejsza = a[i]
        else:
            najwieksza = a[i]

    return najmniejsza, najwieksza

# Zadanie 6

def alternateSum(b):

    suma = 0

    for i in range(len(b)):
        if i % 2 != 0:
            b[i] *= -1
        suma += b[i]
    return suma

###

# Zadanie 8

def list_appender(start, stop):
    lista = []
    for i in range(start, stop):
        lista.append(i)
    return lista

def list_remover(lista):
    for i in range(2, 100):
        for j in lista[:]:
            if j % i == 0 and j != i:
                lista.remove(j)
    return lista

def list_remover2(lista):
    for i in range(2, 100):
        idx = 0
        while idx < len(lista):
            if lista[idx] % i == 0 and lista[idx] != i:
                lista.pop(idx)
                continue
            idx += 1
    return lista


def main():
    a = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    b = [1, 4, 9, 16, 9, 7, 4, 9, 11]

    print(minmax(a))
    print(alternateSum(b))

    # print(list_remover(list_appender(2, 10001)))
    print(list_remover2(list_appender(2, 10001)))

main()