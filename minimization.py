from functions import display, automata_type
import copy   # syntax: cop = copy.deepcopy(partition0)


def minimizeReal(A, L, E, partition0, letter='@'):
    cop = copy.deepcopy(partition0)

    # Check if partition contains only singletons
    singletons = True
    for i in partition0:
        if len(partition0[i]) != 1:
            singletons = False
            break
    if singletons:   # Default case of the recursive function
        print("The partition is made only of singletons.\nThe automaton was already minimal.")
        return (A, E)
    
    # If not, study the states
    else:
        # Extract the states from the partition and store them as new automata in a list of automata
        study = []   # List of automata
        targets = []
        names = []
        for set in partition0:
            names.append(set)
            for i, state in enumerate(partition0[set]):
                targets.append([state])
            study.append(targets)
            targets = []

        # For each new automata in the list
        for namenum, aut in enumerate(study):
            # Fill the new automata with transitions to the sets in the partition
            if len(aut) > 1:
                for st1 in aut:
                    for stf in A:
                        if stf[0] == st1[0]:
                            partition0 = copy.deepcopy(cop)
                            for sett in partition0:
                                for sh in stf[1:]:   # i[1:] because i[0] is the state itself
                                    if sh in partition0[sett]:
                                        st1.append(sett)
                print("Study of", names[namenum]+':')
                display(aut, L)
                print()

            # If the automaton is a singleton, do nothing
            else:
                #print("Study of", names[namenum]+":", el[0], "singleton")
                pass

        # Study the separation of the new automaton
        separation = []
        # Create a list of booleans to check if there is separation in the studies
        for a in study:
            if len(a) == 1:
                separation.append(False)
            else:
                sep = []
                for s in a:
                    sb = ""
                    for sh in s[1:]:
                        sb += str(sh)
                    sep.append(sb)
                if all(element == sep[0] for element in sep):   # check if all the elements of sep are the same
                    separation.append(False)
                else:
                    separation.append(True)

        # If there is separation, create a new partition
        if True in separation:
            print("There is separation in the studies. We need to create a new partition.\n")
            # Create the new partition
            partition1 = {}
            # The keys of the partitions are the patterns of the transitions of the automata
            for i, a in enumerate(study):
                for s in a:
                    # sb is the pattern of the transitions of the automata
                    sb = ""
                    for sh in s[1:]:
                        sb += str(sh)
                    if sb == "":
                        sb = str(i)
                    sb += str(i)   # Differentiate same patterns but from different automaton
                    # If the pattern is not in the partition, add it
                    if sb not in partition1:
                        partition1[sb] = []
                    # Group the states of the automata with the same transition pattern
                    partition1[sb] += [s[0]]
            # Change the keys of the partition to letters
            letter = chr(ord(letter)+1)
            keys_to_change = list(partition1.keys())   # Create a list of the keys we want to change
            for i, old_key in enumerate(keys_to_change):   # Replace the keys
                new_key = letter+str(i)
                partition1[new_key] = partition1.pop(old_key)

            # Display the new partition
            printPartition(partition1, ord(letter)-64)
            return minimizeReal(A, L, E, partition1, letter)


        # If there is no separation, create the minimized automaton
        else:
            print("There is no separation in the studies.")
            # Create an automaton with the states of the partition (no transitions yet)
            Amin = []
            # Create the new list of initial/final states
            Emin = ["   " for _ in range(len(partition0))]
            for index, st in enumerate(partition0):
                partition0 = copy.deepcopy(cop)
                if len(partition0[st]) == 1:
                    Amin.append(partition0[st])
                    for i, aut in enumerate(A):
                        if aut[0] == partition0[st][0]:
                            Emin[index] = E[i]
                else:
                    Amin.append([st])
                    FI = []
                    for stateaa in partition0[st]:
                        for i, aut in enumerate(A):
                            if aut[0] == stateaa:
                                if E[i] != "   ":
                                    FI.append(E[i])
                    if FI == []:
                        Emin[index] = "   "
                    else:
                        if "<->" in FI or "<- " in FI and " ->" in FI:
                            Emin[index] = "<->"
                        elif "<- " in FI:
                            Emin[index] = "<- "
                        else:
                            Emin[index] = " ->"

            # Add the transitions of the new automaton
            for st in Amin:
                # Check if the state is a set of states in the partition
                partition0 = copy.deepcopy(cop)
                partmaster = False
                for mer in partition0:
                    if mer == st[0]:
                        partmaster = True
                # If it is
                if partmaster == True:
                    for aut in study:
                        for set in partition0:
                            if aut[0][0] in partition0[set]:
                                partition0 = copy.deepcopy(cop)
                                for tr in aut[0][1:]:
                                    if tr in partition0 and len(partition0[tr]) == 1:
                                        st.append(partition0[tr][0])
                                    else:
                                        st.append(tr)

                # Otherwise, if the state is a singleton in the partition
                else:
                    for og in A:
                        if og[0] == st[0]:
                            for tr in og[1:]:
                                partition0 = copy.deepcopy(cop)
                                for set in partition0:
                                    if tr in partition0[set]:
                                        if len(partition0[set]) == 1:
                                            st.append(tr)
                                        else:
                                            st.append(set)
            # Return the minimal automaton
            return (Amin, Emin)




