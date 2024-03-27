# Loader to extract the data from the text file


def load_data(file):

     mylines = []
     with open (file, 'rt') as myfile:                                   # Open the file given and reads it
         for myline in myfile:                                           # For each line, stored as myline
             mylines.append(myline.replace('\n', ''))        # add its contents to mylines and replaces the next line character by nothing
     return mylines


def load_language(data):
    L = []

    for i in range(5, len(data)):
        if data[i][1] not in L:
            L.append(data[i][1])
    return L


def load_state(data):

    E = []

    for i in range(0, ord(data[1]) - 48):                               #convert string to number
        if str(i) in (data[2][1:]) and str(i) in (data[3][1:]):
            E.append("<->")
        elif str(i) in (data[2][1:]):
            E.append(" ->")
        elif str(i) in (data[3][1:]):
            E.append("<- ")
        else:
            E.append("   ")
    return E;


def load_transition(data):

    A = [[-1 for j in range(len(L) + 1)] for i in range((ord(data[1]) - 48))]

    for i in range(ord(data[1]) - 48):
        A[i][0] = i

    for i in data[5:]:

        if A[ord(i[0]) - 48][ord(i[1]) - 96] == -1:
            A[ord(i[0]) - 48][ord(i[1]) - 96] = ord(i[2]) - 48
        else:
            if not isinstance(A[ord(i[0]) - 48][ord(i[1]) - 96], list):
                A[ord(i[0]) - 48][ord(i[1]) - 96] = [A[ord(i[0]) - 48][ord(i[1]) - 96]]
            A[ord(i[0]) - 48][ord(i[1]) - 96].append(ord(i[2]) - 48)

    return A

"""
Example of the text file:
2
5
1 0
1 4
6
0a0
0b0
0a1
1b2
2a3
3a4

Format needed for the data:
L = ["a","b"]
E = [" ->", "   ", "   ", "   ", "<- "]   # " ->" is initial, "   " is neither, "<->" is both, "<- " is final
A = [[0, [0,1], 0],
     [1, -1, 2],
     [2, 3, -1],
     [3, 4, -1],
     [4, -1, -1]]

"""