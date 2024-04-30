# Operations-on-Finite-Automata
## Project
The goal of this project was to implemnt in python all the functions appliable on a finite automaton.<br>
The folder contains 44 txt files each representing an automaton that you can test in the program. Each automaton also has an execution trace file showing the output obtained after using the program so that you do not have to test each one of them.
## Functions
1. Read a finite automaton from a text file, then store it in memory
2. Display it in the terminal
3. Display other types of information: is the FA deterministic? deterministic and complete? standard?
4. Standardize the FA
5. Complete and determinize the FA
6. Minimize the FA showing all the partitions and the studies
7. Test word recognition
8. Create a FA recognizing the complementary language
## Data format
### Example of a text file:<br>
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
### Explication of the text file:<br>
2 symbols in the alphabet<br>
A={a,b}<br>
5 states<br>
Q={0,1,2,3,4}<br>
1 initial state<br>
I={0}<br>
1 final state<br>
T={4}<br>
6 transitions
### Format of the data after extraction:<br>
L = ["a","b"]<br>
E = [" ->", "   ", "   ", "   ", "<- "]<br>
A = [[0, [0,1], 0],<br>
     [1, -1, 2],<br>
     [2, 3, -1],<br>
     [3, 4, -1],<br>
     [4, -1, -1]]<br> 

- L is the alphabet
- E is the list of initial/final states in order (" ->" is initial, "<- " is final, "   " is neither, "<->" is both)
- A is the automaton. The first column of A is the states of A, the other columns are the targets of the transitions according to the alphabet. -1 is for no transition. The automaton accepts integers, lists and characters / strings.
