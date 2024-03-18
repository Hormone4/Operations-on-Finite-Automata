
def show(M, T, E):   # T is symbols in the alphabet, E is list of initial/ final
    m = max(len(str(max(map(max,M)))), len(str(min(map(min,M)))))
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


L = ["a","b","c","d","e"]
E = [" ->", "   ", "<->", "<- "]
A = [
     [0, 1, 222, 3, 4, 1],
     [2, 1, 2, 3, 4, 3],
     [3, 1, 2, 3, 4, 3],
     [4, 1, 2, 3, 4, 3]
    ]



print()
show(A, L, E)
i = input()