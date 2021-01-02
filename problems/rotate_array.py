from copy import deepcopy
from typing import List


def rotate_array(a: List[int], k: int) -> None:
    temp = [0] * k
    offset = len(a) - k
    for temp_index in range(k):
        temp[temp_index] = a[temp_index + offset]

    for i in range(len(a) - 1, k - 1, -1):
        a[i] = a[i - k]
    for i in range(k - 1, -1, -1):
        a[i] = temp[i]


def rotate_array_1(a: List[int], k: int) -> None:
    num_partition = gcd(len(a), abs(k))
    for i in range(num_partition):
        temp = a[i]
        next_index = i + k
        start_index = i
        while start_index != next_index:
            print(i, next_index)
            a[i] = a[next_index]
            i = next_index
            next_index = next_index + k
            if next_index >= len(a):
                next_index = next_index - len(a)
            if next_index < 0:
                next_index += len(a)
        a[i] = temp


def gcd(n1, n2):
    if n1 < n2:
        n1, n2 = n2, n1
    if n2 == 0:
        return n1
    else:
        return gcd(n2, n1 % n2)


arr = [1, 2, 3, 4, 5, 6]

rotated_1 = deepcopy(arr)
rotate_array(rotated_1, 2)
print(rotated_1)

rotated_2 = deepcopy(arr)
rotate_array_1(rotated_2, -2)
print(rotated_2)
