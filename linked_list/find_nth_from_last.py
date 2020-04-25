def find_nth(lst, n):
    l = lst.length()
    advance = l - n
    if advance < 0:
        return -1
    curr = lst.get_head()
    counter = 0
    if curr is None:
        return - 1

    while curr.next_element is not None:
        if counter == advance:
            return curr.data
        else:
            counter += 1
        curr = curr.next_element
    return -1


# two pointer method
def find_nth(lst, n):
    curr = lst.get_head()
    if curr is None:
        return -1
    first = curr
    second = curr
    counter = 1
    while second.next_element is not None:
        if counter == n:
            break
        second = second.next_element
        counter += 1
    else:
        return -1

    while second.next_element is not None:
        first = first.next_element
        second = second.next_element

    return first.data
