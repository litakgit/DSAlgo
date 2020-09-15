import collections

class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.valid_word = False
        self.closest_words = []

class Trie(object):
    def __init__ (self):
        self.root = TrieNode()

    def insert(self, word):
        #import pdb; pdb.set_trace()
        node = self.root
        for ch in word:
            node = node.children[ch]
            node.closest_words.append(word)
            node.closest_words.sort()
            #del node.closest_words[2:]
        node.valid_word = True

    def get_all_words_in_dict(self, node, res=[]):
        #print (res[-1] if res else None)
        #print (node.closest_words)
        if node.valid_word:
            print (''.join(res.copy()))
        for ch in node.children:
            self.get_all_words_in_dict(node.children[ch], res+[ch])


if __name__ == "__main__":
    dic = Trie()
    dic.insert("ask")
    dic.insert("askme")
    dic.insert("and")
    dic.insert("andor")
    dic.insert("andorand")
    dic.get_all_words_in_dict(dic.root)
