"""A computer gaame allows players to perform special actions using the key combinations "QEE" or "ZCC".
A player gets extra points if they use these combinations equally in a gaming session.
Skilled players who don't use any of the special actions also get extra points.
Complete the function match_key_combo, which returns True if the number of occurences of "QEE" matches the number of occurrences of "ZCC" in a sequence of keypresses recieved from player,
or if both key combinations have an occurrence of 0. Otherwise it should return False.
String comparison should be case insensitive. Code looks like: def match_key_combo(sequence): return None , print(match_key_combo("QEEAZCC"))"""

def match_key_combo(sequence):
    # Convert the sequence to lowercase for case-insensitive comparison
    sequence = sequence.lower()
    
    # Count the occurrences of "qee" and "zcc"
    qee_count = sequence.count("qee")
    zcc_count = sequence.count("zcc")
    
    # Check if the counts match or if both are zero
    return qee_count == zcc_count

# Example usage
print(match_key_combo("QEEAZCC"))  # Should return True
print(match_key_combo("QEEQEEZCCZCC"))  # Should return True
print(match_key_combo("QEEZCCQEE"))  # Should return False
print(match_key_combo("XYZ"))  # Should return True (no QEE or ZCC)

#1. sequence.lower(): This converts the input sequence to lowercase, making the comparison case-insensitive.
#2. sequence.count("qee") and sequence.count("zcc"): These count the occurrences of the key combinations "QEE" and "ZCC" in the string.
#3. Return True: The function checks if the counts of "QEE" and "ZCC" are equal, including the case where both counts are zero (i.e., neither "QEE" nor "ZCC" appears in the sequence).

#Example output: 
""" match_key_combo("QEEAZCC") → True (one "QEE" and one "ZCC")
    match_key_combo("QEEQEEZCCZCC") → True (two "QEE" and two "ZCC")
    match_key_combo("QEEZCCQEE") → False (two "QEE" but one "ZCC")
    match_key_combo("XYZ") → True (no "QEE" or "ZCC") """