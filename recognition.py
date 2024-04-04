from functions import display

# Word recognition fuction
# The function should return a boolean
# True if the word is recognized by the automaton, False otherwise.


def recognize(A, L, E, word):


    return







if __name__ == "__main__":
    from functions import *
    from loader import *

    # Read the data from the text file
    data = load_data('test_automata.txt')

    # Create the language list
    L = load_language(data)

    # Create the list of terminal / non terminal states
    E = load_state(data)

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

    display(A, L, E)

    # Test the recognize function
    word = input("Enter a word to recognize: ")
    print(recognize(A, L, E, word))