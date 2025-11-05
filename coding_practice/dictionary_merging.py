"""
Merge two dictionaries and sum the values of common keys.
dict1 = {'a': 2, 'b': 3, 'c': 1}
dict2 = {'a': 1, 'b': 2, 'd': 4}

"""
dict1 = {'a': 2, 'b': 3, 'c': 1}
dict2 = {'a': 1, 'b': 2, 'd': 4}


dict3 = {}

for key1, key2 in zip(dict1, dict2):
    if key1 in dict2:
        dict3[key1] = dict1[key1] + dict2[key1]

    if key1 not in dict2:
        dict3[key1] = dict1[key1]

    if key2 not in dict1:
        dict3[key2] = dict2[key2]


# ChatGpt Code
# Combine all unique keys from both dictionaries
"""
set(dict1.keys()) | set(dict2.keys()) → combines keys from both dictionaries (union).
get(key, 0) → safely gets the value of a key, returning 0 if it doesn’t exist.
Then you just add the two values and store them in dict3.
"""

all_keys = set(dict1.keys()) | set(dict2.keys())  # Union Method
for key in all_keys:
    # Get value from dict1 (if key not present, default to 0)
    val1 = dict1.get(key, 0)
    # Get value from dict2 (if key not present, default to 0)
    val2 = dict2.get(key, 0)

    # Add both values
    dict3[key] = val1 + val2


print(dict3)


