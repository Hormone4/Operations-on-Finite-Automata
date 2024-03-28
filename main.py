# Mainloop
from loader import *
from functions import *

data = load_data('test_automata.txt')  #import data
print(data)


#create the language

L = load_language(data)
print(L)

#terminal and non terminal matrice
E = load_state(data)
print(E)

#transition matrice

A = load_transition(data,L)
print(A)

#type of automata

automata_type(A,E,L)

#automata_type(A,E,L)

A_standard =standardize(A,E,L)
print(A_standard)