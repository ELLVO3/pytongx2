import math

def zad1(a):

    """
    Użytkownik wprowadza liczbę zmiennoprzecinkową, jeśli podana liczba jest < 0, to zachodzi wartość bezwzględna
    a jeśli podana liczba jest >= 0 to znak się nie zmienia
    """

    a = float(input("Podaj liczbę zmiennoprzecinkową: "))
    if a < 0:
        a *= -1
    print(a)

def zad2():
    """
    Użytkownik podaje liczbę od minus nieskończoności do plus nieskończoności, jeśli liczba jest > 0, to
    funkcja zwraca 1, jeśli jest == 0, to funkcja zwraca 0, a w innym przypadku zwraca -1
    """

    def sgn(x):
        if x < 0:
            return -1
        elif x == 0:
            return 0
        else:
            return 1
    print(sgn(x=-10))

def zad3():

    """
    Użytkownik wprowadza 2 liczby i funkcja wypisuje wynik dzielenia pierwszej przez drugą o ile druga != 0
    """

    a = float(input("Podaj pierwszą liczbę zmiennoprzecinkową: "))
    b = float(input("Podaj drugą liczbę zmiennoprzecinkową: "))

    if b == 0:
        print("Nie dzieli się przez 0")
    else:
        print(a/b)

def zad4(a, b):

    """
    Funkcja rozwiązuje równanie liniowe:

    jeśli a == 0 i b == 0 -> Nieskończenie wiele rozwiązań
    jeśli a == 0 i b != 0 -> Brak roziwązań
    jeśli a != 0 i b != 0 -> Jedno rozwiązanie
    """

    if a == 0:
        if b == 0:
            print("Nieskończenie wiele rozwiązań")
        else:
            print("Brak rozwiązań")
    else:
        x = -(b / a)
        print("Rozwiązanie:", x)

def zad5(a, b, c):

    """
    Użytkownik podaje 3 liczby i z nich wypisuje się największą i najmniejszą liczbę
    """

    najw = a
    najm = a

    if b > najw:
        najw = b

    if c > najw:
        najw = c

    if b < najm:
        najm = b

    if c < najm:
        najm = c

    print("Największa:", najw, "Najmniejsza:", najm)

def zad6():

    """
    Użytkownik ponownie wprowadza 3 liczby tylko tym razem korzysta z funkcji max3(arg x, arg y, arg z)
    i funkcja wypisuje największą z nich
    """

    def max3(x, y, z):
        najw = x

        if z > najw:
            najw = z
        if y > najw:
            najw = y
        return najw

    print(max3(11, 222, 41))

def zad7():

    """
    Użytkownik wprowadza z klawiatury 3 liczby, a program sprawdza czy z podanych długości boków można utworzyć
    trójkąt, i jeśli tak to liczy obwód trójkąta o podanych bokach i jego pole.
    Jeśli boki się nie zgadzają to program wypisuje komunikat: To nie są boki trójkąta! Kończę program.
    """

    a = float(input("Podaj pierwszy bok trójkąta: "))
    b = float(input("Podaj drugi bok trójkąta: "))
    c = float(input("Podaj trzeci bok trójkąta: "))

    if a > 0 and b > 0 and c > 0 and (a + b > c and a + c > b and b + c > a):
        obw = a + b + c
        p = obw/2
        Po = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("Obwód trójkąta:", obw)
        print("Pole trójkąta:", Po)

    else:
        print("To nie są boki trójkąta! Kończę program.")



def poprawne_boki(a, b, c):
    if a > 0 and b > 0 and c > 0 and (a + b > c and a + c > b and b + c > a):
        return True
    else:
        return False

def obwod_trojkata(a, b, c):
    obw = a + b + c
    return obw

def pole_trojkata(a, b, c):
    obw = a + b + c
    p = obw/2
    Po = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return Po



def zad8():

    """
    Użytkownik wczytuje trzy długości boków. Używając funkcja: poprawne_boki(a, b, c), program sprawdza czy podane boki
    tworzą trójkąt i jeśli nie to od razu kończy program, a jeśli boki się zgadzają
    to program liczy obwód i pole trójkąta.
    """

    a = float(input("Podaj pierwszy bok trójkąta: "))
    b = float(input("Podaj drugi bok trójkąta: "))
    c = float(input("Podaj trzeci bok trójkąta: "))

    if poprawne_boki(a, b, c):
        obw = obwod_trojkata(a, b, c)
        po = pole_trojkata(a, b, c)
        print("Obwód:", obw)
        print("Pole:", po)
    else:
        print("To nie są boki trójkąta! Kończę program.")

def main():

    zad1(-4)
    zad2()
    zad3()
    zad4(2, 6)
    zad5(-10,-1, -3)
    zad6()
    zad7()
    zad8()

main()