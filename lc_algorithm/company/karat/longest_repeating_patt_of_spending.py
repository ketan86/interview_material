"""
If you have an input which is having userid and the category of the payments
that they made with their credit card given as,

UseridList - List<String>
category_list - List<List<String>>

find the 2 users with the longest common contiguous spending pattern. 
Return null if none exists.

Eg:

UseridList : {"user1", "user2", "user3", "user4"}
category_list: {
    {"fashion","restaurant","grocery","utility"}, 
    {"fuel","fashion","restaurant","grocery"}, 
    {"fuel","utility","restaurant","grocery"}, 
    {"internet","transportation","water","grocery"}
}

Longest repeating sequence is between user1 and user2 which is
{"fashion","restaurant","grocery"}. 
Output : {"user1","user2"}

Follow up question: Optimal way to get list of users (2 or more) which have the
the longest common spending pattern.

"""


def max_sub(a, b):
    m = len(a)
    n = len(b)

    # dp to store the max length
    dp = [[0] * (n+1) for i in range(m+1)]

    mx = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            # if category is same, calculate the max length by adding
            # 1 to previous length
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                # update max
                mx = max(mx, dp[i][j])
    return mx


def find_users(userid_list, category_list):
    """
    Steps :
        1. Loop over the userid pair at a time
        2. Find the size of the longest contiguous sub-sequence
        3. Save sequence size -> userid pair for result
        4. Keep running max sequence size
        5. Return userid pair with max sequence size

    """
    # max to store the max count
    mx = 0
    # result dict with count as key and userids are values
    res = {}

    # iterate over the userids in two pair
    for i in range(len(userid_list)):
        for j in range(i + 1, len(userid_list)):
            # find the length of the matching items
            count = max_sub(
                category_list[userid_list[i]],
                category_list[userid_list[j]])
            # use count to store the respective userids
            res[count] = [userid_list[i], userid_list[j]]
            # update the max length
            mx = max(mx, count)

    # return the userids where length is longest
    return res[mx]


userid_list = ["user1", "user2", "user3", "user4"]
category_list = {
    'user1': ["fashion", "restaurant", "grocery", "utility"],
    'user2': ["fuel", "fashion", "restaurant", "grocery"],
    'user3': ["fuel", "utility", "restaurant", "grocery"],
    'user4': ["internet", "transportation", "water", "grocery"]
}
print(max_sub(category_list['user1'], category_list['user2']))
print(max_sub(category_list['user2'], category_list['user3']))
print(find_users(userid_list, category_list))
