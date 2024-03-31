from loader import *
from functions import *
from minimize import *
from menu import *







# Mainloop

data = load_data('test_automata.txt')  #import data
print("text file:", data)

#create the language
L = load_language(data)
print("\nAlphabet: ", L)

#terminal and non terminal list
E = load_state(data)
#print("Initial / terminal states:", E)
E[2] = " ->"
print("Initial / terminal states:", E)

#transition matrice
A = load_transition(data,L)
display(A, L, E)

#type of automata
S = automata_type(A,L,E)
print("\nStandard, complete, deterministic:",S,"\n")

#standardize automata
A, E = standardize(A,L,E,data)
print("Standard automaton:", A)
display(A, L, E)







input()