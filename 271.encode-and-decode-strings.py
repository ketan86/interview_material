#
# @lc app=leetcode id=271 lang=python3
#
# [271] Encode and Decode Strings
#
# https://leetcode.com/problems/encode-and-decode-strings/description/
#
# algorithms
# Medium (30.70%)
# Likes:    460
# Dislikes: 157
# Total Accepted:    60.8K
# Total Submissions: 191.9K
# Testcase Example:  '["Hello","World"]'
#
# Design an algorithm to encode a list of strings to a string. The encoded
# string is then sent over the network and is decoded back to the original list
# of strings.
#
# Machine 1 (sender) has the function:
#
#
# string encode(vector<string> strs) {
# ⁠ // ... your code
# ⁠ return encoded_string;
# }
# Machine 2 (receiver) has the function:
#
#
# vector<string> decode(string s) {
# ⁠ //... your code
# ⁠ return strs;
# }
#
#
# So Machine 1 does:
#
#
# string encoded_string = encode(strs);
#
#
# and Machine 2 does:
#
#
# vector<string> strs2 = decode(encoded_string);
#
#
# strs2 in Machine 2 should be the same as strs in Machine 1.
#
# Implement the encode and decode methods.
#
#
#
# Note:
#
#
# The string may contain any possible characters out of 256 valid ascii
# characters. Your algorithm should be generalized enough to work on any
# possible characters.
# Do not use class member/global/static variables to store states. Your encode
# and decode algorithms should be stateless.
# Do not rely on any library method such as eval or serialize methods. You
# should implement your own encode/decode algorithm.
#
#
#

# @lc code=start
class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        """
        # strings within the strs array contain 256 valid ascii chars
        # so we can use any char beyond 256 to separate the strings
        # after they are encoded.

        # if strs array is empty, encode it using chr(257) -> 'ā' so when
        # we have to decode the string, we know if strs is empty or values
        # within the strs array are empty
        # for ex, [] -> encode -> "ā" -> decode -> []
        #         ["",""] -> encode -> "ĂĂ" -> decode -> ["", ""]
        #               # In [3]: chr(258).join(["",""])
        #               # Out[3]: 'Ă'
        #               # In[4]: chr(258).join(["", "", ""])
        #               # Out[4]: 'ĂĂ'
        #               # In[5]: chr(258).join(["", "", "", ""])
        #               # Out[5]: 'ĂĂĂ'
        if not strs:
            return chr(257)
        return chr(258).join(s for s in strs)

    def decode(self, s):
        """Decodes a single string to a list of strings.
        """
        # if string contains chr(257) -> 'ā', return empty array
        if s == chr(257):
            return []
        # split string by chr(258) -> 'Ă' and return
        return s.split(chr(258))


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
# @lc code=end
