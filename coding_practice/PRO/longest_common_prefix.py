"""
Longest common prefix
"""


def longest_common_prefix(input_val:list):
    if not input_val:
        return ""

    reference = input_val[0]
    result = ""

    for i in range(len(reference)):
        char = reference[i]

        for string in input_val[1:]:
            # If string is too short or character doesn't match
            if i >= len(string) or char != string[i]:
                return result

        result += char

    return result



strs = ["flower", "flow", "flight"]
print(longest_common_prefix(strs))
