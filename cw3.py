import math

# Cw 1a

"""

suma = 0

for i in range(2, 101, 2):
    suma += i

print(suma)

"""

# Cw 1b

"""

suma2 = 0

for i in range(1, 101):
    suma2 += i**2


print(suma2)

"""

# Cw 1c

"""

suma3 = 0

for i in range(2, 64):
    suma3 += 2**i

print(suma3)

"""

# Cw 1d

"""

a = int(input("Podaj zakres a (od): "))
b = int(input("Podaj zakres b (do (nie-włącznie)): "))

suma = 0

for i in range(a, b):
    if a > b:
        print("Zakresy niepoprawnie podane, try again")
    suma += i
print(suma)

"""

# Cw 2a

"""

def main2a():
    n = int(input("Podaj zakres n: "))
    suma = 0
    for i in range(n):
        a = float(input("Wpisz liczbę a: "))
        suma += a
    print(suma)
main2a()

"""

# Cw 2b

"""

def main2b():
    n = int(input("Podaj zakres n: "))
    iloczyn = 1
    for i in range(n):
        a = float(input("Wpisz liczbę a: "))
        iloczyn *= a
    print(iloczyn)
main2b()

"""

# Cw 2c

"""

def main2c():
    n = int(input("Podaj zakres n: "))
    suma = 0
    for i in range(n):
        a = float(input("Wpisz liczbę a: "))
        suma += abs(a)
    print(suma)
main2c()

"""

# Cw 2h

def main2h():
    n = int(input("Podaj zakres n: "))
    suma = 0
    for i in range(n):
        a = float(input("Wpisz liczbę a: "))
        suma += math.pow((-1), i) * a
    print(suma)

main2h()