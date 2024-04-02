from loader import *
from functions import *
from minimization import *
from recognition import *



def displayInMenu(A, L, E=None):
    print()
    print("┌──────────────────────────┐")
    print("│   AUTOMATON              │")
    print("└──────────────────────────┘")
    display(A, L, E)
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
        S = automata_type(A,L,E)
        sb = ["Standard:","Complete:","Deterministic:"]
        for i in sb:
            if S[sb.index(i)] == 1:
                print(i,"yes")
            else:
                print(i,"no")

        menu(A, L, E, data)

    elif choice == '3':
        if automata_type(A,L,E)[0] == 1:
            displayInMenu(A, L, E)
            print("Automaton is already standard.")
        else:
            A, E = standardize(A,L,E,data)          # STANDARDIZE FUNCTION TO BE FIXED
            print("Standard equivalent automaton:")
            displayInMenu(A, L, E)

        menu(A, L, E, data)
        
    elif choice == '4':
        if automata_type(A,L,E)[1] == 1:
            displayInMenu(A, L, E)
            print("Automaton is already complete.")
        else:
            #A, E = complete(A,L,E,data)             # COMPLETE FUNCTION HERE
            displayInMenu(A, L, E)
            print("Not implemented yet.")

        menu(A, L, E, data)
        
    elif choice == '5':
        if automata_type(A,L,E)[2] == 1:
            displayInMenu(A, L, E)
            print("Automaton is already deterministic.")
        else:
            #A, E = determinize(A,L,E,data)          # DETERMINIZE FUNCTION HERE
            displayInMenu(A, L, E)
            print("Not implemented yet.")

        menu(A, L, E, data)
        
    elif choice == '6':
        displayInMenu(A, L, E)
        A, E = minimize(A,L,E)
        displayInMenu(A, L, E)
        print("Equivalent minimal automaton.")
        menu(A, L, E, data)

    elif choice == '7':
        displayInMenu(A, L, E)
        word = input("Enter a word to recognize: ")
        #if recognize(A,L,word):                    # RECOGNIZE FUNCTION HERE
        #    print("The word is recognized.")
        #else:
        #    print("The word is not recognized.")
        print("Not implemented yet.")
        menu(A, L, E, data)
    
    elif choice == '8':
        displayInMenu(A, L, E)
        #A, E = complementary(A,L,E,data)   # COMPLEMENTARY FUNCTION HERE
        displayInMenu(A, L, E)
        print("Not implemented yet.")
        menu(A, L, E, data)
        
    elif choice == '9':
        exit()

    else:
        print("Invalid choice. Please try again.")
        menu(A, L, E, data)





if __name__ == "__main__":

    # Read the data from the text file
    data = load_data('test_automata.txt')

    # Create the language list
    L = load_language(data)

    # Create the list of terminal / non terminal states
    E = load_state(data)
    E[2] = " ->"   # for test purposes

    # Create the automaton
    A = load_transition(data,L)


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







    print("┌──────────────────────────┐")
    print("│   AUTOMATON              │")
    print("└──────────────────────────┘")
    display(A, L, E)
    print()

    menu(A, L, E, data)