# A Python class that represents an 
# individual node in a Binary Tree

class Node:
    def __init__(self, value=None):
        self.value = value
        self.leftChild = None
        self.rightChild = None

    def __str__(self):
        return 'node [ {data} ]'.format(data=self.value)