# # Tuple o'zgarmas ro'yhat
# ismlar = ["Elbek", "Ixtiyor"]             # oddiy ro'yhat
# familiya = ("Karimboyev", "Abdullayev")   # o'zgarmas ro'yhat
# print("oddiy ro'yhat:", ismlar)
# print("o'zgarmas ro'yhat", familiya)

# ismlar.append("sardor")
# print(ismlar)

# familiya.append("Toshboyev")
# print(familiya)

# o_familiya = list(familiya)
# print(o_familiya)  # tupleni listga aylantiramiz

# o_familiya.append("Toshboyev")
# print(familiya) # endi yangi element qo'shamiz

# familiya = tuple(o_familiya) # listni yana tuplega o'zgartiramiz
# print(familiya)

# Amaliyot
davlatlar = ["Norvegiya", "Britaniya", "Cameroon"]
print(davlatlar)

print(len(davlatlar))

tartiblangan = sorted(davlatlar)
print(tartiblangan)

teskari = sorted(davlatlar, reverse=True)
print(teskari)

davlatlar.sort()
print(davlatlar)

davlatlar.reverse()
print(davlatlar)

davlatlar.sort()
print(davlatlar)

davlatlar.sort(reverse=True)
print(davlatlar)

sonlar = list(range(120,2000,2))
print(sonlar)







