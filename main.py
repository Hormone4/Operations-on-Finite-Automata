# Mainloop
from loader import *
from functions import *

data = load_data('test_automata.txt')  #import data
print("text file:", data)

#create the language
L = load_language(data)
print("\nAlphabet: ", L)

#terminal and non terminal list
E = load_state(data)
print("Initial / terminal states:", E)

#transition matrice
A = load_transition(data,L)
print("Automaton:", A)
display(A, L, E)