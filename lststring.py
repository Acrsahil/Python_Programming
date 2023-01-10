result = []
def same_le(strings):
    for s in strings:
        if s[0] == s[-1]:
            result.append(s)
    return result
strings = ["hit","mum","dad","mam","wow"]
print(same_le(strings))
