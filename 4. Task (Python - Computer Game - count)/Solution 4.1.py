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

