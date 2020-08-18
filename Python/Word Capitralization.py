def solve():
    chars = str(input())
    new_chars = []

    for letter in chars:
        new_chars.append(letter)

    d = new_chars.pop(0)
    new_chars.insert(0, d.upper())
    return "".join(new_chars)
    
print(solve())
