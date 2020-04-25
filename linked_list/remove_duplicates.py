def remove_duplicates(lst):
    curr = lst.get_head()
    if curr is None:
        return lst
    visited = set()
    prev = curr
    while curr.next_element is not None:
        if curr.data in visited:
            prev.next_element = curr.next_element
        else:
            visited.add(curr.data)
        prev = curr
        curr = curr.next_element
    if curr.data in visited:
        prev.next_element = None
