# A Python class that represents a Binary Tree
from Node import Node

class Binary_search_tree:

    def __init__(self):
        self.root = None
        
    # def __str__(self):
    #      return 'root [ {data} ]'.format(data=self.root)

    def insert_value(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert_value(value, self.root)

    def _insert_value(self, value, currentNode):
        if value < currentNode.value:
            if currentNode.leftChild == None:
                currentNode.leftChild = Node(value)
            else:
                self._insert_value(value, currentNode.leftChild)
        elif value > currentNode.value:
            if currentNode.rightChild == None:
                currentNode.rightChild = Node(value)
            else:
                self._insert_value(value, currentNode.rightChild)
        else:
            print("Value already in tree")
    
    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)
    
    def _print_tree(self, currentNode):
        if currentNode != None:
            self._print_tree(currentNode.leftChild)
            print (str(currentNode.value))
            self._print_tree(currentNode.rightChild)
    
    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0 
    
    def _height(self, currentNode, currentHeight):
        if currentNode == None:
            return currentHeight
        leftHeight = self._height(currentNode.leftChild, currentHeight + 1)
        rightHeight = self._height(currentNode.rightChild, currentHeight + 1)
        return max(leftHeight, rightHeight)
    
    def find(self, value):
        if self.root!=None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, currentNode):
        if value ==currentNode.value:
            return currentNode
        elif value < currentNode.value and currentNode.leftChild != None:
            return self._find(value, currentNode.leftChild)
        elif value > currentNode.value and currentNode.rightChild != None: 
            return self._find(value, currentNode.rightChild)