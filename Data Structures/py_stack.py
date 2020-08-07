# Represents a node
class ListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

# Modified Py Linked List for creating a stack
class PyLinkedList(object):
    def __init__(self, head=None):
        self.head = head
    
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        """ Add an element to the head """
        new_element.next = self.head
        self.head = new_element


    def delete_first(self):
        """ Delete the head """
        # make sure to check if a head exists
        if self.head:
            prev = self.head
            self.head = self.head.next
            return prev
        else:
            return None

# Will consider the 'head' of the list to be the last element added
class PyStack(object):
    def __init__(self,top=None):
        self.ll = PyLinkedList(top)

    def push(self, new_element):
        self.ll.insert_first(new_element)

    def pop(self):
        return self.ll.delete_first()
