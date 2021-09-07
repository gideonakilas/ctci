class Trie:
    def __init__(self):
        self.trie = dict()

    def addWord(self, word: str):
        trie = self.trie
        charArray = list(word)

        for char in charArray:
            if not trie.get(char):
                trie[char] = dict()
            trie = trie.get(char)
        trie['isEnd'] = True

    def searchWord(self, word: str):
        charArray = list(word)
        trie = self.trie
        for char in charArray:
            if not trie.get(char):
                return False
            trie = trie.get(char)

        return trie.get('isEnd')


trie = Trie()
trie.addWord('camel')
trie.addWord('camera')
trie.addWord('taylor')
trie.addWord('tape')
print(trie.searchWord('tape'))
print(trie.searchWord('taper'))
print(trie.trie)
