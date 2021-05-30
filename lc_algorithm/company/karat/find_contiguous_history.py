"""
We have some clickstream data that we gathered on our client's website. Using
cookies, we collected snippets of users' anonymize URL histories while they
browsed the site. The histories are in chronological order, and no URL was
visited more than once per person.

Write a function that takes two users' browsing histories as input and returns
the longest contiguous sequence of URLs that appears in both.

Sample input:

user0 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
user1 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
user2 = ["a", "/one", "/two"]
user3 = ["/pink", "/orange", "/yellow", "/plum", "/blue", "/tan", "/red", "/amber",
    "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow", "/BritishRacingGreen"]
user4 = ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan",
    "/red", "/lavender", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"]
user5 = ["a"]
user6 = ["/pink","/orange","/six","/plum","/seven","/tan","/red", "/amber"]

Sample output:

findContiguousHistory(user0, user1) => ["/pink", "/register", "/orange"]
findContiguousHistory(user0, user2) => [] (empty)
findContiguousHistory(user0, user0) => ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
findContiguousHistory(user2, user1) => ["a"]
findContiguousHistory(user5, user2) => ["a"]
findContiguousHistory(user3, user4) => ["/plum", "/blue", "/tan", "/red"]
findContiguousHistory(user4, user3) => ["/plum", "/blue", "/tan", "/red"]
findContiguousHistory(user3, user6) => ["/tan", "/red", "/amber"]

n: length of the first user's browsing history
m: length of the second user's browsing history

"""


def find_contiguous_history(a, b):
    """ 
        user0 = ["/start", "/pink", "/blue", "/pink", "/register"]
        user1 = ["/start", "/pink", "/register"]
    """
    # [
    #                   start pink blue pink  register
    #            [0,    0,    0,    0,   0,   0]
    #  /start    [0,    1,    0,    0,   0,   0]
    #  /pink     [0,    0,    2,    0,   1,   0]
    #  /register [0,    0,    0,    0,   0,   2]
    # ]
    m = len(a)
    n = len(b)

    # build dp matrix with 1 extra length (so diagonal index check does not fail)
    dp = [[0] * (n+1) for i in range(m+1)]

    # maintain max_so_far and when max_so_far changes, update last index
    # of either list to build the max path list later.
    max_so_far = 0
    max_last_index = -1

    # result list
    result = []

    # start from 1,1 till end
    for i in range(1, m+1):
        for j in range(1, n+1):
            # if both strings are same
            if a[i-1] == b[j-1]:
                # if previous both strings were same, and value was set,
                # increment since we found a new match.
                # update max_so_far with new value if current is max legnth
                max_so_far_new = max(max_so_far, dp[i-1][j-1] + 1)

                # if new max is found,
                if max_so_far_new != max_so_far:
                    # store one of the list index in the last index
                    max_last_index = i - 1
                    # update max so far
                    max_so_far = max_so_far_new

                # update dp value
                dp[i][j] = dp[i-1][j-1] + 1

    # build visited path list in reverse
    for i in range(max_last_index, max_last_index - max_so_far, -1):
        result.insert(0, a[i])

    return result


data = {
    'user0': ["/start", "/green", "/blue", "/pink",
              "/register", "/orange", "/one/two"],
    'user1': ["/start", "/pink", "/register", "/orange", "/red", "a"],
    'user2': ["a", "/one", "/two"],
    'user3': ["/pink", "/orange", "/yellow", "/plum", "/blue", "/tan", "/red", "/amber",
              "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow", "/BritishRacingGreen"],
    'user4': ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan",
              "/red", "/lavender", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"],
    'user5': ["a"],
    'user6': ["/pink", "/orange", "/six", "/plum",
              "/seven", "/tan", "/red", "/amber"]
}

print(find_contiguous_history(
    ["/start", "/green", "/blue", "/pink", "/register"],
    ["/start", "/pink", "/register"]))
print(find_contiguous_history(data['user0'], data['user1']))
print(find_contiguous_history(data['user0'], data['user2']))
print(find_contiguous_history(data['user2'], data['user1']))
print(find_contiguous_history(data['user3'], data['user4']))
print(find_contiguous_history(data['user3'], data['user6']))
