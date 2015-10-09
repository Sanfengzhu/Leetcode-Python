#You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if not l1:
            return l2
        if not l2:
            return l1
        
        def length(l):
            cur, count = l, 0
            while cur:
                cur=cur.next
                count=count+1
            return count
        
        c1, c2 = length(l1), length(l2)
        if c1 < l2:
            l1, l2 = l2, l1
        x=0
        head=pre=l1
        while l2:
            temp=l1.val+l2.val+x
            l1.val=temp%10
            x=temp/10
            pre=l1
            l1=l1.next
            l2=l2.next
        while l1 and x:
            temp = l1.val+x
            l1.val=temp%10
            x=temp/10
            pre=l1
            l1=l1.next
        if not l1 and x:
            pre.next=ListNode(x)
        
        return head
