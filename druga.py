#a = input()
#print(f"wprowadziłeś: {a}")
#print(type(a))
# <class 'str'>

liczba = 100
if liczba < 100 and liczba > 0:
    print("Liczba mniejsza niż 100")
elif liczba > 0:
    print("Liczba większa od 0")
else:
    print("")
    

if 0 < liczba < 100:
    print("Liczba mniejsza niż 100")

# pętla for
imie = "Amanda"
# for jako foreach
for litera in imie:
    print(litera, end='')
print()

# for i range
for liczba in range(1,11):
    print(liczba)

for liczba in range(1, 11, 2):
    print(liczba)
# range to generator
print(list(range(1, 11, 2)))


print(list(range(11, 1, -2)))

#slice
#print(imie[0:2:1])
# start(0) stop(2) step(1)
print(imie[::2])


