lista = []
liczba = int(input("Podaj liczbe elementow: "))
for x in range(0, liczba, 1):
    lista.append(int(input()))

print("Twoje liczby to :", lista)
print("--------------------")
print("Najwieksza to: ", max(lista))
