
def display(M, L, E):   # L is symbols in the alphabet, E is list of initial/ final states (in order)
    # The goal is to find m, the maximum length of the strings in the matrix M
    contains_list = False
    m = 0
    for i in A:
        for j in i:
            # if the matrix contains a list
            # aka if the automaton is non-deterministic
            if isinstance(j, list):
                contains_list = True
                b = 0
                for k in j:   # for each string/char in the list, add 2 to b
                    if isinstance(k, str):
                        b += 2
                if b == 0:
                    m = max(m, len(str(j)))
                else:
                    m = max(m, len(str(j))) - b+1
    m -= 2

    if contains_list == False:   # if the automaton is deterministic
        m = len(str(max(map(max,A))))
        
    print(" "*(m*2+6),end="")
    for i in range(len(M[0])-1):
        print(L[i],end=" "*(m+2))   # print the symbols in the alphabet
    print()

    a = '{:'+str(m+1)+'}'   # define the format string
    for i in range(len(M)) :
        print(E[i],end="")   # print initial or final
        for j in range(len(M[0])):
            if isinstance(M[i][j], list):
                word = str(M[i][j])
                word = word.replace("'","")
                print(a.format(" "+" "*(m+2-len(word))+word[1:-1]),end="")
            elif isinstance(M[i][j], str):
                print(a.format(" "*m+M[i][j]),end="")
            else:
                if M[i][j] == -1:
                    print(a.format(" "*m+"-"),end="")
                else:
                    print(a.format(M[i][j]),end="")

            if j == len(M[0])-1:
                print(" |")
            else:
                print("",end=" |")
    print()













if __name__ == "__main__":
    # TEST
    # L is symbols in the alphabet, E is list of initial/ final states (in order)
    L = ["a","b","c","d"]
    E = [" ->", "   ", "<->", "<- "]
    A = [[0, 1, [2,'P'], 3, 4],
         [2, 2, 2, 3, 1],
         [3, 4, 2, -1, 4],
         [4, -1, "P", 3, 4]]
    display(A, L, E)

    L = ["a","b"]
    E = [" ->", "   ", "   ", "   ", "<- "]
    A = [[0, ['B','A',0,"P"], 0],
        [1, -1, [2, 3]],
        [2, 3, -1],
        [3, [4,'P'], -1],
        [4, -1, 4]]
    display(A, L, E)