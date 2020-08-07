# It is very simple to create a queue using Python's list
# Python also provides a deque: from collections import deque
class PyQueue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        return self.storage[0] 

    def dequeue(self):
        return self.storage.pop(0)
    
