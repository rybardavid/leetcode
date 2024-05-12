def run(s: str) -> bool:
    charMap = {
        ']' : '[',
        ')' : '(',
        '}' : '{',
    }

    openParenthes = []
    for char in s:
        try:
            if char in charMap.keys() and openParenthes.pop() != charMap[char]:
                return False
            elif char not in charMap.keys():
                openParenthes.append(char)
        except IndexError:
            return False

    return len(openParenthes) == 0