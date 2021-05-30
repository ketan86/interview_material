"""
Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an
element as pivot and partitions the given array around the picked pivot.

There are many different versions of quickSort that pick pivot in different
ways.
1. Always pick first element as pivot.
2. Always pick last element as pivot (implemented below)
3. Pick a random element as pivot.
4. Pick median as pivot.

The key process in quickSort is partition(). Target of partitions is, given an
array and an element x of array as pivot, put x at its correct position in
sorted array and put all smaller elements (smaller than x) before x, and put all
greater elements (greater than x) after x. All this should be done in linear
time.

Pseudo Code for recursive QuickSort function :
/* low  --> Starting index,  high  --> Ending index */
quickSort(arr[], low, high)
{
    if (low < high)
    {
        /* pi is partitioning index, arr[p] is now
           at right place */
        pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);  // sort left
        quickSort(arr, pi + 1, high); // soft right
    }
}

Time Complexity Of QuickSort
Best CaseO (n log n)
Average Case O(n log n)
Worst Case O(n2)

"""


def quick_sort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        # find the partitioning index
        pi = partition(arr, low, high)

        # sort elements before and after partition
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

    return arr


def partition(arr, low, high):
    # set ith index to low-1. This means we are going to increase
    # the ith index before swapping the i and j values.
    i = low - 1
    # set j to low index
    j = low
    # set pivot to high index
    pivot = high

    # while j is less than pivot, run the loop
    while j < pivot:
        # if value of the jth index is less than <= pivot,
        # increment the ith index and swap i and j to
        # move j to left side of the array.

        # if value of the jth index is greather than pivot,
        # increment j by 1.
        if arr[j] <= arr[pivot]:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
        j += 1

    # we are at the rightmost index of the lowest
    # array. so swap i+1 to pivot
    arr[i+1], arr[pivot] = arr[pivot], arr[i+1]

    return i+1


print(quick_sort([1, 5, 2, 8, 12, 19, 2, 3], 0, 7))


# 1, 2, 2, 8, 12, 19, 5, 3
# ij            p
# 1 2 2 3 12 5 8
# ji     p
# 1 3 2 8 12 2 5
# s    e
# 1 3 2 5 12 2 8
# s e
# 1 3 2 5 8 2 12
# se

# 1 2 2
# j ip
