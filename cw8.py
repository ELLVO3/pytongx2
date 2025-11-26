import math


def zadanie1d(n):

    if n == 0:
        return 0

    podsuma = math.sin(1)
    wynik = 1 / (1 + podsuma)
    i = 2

    while i <= n:
        podsuma += 1 + math.sin(i)
        wynik += 1 / podsuma
        i += 1
    return wynik

def zadanie2a(n, a):

    if n == 0:
        return 1

    result = 1
    i = 0

    while i < n:
        result *= a
        i += 1
    return result

def zadanie2e(x, y):
    wynik = 1
    i = 0
    while i <= x:
        wynik *= (y - i * x)
        i += 1

    return wynik

def zadanie5(n):

    def zadanie5a(n):
        i = 0
        while n > 0:
            n //= 10
            i += 1
        return i

    def zadanie5b(n):
        suma = 0
        while n > 0:
            suma += n%10
            n //= 10
        return suma

    def zadanie5c(n):
        lastMeaningful = 0
        while n > 0:
            lastMeaningful = n
            n //= 10
        return lastMeaningful


    print(zadanie5a(n))
    print(zadanie5b(n))
    print(zadanie5c(n))


def main():
    n = int(input("Podaj liczbę naturalną n: "))
    a = float(input("Podaj liczbe rzeczywistą a: "))
    if n >= 0:
        # print(zadanie1d(n))
        # print(zadanie2a(n, a))
        # print(zadanie2e(n, a))
        print(zadanie5(n))

main()