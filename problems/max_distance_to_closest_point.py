from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_zero_index_end = 0
        max_zero_index_start = 0
        max_zero_length = 0
        current_distance_to_left = 0
        current_run_is_max = False
        last_one_index = -1
        for i, seat in enumerate(seats):
            if seat == 1:
                current_distance_to_left = 0
                last_one_index = i
                if current_run_is_max:
                    current_run_is_max = False
                    max_zero_index_end = i
                    if max_zero_index_start == -1:
                        max_zero_length *= 2
            else:
                current_distance_to_left += 1
                if current_distance_to_left > max_zero_length:
                    max_zero_length = current_distance_to_left
                    max_zero_index_start = last_one_index
                    current_run_is_max = True
        if current_distance_to_left != 0:
            if current_run_is_max or current_distance_to_left > max_zero_length // 2:
                return len(seats) - last_one_index -  1
        if max_zero_index_start == -1:
            return max_zero_index_end
        place = (max_zero_index_end + max_zero_index_start) // 2
        return min(place - max_zero_index_start, max_zero_index_end - place)



print(Solution().maxDistToClosest([1,0,0,0,0,1,0,1]))
print(Solution().maxDistToClosest([1,0,0,0,1,0,1]))

print(Solution().maxDistToClosest([1,0,0,0]))

print(Solution().maxDistToClosest([0,0,0,1,0,0,0,1]))

print(Solution().maxDistToClosest([0, 0, 0,  1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]))



1,0,1,0,0,0,1