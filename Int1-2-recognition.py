from functions import display

# Word recognition function
# The function should return a boolean
# True if the word is recognized by the automaton, False otherwise.


def recognize(A, L, E, word):
    #/!\ penser à mettre le empty word si <- <-> et si " "
    if len(word) == 0: #empty word recognition
        for j in range (0, len(E)-1):
            if E[j] == "<->": 
                print("emptyyyy word recognized")
                return 1
    if word[0] == " " and all(element == word[0] for element in word): #empty word recognition
        print("mot vide reconnu")
        return 1

    
    word = word.replace(" ", "")
    #print(word)
    
    i = 0
    states=[]
    if word[0] not in L: #if the first letter of word isn't in alphabet L
        print("First letter not in language")
        return 0
    else :
        first_letter=L.index(word[0]) + 1 #takes the index of the first letter of the word compared to alphabet L, and we add 1 because there are +1 states compared to L 
        
        for el in E : #number of element in E
            if el==" ->" or el=="<->": #we check if we can enter in the automata
                if word[0] in L and A[i][first_letter] != -1: #if the first letter is in alphabet and if its value isn't -1 (-) 
                    outputs = A[i][first_letter] 
                    if isinstance (outputs, list): #permits to have a list containing only integers and no list
                        for a in range(0,len(outputs)):
                            states.append(outputs[a])
                    else: 
                        states.append(outputs)
            i+=1

        if len(word) == 1: #if the word is only one character of the alphabet
            for element in states:
                if E[element]=="<-" or E[element]=="<->": #checks if we can go out of the automata 
                        print("mot avec 1 lettre reconnue")
                        return 1
                        break
                else : 
                    return 0
        

        j = 1
        k = 0
        while k<len(word)-1:
            if word[j] not in L: #if a letter of the word isn't in the language
                print("Letter not in language")
                return 0
            current_letter = L.index(word[j]) + 1 #gives the index in the L list of the current letter   
            not_doublons = [] #this list doesn't contain the duplicates
            next_states = []
            
            for element in states:
                for i, linee in enumerate(A):   # Convert the state into its index in the automaton
                    if element == linee[0]:
                        element = i
                
                #print(element,states)
                if element in not_doublons: #avoid repeating the actions if a state has already been computed
                    break
                else :
                    
                    outputs = A[element][current_letter]

                    if isinstance (outputs, list): #only if it's a list, it permits to have a list containing only integers and no lists 
                        for a in range(0,len(outputs)):
                            next_states.append(outputs[a])
                            not_doublons.append(element)
                        break

                    if outputs == -1 : #doesn't go if there is a -1 (-)
                        break 
                    else : 
                        next_states.append(outputs)
                        not_doublons.append(element)
            states = next_states 
            k+=1
            j+=1
            if k<len(word)-1 and states == []: #if the word can't be written due to a letter in the word
                print("nan, mot pas reconnu")
                return 0
                
            if k == len(word)-1: #if we are at the last letter of the word
                

                #for element in states:
                for element in states:
                    for i, linee in enumerate(A):
                        if element == linee[0]:
                            element = i
                            break
                        
                    if E[element]=="<- " or E[element]=="<->": #if the states are <- or <->
                        print("mot reconnu")
                        return 1
                        break
                else :
                    print("nan, mot pas reconnu") #if there is no <- or <->
                    return 0



        



def read_word (word):
    word = str(input("Enter a word (write 'end' to stop) : "))
    return word





if __name__ == "__main__":
    from functions import *
    from loader import *

    # Read the data from the text file
    data = load_data('test_automata.txt')

    # Create the language list
    L = load_language(data)

    # Create the list of terminal / non terminal states
    E = load_state(data)
    E[1] = "<->"



    # Create the automaton
    A = load_transition(data,L)



    display(A, L, E)

    '''# Test the recognize function
    print(read_word(word))'''

    #recognize(A,L,E,"          ")
    #word = input("Enter a word : ")
    #read_word(word)
    
    #word = input ("enter a word pls : ")
    #read_word(word)

