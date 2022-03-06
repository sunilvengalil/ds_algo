from heapq import heappush, heappushpop
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        queue = []
        distance = points[0][0] * points[0][0]  + points[0][1]  * points[0][1]
        current_max = distance
        for point in points:
            distance = point[0] * point[0] + point[1] * point[1]
            if len(queue) < K:
                heappush(queue,(-distance,point))
                if distance > current_max:
                    current_max = distance
            else:
                # queue has the k closest points
                if distance < current_max:
                    # replace the new closest point in queue
                    max_in_heap = heappushpop(queue, (-distance, point))
                    current_max = -max_in_heap[0]
        return [l[1] for l in queue]


points = [[1,3],[-2,2],[2,1]]
print(Solution().kClosest(points, 1))



