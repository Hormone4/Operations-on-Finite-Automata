import importlib
loader = importlib.import_module("loader")
menu = importlib.import_module("menu")





AUTOMATON_NUMBER = 22


# Load the data
data = loader.load_data("test-automata/"+str(AUTOMATON_NUMBER)+".txt")   # Read the data from the text file

# Create the automaton
L = loader.load_language(data)      # Create the list containing the language 
E = loader.load_state(data)         # Create the list of terminal / non terminal states
A = loader.load_transition(data,L)  # Create the automaton

# Mainloop
menu.displayInMenu(A, L, E)
menu.menu(A, L, E, data)