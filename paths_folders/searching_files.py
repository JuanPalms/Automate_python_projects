"""
This python module implements a simple procedure to look for files anywere in your computer
"""
from pathlib import Path
import os

print("This is an engine for searching files in the system, please input the root directory from which you wish to start your search")
print(f"Remember the engine search is located at {os.getcwd()}")
var = input("Please enter root directory: ")

# Expand the '~' to the actual path to the home directory
var = os.path.expanduser(var)

root_dir = Path(var)
print(root_dir)
search_term = input("Please input a search term:")

for path in root_dir.rglob("*"):
    if search_term in path.stem:
        print(path.absolute())
