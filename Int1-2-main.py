import importlib
loader = importlib.import_module("Int1-2-loader")
functions = importlib.import_module("Int1-2-functions")
minimization = importlib.import_module("Int1-2-minimization")
recognition = importlib.import_module("Int1-2-recognition")
menu = importlib.import_module("Int1-2-menu")



# Mainloop

data = loader.load_data('test_automata.txt')  #import data
print("text file:", data)

#create the language
L = loader.load_language(data)
print("\nAlphabet: ", L)

#terminal and non terminal list
E = loader.load_state(data)
#print("Initial / terminal states:", E)
E[2] = " ->"
print("Initial / terminal states:", E)

#transition matrice
A = loader.load_transition(data,L)
functions.display(A, L, E)

#type of automata
S = functions.automata_type(A,L,E)
print("\nStandard, complete, deterministic:",S,"\n")

#standardize automata
A, E = functions.standardize(A,L,E)
print("Standard automaton:", A)
functions.display(A, L, E)

#get the complementary automaton
A, E = functions.complementary(A, L, E)
print("Complementary automaton")
functions.display(A, L, E)





input()