#
# @lc app=leetcode id=811 lang=python3
#
# [811] Subdomain Visit Count
#

# @lc code=start
from collections import defaultdict


class Solution:
    def subdomainVisits(self, cpdomains):
        """Runtime: 56 ms, faster than 38.75%"""

        result = []
        if not cpdomains:
            return result

        per_domain_map = defaultdict(int)

        for cp_domain in cpdomains:
            count, domain = cp_domain.split(' ')
            domain_fragments = domain.split('.')
            i = len(domain_fragments) - 1
            while i >= 0:
                per_domain_map['.'.join(
                    domain_fragments[i:len(domain_fragments)])] += int(count)
                i -= 1

        for domain, count in per_domain_map.items():
            result.append(f"{count} {domain}")

        return result

# @lc code=end
