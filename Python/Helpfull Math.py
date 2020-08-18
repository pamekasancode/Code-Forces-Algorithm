def solve():
    chars = str(input())
    signs = ["+", "-", "/", "*"]
    sign = [sign for sign in signs if sign in chars]

    if not sign:
        return chars

    return sign[0].join(sorted(chars.split(sign[0])))
    
print(solve())
