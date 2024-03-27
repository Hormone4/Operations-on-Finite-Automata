# L is symbols in the alphabet, E is list of initial/ final states (in order)
def display(M, L, E):
    # The goal is to find m, the maximum length of the strings in the matrix M
    print()
    # if the matrix contains a list aka if the automaton is non-deterministic
    contains_list = False
    m = 0
    for i in M:
        for j in i:
            if isinstance(j, list):
                contains_list = True
                b = 0
                for k in j:   # for each string/char in the list, add 2 to b
                    if isinstance(k, str):
                        b += 2
                m = max(m, len(str(j))- b)   # take the lenght of the list
    m -= 2
    
    # if the automaton is deterministic
    if contains_list == False:
        m = len(str(max(map(max,A))))
    
    # print the symbols in the alphabet
    print(" "*(m*2+6),end="")
    for i in range(len(M[0])-1):
        print(L[i],end=" "*(m+2))
    print()

    # print the automaton
    a = '{:'+str(m+1)+'}'   # define the format string
    for i in range(len(M)) :
        print(E[i],end="")   # print if the state is initial or final
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
    E = [" ->", "   ", "<->", "<- ", "   "]
    # the first column of A is the list of states, the others are the transitions
    A = [[0, 1, [2,'P'], 3, 4],
         [2, 2, 2, 3, 1],
         [3, 4, 2, -1, 4],
         [4, -1, "P", 3, 4],
         ['P', 'P', 'P', 'P', 'P']]
    display(A, L, E)

    L = ["a","b"]
    E = [" ->", "   ", "   ", "   ", "<- "]
    A = [['A', ['B','A','P'], 'B'],
        ['B', -1, ['E','D']],
        ['C', 'D', -1],
        ['D', ['B','P'], -1],
        ['E', -1, 'C']]
    display(A, L, E)