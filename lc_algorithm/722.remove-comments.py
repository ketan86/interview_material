#
# @lc app=leetcode id=722 lang=python3
#
# [722] Remove Comments
#

# @lc code=start
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        """Runtime: 20 ms, faster than 99.16%"""
        result = []
        mode = False
        buffer = ''

        for line in source:
            # start of the line
            i = 0
            while i < len(line):
                if not mode:
                    # if line comment, ignore the line
                    if line[i:i+2] == '//':
                        break
                    # if comment start, set the mode and skip the comment
                    # continue capturing skipping the lines
                    elif line[i:i+2] == '/*':
                        mode = True
                        i += 2
                        continue
                    # store lines in buffer
                    else:
                        buffer += line[i]
                else:
                    # end of comment, reset the mod
                    if line[i:i+2] == '*/':
                        mode = False
                        i += 2
                        continue

                i += 1

            # if comment was completed in that line, and buffer, add to result
            # else multiline comment so skip.
            if not mode and len(buffer):
                result.append(buffer)
                buffer = ''

        return result
# @lc code=end
