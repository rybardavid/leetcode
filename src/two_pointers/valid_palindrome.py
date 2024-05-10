def run(s: str) -> bool:
    l, r = 0, len(s) -1

    while l < r:
        if not isAlphaNumeric(s[l]):
            l += 1
            continue
        if not isAlphaNumeric(s[r]):
            r -= 1
            continue
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True

def isAlphaNumeric(s: str) -> bool:
    return (ord(s) >= ord('a') and ord(s) <= ord('z')
            or ord(s) >= ord('A') and ord(s) <= ord('Z')
            or ord(s) >= ord('0') and ord(s) <= ord('9'))