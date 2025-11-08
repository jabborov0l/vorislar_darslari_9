# #For10.
# n = int(input("n = "))
# S = 0
# for i in range(1, n+1):
#     S += 1 / i
# print("Yig‘indi S =", S)

# #For11.
# n = int(input("n = "))
# S = 0
# for i in range(n, 2*n + 1):
#     S += i**2
# print("Yig‘indi S =", S)

# #For13.
# n = int(input("n = "))
# S = 1
# for i in range(1, n+1):
#     S *= 1 + 0.1 * i
# print("Ko‘paytma S =", S)

# #For14.
# n = int(input("n = "))
# kvadrat = 0
# for i in range(1, 2*n, 2):
#     kvadrat += i
# print("Natija:", kvadrat)

# #For15.
# a = float(input("a = "))
# n = int(input("n = "))
# natija = 1
# for i in range(n):
#     natija *= a
# print("Natija:", natija)

# #For16.
# a = float(input("a = "))
# n = int(input("n = "))
# for i in range(1, n+1):
#     print(f"a^{i} =", a**i)

# #For17.
# a = float(input("a = "))
# n = int(input("n = "))
# yigindi = 0
# for i in range(n+1):
#     yigindi += a**i
# print("Yig‘indi:", yigindi)

# #For18.
# a = float(input("a = "))
# n = int(input("n = "))
# yigindi = 0
# for i in range(n+1):
#     yigindi += (-1)**i * (a**i)
# print("Yig‘indi:", yigindi)

# #For19.
# n = int(input("n = "))
# fakt = 1
# for i in range(1, n+1):
#     fakt *= i
# print("Faktorial:", fakt)

# #For20.
# n = int(input("n = "))
# yigindi = 0
# fakt = 1
# for i in range(1, n+1):
#     fakt *= i
#     yigindi += fakt
# print("Yig‘indi:", yigindi)

# #For21.
# n = int(input("n = "))
# yigindi = 1
# fakt = 1
# for i in range(1, n+1):
#     fakt *= i
#     yigindi += 1/fakt
# print("Yig‘indi:", yigindi)

# #For22.
# x = float(input("x = "))
# n = int(input("n = "))
# yigindi = x
# fakt = 1
# for i in range(2, n+1):
#     fakt *= i
#     yigindi += (x**i) / fakt
# print("Yig‘indi:", yigindi)

# #For23.
# x = float(input("x = "))
# n = int(input("n = "))
# yigindi = 0
# for i in range(n+1):
#     fakt = 1
#     for j in range(1, 2*i+2):
#         fakt *= j
#     yigindi += ((-1)**i) * (x**(2*i+1)) / fakt
# print("Yig‘indi:", yigindi)

# #For24.
# x = float(input("x = "))
# n = int(input("n = "))
# yigindi = 1
# for i in range(1, n+1):
#     fakt = 1
#     for j in range(1, 2*i+1):
#         fakt *= j
#     yigindi += ((-1)**i) * (x**(2*i)) / fakt
# print("Yig‘indi:", yigindi)

# #For25.
# x = float(input("x = "))
# n = int(input("n = "))
# yigindi = 0
# for i in range(1, n+1):
#     yigindi += ((-1)**(i-1)) * (x**i) / i
# print("Yig‘indi:", yigindi)
