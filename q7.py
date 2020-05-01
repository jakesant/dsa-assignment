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
    #Tree will be printed using In-Order traversal (LNR)
    if(tree.root.left is not None): #using is not is preferred in Python
        print_tree(tree.root.left)
    print(Tree.root.number)
    if(tree.root.right is not None):
        print_tree(tree.root.right)


seq = [10, 5, 1, 7, 40, 50]
med = statistics.median(seq)
bst = Tree()
new_node(5)
new_node(10)
new_node(1)
print_tree(bst)