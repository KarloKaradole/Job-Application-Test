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