# Operations-on-Finite-Automata
## Functions
1. Reading a FA that you should first code in a text file, then storing that information in memory
2. Display it on the screen.
3. Displaying other types of information: is the FA deterministic? deterministic and complete? standard?
4. If the FA is not standard, standardizing it on demand.
5. If the FA is not complete deterministic, obtaining an equivalent complete deterministic FA. 
6. Calculating the equivalent minimal FA. 
7. Testing word recognition. 
8. Creating an automaton recognizing the complementary language and testing word recognition on that automaton.
## Data format
Example of the text file:<br>
2<br>
5<br>
1 0<br>
1 4<br>
6<br>
0a0<br>
0b0<br>
0a1<br>
1b2<br>
2a3<br>
3a4<br>
<br>
Format of the data after extraction:<br>
L = ["a","b"]<br>
E = [" ->", "   ", "   ", "   ", "<- "]   # " ->" is initial, "   " is neither, "<->" is both, "<- " is final<br>
A = [[0, [0,1], 0],<br>
     [1, -1, 2],<br>
     [2, 3, -1],<br>
     [3, 4, -1],<br>
     [4, -1, -1]]<br>
