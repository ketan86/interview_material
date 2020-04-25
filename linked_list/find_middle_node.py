def find_mid(lst):
    curr = lst.get_head()
    if curr is None:
        return
    slow = curr
    fast = curr
    while fast.next_element is not None:
        fast = fast.next_element
        if fast.next_element is not None:
            slow = slow.next_element
            fast = fast.next_element
    return slow.data
