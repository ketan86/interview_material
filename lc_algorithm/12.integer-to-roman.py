#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#
# In rules for formation of Roman-numerals system there is no symbol or digit for zero. This system has no place value system. The digit or digits of lower value is/are placed after or before the digit of higher value. The value of digits of lower value is added to or subtracted from the value of digit of higher value. Using the certain rules for formation of Roman-numerals is given below.
# Rule 1: The roman digits I, X and C are repeated upto three times in succession to form the numbers.
# (a) We know the value of I = 1, value of X is 10 and value of C is 100.
# (b) The value of I, X and C are added as:

# I = 1

# II = 1 + 1 = 2

# III = 1 + 1 + 1 = 3
# X = 10
# XX = 10 + 10 = 20
# XXX = 10 + 10 +10 = 30
# C = 100

# CC = 100 + 100 = 200

# CCC = 100 + 100 + 100 = 300

# (c) No digit is repeated in succession more than thrice, i.e., I, X and C cannot be repeated more than 3 times.


# (d) The digits V, L and D are not repeated. The repetition of V, L and D is invalid in the formation of numbers.


# Rule 2: (a) When a digit of lower value is written to the right or after a digit of higher value, the values of all the digits are added. As:

# VI = 5 + 1 = 6

# VII = 5 + 1 + 1 = 7

# VIII = 5 + 1 + 1 + 1 = 8

# XI = 10 + 1 = 11

# XII = 10 + 1 + 1 = 12

# XV = 10 + 5 = 15

# XVI = 10 + 5 + 1 = 16

# LX = 50 + 10 = 60

# LXV = 50 + 10 + 5 = 65


# (b) Value of similar digits are also added as indicated in rule 1

# III = 1 + 1 + 1 = 3


# XXX = 10 + 10 + 10 = 30

# XX = 10 + 10 = 20

# Rule 3: When a digit of lower value is written to the left or before a digit of higher value, then the value of the lower digit is subtracted from the value of the digit of higher value. As:

# IV = 5 - 1 = 4

# IX = 10 - 1 = 9

# XL = 50 - 10 = 40

# XIV = 10 + (5 - 1) = 14

# XIX = 10 + (10 - 1) = 19

# XXIX = 10 + 10 + (10 - 1) = 29

# XLV = (50 - 10) + 5 = 45

# CLIX = 100 + 50 + (10 - 1) = 159

# However, V is never written to the left of X.

# Rule 4: (a) If we have to write the numbers beyond 10 we should write the number 10 or groups of number 10 and then number 1 or 5 as the case may be. Then these numbers are used to change to the corresponding Roman numerals. As:

# 12 = 10 + 2 = 1 0 + 1 + 1 = XII

# 20 = 10 + 10 = XX

# 22 = 10 + 10 +1 + 1= XXII

# 26 = 10 + 10 + 5 + 1 = XXVI

# 39 = 10 + 10 + 10 + (10 - 1) = XXXIX

# 37 = 10 + 10 + 10 + 5 + 1 + 1 = XXXVII


# (b) According to this pattern, numbers higher than number 40 are also formed:

# 43 = (50 - 10) + 1 +1 + 1= XLIII

# 56 = 50 + 5 + 1 = LVI1

# 59 = 100 + 50 + (10 - 1) = CLIX

# 1238 = 1000 + 100 + 100 + 10 + 10 + 10 + 5 + 1 + 1 + 1 = MCCXXXVIII


# Rule 5: If a horizontal line is drawn over the symbols or digits of Roman numerals, then the value of the numerals becomes 1000 times. As:

# XV = 15 but XV = 15000,

# CLV = 155 but CLV = 155000

# For example:

# 1. Write the Roman numerals for the following numbers:

# (i) 13 = XIII

# (ii) 14 = XIV

# (iii) 18 = XVIII

# (iv) 26 = XXVI

# (v) 39 = XXXIX

# (vi) 42 = XXXXII

# (vii) 61 = LXI

# (viii) 545 = DXLV

# (ix) 217 = CCXVII


# 2. Write the numbers for the following Roman numerals:

# (i) VII = 7

# (ii) XXXIV = 34

# (iii) XXXVII = 37

# (iv) XLIII = 43

# (v) XLVIII = 48

# (vi) LII = 52

# (vii) CXL = 140

# (viii) CXLV = 145

# These are the five rules for formation of Roman-numerals system explained using examples.

"""
1 - > I    -> can be repeated up to 3 max
5 -> V -> once 
10 -> X -> can be repeated up to 3 max
50 -> L -> once 
100 -> C -> can be repeated up to 3 max
500 -> D    -> once 
1000 -> M -> n number of times 


50 -> if found in above map, return
49 -> 40 (XL) + 9 (IX)
58 -> 50 + 5 +  1 +  1 + 1 (LVIII)
4 -> V - I (IV)
1994 -> 1000(M) + 900 + 90 (XC) + 4 (IV)
90 -> 100 - 10 (XC)
999 -> 900 (CM) + 90 (XC) + 9 (IX)
56 -> 50 (L) + 6 (VI)
134 -> 100 (C) + 30 (XXX) + 4 (IV)
"""
# pylint:skip-file


class Solution:
    def intToRoman(self, num):
        """
        num = 1320

        for 1000 .. 1:

            at 1000
                1320//1000 = 1 -> 1 time M
                1320-(1000*1) = 320
            900..500..400
            at 100
                320//100 = 3 -> 3 times C
                320-(100*3) = 20

            90..50..40
            at 10
                20//10 = 2 -> 2 times X
                20-(10*2) = 0

        Answer: MCCCXX
        """
        result = []
        ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        nums = ('M', 'CM', 'D', 'CD', 'C', 'XC',
                'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')

        # divide the number from 1000 to 1 and keep adding relevent roman
        # characters counts time.
        for i in range(len(ints)):
            remainder = num // ints[i]
            result.append(nums[i] * remainder)
            num -= remainder * ints[i]
        return ''.join(result)


print(Solution().intToRoman(1320))
