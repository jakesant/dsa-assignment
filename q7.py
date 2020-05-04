#Write a program that accepts as input a sequence of integers (one by
#one) and then incrementally builds, and displays, a Binary Search Tree
#(BST). There is no need to balance the BST.

class Node:
    def __init__(self, number = None):
        self.number = number
        self.left = None
        self.right = None

    def new_node(self, number):
        if(self.number is None):
            self.number = number
        else:
            if(number > self.number):
                if(self.right is None):
                    self.right = Node(number) #Creates the right side as a new node if doesn't already exist
                else:
                    self.right.new_node(number)
            elif(number < self.number):
                if(self.left is None):
                    self.left = Node(number) #Creates the left side as a new node if doesn't already exist
                else:
                    self.left.new_node(number)

class Tree:
    def __init__(self):
        self.root = None

    def print_tree(self, currentNode):
        if(currentNode is not None):
            if(currentNode.left is not None):
                self.print_tree(currentNode.left)
            elif(currentNode.left is None and currentNode.right is not None):
                print(currentNode.number)
                self.print_tree(currentNode.right)
            elif(currentNode.left is None and currentNode.right is None):
                print(currentNode.number)
        else:
            print("An error has occured")


    def print2(self, currentNode):
        if(currentNode is not None):
            if(currentNode.left is not None):
                self.print2(currentNode.left)
            print(currentNode.number)
            if(currentNode.right is not None):
                self.print2(currentNode.right)
        else:
            print("An error has occured")
    def new_node(self, number):

        #This is needed to use the node's functions without making it a subclass and fucking everything over
        if(self.root is None):
            self.root = Node(number) #Creates new node for root
        else:
            self.root.new_node(number)


seq = [10, 5, 1, 7, 40, 50]
bst = Tree()
bst.new_node(10)
bst.new_node(5)
bst.new_node(7)
bst.new_node(14)
bst.new_node(12)
bst.new_node(20)
#for i in seq:
 #   bst.new_node(i) #Builds binary search try milewwel
#bst.print_tree(bst.root)
bst.print2(bst.root)