import importlib
loader = importlib.import_module("Int1-2-loader")
functions = importlib.import_module("Int1-2-functions")
minimization = importlib.import_module("Int1-2-minimization")
recognition = importlib.import_module("Int1-2-recognition")



def displayInMenu(A, L, E=None):
    print()
    print("┌──────────────────────────┐")
    print("│   AUTOMATON              │")
    print("└──────────────────────────┘")
    functions.display(A, L, E)
    print()


def menu(A, L, E, data):
    print()
    print("╔══════════════════════════╗")
    print("║   MENU                   ║")
    print("╟──────────────────────────╢")
    print("║ 1. Display automaton     ║")
    print("║ 2. Automaton type        ║")
    print("║ 3. Standardize automaton ║")
    print("║ 4. Complete automaton    ║")
    print("║ 5. Determinize automaton ║")
    print("║ 6. Minimize automaton    ║")
    print("║ 7. Word recognition      ║")
    print("║ 8. Complementary         ║")
    print("║ 9. Exit                  ║")
    print("╚══════════════════════════╝")

    choice = input("Enter your choice (number): ")

    if choice == '1':
        displayInMenu(A, L, E)

        menu(A, L, E, data)

    elif choice == '2':
        displayInMenu(A, L, E)
        S = functions.automata_type(A,L,E)
        sb = ["Standard:","Complete:","Deterministic:"]
        for i in sb:
            if S[sb.index(i)] == 1:
                print(i,"yes")
            else:
                print(i,"no")

        menu(A, L, E, data)

    elif choice == '3':
        if functions.automata_type(A,L,E)[0] == 1:
            displayInMenu(A, L, E)
            print("Automaton is already standard.")
        else:
            A, E = functions.standardize(A,L,E)
            displayInMenu(A, L, E)
            print("Standard equivalent automaton.")

        menu(A, L, E, data)
        
    elif choice == '4':
        if functions.automata_type(A,L,E)[1] == 1:
            displayInMenu(A, L, E)
            print("Automaton is already complete.")
        else:
            A, E = functions.complete(A, E, L)
            displayInMenu(A, L, E)
            print("Equivalent complete automaton.")

        menu(A, L, E, data)
        
    elif choice == '5':
        if functions.automata_type(A,L,E)[2] == 1:
            displayInMenu(A, L, E)
            print("Automaton is already deterministic.")
        else:
            #A, E = determinize(A,L,E,data)                      # DETERMINIZE FUNCTION HERE
            displayInMenu(A, L, E)
            print("Not implemented yet.")

        menu(A, L, E, data)
        
    elif choice == '6':
        displayInMenu(A, L, E)
        # Check if the automaton is complete deterministic
        type = functions.automata_type(A, L, E)
        if type[1] == 1 and type[2] == 1:
            A, E = minimization.minimize(A,L,E)
            displayInMenu(A, L, E)
            print("Equivalent minimal automaton.")
        else:
            print("Automaton is not complete deterministic. Cannot be minimized.")
        menu(A, L, E, data)

    elif choice == '7':
        displayInMenu(A, L, E)
        word = ""
        while word != "end":
            word2 = recognition.read_word(word)
            if recognition.recognize(A, L, E, word2) : 
                print("The word is recognized.")
            else:
                print("The word is not recognized.")
        
        menu(A, L, E, data)
    
    elif choice == '8':
        # Check if the automaton is complete deterministic
        type = functions.automata_type(A, L, E)
        if type[1] == 1 and type[2] == 1:
            A, E = functions.complementary(A, L, E)
            displayInMenu(A, L, E)
            print("Automaton recognizing the complementary language.")
        else:
            displayInMenu(A, L, E)
            print("Automaton is not complete deterministic. Cannot find the automaton recognizing the complementary language.")
        menu(A, L, E, data)

        
    elif choice == '9':
        exit()

    else:
        print("Invalid choice. Please try again.")
        menu(A, L, E, data)





if __name__ == "__main__":

    # Read the data from the text file
    data = loader.load_data('Int1-2-15.txt')

    # Create the language list
    L = loader.load_language(data)

    # Create the list of terminal / non terminal states
    E = loader.load_state(data)
    #E[2] = " ->"   # for test purposes

    # Create the automaton
    A = loader.load_transition(data,L)

    

    # for test purposes
    
    L = ['a', 'b']
    E = ['<->', '<- ', '<- ', '<- ', '<- ', '   ']
    A = [
        ["02", "01", "12"],
        ["01", "1", "012"],
        ["12", "01", "02"],
        ["012", "01", "012"],
        ["1", "P", "02"],
        ["P", "P", "P"]
        ]
    




    displayInMenu(A, L, E)
    menu(A, L, E, data)