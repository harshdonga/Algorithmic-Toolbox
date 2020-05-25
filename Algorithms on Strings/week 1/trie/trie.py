#Uses python3
import sys

def build_trie(patterns):
    tree = dict()
    tree[0] = {}
    index = 1
    
    for p in patterns:
        curr = tree[0]
        for l in p:
            if l in curr.keys():
                curr = tree[curr[l]]

            else:
                curr[l] = index
                tree[index] = {}
                curr = tree[index]
                index += 1
    
    return tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))