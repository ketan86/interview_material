# brute-force approach
def avg_of_contiguous_subarray(arr, k):
    results = []
    for i in range(0, len(arr) - k + 1):
        sum_ = arr[i]
        for j in range(i + 1, i + k):
            sum_ += arr[j]
        results.append(sum_ / k)
    return results


print(avg_of_contiguous_subarray([1, 3, 2, 6, -1, 4, 1, 8, 2], k=5))


# sliding window approach
def avg_of_contiguous_subarray(arr, k):
    results = []
    sum_ = 0
    for i in range(len(arr)):
        sum_ += arr[i]
        if i == k - 1:
            avg = sum_ / k
            results.append(avg)
        elif i >= k:
            sum_ -= arr[i - k]
            avg = sum_ / k
            results.append(avg)

    return results


print(avg_of_contiguous_subarray([1, 3, 2, 6, -1, 4, 1, 8, 2], k=5))
