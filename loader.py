# Loader to extract the data from the text file


def load_data(file):

     mylines = []
     with open (file, 'rt') as myfile:                  # Open the file given and reads it
         for myline in myfile:                          # For each line, stored as myline
             mylines.append(myline.replace('\n', ''))   # add its contents to mylines and replaces the next line character by nothing
     return mylines


def load_language(data):
    L = []
    i=5
    if((ord(data[0])-48) == 0):
        L.append("None")
    else :
        while len(L) != (ord(data[0])-48):                  # we use while to not go through the whole list
            if data[i][1] not in L:
                L.append(data[i][1])
            i += 1
    return L


def load_state(data):

    E = []

    for i in range(0, ord(data[1]) - 48):                # convert string to number
        if str(i) in (data[2][1:]) and str(i) in (data[3][1:]):
            E.append("<->")
        elif str(i) in (data[2][1:]):
            E.append(" ->")
        elif str(i) in (data[3][1:]):
            E.append("<- ")
        else:
            E.append("   ")
    return E;


def load_transition(data,L):

    A = [[-1 for j in range(len(L) + 1)] for i in range((ord(data[1]) - 48))]

    for i in range(ord(data[1]) - 48):
        A[i][0] = i

    for i in data[5:]:

        if A[ord(i[0]) - 48][ord(i[1]) - 96] == -1:
            A[ord(i[0]) - 48][ord(i[1]) - 96] = ord(i[2]) - 48
        else:
            if not isinstance(A[ord(i[0]) - 48][ord(i[1]) - 96], list):                     #check if its not yet a list so that we can use append
                A[ord(i[0]) - 48][ord(i[1]) - 96] = [A[ord(i[0]) - 48][ord(i[1]) - 96]]
            A[ord(i[0]) - 48][ord(i[1]) - 96].append(ord(i[2]) - 48)

    return A





if __name__ == "__main__":
    import importlib
    functions = importlib.import_module("functions")

    data = load_data('15.txt')  #import data
    print("text file:", data)


    #create the language

    L = load_language(data)
    print("\nAlphabet: ", L)

    #terminal and non terminal matrice
    E = load_state(data)
    print("Initial / terminal states:", E)

    #transition matrice

    A = load_transition(data,L)
    print("Automaton:", A)

    functions.display(A, L, E)

    input()