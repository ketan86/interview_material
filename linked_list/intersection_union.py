def union(list1, list2):
    list1_curr = list1.get_head()
    if list1_curr is not None:
        while list1_curr.next_element is not None:
            list1_curr = list1_curr.next_element

    list2_curr = list2.get_head()
    if list2_curr is not None:
        list1_curr.next_element = list2_curr

    return list1


# Returns a list containing the intersection of list1 and list2
def intersection(list1, list2):
    list1_items = set()

    list1_curr = list1.get_head()
    if list1_curr is None:
        return

    while list1_curr.next_element is not None:
        list1_items.add(list1_curr.data)
        list1_curr = list1_curr.next_element

    list1_items.add(list1_curr.data)

    list2_curr = list2.get_head()
    if list2_curr is None:
        return
    prev = list2_curr
    while list2_curr.next_element is not None:
        if list2_curr.data not in list1_items:
            prev.next_element = list2_curr.next_element
        prev = list2_curr
        list2_curr = list2_curr.next_element

    if list2_curr.data not in list1_items:
        prev.next_element = None

    return list2
