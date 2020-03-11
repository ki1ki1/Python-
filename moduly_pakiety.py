# import start
#from start import pow

from timeit import timeit

print(timeit('[]',number=100000))
print(timeit('list()',number=100000))

kod = """lista = []
for znak in 'Wojtek':
    lista.append(znak)"""
kod2 = """[znak for znak in 'Wojtek']"""
print(timeit(stmt=kod, number=100000))
print(timeit(stmt=kod2, number=100000))

import string
import itartools

def gen_kod(ile_liter=1, ile_liczb=1):
    itertools

