# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def get_tree(root, left, right):
    # Create a root node
    root = TreeNode(root)
    # Create left subtree by recursion
    if len(left_tree) > 0:
        left_tree = get_tree(left[0])
    # Create right subtree by recursion

    return root


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # find the root index in post order - O(n)
        root_index_in_post_order = postorder.index(preorder[0])
        n = len(preorder)
        return (preorder[0], postorder[:root_index_in_post_order] if root_index_in_post_order > 0 else [],
                postorder[root_index_in_post_order + 1:] if root_index_in_post_order < n - 1 else [])
