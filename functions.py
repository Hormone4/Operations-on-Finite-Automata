
def display(M, L, E):
    # m = max(len(str(max(map(max,M)))), len(str(min(map(min,M)))))   # if negative numbers
    m = len(str(max(map(max,M))))
    print(" ",end=" "*(m+2)); print(" ",end=" "*(m+2))
    for i in range(len(M[0])-1): print(L[i],end=" "*(m+2))   # print the entries
    print()
    a = '{:'+str(m+1)+'}'
    for i in range(len(M)) :
        print(E[i],end="")   # print initial or final
        for j in range(len(M[0])):
            if j == len(M[0])-1: print(a.format(M[i][j]),"|")
            else               : print(a.format(M[i][j]),end=" |")
    print()




if __name__ == "__main__":
    # TEST
    # L is symbols in the alphabet, E is list of initial/ final states (in order)
    L = ["a","b","c","d","e"]
    E = [" ->", "   ", "<->", "<- "]
    A = [
        [0, 1, 2, 3, 4, 1],
        [2, 1, 2, 3, 4, 3],
        [3, 1, 2, 3, 4, 3],
        [4, 1, 2, 3, 4, 3]
        ]



    print()
    display(A, L, E)