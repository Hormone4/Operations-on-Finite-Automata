# Loader to extract the data from the text file


# def load_data(file):









# Example of the text file:
# 2
# 5
# 1 0
# 1 4
# 6
# 0a0
# 0b0
# 0a1
# 1b2
# 2a3
# 3a4

# Format needed for the data:
L = ["a","b"]
E = [" ->", "   ", "   ", "   ", "<- "]
A = [[0, (0,1), 0],
     [1, -1, 2],
     [2, 3, -1],
     [3, 4, -1],
     [4, -1, -1]]
