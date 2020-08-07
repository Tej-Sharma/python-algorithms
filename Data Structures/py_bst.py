class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        """ Take advantage of time to get O(log n) run time """
        currNode = self.root
        # Iterate until the right value is found
        while True:
            if new_val <= currNode.value:
                if currNode.left == None:
                    currNode.left = Node(new_val)
                    return
                else:
                    currNode = currNode.left
            elif new_val > currNode.value:
                if currNode.right == None:
                    currNode.right = Node(new_val)
                    return
                else:
                    currNode = currNode.right
                    
    def search(self, find_val):
        """ As it's a BST, it is kind of similar to the insert function,
            but here we do not need to do insertion. O(log n) run time """
        currNode = self.root
        while True:
            if currNode == None:
                # No such item exists
                return False
            if find_val < currNode.value:
                currNode = currNode.left
            elif find_val > currNode.value:
                currNode = currNode.right
            else:
                # It is equal to the value: found it
                return True
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print (tree.search(4))
# Should be False
print (tree.search(6))
