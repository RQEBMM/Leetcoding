# 101. Symmetric Tree
# Easy
# 14.7K
# 352
# Companies

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

# Example 1:

# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Example 2:

# Input: root = [1,2,2,null,3,null,3]
# Output: false

 

# Constraints:

#     The number of nodes in the tree is in the range [1, 1000].
#     -100 <= Node.val <= 100


# The Easy Way:
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        if not left or not right or left.val != right.val:
            return False

        return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)'


# The Hard Way:
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        l = root.left
        r = root.right
        if l is None and r is None:
            return True
        if l is None or r is None:
            return False
        
        def flip_tree(root):
            if root is None:
                return
                
            flip_tree(root.right)
            flip_tree(root.left)
            swap = root.left
            root.left = root.right
            root.right = swap


            return root
          
        # def print_tree(root, lst):
        #     if root is None:
        #         return
        #     lst += [root.val]
        #     print_tree(root.right, lst)
        #     print_tree(root.left, lst)
        #     return lst
        # lst = print_tree(root, [])
        # print(lst)
        # print(print_tree(l, []))
        # print(print_tree(r, []))
        # r = flip_tree(r)
        # print(print_tree(r, []))
      
        def is_same_tree(l, r):
          if l is None and r is None:
            return True
          if l is None or r is None:
            return False
          if l.val == r.val:
            return is_same_tree(l.left, r.left) and is_same_tree(l.right, r.right)

        return is_same_tree(l, flip_tree(r))
