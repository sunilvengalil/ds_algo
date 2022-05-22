# https://www.pramp.com/challenge/0QmxM9x81lTKO47p43Jr


def isToeplitz(arr):
    num_rows = len(arr)
    num_cols = len(arr[0])
    # Check for leading diagonal
    result = True
    for row in range(num_rows - 1):
        for col in range(num_cols - 1):
            if arr[row][col] != arr[row + 1][col + 1]:
                result = False
                break
    return result

a= [[1,  2, 3, 4, 5],
    [10, 1, 2, 3, 4],
    [20, 10, 1, 2,3]
]

assert(isToeplitz(a))


# row 0, 0, 0, 0, 0
# col 0, 1, 2, 3, 4

