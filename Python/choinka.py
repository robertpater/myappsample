print("UWAGA! Rysujemy choinke!")
wysokosc = int(input("Podaj wysokosc chonki: "))
print('\n')
zmiennaX = wysokosc
zmiennaY = 1
for i in range(0, wysokosc):
    print(zmiennaX * " " + zmiennaY * "*")
    zmiennaX -= 1
    zmiennaY += 2
zmiennaX = wysokosc
for i in range(0, 3):
    print((zmiennaX - 1) * " " + 3 * "|")
print(2 * wysokosc * "^")

print('\n')
print('\n')


#    *
#   ***
#  *****
# *******
#   |||
#   |||
