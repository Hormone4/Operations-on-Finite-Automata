# Operations-on-Finite-Automata

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
Format needed for the data:<br>
L = ["a","b"]<br>
E = [" ->", "   ", "   ", "   ", "<- "]   # " ->" is initial, "   " is neither, "<->" is both, "<- " is final<br>
A = [[0, [0,1], 0],<br>
     [1, -1, 2],<br>
     [2, 3, -1],<br>
     [3, 4, -1],<br>
     [4, -1, -1]]<br>