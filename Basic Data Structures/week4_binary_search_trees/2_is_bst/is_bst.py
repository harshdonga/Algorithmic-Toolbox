#!/usr/bin/python3

import sys, threading, math

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def inOrder(tree):
    result = []
    def inOrderRec(i,result):
        if tree[i][1] != -1:
            inOrderRec(tree[i][1], result)
        result.append(tree[i][0])
        if tree[i][2] != -1:
            inOrderRec(tree[i][2], result)
    inOrderRec(0, result)
    return result

def IsBinarySearchTree(tree, stree):
    traversed = inOrder(tree)
    if traversed == stree:
        return True
    else:
        return False
    

def main():
    nodes = int(input().strip())
    if nodes == 0:
      print('CORRECT')
      exit()
    tree = []
    for i in range(nodes):
        tree.append(list(map(int,input().strip().split())))
    stree = sorted([x[0] for x in tree])
    if IsBinarySearchTree(tree, stree):
        print("CORRECT")
    else:
        print("INCORRECT")
    
threading.Thread(target=main).start()