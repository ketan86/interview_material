from collections import defaultdict


def find_substring(s, p):
    if len(s) < len(p):
        return ''
        # initialize the variable to store the min substring
        # use existing string and add one extra character. any substring of the string would be less than m.
    m = s + '-'
    start = 0
    end = 0
    # variable that represents the number of unique characters in the map.
    # for ex,
    # pattern -> "abc" -> {a->2, b->1, c->1 }, match = 0
    # if a is found, a ->1 and match -> 0 since freq is still not 0.
    # if a is found, a ->0 and match -> 1 since freq of the char *a* is 0.
    # if b is found, b ->0 and match -> 2 and so on.
    match = 0
    d = defaultdict(int)

    # initialize the map with freq of the chr from pattern string.
    for ch in p:
        d[ch] += 1

    # expand the window size
    for end in range(len(s)):
        # if chr found in map, reduce the freq of the char
        if s[end] in d:
            d[s[end]] -= 1
            # when freq goes to 0, increase the match count
            if d[s[end]] == 0:
                match += 1
        # when match count equal to lenght of the map. in other words, window contains all the characters from the pattern.
        # 1. we found the substring so calculate min by comparing with previous string.
        # 2. reduce the widow size.

        # while loop to make sure we eliminate all the chr that are not paresent in patter and stop at the first match.
        while match == len(d):
            m = min(m, s[start: end + 1], key=len)
            # keep reducing the window size, until the first char of the pattern is found.
            if s[start] in d:
                # if freq of the char is 0, reduce the match count. in other words, window now contains 1 less char.
                if d[s[start]] == 0:
                    match -= 1
                # increament the freq of the char
                d[s[start]] += 1
            # increament the window start index, shrink the window
            start += 1

        # increament the end index
        end += 1

    # if len of the min is greater than string size, we have not found any match.
    if len(m) > len(s):
        return ''
    return m


print(find_substring('ADOBECODEBANC', 'ABC'))
