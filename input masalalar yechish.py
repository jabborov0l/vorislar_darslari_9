

#ism = input("ismingiz nima?")
#print("Assalomu alaykum", ism)

#print("kiritilgan sonning kvadrati:", son*son)
#ism3 = input("onangizni ismi nima?")
#ism4 = input("ukangizni ismi nima?")
#print("salom hurmatli", + ism)
#ism5 = input(Elbek)


 #Kvadratning tomoni
#a = float(input("Kvadratning tomonini kiriting: "))

 #Begin1.
#P = 4 * a
#print("Kvadratning perimetri:", P)

import math

son = int(input("kvadratning tomonini kiriting"))
S = son * son
print("Kvadratning yuzi:", S)
# begin5.

# Kubning qirrasi
a = float(input("Kubning qirrasini kiriting: "))

# Hajm va sirtni hisoblash
V = a ** 3
S = 6 * (a ** 2)

# Natijalarni chiqarish
print("Kubning hajmi:", V)
print("Kubning to‘la sirti:", S)

# begin14.
import math
# Aylana uzunligini kiriting
L = float(input("Aylana uzunligini kiriting : "))

# Radiusni hisoblash
r = L / (2 * math.pi)

# Yuzani hisoblash
S = math.pi * r ** 2

# Natijalarni chiqarish
print("Aylananing radiusi: ")
print("Aylananing yuzasi: ")

#begin23.

# A, B, C qiymatlarini kiritish
A = int(input("A ni kiriting: "))
B = int(input("B ni kiriting: "))
C = int(input("C ni kiriting: "))


# Qiymatlarni almashtirish
A = B
B = C
C = A

# NATiJA chiqarish
print("Qiymatlar almashtirilgandan so'ng:")
print(f"A = {A}")
print(f"B = {B}")
print(f"C = {C}")

# begin17.
# A, B, C qiymatlar kiritish
AB = int(input("AB ni kiriting"))
BC = int(input("BC ni kiriting"))
CA = int(input("CA ni kiriting"))

# AC va BC kesmalarni uzunligi va yig'indisini hisoblash.
AC = AB + BC
BC = AC - AB

# Natija chiqaramiz
print("AC kesmaning uzunligi=", AC)
print("BC kesmaning uzunligi=", BC)


