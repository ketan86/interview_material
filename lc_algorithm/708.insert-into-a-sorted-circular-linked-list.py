"""
708. Insert into a Sorted Circular Linked List
Medium

Given a Circular Linked List node, which is sorted in ascending order, write a
function to insert a value insertVal into the list such that it remains a sorted
circular list. The given node can be a reference to any single node in the list
and may not necessarily be the smallest value in the circular list.

If there are multiple suitable places for insertion, you may choose any place to
insert the new value. After the insertion, the circular list should remain
sorted.

If the list is empty (i.e., the given node is null), you should create a new
single circular list and return the reference to that single node. Otherwise,
you should return the originally given node.


Example 1:


Input: head = [3, 4, 1], insertVal = 2
Output: [3, 4, 1, 2]
Explanation: In the figure above, there is a sorted circular list of three 
    elements. You are given a reference to the node with value 3, and we need 
    to insert 2 into the list. The new node should be inserted between node 1 
    and node 3. After the insertion, the list should look like this, and we 
    should still return node 3.


Example 2:

Input: head = [], insertVal = 1
Output: [1]
Explanation: The list is empty(given head is null). We create a new single 
circular list and return the reference to that single node.
Example 3:

Input: head = [1], insertVal = 0
Output: [1, 0]


Constraints:

0 <= Number of Nodes <= 5 * 104
-106 <= Node.val, insertVal <= 106
Accepted
66, 790
Submissions
203, 187

"""

# Definition for a Node.


class Node:
    def __init__(self, val=None):
        self.val = val


class Solution:
    def insert(self, head, insertVal):
        """Runtime: 40 ms, faster than 46.53%

        Cases to cover:
        1. If head is none
        2. If both nodes are same or current is less than next 
        3. if current is greater than next

        """

        # if head is none, create a new node and make it circular
        if not head:
            head = Node(insertVal)
            head.next = head
            return head

        curr = head

        # loop until next node is head (circle)
        while curr.next != head:
            # if current node is less than equal to next node
            if curr.val <= curr.next.val:
                # check if node can be inserted in between two nodes
                if insertVal >= curr.val and insertVal <= curr.next.val:
                    break
            # if current value is greater than next node.
            # because there could be a point where head node
            # may not be a smallest node.
            #   head -> 3 -> 4 -> 1 -> 2 -> head
            #               curr  next
            #               curr > next
            else:
                if insertVal >= curr.val or insertVal <= curr.next.val:
                    break

            curr = curr.next

        # insert new node after current node.
        nxt = curr.next
        node = Node(insertVal)
        node.next = nxt
        curr.next = node
        return head
