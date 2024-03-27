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

A = load_transition(data)
print(A)

display(A, L, E)