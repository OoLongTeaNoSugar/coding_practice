# dic = {'a':1, 'c':3, 'd':4, 'b':4}
# new_dic = sorted(dic.values())
#
# s = [1,2,'3']
# # b = str(s)
# print(ord('A'))
class TrieNode:
    def __init__(self):
        self.lookup = {}

    def insert(self, word):
        tree = self.lookup
        for a in word:
            if a not in tree:
                tree[a] = {}
            tree = tree[a]
        # end label
        tree['#'] = '#'

    def search(self, word):
        tree = self.lookup
        for a in word:
            if a not in tree:
                return False
            tree =tree[a]
        if '#' in tree:
            return True
        return False

    def startwith(self, prefix):
        tree = self.lookup
        for a in prefix:
            if a not in tree:
                return False
            tree = tree[a]
        return True
