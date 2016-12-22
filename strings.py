'''
O(n*m) time complexity where m is the length of the longest string
O(m) space complexity since each hashmap can only contain 26 keys
Find shortest unique prefix to represent each word in the list.
This question didn't make much sense to me when
I first read it but basically you are supposed
return the shortest prefix that doesn't exist in any other word
if given ['dog', 'duck'] both begin with 'd' so the shortest prefixes
are ['do', 'du']
'''
class Trie:
    def __init__(self):
        self.table = {}
        self.val = 0

def prefix(A):
    out = []
    trie = Trie()
    for x in A:
        temp = trie
        for c in x:
            if c in temp.table:
                temp.table[c].val += 1
                temp = temp.table[c]
            else:
                temp.table[c] = Trie()
                temp.table[c].val = 1
                temp = temp.table[c]
    for i in xrange(len(A)):
        temp = trie
        out.append('')
        for c in A[i]:
            if temp.table[c].val == 1:
                out[i]+=c
                break
            else:
                temp = temp.table[c]
                out[i]+=c
    return out

if __name__ == '__main__':
    print prefix([ "zebra", "dog", "duck", "dot" ])
