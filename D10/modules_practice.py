# --- Using Built-in Modules ---

import math
import os

# Math module examples
print("Square root of 25:", math.sqrt(25))
print("Factorial of 5:", math.factorial(5))
print("Value of pi:", math.pi)

# OS module examples
print("\nCurrent Working Directory:", os.getcwd())
print("Files in current directory:", os.listdir())

# --- Using from-import syntax ---
from math import pow, floor
print("\nPower (2^3):", pow(2, 3))
print("Floor of 5.9:", floor(5.9))
