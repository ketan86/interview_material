#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        """Runtime: 32 ms, faster than 72.71%"""
        stack = []

        for segment in path.split('/'):
            # if segment value is not empty ( takes care of '//')
            if segment:
                # if segment value is '..', go back one directory
                if segment == '..':
                    if stack:
                        stack.pop()
                # if anything other than '.', insert in stack
                elif segment != '.':
                    stack.append(segment)
        
        # build final path by adding '/' in the beginning and joining stack
        # values by '/'
        return '/' + '/'.join(stack)

print(Solution().simplifyPath( "/a/./b/../../c/"))
# @lc code=end

