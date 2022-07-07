from collections import defaultdict
from typing import List, Dict


def get_shortest_string(current_speed, current_pos, target, memo):
    print(f"current_speed={current_speed}, current_pos={current_pos}, target={target}")
    if current_pos in memo and len(memo[current_pos]) > 0 and (
            current_speed in memo[current_pos] or 0 in memo[current_pos]):
        return memo[current_pos][current_speed]

    # Terminiation condition
    if target == current_pos + current_speed:
        memo[current_pos][current_speed] = "A"
#        print("terminating")
        return "A"

    # Explore forward accelerate
    forward_solution = None
    reverse_solution = None
    if current_speed > 0:
        if current_pos + current_speed - target < 2 * target:
            # Explore A
            new_speed = current_speed * 2
            new_current_pos = current_pos + current_speed
            if new_speed != current_speed and new_current_pos != current_pos:
                forward_solution = get_shortest_string(new_speed,
                                                       new_current_pos,
                                                       target,
                                                       memo)
                print("forward_solution", forward_solution)

                forward_solution = "A" + forward_solution
        else:
            # Explore R
            new_speed = -1 if current_speed > 0 else 1
            new_current_pos = current_pos
            if new_speed != current_speed or new_current_pos != current_pos:
                reverse_solution = get_shortest_string(new_speed,
                                                       new_current_pos,
                                                       target,
                                                       memo
                                                       )
                reverse_solution = "R" + reverse_solution
    else:
        if target - (current_pos + current_speed) < 2 * target:
            # Explore A
            new_speed = current_speed * 2
            new_current_pos = current_pos + current_speed

            forward_solution = "A" + get_shortest_string(new_speed,
                                                         new_current_pos,
                                                         target,
                                                         memo)
        else:
            # Explore R
            new_speed = -1 if current_speed > 0 else 1
            new_current_pos = current_pos
            if new_speed != current_speed or new_current_pos != current_pos:
                reverse_solution = "R" + get_shortest_string(new_speed,
                                                             new_current_pos,
                                                             target,
                                                             memo
                                                             )

    if reverse_solution is not None:
        solution = reverse_solution
        if forward_solution is not None and len(forward_solution) < len(solution):
            print(forward_solution)
            solution = forward_solution
    else:
        solution = forward_solution

    print(f"current_speed={current_speed}, current_pos={current_pos}, solution={solution}, solution_len={len(solution)}")
    memo[current_pos][current_speed] = solution
    return solution

class Solution:
    def racecar(self, target: int) -> int:
        memo = defaultdict(dict)  # [{speed:num_steps}]
        # speed 0 is don't care - any  initial speed
        memo[target] = {0: ""}
        solution = get_shortest_string(1, 0, target, memo)
        print("final solution string",solution)
        return len(solution)

final_solution = Solution().racecar(4)
print("final_solution", final_solution)