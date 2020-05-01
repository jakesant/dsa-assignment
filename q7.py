#Write a program that accepts as input a sequence of integers (one by
#one) and then incrementally builds, and displays, a Binary Search Tree
#(BST). There is no need to balance the BST.

class Node:
    def __init__(self, number = None):
        self.number = number
        self.left = None
        self.right = None

class Tree:

    def __init__(self):
        self.root = None

    def print_tree(self):
        if(self.root is not None):
            print(self.root.left, self.root.number, self.root.right) #"Technically" this is In-Order lol 
        else:
            print("An error has occured")

    def new_node(self, number):
        if(self.root is not None):
            self.root = Node(number)
        else:
            if(number > self.root.number):
                if(self.root.right is None):
                    self.root.right = Node(number) #Creates the right side as a new node if doesn't already exist 
            elif(number < self.root.number):
                if(self.root.left is None):
                    self.root.left = Node(number) #Creates the left side as a new node if doesn't already exist



seq = [10, 5, 1, 7, 40, 50]
bst = Tree()
bst.new_node(5)
bst.new_node(10)
bst.new_node(1)
print("Yo")