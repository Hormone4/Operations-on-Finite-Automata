import importlib
loader = importlib.import_module("Int1-2-loader")
functions = importlib.import_module("Int1-2-functions")
minimization = importlib.import_module("Int1-2-minimization")
recognition = importlib.import_module("Int1-2-recognition")
menu = importlib.import_module("Int1-2-menu")


AUTOMATON_NUMBER = 1


# Load the data
data = loader.load_data("Int1-2-"+str(AUTOMATON_NUMBER)+".txt")   # Read the data from the text file

# Create the automaton
L = loader.load_language(data)      # Create the list containing the language 
E = loader.load_state(data)         # Create the list of terminal / non terminal states
A = loader.load_transition(data,L)  # Create the automaton

# Mainloop
menu.displayInMenu(A, L, E)
menu.menu(A, L, E, data)