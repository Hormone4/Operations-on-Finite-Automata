




def determinizeReal(A,L,E, Adet, Edet):
    pass


def determinize(A,L,E):
    # Merge all initial states into one new state
    index_list = []
    # Find indexes of all initial states
    for i, e in enumerate(E):
        if e in ("<->", " ->"):
            index_list.append(i)
    print("index_list: ", index_list)

    # Create a new state
    new_state = ""
    for i, el in enumerate(A):
        if i in index_list:
            new_state += str(el[0])
    print("new_state: ", new_state)

    # Create new A and E and add new state
    Adet = []
    Edet = []
    Adet.append([new_state])
    inout = False
    for i in index_list:
        if E[i] == "<->":
            inout = True
            break
    if inout: Edet.append("<->")
    else: Edet.append(" ->")

    print("Adet: ", Adet)
    print("Edet: ", Edet)




if __name__ == "__main__":
    import importlib
    functions = importlib.import_module("Int1-2-functions")

    # L is symbols in the alphabet, E is list of initial/ final states (in order)
    L = ["a","b","c","d"]
    E = [" ->", "   ", "<->", "<- ", "   "]
    # the first column of A is the list of states, the others are the transitions
    A = [[0, 1, [2,'P'], 3, 4],
         [2, 2, 2, 3, 1],
         [3, 4, 2, -1, 4],
         [4, -1, "P", 3, 4],
         ['P', 'P', 'P', 'P', 'P']]
    A, E = functions.complete(A, E, L)
    functions.display(A, L, E)

    determinize(A,L,E)

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