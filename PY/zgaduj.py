

import random
wymyslona = random.randint(0, 100)
print('Wymyslilem liczbe')
print(wymyslona)

licznik = 0


while(1):
    licznik += 1
    liczba = int(input('Podaj liczbe od 0 do 100: '))

    if liczba == wymyslona:
        print('w koncu udalo sie !! liczba prob= ', licznik)
        break

    if liczba < wymyslona:
        print('za malo')
    else:
        print('za duzo')


for num in [1, 2, 3, 4]:
    print(num)
