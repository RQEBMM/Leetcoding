# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Example 1: https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

 

# Constraints:

#     The number of nodes in each linked list is in the range [1, 100].
#     0 <= Node.val <= 9
#     It is guaranteed that the list represents a number that does not have leading zeros.


# # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):

    def listForNode(self, start_node):
        retlist = [start_node.val]
        node = start_node.next 
        while node:
            retlist.append(node.val)
            node = node.next
        return retlist

    def nodeForList(self, list_o_stuff):
        lastnode = None
        for x in list_o_stuff:
            newnode = ListNode(val=x, next=lastnode)
            lastnode = newnode

        return lastnode

    def numForList(self, list_of_vals):
        return sum([x * pow(10, idx) for idx, x in enumerate(list_of_vals)])

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val1 = self.numForList(self.listForNode(l1))
        val2 = self.numForList(self.listForNode(l2))

        val = int(val1) + int(val2)

        val_list = list(str(val))

        return self.nodeForList(val_list)
