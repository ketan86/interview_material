

def merge_sort(arr):
    # if more than 1 items in arr,
    if len(arr) > 1:
        # find mid and divide into two
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # send for sorting
        merge_sort(left)
        merge_sort(right)

        # merge left and right
        merge(arr, left, right)


def merge(arr, left, right):
    # only merge left and right to given arr
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(arr)
print(arr)
