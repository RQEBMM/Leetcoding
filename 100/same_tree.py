
# 100. Same Tree
# Easy
# 10.7K
# 214
# Companies

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Example 1:

# https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg

# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:

# https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg

# Input: p = [1,2], q = [1,null,2]
# Output: false

# Example 3:

# Input: p = [1,2,1], q = [1,1,2]
# Output: false

 

# Constraints:

#     The number of nodes in both trees is in the range [0, 100].
#     -104 <= Node.val <= 104



# Easy Way (implicit post-order traversal)
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Hard Way (explicit traversal)
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # bfs or dfs simultaneously or traversal
        # return False if ever not equal
        def traverse(p_node, q_node):
            print(p_node, q_node)
            if p_node is None and q_node is None:
                return True
            if p_node is None or q_node is None:
                return False
            
            while p_node and q_node:
                if p_node.val != q_node.val:
                    return False
                return traverse(p_node.left, q_node.left) and traverse(p_node.right, q_node.right)

            return True
        
        return traverse(p, q)
