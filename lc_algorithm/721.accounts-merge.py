#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#

# @lc code=start
from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts):
        """
        We give each account an ID, based on the index of it within the list of accounts.

        [
        ["John", "johnsmith@mail.com", "john00@mail.com"], # Account 0
        ["John", "johnnybravo@mail.com"], # Account 1
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],  # Account 2
        ["Mary", "mary@mail.com", "john_newyork@mail.com"] # Account 3
        ]
        Next, build an emails_accounts_map that maps an email to a list of
        accounts, which can be used to track which email is linked to which
        account. This is essentially our graph.

        # emails_accounts_map of email to account ID
        {
            "johnsmith@mail.com": [0, 2],
            "john00@mail.com": [0],
            "johnnybravo@mail.com": [1],
            "john_newyork@mail.com": [2,3],
            "mary@mail.com": [3]
        }

        Next we do a DFS on each account in accounts list and look up
        emails_accounts_map to tell us which accounts are linked to that
        particular account via common emails. This will make sure we visit each
        account only once. This is a recursive process and we should collect all
        the emails that we encounter along the way.

        Lastly, sort the collected emails and add it to final results, res along
        with the name.
        """
        results = []
        visited_accounts = set()
        emails_accounts_map = defaultdict(list)

        # build graph
        for index, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                emails_accounts_map[email].append(index)

        def dfs(i, emails):
            if visited_accounts[i]:
                return
            visited_accounts[i] = True
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                for index in emails_accounts_map[email]:
                    dfs(index, emails)

        # iterate over all emails
        for index, account in enumerate(accounts):
            if not visited_accounts[index]:
                emails = set()
                dfs(index, emails)
                results.append([account[0]] + sorted(emails))

        return results


accounts = [
    ["John", "johnsmith@mail.com", "john00@mail.com"],  # Account 0
    ["John", "johnnybravo@mail.com"],  # Account 1
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],  # Account 2
    ["Mary", "mary@mail.com"]  # Account 3
]

# print(Solution().accountsMerge(accounts))
accounts = [
    ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
    ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
    ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
    ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"]
]

accounts = [
    ["Alex", "Alex5@m.co", "Alex4@m.co", "Alex0@m.co"],
    ["Ethan", "Ethan3@m.co", "Ethan3@m.co", "Ethan0@m.co"],
    ["Kevin", "Kevin4@m.co", "Kevin2@m.co", "Kevin2@m.co"],
    ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe2@m.co"],
    ["Gabe", "Gabe3@m.co", "Gabe4@m.co", "Gabe2@m.co"]]
print(Solution().accountsMerge(accounts))


# @lc code=end
