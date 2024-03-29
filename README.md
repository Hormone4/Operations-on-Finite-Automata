# Operations-on-Finite-Automata
## Functions
1. Read a FA from a text file, then store it in memory
2. Display it in the terminal
3. Display other types of information: is the FA deterministic? deterministic and complete? standard?
4. Standardize the FA
5. Determinize and complete the FA
6. Minimize the FA
7. Test word recognition
8. Create a FA recognizing the complementary language
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
