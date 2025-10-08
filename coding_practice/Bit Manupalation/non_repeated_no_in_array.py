"""
Find the only non-repeated number in an array where every other number repeats twice.
"""

arr = [2, 3, 5, 4, 5, 3, 4]

no_dict = {

}

for i in arr:
    if i in no_dict:
        no_dict[i] += 1
    else:
        no_dict[i] = 1

for key, value in no_dict.items():
    if value == 1:
        print(f"This is the no which only repeated once {key}")

print(no_dict)

"""
XOR Logic

0 ^ 2 = 2  
2 ^ 3 = 1  
1 ^ 5 = 4  
4 ^ 4 = 0  
0 ^ 5 = 5  
5 ^ 3 = 6  
6 ^ 4 = 2
"""
only_once = 0

for i in arr:
    only_once ^= i

print(f"Using the XOR logic {only_once}")
