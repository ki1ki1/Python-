# argumenty pozycyjne
def dodaj(liczba1, liczba2):
    return liczba1 + liczba2

dodaj(1, 2)

# wartosci domyślne
def witaj(imie = 'Jan', nazwisko = 'Kowalski'):
    print(f'Witaj {imie} {nazwisko}!')

witaj()

# def witaj(nazwisko='Kowalski', imie):
    # print(f'Witaj {imie} {nazwisko}!') - błędna

witaj('Malinowski')

def dodaj(* liczby):
    suma = 0
    [suma+=liczba for liczba in liczby]
    return suma

def dodaj(* liczby):
    # return sum[liczby for liczba in liczby]
    return suma(liczby)

print(dodaj(1, 2))
dodaj(1,2,3,4)
print(dodaj(1,2,98678,34536125))
