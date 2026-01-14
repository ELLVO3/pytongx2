set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set2 = {10, 11, 2, 1, 3, 4, 5, 13}
set3 = {10, 11, 14, 15, 1, 2, 3}


# (a) Utworzą zbiór tych wszystkich elementów, które
# należą do set1 lub w set2, ale nie należą do obydwu jednocześnie.
seta = set1 ^ set2
print(seta)


# (b) Utworzą zbiór tych wszystkich elementów, które
# należą tylko do jednego z trzech zbiórów set1, set2 i set3.
setb = set1 - set2 - set3
print(setb)


# (c) Utwórzą zbiór wszystkich elementów, które
# należą do dokładnie dwóch zbiorów spośród set1, set2 i set3.
setc = (set1 & set2) - set3 | (set1 & set3) - set2 | (set2 & set3) - set1
print(setc)

# (d) Utwórzą zbiór wszystkich tych liczb całkowitych w zakresie od 1 do 25, które
# nie należą do set1.
wszystie = set(range(1, 26))

setd = wszystie - set1
print(setd)

# (e) Utwórzą zbiór wszystkich tych liczb całkowitych w zakresie od 1 do 25, które
# nie należą do któregoś z trzech zbiórów set1, set2 i set3.
sete = wszystie - (set1 | set2 | set3)
print(sete)