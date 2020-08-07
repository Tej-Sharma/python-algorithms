class ListObject(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
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
            
    def get_position(self, position):
        """Return an element by index"""
        counter = 1
        current = self.head
        if self.head:
            while counter != position:
                current = current.next
                counter += 1
            return current if current else "None"
        else:
            return "None"
            
    
    def insert(self, new_element, position):
        """Insert at a position. For example, inserting at 2 means
            insert between 1 and 2"""
        counter = 1
        current = self.head
        if self.head:
            while counter != position - 1: # needs to be between the elements, so -1
                current = current.next
                counter += 1
            # make sure to point to the element that was originally there
            new_element.next = current.next 
            # insert the element
            current.next = new_element
        else:
            self.head = new_element
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        prev = None
        current = self.head
        if self.head.value == value:
            self.head = self.head.next
            return
        while current.next:
            if current.value == value:
                # delete this
                prev.next = current.next
            prev = current
            current = current.next
                
# Test cases (taken from Udacity's Google Python Data Structures course)
# Set up some Elements
e1 = ListObject(1)
e2 = ListObject(2)
e3 = ListObject(3)
e4 = ListObject(4)

# Start setting up a LinkedList
ll = PyLinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print (ll.head.next.next.value)
# Should also print 3
print (ll.get_position(3).value)

# Test insert
ll.insert(e4,3)
# Should print 4 now
print (ll.get_position(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
print (ll.get_position(1).value)
# Should print 4 now
print (ll.get_position(2).value)
# Should print 3 now
print (ll.get_position(3).value)
