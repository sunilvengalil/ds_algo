"""
https://www.pramp.com/challenge/gKQ5zA52mySBOA5GALj9
"""

def bin_search(arr, target):
    #
    pass


def find_tuples(arr, n, from_index, target):
    #
    if n == 1:
        index = bin_search(arr[from_index:], target)
        if index != -1:
            return arr[index]
        else:
            return []

    # impment other cases also
    for i in range(len(arr)):
        resut = find_tuples(arr[i + 1:], n - 1, target - arr[i])
        if len(result) == n - 1:
            return [arr[i]] + result

    return []


def find_array_quadruplet(arr, s):
    # Sort the array
    sorted_arr = sorted(arr)
    for i in range(len(arr)):
        # search for a triplet in arr[i+:]
        resut = find_tuples(arr[i + 1:], 3, s - arr[i])
        if len(result) == 3:
            return [arr[i]] + result

    return []


# [2, 7, 4, 0, 9, 5, 1, 3]
[0, 1, 2, 3, 4, 5, 7, 9]

[2, 3, 4, 5, 6, 7, 9]




