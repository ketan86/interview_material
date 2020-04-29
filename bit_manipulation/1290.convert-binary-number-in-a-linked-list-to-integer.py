"""
Given head which is a reference node to a singly-linked list.
The value of each node in the linked list is either 0 or 1.
The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

 

Example 1:


Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
Example 2:

Input: head = [0]
Output: 0
Example 3:

Input: head = [1]
Output: 1
Example 4:

Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
Output: 18880
Example 5:

Input: head = [0,0]
Output: 0
 

Constraints:

The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.
"""
# pylint:skip-file

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        decimal = 0
        curr = head 
        while curr:
            # left shift the number by 1.
            decimal <<= 1 
            # if node value is 1, OR with existing value. when node value is
            # 0, left shift would have added right bit 0 anyway.
            if curr.val == 1:
                decimal |= 1 
            curr = curr.next
        return decimal

head = ListNode(1)
head.next = ListNode(0)
head.next.next = ListNode(0)
head.next.next.next = ListNode(1)
head.next.next.next.next = ListNode(0)
head.next.next.next.next.next = ListNode(0)
head.next.next.next.next.next.next = ListNode(1)
head.next.next.next.next.next.next.next = ListNode(1)
head.next.next.next.next.next.next.next.next = ListNode(1)
head.next.next.next.next.next.next.next.next.next = ListNode(0)
head.next.next.next.next.next.next.next.next.next.next = ListNode(0)
head.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
head.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
head.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
head.next.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
print(Solution().getDecimalValue(head))