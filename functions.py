
def display(M, L, E=None):   # L is symbols in the alphabet, E is list of initial/ final states (in order)
    # The goal is to find m, the length of the longest element in the matrix M
    #print()
    if E == None:   # if there is no list of initial/final states
        E = ["   " for _ in range(len(M))]
    
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
        for i in M:
            for j in i:
                if isinstance(j, str):
                    m = max(m, len(j))
                else:
                    m = max(m, len(str(j)))

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
                print(a.format(" "*(m-len(M[i][j])+1)+M[i][j]),end="")
            else:
                if M[i][j] == -1:
                    print(a.format(" "*m+"-"),end="")
                else:
                    print(a.format(M[i][j]),end="")
            if j == len(M[0])-1:
                print(" |")
            else:
                print("",end=" |")










def automata_type(M, L, E) :   #defines type of the automata
    complete = 1
    deterministic = 1
    standard = 1
    for i in M :
        for j in range(1, len(L)+1) :
            if isinstance(i[j], list) :
                if len(i[j] )> 1:
                    deterministic = 0
                for k in i[j] :
                    if k == -1 :
                        complete = 0
                    if k == M[0][0]:
                        standard = 0
            else :
                if i[j] == -1:
                    complete = 0
                if i[j] == M[0][0]:
                    standard = 0
    if deterministic == 1 :
        count = 0
        for m in E:
            if m == " ->":
                count += 1
            if count >1:
                deterministic = 0
                standard = 0
                break
    S = [standard,complete,deterministic] # return the types as a list for later use
    return S


def standardize(M, L, E): #only works for single entry
    F = []
    for k in range(0,len(E)):
        if E[k]==" ->" or E[k]=="<->":
            F.append(k)
    i = ["i"]
    for x in F:
        if E[x] == "<->" :
            E[x] = "<- "
        else :
            E[x] = "   "
        for m in range(1,len(L)+1): #creation of the new starting point of the automaton
            if len(i) != len(L)+1:
                i.append([])   #check not empty at the end
            if not isinstance(M[x][m],list):
                i[m].append(M[x][m])
            else:
                for y in M[x][m]:
                    i[m].append(y)
    for z in range(1, len(L)+1): # remove unnecessary -1
        if len(i[z]) > 1 and -1 in i[z]:
            i[z] = [item for item in i[z] if item!= -1]
    E.insert(0," ->") #update of the state matrice
    M.insert(0,i) #insertion of the new starting point

    return(M,E)
















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

    display(A, L)