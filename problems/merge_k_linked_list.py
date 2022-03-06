from typing import List
# Definition for singly-linked list.
from heapq import heappush, heapify, heappop

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def find_min(self, lists:List[ListNode]):
        min_list = lists[0]
        min_index = 0
        for i, l in enumerate(lists[1:]):
            if l.val < min_list.val:
                min_list = l
                min_index = i + 1
        return min_list, min_index

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lists = [l for l in lists if l is not None]
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        heap = [(l.val, l) for l in lists]
        heapify(heap)
        min_list = heappop()[1]
        head = min_list
        current_pointer = min_list
        if min_list.next is not None:
            heappush(heap, (min_list.next.val, min_list.next))
        current_pointer.next = None
        while len(lists) > 0:
            min_list = heappop()[1]
            current_pointer.next = min_list
            if min_list.next is not None:
                heappush(heap, (min_list.next.val, min_list.next))
            current_pointer = current_pointer.next
            current_pointer.next = None
        return head
