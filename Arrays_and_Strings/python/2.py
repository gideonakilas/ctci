def isPermuation(word1: str, word2: str):
    if len(word1) != len(word2):
        return False
    charMap = dict()
    for i in range(len(word1)):
        char1 = word1[i]
        char2 = word2[i]

        if isinstance(charMap.get(char1), int):
            charMap[word1[i]] += 1
            if charMap[word1[i]] == 0:
                charMap.pop(word1[i])

        else:
            charMap[word1[i]] = 1

        if isinstance(charMap.get(char2), int):
            charMap[word2[i]] -= 1
            if charMap[word2[i]] == 0:
                charMap.pop(word2[i])
        else:
            charMap[word2[i]] = -1

    return not bool(charMap)


print(isPermuation("hello", "helol"))
print(isPermuation("tello", "helol"))
print(isPermuation("hellp", "helpl"))
print(isPermuation("hello", "helol"))
print(isPermuation("hello", "heloL"))
