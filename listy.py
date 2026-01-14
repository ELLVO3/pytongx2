import math

# Zadanie 7

def zadanie7():
    lista = []

    while len(lista) < 10:
        try:
            liczba = int(input("Podaj liczbę: "))

            if liczba not in lista:
                lista.append(liczba)
            else:
                print("Ta liczba już jest w liście")
        except ValueError:
            print("To nie jest poprawna liczba")
    print("Pełna lista: ", lista)


# Zadnaie 9

def zamien_skrajne(lista):
    if len(lista) < 2:
        return lista
    lista[0], lista[-1] = lista[-1], lista[0]
    return lista

def przesun_w_prawo(lista):
    if len(lista) < 2:
        return lista
    # Ostatni element + reszta listy bez ostatniego
    return [lista[-1]] + lista[:-1]

def zeruj_parzyste(lista):
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            lista[i] = 0
    return lista

def wiekszy_sasiad(lista):
    if len(lista) < 3:
        return lista

    nowa_lista = list(lista)
    for i in range(1, len(lista) - 1):
        nowa_lista[i] = max(lista[i-1], lista[i+1])
    return nowa_lista

def usun_srodek(lista):
    if len(lista) == 0:
        return lista

    srodek = len(lista) // 2

    if len(lista) % 2 != 0:
        lista.pop(srodek)

    else:
        lista.pop(srodek)
        lista.pop(srodek - 1)

    return lista

def parzyste_na_poczatek(lista):
    parzyste = [x for x in lista if x % 2 == 0]
    nieparzyste = [x for x in lista if x % 2 != 0]
    return parzyste + nieparzyste

def drugi_najwiekszy(lista):
    if len(lista) < 2:
        return None

    unikalne = sorted(list(set(lista)))
    if len(unikalne) < 2:
        return None
    return unikalne[-2]

def czy_posortowana(lista):
    if lista != sorted(lista):
        return False
    return True

def czy_duplikaty_obok(lista):
    for i in range(len(lista) - 1):
        if lista[i] == lista[i+1]:
            return True
    return False

def czy_duplikaty(lista):
    if len(lista) != len(set(lista)):
        return True
    return False


# Zadanie 10

def equals(a, b):
    if a != b:
        return False
    return True

def main():

    # zadanie7()

    # (a)
    print(zamien_skrajne([1, 4, 9, 16, 25]))

    # (b)
    print(przesun_w_prawo([1, 4, 9, 16, 25]))

    # (c)
    print(zeruj_parzyste([1, 2, 3, 4, 5]))

    # (d)
    print(wiekszy_sasiad([1, 10, 5, 20, 2]))

    # (e) - przykład nieparzysty
    print(usun_srodek([1, 2, 3, 4, 5]))
    # (e) - przykład parzysty
    print(usun_srodek([1, 2, 3, 4, 5, 6]))

    # (f)
    print(parzyste_na_poczatek([1, 2, 3, 4, 5, 6]))

    # (g)
    print(drugi_najwiekszy([10, 20, 4, 4, 20, 5]))

    # (h)
    print(czy_posortowana([1, 2, 3]))
    print(czy_posortowana([1, 3, 2]))

    # (i)
    print(czy_duplikaty_obok([1, 2, 2, 3]))

    # (j)
    print(czy_duplikaty([1, 2, 3, 1]))

    # Test 1: Listy identyczne -> True
    print(equals([1, 2, 3], [1, 2, 3]))

    # Test 2: Inny element -> False
    print(equals([1, 2, 3], [1, 2, 4]))

    # Test 3: Ta sama zawartość, inna kolejność -> False
    print(equals([1, 2, 3], [3, 2, 1]))

    # Test 4: Różna długość -> False
    print(equals([1, 2], [1, 2, 3]))

main()