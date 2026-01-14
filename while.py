import math

# Zad 1

def potegaDwojki(n):
    wynik = 1
    licznik = 1

    while licznik <= n:
        wynik *= 2
        licznik += 1
    return wynik


def silnia(n):
    wynik = 1
    licznik = 1

    while licznik <= n:
        wynik *= licznik
        licznik += 1
    return wynik


def iloczynSzeregu(n):
    wynik = 1.0
    i = 1

    while i <= n:
        skladnik = 1 + (1/(i * i))
        wynik *= skladnik
        i += 1
    return wynik


def sumaOdwrotnosciSinusow(n):
    if n == 0:
        return 0

    podsuma = math.sin(1)
    wynik = 1 / (1 + podsuma)
    i = 2

    while i <= n:
        podsuma += math.sin(i)
        wynik += 1 / podsuma
        i += 1
    return wynik

# Zad 2

def potega(a, n):
    wynik = 1
    licznik = 1

    while licznik <= n:
        wynik *= a
        licznik += 1
    return wynik


def iloczynRosnacy(a, n):
    wynik = 1
    i = 0

    while i < n:
        wynik *= a + i
        i += 1
    return wynik


def sumaOdwrotnosciIloczynu(a, n):
    mianownik = 1
    suma = 0
    i = 0

    while i <= n:
        mianownik *= a + i
        suma += 1/mianownik
        i += 1
    return suma


def sumaPotegGeometrycznych(a, n):
    suma = 0
    aktualnyMianownik = a
    i = 0

    while i <= n:
        suma += 1/aktualnyMianownik
        aktualnyMianownik *= aktualnyMianownik
        i += 1
    return suma


def iloczynMalejacy(a, n):
    wynik = 1
    i = 0
    while i <= n:
        wynik *= a - (i * n)
        i += 1
    return wynik


# Zad 3

def szerergSinusa(x):
    wyraz = x
    suma = x
    i = 3

    while i <= 13:
        mnoznik = (-1 * x * x) / (i * (i - 1))
        wyraz *= mnoznik

        suma += wyraz
        i += 2
    return suma


def ulamkiPotegi(x):
    licznikWynik = 1
    mianownikWynik = 1
    i = 2

    while i <= 64:
        licznikWynik *= (x - i)
        mianownikWynik *= (x - (i - 1))
        i *= 2

    if mianownikWynik == 0:
        return None

    return licznikWynik / mianownikWynik


def sumaPotegiSinusa(x, n):
    sin_x = math.sin(x)
    aktualny_skladnik = sin_x
    suma = 0
    i = 1

    while i <= n:
        suma += aktualny_skladnik
        aktualny_skladnik *= sin_x
        i += 1
    return suma


def sumaSinusowPotegiArgumentu(x, n):
    aktualny_skladnik = x
    suma = 0
    i = 1

    while i <= n:
        suma += math.sin(aktualny_skladnik)
        aktualny_skladnik *= x
        i += 1
    return suma


def sumaZagniezdzonychSinusow(x, n):
    aktualna_wartosc = math.sin(x)
    suma = 0
    i = 1

    while i <= n:
        suma += aktualna_wartosc
        aktualna_wartosc = math.sin(aktualna_wartosc)
        i += 1
    return suma


# Zad 4

def zadanie4a(a):
    suma = 0.0
    i = 1

    while suma <= a:
        suma += (1/i)
        i += 1
    return suma


def zadanie4b(a):
    suma = 0.0
    i = 0

    while suma <= a:
        i += 1
        suma += (1 / i)
    return i


# Zad 5

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


# Zad 6

def sumaKoncowychCyfr(m, n):
    suma = 0
    licznik = 0

    while licznik < m:
        if n == 0:
            print("Niepoprawne dane")
            return None
        cyfra = n%10
        suma += cyfra
        n //= 10
        licznik += 1
    return suma


# Zad 7

def czyPierwsza(n):
    if n < 2:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


# Zad 8

def wypiszPierwszeWPrzedziale(m, n):
    i = m

    while i <= n:
        if czyPierwsza(i) == True:
            print(i)
        i += 1


# Zad 9

def IlePierwszychWPrzedziale(m, n):
    i = m
    suma = 0
    while i <= n:
        if czyPierwsza(i) == True:
            suma += 1
        i += 1
    return suma


# Zad 10

def sumaWczytanych(n):
    suma = 0
    i = 1

    while i <= n:
        a = int(input("Podaj liczbę a: "))
        suma += a
        i += 1
    return suma


def iloczynWczytanych(n):
    iloczyn = 1
    i = 1

    while i <= n:
        a = int(input("Podaj liczbę a: "))
        iloczyn *= a
        i += 1
    return iloczyn


def sumaOrazIloczyn(n):
    suma = 0.0
    iloczyn = 1
    i = 1

    while i <= n:
        a = float(input("Wczytaj liczbę rzeczywistą a: "))
        suma += a
        iloczyn *= a
        i += 1
    return suma, iloczyn



def sumaNaprzemienna(n):
    suma = 0.0
    znak = 1
    i = 1

    while i <= n:
        a = int(input("Podaj liczbę a: "))
        suma += a * znak
        znak *= -1
        i += 1
    return suma


def sumaZSilnia(n):
    suma = 0.0
    silnia = 1
    znak = -1
    i = 1

    while i <= n:
        a = int(input("Podaj liczbę a: "))
        silnia *= i
        wyraz = (znak * a) / silnia
        suma += wyraz
        znak *= -1
        i += 1
    return suma

def main():

    # n = int(input("Podaj liczbę n: "))
    # print(potegaDwojki(n))
    # print(silnia(n))
    # print(iloczynSzeregu(n))
    # print(sumaOdwrotnosciSinusow(n))



    # a = float(input("Podaj liczbę rzeczywistą a: "))
    # n = int(input("Podaj liczbę naturalną n: "))
    # print(potega(a, n))
    # print(iloczynRosnacy(a, n))
    # print(sumaOdwrotnosciIloczynu(a, n))
    # print(sumaPotegGeometrycznych(a, n))
    # print(iloczynMalejacy(a, n))



    # x = float(input("Podaj liczbę rzeczywistą x: "))
    # n = int(input("Podaj licznę naturalną n: "))
    # print(szerergSinusa(x))
    # print(ulamkiPotegi(x))
    # print(sumaPotegiSinusa(x, n))
    # print(sumaSinusowPotegiArgumentu(x, n))
    # print(sumaZagniezdzonychSinusow(x, n))



    # a = float(input("Podaj liczbę rzeczywistą a: "))
    # print(zadanie4a(a))
    # print(zadanie4b(a))



    # n = int(input("Podaj liczbę naturalną n: "))
    # zadanie5(n)

    # n = int(input("Podaj liczbę naturalną n: "))
    # m = int(input("Podaj liczbę naturalną m: "))
    # print(sumaKoncowychCyfr(n, m))



    # n = int(input("Podaj liczbę naturalną n: "))
    # print(czyPierwsza(n))



    # m = int(input("Podaj liczbę naturalną m: "))
    # n = int(input("Podaj liczbę naturalną n: "))
    # wypiszPierwszeWPrzedziale(m, n)



    # m = int(input("Podaj liczbę naturalną m: "))
    # n = int(input("Podaj liczbę naturalną n: "))
    # print(IlePierwszychWPrzedziale(m, n))

    n = int(input("Podaj liczbę naturalną n: "))
    print(sumaOrazIloczyn(n))

main()