def minimize(A, L, E):
        
    # Create the initial partition
    partition = {'T': [], 'NT': []}
    for i, s in enumerate(E):
        if s in ['<->', '<- ']:
            partition['T'].append(A[i][0])
        else:
            partition['NT'].append(A[i][0])
    
    printPartition(partition, 0)
    return minimizeReal(A, L, E, partition)
    










def printPartition(partition, num):
    l = len(str(num))-1
    if l < 0: l = 0
    print("┌───────────────────────────"+"─"*l+"┐")
    print("│   PARTITION "+str(num)+"             │")
    print("└───────────────────────────"+"─"*l+"┘")

    # Print the sets of the partition
    print("Sets:")
    for i in partition:
        s = str(partition[i])
        s = s.replace("[", "{")
        s = s.replace("]", "}")
        s = s.replace("\'", "")
        print(" "+i + " = " + s)

    # Print the union of the sets of the partition
    print("Theta:")
    print(' θ'+str(num), end=" = ")
    s = ""
    for i in partition:
        s += i + " ∪ "
    print(s[:-3])

    print()








if __name__ == "__main__":
    from functions import *
    
    
    """
    print()
    L = ['a', 'b']
    E = ['<->', '<- ', '<- ', '<- ', '<- ', '   ']
    A = [
        ["02", "01", "12"],
        ["01", "1", "012"],
        ["12", "01", "02"],
        ["012", "01", "012"],
        ["1", "P", "02"],
        ["P", "P", "P"]
        ]
    
    print("\nAutomaton:")
    display(A, L, E)
    
    A, E = minimize(A, L, E)
    print("\nEquivalent minimal automaton:")
    display(A, L, E)
    
    for _ in range(10): print()

    E = [' ->', '   ', '   ', '   ', '<- ', '   ']
    A = [
         [0, 1, 0],
         [1, 'P', 2],
         [2, 3, 'P'],
         [3, 4, 'P'],
         [4, 'P', 'P'],
         ['P', 'P', 'P']
        ]
    
    #print(A)
    print("\nAutomaton:")
    display(A, L, E)
    
    A, E = minimize(A, L, E)
    print("\nEquivalent minimal automaton:")
    display(A, L, E)
    
    
    
    
    
    for _ in range(10): print()
    """

    A = [['i', '01', '12'], ['02', '01', '12'], ['01', '1', '012'], ['12', '01', '02'], ['012', '01', '012'], ['1', 'P', '02'], ['P', 'P', 'P']]
    E = [' ->', '<- ', '<- ', '<- ', '<- ', '<- ', '   ']
    L = ['a', 'b']
    
    print("\nAutomaton:")
    display(A, L, E)
    
    A, E = minimize(A, L, E)
    print("\nEquivalent minimal automaton:")
    display(A, L, E)
    
    
    

    input()