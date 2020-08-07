"""Simple implementation of a PyHashTable"""

class PyHashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Add a string to the hash table"""
        index = self.calculate_hash_value(string)
        
        if self.table[index] == None:
            self.table[index] = [string]
        else:
            self.table[index].append(string)

    def lookup(self, string):
        """Check if the item exists, if yes, return the index,
            otherwise, return -1 """
        index = self.calculate_hash_value(string)
        
        if self.table[index] == None:
            return -1
        else:
            for i in self.table[index]:
                if i == string:
                    return index
            return -1

    def calculate_hash_value(self, string):
        """ Hashify the value to create a key (the index) """
        return ord(string[0]) * 100 + ord(string[1])
