import math

def zad1():

    n = abs(int(input("Podaj liczbę naturalną n (ilość): ")))

    for i in range (n):
        a = int(input("Wprowadź liczbę: "))
        if(a % 2 != 0):
            print("Ta liczba jest nieparzysta:", a)
        else:
            print("Ta liczba nie jest nieparzysta:", a)

def zad2():

    n = abs(int(input("Podaj liczbę naturalną n (ilość): ")))

    for i in range(n):
        a = int(input("Wprowadź liczbę: "))
        if(a % 3 == 0 and a % 5 != 0):
            print("Ta liczba spełnia warunek a % 3 == 0 and a % 5 != 0:", a)
        else:
            print("ta liczba nie spełnia warunku a % 3 == 0 and a % 5 != 0:", a)


def zad3():

    n = abs(int(input("Podaj liczbę naturalną n (ilość): ")))

    for i in range(n):
        a = int(input("Wprowadź liczbę: "))
        if(math.sqrt(a) % 2 == 0):
            print("To jest kwadrat liczby parzystej:", a)
        elif(a == 0):
            print("To jest kwadrat liczby parzystej:", a)
        else:
            print("To nie jest kwadrat liczby parzystej:", a)


def zad4():
    n = abs(int(input("Podaj liczbę naturalną n (ilość): ")))

    a1 = abs(int(input("Podaj liczbę: ")))
    a2 = abs(int(input("Podaj liczbę: ")))
    counter = 0

    for k in range(2, n):
        a3 = abs(int(input("Podaj liczbę: ")))
        if(a2 < (a1 + a3)/2):
            counter += 1
        a1 = a2
        a2 = a3
    print(counter)


def main():
    # zad1()
    # zad2()
    # zad3()
    zad4()


main()