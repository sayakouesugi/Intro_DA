"""A dictionary is a mutable data type that stores mapping of unique keys to values. Here's dictionary that stores elements and their atomic numbers"""

elements = {"hydrogen": 1, "helium": 2, "carbon": 6}

print(elements["helium"]) # print the value mapped to "helium"
elements["lithium"] = 3 # insert "lithium" with a value of 3 into the dictionary

print("carbon" in elements)
