# Zadanie 1

def zadanie1a(lancuch):
    slownik = {}
    for znak in lancuch:
        # To jest ten sam mechanizm co przy liczbach:
        # Jeśli znaku nie ma, weź 0 i dodaj 1.
        # Jeśli jest, weź obecną wartość i dodaj 1.
        slownik[znak] = slownik.get(znak, 0) + 1
    return slownik

def zadanie1b(lancuch):
    slownik = {}
    for znak in lancuch:
        if znak.isalpha():
            slownik[znak] = slownik.get(znak, 0) + 1
    return slownik

def zadanie1c(lancuch):
    slownik = {}
    for znak in lancuch:
        if znak.isalpha():
            znak_lower = znak.lower()
            slownik[znak_lower] = slownik.get(znak_lower, 0) + 1
    return slownik

def zadanie1d(lancuch):
    slownik = {}
    for znak in lancuch:
        if znak.isalpha():
            slownik[znak] = slownik.get(znak, 0) + 1

    najczestsza = max(slownik, key=slownik.get)
    return najczestsza


# Zadanie 2

def zadanie2():
    slownik = {}
    print("Podaj liczby (pusty Enter kończy):")
    while True:
        tekst = input()
        if not tekst:
            break

        # Standardowa metoda .isdigit() sprawdza tylko, czy znaki są cyframi (0-9).
        # Dla liczby "-5" zwróciłaby False, ponieważ znak minusa - nie jest cyfrą.
        # Użycie .lstrip('-') powoduje, że jeśli na początku tekstu jest minus,
        # to zostaje on tymczasowo "odcięty".
        # Dopiero ten "oczyszczony" z minusa tekst jest sprawdzany przez .isdigit().

        if tekst.lstrip('-').isdigit():
            liczba = int(tekst)
            slownik[liczba] = slownik.get(liczba, 0) + 1
    print(slownik)


def zadanie3():
    slownik = {}
    with open('readme.txt', 'r') as f:
        tekst = f.read()
        for znak in tekst:
            if znak.isalpha():
                slownik[znak] = slownik.get(znak, 0) + 1
    print(slownik)

def zadanie4():
    slownik = {}
    with open('readme.txt', 'r') as f:
        for linia in f:
            for element in linia.split():
                if element.lstrip('-').isdigit():
                    liczba = int(element)
                    slownik[liczba] = slownik.get(liczba, 0) + 1
    return slownik



def main():
    tekst = "Abrakadabra"
    print("1a:", zadanie1a(tekst))
    print("1b:", zadanie1b(tekst))
    print("1c:", zadanie1c(tekst))
    print("1d:", zadanie1d(tekst))

    with open('readme.txt', 'r') as f:
        print("1a (plik):", zadanie1a(f.read()))

    with open('readme.txt', 'r') as f:
        print("1b (plik):", zadanie1b(f.read()))

    with open('readme.txt', 'r') as f:
        print("1c (plik):", zadanie1c(f.read()))

    with open('readme.txt', 'r', encoding='utf-8') as f:
        print("1d (plik):", zadanie1d(f.read()))

    zadanie2()
    zadanie3()
    print(zadanie4())

main()