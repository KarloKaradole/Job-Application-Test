"""A hospital patient tracking system is restructuring its patient records.
The current format i fragmented, each patient is represented as a namedtuple.
Each element contains a different piece of info about the patient.
Your task is to write a functioin that merges all of the info into one namedtuple, named Patient, in the order that it's provided to the function.
For example:
    PersonalDetails=namedtuple("PersonalDetails", ["date_of_birth"]) personal details = PersonalDetails(date_of_birth ="06-04-1972")
    Complexion = namedtuple("Complexion", ["eye_color","hair_color"]) complexion = Complexion(eye_color = "Blue", hair_color = "Black" print(merge(personal_details, complexion).
Should desplay: Patient(date_of_birth = "06-04-1972", eye_color = "Blue", hair_color = "Black")"""

from collections import namedtuple # function that returns a new tuple subclass with named fields. You can access its fields both by index and by name.

def merge(*args):
    """This function accepts a variable number of arguments (*args), which are expected to be instances of different namedtuple types.
       The *args syntax allows the function to take any number of arguments as a tuple."""
    # Collect all field names and values from the provided namedtuples
    fields = [] # This list will collect the field names (like date_of_birth, eye_color, etc.) from each namedtuple.
    values = [] # This list will collect the corresponding values for each field.
    
    for namedtuple_instance in args:
        fields.extend(namedtuple_instance._fields)  # Collect field names 
                                                    # Each namedtuple has a special attribute called _fields that stores the names of the fields in a tuple (e.g., for PersonalDetails, _fields will be ('date_of_birth',)).
        values.extend(namedtuple_instance)          # Collect corresponding values
                                                    # The namedtuple instance itself is iterable (i.e., it can be unpacked like a regular tuple), so you can access its values directly.
                                                    # The values.extend(namedtuple_instance) adds all the field values (like "06-04-1972", "Blue", "Black") to the values list.
    
    # Create a new namedtuple called "Patient" with the collected fields
    Patient = namedtuple("Patient", fields) # A new namedtuple class called Patient is created using the collected field names (fields).
                                            # This namedtuple will have all the fields from the input namedtuple instances.
    
    # Create an instance of Patient with the collected values
    return Patient(*values) # The values list is passed to the Patient constructor using the *values syntax (which unpacks the list of values into individual arguments).
                            # This creates an instance of the Patient namedtuple with all the merged fields and values.

# Example usage
PersonalDetails = namedtuple("PersonalDetails", ["date_of_birth"]) # PersonalDetails: A namedtuple with a single field date_of_birth.
Complexion = namedtuple("Complexion", ["eye_color", "hair_color"]) # Complexion: A namedtuple with two fields, eye_color and hair_color.

personal_details = PersonalDetails(date_of_birth="06-04-1972") # personal_details: An instance of PersonalDetails with the value "06-04-1972".
complexion = Complexion(eye_color="Blue", hair_color="Black") # complexion: An instance of Complexion with the values "Blue" for eye_color and "Black" for hair_color.

# Merging the namedtuples into a single Patient namedtuple
patient = merge(personal_details, complexion)
print(patient)