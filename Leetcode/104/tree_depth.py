# 104. Maximum Depth of Binary Tree
# Easy
# 12K
# 197
# Companies

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:

# Input: root = [1,null,2]
# Output: 2

 

# Constraints:

#     The number of nodes in the tree is in the range [0, 104].
#     -100 <= Node.val <= 100

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        node = root
        visited = {}

        def visit(node, depth):
            if node and node is not None and not visited.get(node):
                depth += 1
                visited[node] = depth
                for node in [node.left, node.right]:
                    visit(node, depth)
        
        visit(root, 0)
        
        try:
            return max(visited.values())
        except ValueError:
            return 0
