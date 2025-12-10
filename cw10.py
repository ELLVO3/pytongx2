set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set2 = {10, 11, 2, 1, 3, 4, 5, 13}
set3 = {10, 11, 14, 15, 1, 2, 3}

seta = set1 ^ set2
print(seta)

setb = set1 - set2 - set3
print(setb)

setc = set1 & set2 and set1 & set3 and set2 & set3
print(setc)
