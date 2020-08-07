import random # for balancing the tree

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class PyBinaryTree(object):
    """ Contains add, search and print (no delete) """
    def __init__(self, root):
        self.root = Node(root)

    def add_item(self, new_node):
        currNode = self.root
        while True:
            # Balance the tree by randomly chosing whether to place it in the left or right
            if random.randint(0, 1) == 0:
                # Go with right
                if currNode.right == None:
                    currNode.right = new_node
                    return
                elif currNode.left == None:
                    currNode.left = new_node
                    return
            # Randomly chose whether to go left or right
            currNode = currNode.right if random.randint(0, 1) == 0 else currNode.left
            
        
    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        result = self.preorder_traverse(self.root)
        if find_val in result:
            return True:
        else:
            return False
    
    def print_tree(self):
        """Print out the tree as a list in pre-order visit """
        return self.preorder_traverse(self.root)

    def preorder_traverse(self, node):
        if node.left == None and node.right == None:
            return [node.value]
        else:
            return [node.value] + self.preorder_traverse(node.left) + self.preorder_traverse(node.right) 

