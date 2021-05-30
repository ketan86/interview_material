# pylint: skip-file
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def is_palindrome(head):
    """
    Palindrome is a word, phrase, or sequence that reads the same backward as
    forward, e.g., madam or nurses run.

                1 -> 2 -> 3 -> 2 -> 1

    Approaches:
    1. We can find the middle of the ll and iterate on the both side until
    they do not match the node.
        - This approach would work with doubly linked list but not with singly
        linked list because there is not pointer towards back node.

    2. We can find the middle of the ll and then reverse the first half of the
    linked list and compare both first half(reversed) and second half and at
    any point, nodes don't match, return False. else True.

        - NOTE:  We have to make sure we again reverse the reversed linked
        list to presever the original ll.
    """
    # find middle. when fast reaches the end, slow is at the middle
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # reverse the right half
    slow = reverse(slow)  # pointer to the start of the reversed half

    # copy the node to reset back
    copy_slow = slow

    # move slow and fast and if data differs, break , reset the linked list
    # and return false
    # else, reset and return true
    fast = head

    while slow:
        if slow.data != fast.data:
            break
        slow = slow.next
        fast = fast.next
    else:
        reverse(copy_slow)
        return True

    reverse(copy_slow)
    return False


def reverse(node):
    prev = None
    while node:
        # save next
        nxt = node.next
        # link to prev (NOTE: this makes the head detach from head)
        node.next = prev
        # move prev and node one step ahead
        prev = node
        node = nxt
    return prev


def _print(node):
    while node:
        print(str(node.data) + '->')
        node = node.next


def main():
    head = Node('a')
    head.next = Node('b')
    head.next.next = Node('c')
    head.next.next.next = Node('d')
    head.next.next.next.next = Node('e')
    print("LinkedList is_palindrome: " + str(is_palindrome(head)))
    head.next.next.next.next.next = Node('d')
    print("LinkedList is_palindrome: " + str(is_palindrome(head)))
    head.next.next.next.next.next.next = Node('c')
    print("LinkedList is_palindrome: " + str(is_palindrome(head)))
    head.next.next.next.next.next.next.next = Node('b')
    print("LinkedList is_palindrome: " + str(is_palindrome(head)))
    head.next.next.next.next.next.next.next.next = Node('a')
    print("LinkedList is_palindrome: " + str(is_palindrome(head)))


main()
