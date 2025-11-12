import math


def niepodzielne():
    n = int(input("Podaj liczbę naturalną n: "))


    if n >= 0:
        counter = 0
        for i in range (1, n+1):
            if i % 3 != 0 and i % 5 != 0:
                counter += 1
        print(counter)
    else:
        print("Nie podano liczby naturalnej")


def nieparzyste(n):
    counter = 0

    for i in range(n):
        a = int(input("Podaj liczbę: "))
        if a % 2 != 0:
            counter += 1
    return counter


def obliczenie(n):
    mianownik = 0
    wynik = 0
    for i in range (2, n+1):

        mianownik += math.cos(i)
        wynik += 1/mianownik

    print(wynik)


def main():
    print("Zad1: ")
    niepodzielne()

    n = int(input("Wpisz liczbę naturalną: "))
    if(n >= 0):
        print("Zad2: ")
        print(nieparzyste(n))
        print("Zad3: ")
        obliczenie(n)
    else:
        print("Wpisana liczba nie jest naturalną liczbą")
        
main()
