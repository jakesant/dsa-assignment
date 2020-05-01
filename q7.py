#Write a program that accepts as input a sequence of integers (one by
#one) and then incrementally builds, and displays, a Binary Search Tree
#(BST). There is no need to balance the BST.

import statistics

class Node:
    def __init__(self, number = None):
        self.number = number
        self.left = None
        self.right = None

class Tree:

    def __init__(self):
        self.root = None

def new_node(number):
    if(bst.root == None):
        bst.root = Node(number)
    else:
        if(number > bst.root.number):
            bst.root.right = number
        elif(number < bst.root.number):
            bst.root.left = number

def print_tree(tree):
    if(tree.root is not None):
        print(tree.root.left, tree.root.number, tree.root.right)
    else:
        print("An error has occured")

seq = [10, 5, 1, 7, 40, 50]
med = statistics.median(seq) #Don't actually need this nahseb
bst = Tree()
new_node(5)
new_node(10)
new_node(1)
print_tree(bst)