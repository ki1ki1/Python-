# 1 zadanko
a = input()
spacje = 0 blblblbl
for litera in a:
    if litera == " ":
        spacje+=1
print("To zdanie ma " + str(spacje) + " spacji")

# 2 zadanko
import sys
print("Podaj jakąś liczbe: ")
b = sys.stdin.readline()
print("Podaj drugą liczbe: ")
c = sys.stdin.readline()
wynik = int(b) * int(c)
sys.stdout.write(str(wynik))
print("\n")
# 3 zadanko
# < > <= >= == !=

# 4 zadanko
import cmath
liczba =input()
if int(liczba) < 0:
    print(abs(int(liczba)))
print("\n")

# 5 zadanko
a = input()
b = input()
c = input()
if int(a) in (0,10) and int(a)>int(b) or int(b)>int(c):
    print("Spełnia warunek")
else:
    print("Nie spełnia")
print("\n")

# 6 zadanko
for liczba in range(0,30,5):
    print(liczba)
