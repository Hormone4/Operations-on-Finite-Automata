# The folder contains many txt files
# the goal is to delete all empty lines in all txt files

import os


# Get a list of all files in the directory
files = os.listdir()

# Filter out the automaton files
automaton_files = [f for f in files if f.endswith(".txt") and not(f.startswith("README")) and not(f.startswith(".gitignore")) and not(f.endswith("-Execution-trace.txt"))]


# For each automaton file
for automaton_file in automaton_files:
    print("\n\n\n AUTOMATON FILE:",automaton_file)
    with open(automaton_file, 'r') as file:
        lines = file.read().splitlines()  # this does not include the newline characters
        lines = [line for line in lines if line.strip() != '']
    with open(automaton_file, 'w') as file:
        file.write('\n'.join(lines))


"""
import os

directory = r'C:\Users\sachl\Documents\GitHub\Operations-on-Finite-Automata\Int1-2-Test-automaton'

for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        with open(os.path.join(directory, filename), 'r') as file:
            lines = file.read().splitlines()  # this does not include the newline characters
            lines = [line for line in lines if line.strip() != '']
        with open(os.path.join(directory, filename), 'w') as file:
            file.write('\n'.join(lines))
"""