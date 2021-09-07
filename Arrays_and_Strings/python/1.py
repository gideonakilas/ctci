def isUniqueCharacters(string: str):
    charSet = set()

    for char in string:
        if char in charSet:
            return False
        else:
            charSet.add(char)

    return True


print(isUniqueCharacters("hello"))
print(isUniqueCharacters("hi"))
print(isUniqueCharacters("tale"))
print(isUniqueCharacters("straw"))
print(isUniqueCharacters("people"))
