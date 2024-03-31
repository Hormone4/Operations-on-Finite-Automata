from functions import display, automata_type


def minimizeReal(A, L, partition0, letter='@'):

    # Check if partition contains only singletons
    singletons = True
    for i in partition0:
        if len(partition0[i]) != 1:
            singletons = False
            break
    if singletons:
        print("The partition is made only of singletons.\nThe automaton was already minimal.")
        return A
    
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
        for namenum, el in enumerate(study):
            # Fill the new automata with transitions to the sets in the partition
            if len(el) > 1:
                for en in el:
                    for i in A:
                        if i[0] == en[0]:
                            for kek in partition0:
                                for sh in i[1:]:   # i[1:] because i[0] is the state itself
                                    if sh in partition0[kek]:
                                        en.append(kek)
                print("Study of", names[namenum]+':')
                display(el, L)
                print()

            # If the automaton is a singleton, do nothing
            else:
                #print("Study of", names[namenum]+":\n   ", el[0], "singleton")
                #print("Study of", names[namenum]+":", el[0], "singleton")
                pass
            #print()

        # Study the separation of the new automaton
        separation = []
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

        # If there is a separation, create a new partition
        if True in separation:
            print("There is separation in the studies. We need to create a new partition.\n")
            # Create the new partition
            partition1 = {}
            for i, a in enumerate(study):
                for s in a:
                    sb = ""
                    for sh in s[1:]:
                        sb += str(sh)
                    if sb == "":
                        sb = str(i)
                    if sb not in partition1:
                        partition1[sb] = []
                    partition1[sb] += [s[0]]

            # Change the keys of the partition to letters
            letter = chr(ord(letter)+1)
            keys_to_change = list(partition1.keys())   # Create a list of the keys you want to change
            for i, old_key in enumerate(keys_to_change):   # Use a for loop to replace the keys
                new_key = letter+str(i)
                partition1[new_key] = partition1.pop(old_key)

            # Display the new partition
            printPartition(partition1, ord(letter)-64)
            
            return minimizeReal(A, L, partition1, letter)

        #print(partition0)
        # if partition0 == partition1, the automaton is minimized
        #if equalPartition(partition0, partition1):
        #    print("Automaton is minimized.")
        #    # Display the minimized automaton
        #    return
        #else:
        #    print("Automaton is not yet minimal.")
        #    printPartition(partition1, ord(letter)-64)
        #    return minimizeReal(A, L, partition1, letter)



def minimize(A, L, E):
    # Check if the automaton is complete deterministic
    type = automata_type(A, L, E)
    if type[1] == 1 and type[2] == 1:
        
        # Create the initial partition
        partition = {'T': [], 'NT': []}
        for i, s in enumerate(E):
            if s in ['<->', '<- ']:
                partition['T'].append(A[i][0])
            else:
                partition['NT'].append(A[i][0])
        
        printPartition(partition, 0)
        return minimizeReal(A, L, partition)
    
    else:
        print("Automaton is not complete deterministic. Cannot be minimized.")
        # To be replaced by:
        #complete(A, L, E)
        #determinize(A, L, E)
        #minimize(A, L, E)




def printPartition(partition, num):
    l = len(str(num))-1
    if l < 0: l = 0
    print("┌───────────────────────────"+"─"*l+"┐")
    print("│   PARTITION "+str(num)+"             "+" "*l+"│")
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
    
    display(A, L, E)

    minimize(A, L, E)

    E = [' ->', '   ', '   ', '   ', '<- ', '   ']
    A = [
         [0, 1, 0],
         [1, 'P', 2],
         [2, 3, 'P'],
         [3, 4, 'P'],
         [4, 'P', 'P'],
         ['P', 'P', 'P']
        ]
    print(A)
    display(A, L, E)

    minimize(A, L, E)


    #a = 'A'
    ##print(a+1)
    ## print next character in alphabet
    #print(chr(ord(a)-1))
    #print(a)
    #print(chr(ord(a)+1))
    #print(chr(ord(a)+2))

    #print("\nTESTS:")
    #part = {}
    #if 'T' not in part:
    #    print("cacaa")
    #    #part['T'] = []
    #part['T'] = ['1', 'P']
    #part['NT'] = ['2', '3', '4']
    #
    ## change 'T' to str(i)
#
#
    #for i, s in enumerate(part):
    #    # change 'T' to str(i)
    #    print(i, s)
    #    print(part[s])
#
#
    #print(part)



    input()