
def display(M, L, E):   # L is symbols in the alphabet, E is list of initial/ final states (in order)
    contains_list = False
    m = 0
    for i in A:
        for j in i:
            if isinstance(j, list):
                contains_list = True
                m = max(m, len(str(j)))
    m -= 2

    if contains_list == False:
        m = len(str(max(map(max,A))))
    
    print(" "*(m*2+6),end="")
    for i in range(len(M[0])-1):
        print(L[i],end=" "*(m+2))   # print the symbols in the alphabet
    print()
    a = '{:'+str(m+1)+'}'
    for i in range(len(M)) :
        print(E[i],end="")   # print initial or final
        for j in range(len(M[0])):
            if isinstance(M[i][j], list):
                print(a.format(" "+str(M[i][j])[1:-1]),end="")
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
    A = [[0, 1, [2,3], 3, 4],
         [2, 2, 2, 3, 1],
         [3, 4, 2, 3, 4],
         [4, 4, 4, 3, 4]]
    display(A, L, E)

    L = ["a","b"]
    E = [" ->", "   ", "   ", "   ", "<- "]
    A = [[0, [0,1,8,9], 0],
        [1, -1, 2],
        [2, 3, -1],
        [3, 4, -1],
        [4, -1, -1]]
    display(A, L, E)