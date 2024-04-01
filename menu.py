from loader import *
from functions import *
from minimize import *



def displayInMenu(A, L, E):
    print("")
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
    print("║ 7. Exit                  ║")
    print("╚══════════════════════════╝")

    choice = input("Enter your choice: ")

    if choice == '1':
        displayInMenu(A, L, E)

    elif choice == '2':
        displayInMenu(A, L, E)
        S = automata_type(A,L,E)
        sb = ["Standard:","Complete:","Deterministic:"]
        for i in sb:
            if S[sb.index(i)] == 1:
                print(i,"yes")
            else:
                print(i,"no")

    elif choice == '3':
        if automata_type(A,L,E)[0] == 1:
            displayInMenu(A, L, E)
            print("Automaton is already standard.")
        else:
            A, E = standardize(A,L,E,data)
            print("Standard equivalent automaton:")
            displayInMenu(A, L, E)
        
    elif choice == '4':
        #A, E = complete(A,L,E,data)
        displayInMenu(A, L, E)
        print("Not implemented yet.")
        
    elif choice == '5':
        #A, E = determinize(A,L,E,data)
        displayInMenu(A, L, E)
        print("Not implemented yet.")
        
    elif choice == '6':
        displayInMenu(A, L, E)
        A, E = minimize(A,L,E)
        #minimize(A,L,E)
        displayInMenu(A, L, E)
        print("Equivalent minimal automaton.")
        
    elif choice == '7':
        exit()

    else:
        print("Invalid choice. Please try again.")





if __name__ == "__main__":
    data = load_data('test_automata.txt')  #import data
    #print("text file:", data)

    #create the language
    L = load_language(data)
    #print("\nAlphabet: ", L)

    #terminal and non terminal list
    E = load_state(data)
    #print("Initial / terminal states:", E)
    E[2] = " ->"
    #print("Initial / terminal states:", E)

    #transition matrice
    A = load_transition(data,L)
    #display(A, L, E)





    
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
    while True:
        menu(A, L, E, data)