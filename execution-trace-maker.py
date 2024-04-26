import os
import subprocess

# Get a list of all files in the directory
files = os.listdir()

# Filter out the automaton files
automaton_files = [f for f in files if f.endswith(".txt") and not(f.startswith("README")) and not(f.startswith(".gitignore")) and not(f.endswith("-Execution-trace.txt"))]


# For each automaton file
for automaton_file in automaton_files:
    print("\n\n\n AUTOMATON FILE:",automaton_file)

    # Remove empty lines from the automaton file
    with open(automaton_file, 'r') as file:
        lines = file.read().splitlines()  # this does not include the newline characters
        lines = [line for line in lines if line.strip() != '']
    with open(automaton_file, 'w') as file:
        file.write('\n'.join(lines))


    # Construct the command to run the python script
    command = f"python test.py {automaton_file}"

    # Construct the output file name
    output_file = f"{automaton_file.split('.')[0]}-Execution-trace.txt"

    # Run the command and redirect the output to a text file
    with open(output_file, "w") as f:
        subprocess.run(command, stdout=f, shell=True)


input()