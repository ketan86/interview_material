# memoization (top down)
def find_fib(n, d):
    if n < 2:
        return n
    if n in d:
        return d[n]

    fib = find_fib(n - 1, d) + find_fib(n - 2, d)
    d[n] = fib

    return fib


print(find_fib(200, {}))


# tabulation(bottom up)
def find_fib(n):
    results = [0, 1]
    for i in range(2, n + 1):
        results.append(results[i - 1] + results[i - 2])
    return results[n]


print(find_fib(200))
