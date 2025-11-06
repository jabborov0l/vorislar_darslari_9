# For sikl operatoiga oid masalalar
# For1.
# k = int(input("k ni kiriting"))
# n = int(input("n ni kiriting"))
# for _ in range(n):
#     print(k)

# For2.
# a = int(input("a ni kiriting"))
# b = int(input("b ni kiriting"))
# royhat = len(range(a,b+1))
# for i in range(a, b+1):
#        print(i)
# print(royhat)

# For3.
# a = int(input("a ni kiriting"))
# b = int(input("b ni kiriting"))
# royhat = len(range(a+1,b))
# royhat = sorted(range(a+1,b), reverse=True)
# for i in range(b, a):
#     print(i)
# print(royhat)
# print(len(royhat))

#For4.
# narx = int(input("1 kg konfet narxini kiriting"))
# for i in range(1,11):
#       print(i * narx)

# For5.
# narx = int(input("1 kg konfet narxini kiriting"))
# for i in range(1, 11):
#       print(i/10 * narx)

#For6.
# narx = int(input("1 kg konfet narxini kiriting"))
# for i in range(12, 21, 2):
#        print(i/10 * narx)

#For7.
# a = int(input("a ni kiriting"))
# b = int(input("b ni kiriting"))

# son = list(range(a, b+1))

# print(sum(son))

#For8.
# a = int(input("a ni kiriting : "))
# b = int(input("b ni kiriting : "))
# kopaytma = 1
# sonlar = list(range(a, b+1))
# print(f"Royhat : {sonlar}")
# for i in sonlar:
#     kopaytma *= i # kopaytma = kopaytma * i    
# print(f"Royhatning kopaytmasi : {kopaytma}")

#for9.
a = int(input("a ni kiriting : "))
b = int(input("b ni kiriting : "))
kopaytma = 0
for i in range(a, b+1):
    kopaytma += i ** 2
print(kopaytma)
