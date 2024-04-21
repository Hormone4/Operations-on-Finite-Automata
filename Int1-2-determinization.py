
import importlib
functions = importlib.import_module("Int1-2-functions")




def determinizeReal(A,L,E, Adet, Edet, trans_list):

    # If there are no more new states to add, return the new automaton
    if len(trans_list) == 0:   # Default case of the recursive function
        print("\nFINAL Adet: ", Adet)
        print("FINAL Edet: ", Edet)
        functions.display(Adet, L, Edet)
        return Adet, Edet

    else:
        # Extract the current states to analyze
        trans_current = trans_list[0]
        trans_list.pop(0)
        while len(trans_current) == 0:
            if len(trans_list) == 0:   # Default case of the recursive function
                print("\nFINAL Adet: ", Adet)
                print("FINAL Edet: ", Edet)
                functions.display(Adet, L, Edet)
                return Adet, Edet
            trans_current = trans_list[0]
            trans_list.pop(0)

        print("\ntrans_current:",trans_current)
        print("trans_list:", trans_list)


        # Obtain the indexes of the current states in the transition list
        index_list = []
        for i, el in enumerate(A):
            if el[0] in trans_current:
                index_list.append(i)
        print("index_list: ", index_list)

        # Add the new state to the new automaton
        new_state = ""
        for i in trans_current:
            new_state += str(i)
        Adet.append([new_state])

        # Add the new initial / final state
        ie = [False, False, False]   # [in, out, both]
        for i in index_list:
            if E[i] == " ->":
                ie[0] = True
            elif E[i] == "<- ":
                ie[1] = True
            elif E[i] == "<->":
                ie[2] = True
        if ie[2] or ie[1]: Edet.append("<- ")
        else: Edet.append("   ")

        # Obtain the union of all transitions of the current new state
        new_trans_list = [[] for _ in range(len(L))]
        for index in index_list:
            for i, transition in enumerate(A[index][1:]):
                if isinstance(transition, list):
                    for j in transition:
                        new_trans_list[i].append(j)
                elif transition not in new_trans_list[i] and transition not in ("P", -1):
                    new_trans_list[i].append(transition)
        print("new_trans_list:", new_trans_list)

        # Add them to the list of transitions
        for el in new_trans_list:
            # Check that they are not duplicates
            new_state = ""
            for i in el:
                new_state += str(i)
            state_in_automaton = False
            for gag in Adet:
                if new_state == gag[0]:
                    state_in_automaton = True
                    break

            if state_in_automaton == False and el not in trans_list:
                trans_list.append(el)
        
        # Add the transitions of the new state to the new automaton
        for trans in new_trans_list:
            new_state = ""
            for i in trans:
                new_state += str(i)
            if new_state == "":
                """for i in A:
                    if i[0] == "P":
                        new_state = "P"
                        break
                    else:"""
                new_state = -1
            Adet[len(Adet)-1].append(new_state)

        return determinizeReal(A,L,E, Adet, Edet, trans_list)



        print("\ntrans_list:", trans_list)

        print("Adet: ", Adet)
        print("Edet: ", Edet)



def determinize(A,L,E):
    # Merge all initial states into a new state
    index_list = []
    # Find indexes of all initial states
    for i, e in enumerate(E):
        if e in ("<->", " ->"):
            index_list.append(i)
    print("index_list: ", index_list)

    Adet = []
    Edet = []
    # Add the new state to the new automaton
    new_state = ""
    for i, el in enumerate(A):
        if i in index_list:
            if el[0] != "P":
                new_state += str(el[0])
    #print("new_state: ", new_state)
    Adet.append([new_state])

    # Add the new initial / final state to the new automaton
    inout = False
    for i in index_list:
        if E[i] == "<->":
            inout = True
            break
    if inout: Edet.append("<->")
    else: Edet.append(" ->")



    # Obtain the union of all transitions of the new state
    new_trans_list = [[] for _ in range(len(L))]
    for index in index_list:
        for i, transition in enumerate(A[index][1:]):
            if isinstance(transition, list):
                for j in transition:
                    new_trans_list[i].append(j)
            elif transition not in new_trans_list[i] and transition not in ("P", -1):
                new_trans_list[i].append(transition)
    print("new_trans_list:", new_trans_list)

    # Add them to the list of transitions
    trans_list = []
    for el in new_trans_list:
        # Check that they are not duplicates
        new_state = ""
        for i in el:
            new_state += str(i)
        state_in_automaton = False
        for gag in Adet:
            if new_state == gag[0]:
                state_in_automaton = True
                break
        if state_in_automaton == False:
            trans_list.append(el)



    # Add the transitions of the new state to the new automaton
    for trans_current in new_trans_list:
        new_state = ""
        for i in trans_current:
            if i not in (-1, "P"):
                new_state += str(i)
        if new_state == "":
            """for i in A:
                if i[0] == "P":
                    new_state = "P"
                    break
                else:"""
            new_state = -1
        Adet[0].append(new_state)

    print("Adet: ", Adet)
    print("Edet: ", Edet)
    print("trans_list:", trans_list)
    return determinizeReal(A,L,E, Adet, Edet, trans_list)














if __name__ == "__main__":
    import importlib
    functions = importlib.import_module("Int1-2-functions")

    
    L = ["a","b"]
    E = [" ->", "<- ", "   ", "<- "]
    A = [
        ["i",[1,3],-1],
        [1,-1,2],
        [2,3,-1],
        [3,-1,-1]
    ]

    
    #A, E = functions.complete(A, E, L)
    functions.display(A, L, E)

    determinize(A,L,E)

    """# L is symbols in the alphabet, E is list of initial/ final states (in order)
    L = ["a","b","c","d"]
    E = [" ->", "   ", "<->", "<- ", "   "]
    # the first column of A is the list of states, the others are the transitions
    A = [[0, 2, [2,'P'], 3, 4],
         [2, 2, 2, 3, 2],
         [3, 4, 2, -1, 4],
         [4, -1, "P", 3, 4],
         ['P', 'P', 'P', 'P', 'P']]
    A, E = functions.complete(A, E, L)
    functions.display(A, L, E)

    determinize(A,L,E)"""

"""
    L = ["a","b"]
    E = [" ->", "   ", "   ", "   ", "<- "]
    A = [['A', ['B','A','P'], 'B'],
        ['B', -1, ['E','D']],
        ['C', 'D', -1],
        ['D', ['B','P'], -1],
        ['E', -1, 'C']]
    functions.display(A, L, E)

    A, E = functions.complete(A, E, L)
    print(A)
    functions.display(A, L, E)

    input()
    """
