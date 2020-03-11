for znak in "Wojtek":
    print(znak)

litery = [print(znak) for znak in "Wojtek"]
print(type(litery))
print(litery)

M=[
    [1, 2],
    [3,4]
]

[print(liczba) for wiersz in M for liczba in wiersz]

# for wiersz in M:
    # for liczba i wiersz:
        # print(wiersz)

import this #pep20 - Python manifest

# krotka - tuple, nie jest mutowalna
# pakowanie krotki
punkt = (0, 0)
# rozpakowywanie krotki
x, y = (120, 130)
# (index, wartosc, pesel, imie, nazwisko, wiek,...)

{krotka[0]:krotka[1] for krotka in enumerate ("Wojtek")}
{indeks:litera for indeks, litera  in enumerate ("Wojtek")}


slownik = {'imie':'Marian', 'nazwisko':'Bąbel'}
# for _ in slownik:
    #print(_)

 # {wartosc:klucz for klucz, wartosc in slownik.items()}
 # {klucz for klucz in slownik.keys()}

# timeit
# jaka jest różnica przy inicjalizacji
lista = list()
lista2 = []

wielkie = [znak.upper() for znak in "Wojtek"]
print(wielkie)
# to samo ^ v
wielkie = [str.upper(znak) for znak in "Wojtek"]
print(wielkie)