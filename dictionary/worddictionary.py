
class TrieNode:
    def __init__(self, text:str=None):
        if not text:
            return
        self.val = text[0]
        self.children = dict()
        self.is_word = False
        if len(text) > 1:
            self.children[text[1]] = TrieNode(text[1:])
        else:
            self.is_word = True

    def addWord(self, text:str):
        # search and get the Trie object corresponding to the prefix of the added string
        if not text:
            return
        current_node = self
        for i, ch in enumerate(text):
            if ch in current_node.children.keys():
                current_node = current_node.children[ch]
            else:
                break

        if i < len(text) -1 :
            current_node.children[ch] = TrieNode(text[i:])
        else:
            current_node.is_word = True

    def search(self, text: str) -> bool:
        """
        Returns if the text is in the data structure. A text could contain the dot character '.' to represent any one letter.
        """
        if not text:
            return
        if text[0] == ".":
            # search in all child nodes
            if len(text) == 1:
                if self.children:
                    # check if any of children is word
                    return any([c.is_word for _, c in self.children.items()])
                else:
                    return False

            found = False
            if self.children:
                for ch, trieNode in self.children.items():
                    if trieNode.search(text[1:]):
                        found = True
                        break
            return found

        else:
            if text[0] in self.children:
                if len(text) == 1:
                    return self.children[text[0]].is_word
                else:
                    return self.children[text[0]].search(text[1:])


class WordDictionary:
    def __init__(self):
        self.words = dict()

    def addWord(self, word: str):
        if not word:
            return
        if word[0] in self.words.keys():
            self.words[word[0]].addWord(word[1:])
        else:
            self.words[word[0]] = TrieNode(word)

    def search(self, word: str) -> bool:
        if not word:
            return False
        if word[0] == ".":
            found = False
            if self.words:
                for ch, trieNode in self.words.items():
                    if trieNode.search(word[1:]):
                        found = True
                        break
            return found
        elif word[0] in self.words.keys():
            return self.words[word[0]].search(word[1:])
        else:
            return False


if __name__ == "__main__":
    dictionary = WordDictionary()
    dictionary.addWord("sunil")
    dictionary.addWord("sap")
    dictionary.addWord("manju")
    dictionary.addWord("man")
    # print(node.val)
    print(dictionary.search("sunil"))
    print(dictionary.search("sap"))
    print(dictionary.search("man"))
    print(dictionary.search(".unil"))
    print(dictionary.search("s.nil"))
    print(dictionary.search("s."))
    print(dictionary.search("...."))

