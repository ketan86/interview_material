"""
Given a string, compute recursively (no loops) a new string where all the 
lowercase 'x' chars have been changed to 'y' chars.

changeXY("codex") → "codey"
changeXY("xxhixx") → "yyhiyy"
changeXY("xhixhix") → "yhiyhiy"
"""


def change_char(s, _from, _to):
    if len(s) == 1:
        if s == _from:
            return _to
        return s

    return change_char(s[:1], _from, _to) + change_char(s[1:], _from, _to)


c = change_char('abcdbasfasdbdbbadsfs', 'f', '%')
print(c)
