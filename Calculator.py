menu = int(input('Vyber si operaciu\n'+
                 '1.Plus\n'+
                 '2.Minus\n'+
                 '3.Krat\n'+
                 '4.Delene'))

if menu == 1:
    cislo1 = int(input('Zadaj prve cislo: '))
    cislo2 = int(input('Zadaj druhe cislo: '))
    print('Vysledok = ',cislo1+ cislo2)
    
if menu == 2:
    cislo1 = int(input('Zadaj prve cislo: '))
    cislo2 = int(input('Zadaj druhe cislo: '))
    print('Vysledok = ',cislo1- cislo2)

if menu == 3:
    cislo1 = int(input('Zadaj prve cislo: '))
    cislo2 = int(input('Zadaj druhe cislo: '))
    print('Vysledok = ',cislo1* cislo2)
    
if menu == 4:
    cislo1 = int(input('Zadaj prve cislo: '))
    cislo2 = int(input('Zadaj druhe cislo: '))
    print('Vysledok = ',cislo1 / cislo2)