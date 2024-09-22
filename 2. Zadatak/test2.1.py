"""A script you are writing uses logarithmic functions from the math module.
Implement the add_patch function that should add a log100 function to the math module.
The log100 function should wrap the existing math.log function so that it calculates a logatithm with a base of 100.
For example, math.log100(10) is equivalent to math.log(10,100) and should return 0.5"""

import math

def add_patch():
    # Define the log100 function that wraps math.log with base 100
    def log100(x):
        return math.log(x, 100)
    
    # Add log100 to the math module
    math.log100 = log100

# Call add_patch to patch the math module
add_patch()

# Test the new log100 function
print(math.log100(10))  # Should return 0.5