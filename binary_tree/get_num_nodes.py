
class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def get_num_nodes(root:TreeNode):
    num_nodes = 0
    vals_left = 0
    vals_right  = 0
    if root.left is not None:
        num_nodes_left, val_left = get_num_nodes(root.left)
        num_nodes += num_nodes_left
    if root.right is not None:
        num_nodes_right, val_right = get_num_nodes(root.right)
        num_nodes += num_nodes_right
    return num_nodes + 1, vals_left + vals_right + root.val


def balance_tree(root:TreeNode):
    num_nodes = 0
    vals_left = 0
    vals_right  = 0
    num_moves = 0
    num_nodes_left = 0
    if root.left is not None:
        num_nodes_left, val_left = get_num_nodes(root.left)
        num_nodes += num_nodes_left
    if root.right is not None:
        num_nodes_right, vals_right = get_num_nodes(root.right)
        num_nodes += num_nodes_right

    if vals_left < num_nodes_left:
        to_be_moved = num_nodes_left - vals_left
        if root.val >= to_be_moved:
            root.val -= to_be_moved
            root.left.val += to_be_moved
            num_moves += to_be_moved
        elif root.val > 0:
            num_moves += root.val
            root.left.val += root.val
            root.val = 0
    elif vals_left > num_nodes_left:
        vals_left

    if vals_right < num_nodes_right:
        to_be_moved = num_nodes_right - vals_left
        if root.val >= to_be_moved:
            root.val -= to_be_moved
            root.left += to_be_moved
            num_moves += to_be_moved


