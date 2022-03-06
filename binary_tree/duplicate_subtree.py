# https://leetcode.com/problems/find-duplicate-subtrees/
from typing import List, Optional
from collections import defaultdict

from . import TreeNode

# Possible duplicates
"""
pairs of all nodes with same val
"""

"""
Pairs that can not be duplicates
(node, d)  for all d which is a descentant of node

"""

class Solution:

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        # Get a list of all nodes with duplicate values
        possible_candidates = defaultdict(list)

        # DFS
        stack = [root]
        while stack:
            node = stack.pop()
            possible_candidates[node.val].append(node)
            if node.left

        # Check the tree rooted at thi

