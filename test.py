import importlib
loader = importlib.import_module("loader")
functions = importlib.import_module("functions")
minimization = importlib.import_module("minimization")
recognition = importlib.import_module("recognition")
menu = importlib.import_module("menu")
determinization = importlib.import_module("determinization")

#python tests.py > output.txt





# Load the data
# Read the data from the text file
AUTOMATON_NUMBER = 15
data = loader.load_data("test-automata/"+str(AUTOMATON_NUMBER)+".txt")   # FOR MANUAL TESTS

import sys
# Use the sys module to get the automaton file name as a command-line argument
data = loader.load_data(sys.argv[1])   # FOR AUTOMATED TESTS


# Create the automaton
L = loader.load_language(data)      # Create the list containing the language 
E = loader.load_state(data)         # Create the list of terminal / non terminal states
A = loader.load_transition(data,L)  # Create the automaton

# Display 
print("\n\n\n")
print("+-----------+")
print("| AUTOMATON |")
print("+-----------+")
functions.display(A, L, E)

# Automaton type
S = functions.automata_type(A,L,E)
sb = ["Standard:","Complete:","Deterministic:"]
for i in sb:
    if S[sb.index(i)] == 1:
        print(i,"yes")
    else:
        print(i,"no")



if functions.automata_type(A,L,E)[0] == 1:
    print("\n\n\n")
    print("+-----------+")
    print("| AUTOMATON |")
    print("+-----------+")
    functions.display(A, L, E)
    print("Automaton is already standard.")
else:
    A, E = functions.standardize(A,L,E)
    print("\n\n\n")
    print("+-----------+")
    print("| AUTOMATON |")
    print("+-----------+")
    functions.display(A, L, E)
    print("Standard equivalent automaton.")


if functions.automata_type(A,L,E)[1] == 1:
    print("\n\n\n")
    print("+-----------+")
    print("| AUTOMATON |")
    print("+-----------+")
    functions.display(A, L, E)
    print("Automaton is already complete.")
else:
    A, E = functions.complete(A, E, L)
    print("\n\n\n")
    print("+-----------+")
    print("| AUTOMATON |")
    print("+-----------+")
    functions.display(A, L, E)
    print("Equivalent complete automaton.")


if functions.automata_type(A,L,E)[2] == 1:
    print("\n\n\n")
    print("+-----------+")
    print("| AUTOMATON |")
    print("+-----------+")
    functions.display(A, L, E)
    print("Automaton is already deterministic.")
else:
    A, E = determinization.determinize(A,L,E)
    print("\n\n\n")
    print("+-----------+")
    print("| AUTOMATON |")
    print("+-----------+")
    functions.display(A, L, E)
    print("Equivalent deterministic automaton.")


print("\n\n\n")
print("+-----------+")
print("| AUTOMATON |")
print("+-----------+")
functions.display(A, L, E)
# Check if the automaton is complete deterministic
type = functions.automata_type(A, L, E)
if type[1] == 1 and type[2] == 1:
    A, E = minimization.minimize(A,L,E)
    print("\n\n\n")
    print("+-----------+")
    print("| AUTOMATON |")
    print("+-----------+")
    functions.display(A, L, E)
    print("Equivalent minimal automaton.")
else:
    print("Automaton is not complete deterministic. Cannot be minimized.")

print("\n\n\n")
print("+-----------+")
print("| AUTOMATON |")
print("+-----------+")
functions.display(A, L, E)
print("Enter a word : ")
word = "abba"
print(word)
if recognition.recognize(A, L, E, word) : 
    print("The word is recognized.\n")
else:
    print("The word is not recognized.\n")
print("Enter a word : ")
word = "aba"
print(word)
if recognition.recognize(A, L, E, word) : 
    print("The word is recognized.\n")
else:
    print("The word is not recognized.\n")
print("Enter a word : ")
word = "aac"
print(word)
if recognition.recognize(A, L, E, word) : 
    print("The word is recognized.\n")
else:
    print("The word is not recognized.\n")



# Check if the automaton is complete deterministic
type = functions.automata_type(A, L, E)
if type[1] == 1 and type[2] == 1:
    A, E = functions.complementary(A, L, E)
    print("\n\n\n")
    print("+-----------+")
    print("| AUTOMATON |")
    print("+-----------+")
    functions.display(A, L, E)
    print("Automaton recognizing the complementary language.")
else:
    print("\n\n\n")
    print("+-----------+")
    print("| AUTOMATON |")
    print("+-----------+")
    functions.display(A, L, E)
    print("Automaton is not complete deterministic. Cannot find the automaton recognizing the complementary language.")
print("\n")

print("Enter a word : ")
word = "abba"
print(word)
if recognition.recognize(A, L, E, word) : 
    print("The word is recognized.\n")
else:
    print("The word is not recognized.\n")
print("Enter a word : ")
word = "aba"
print(word)
if recognition.recognize(A, L, E, word) : 
    print("The word is recognized.\n")
else:
    print("The word is not recognized.\n")
print("Enter a word : ")
word = "aac"
print(word)
if recognition.recognize(A, L, E, word) : 
    print("The word is recognized.\n")
else:
    print("The word is not recognized.\n")






#input()