#Made my Moonis Rasheed
#For more check out my Github Account https://github.com/moon18

class USet:
    def __init__(self):
        '''Initializes member variables.

        >>> uset = USet()
        '''
        self.uset=[]
        self.siz=0

    def __str__(self):
        '''Returns a string representation of an object for printing.

        >>> uset = USet()
        >>> print(uset)  # prints uset.__str__()
        '''
        pass

    def add(self, key, val):
        '''Adds the pair (key, val) to the USet if no pair with key
        already exists in the USet, and returns True. Returns False if a
        pair with key already exists in the USet.

        >>> uset = USet()
        >>> uset.add(1, 10)
        True
        >>> uset.add(2, 20)
        True
        >>> uset.add(2, 30)
        False
        '''
        for i in self.uset:
            if i[0]==key:
                return False

        self.uset.append((key,val))
        self.siz += 1
        return True

    def remove(self, key):
        '''Removes the pair with key from the USet and returns it.
        Returns None if no such pair exsits.

        >>> uset = USet()
        >>> uset.add(1, 10)
        True
        >>> uset.add(2, 20)
        True
        >>> uset.remove(1)
        (1, 10)
        >>> uset.remove(10)
        >>>
        '''
        index = 0
        for i in self.uset:
            if i[0]==key:
                self.siz-=1
                return self.uset.pop(index)
            index+=1
        return None

    def find(self, key):
        '''Returns the pair from the USet that contains key; None if no
        such pair exists.

        >>> uset = USet()
        >>> uset.add(1, 10)
        True
        >>> uset.add(2, 20)
        True
        >>> uset.find(1)
        (1, 10)
        >>> uset.find(10)
        >>> 
        '''
        for i in self.uset:
            if i[0]==key:
                return i
        return None
            

    def size(self):
        '''Returns the number of pairs currently in the USet.
        
        >>> uset = USet()
        >>> uset.size()
        0
        >>> uset.add(1, 10)
        True
        >>> uset.add(2, 20)
        True
        >>> uset.size()
        2
        >>> uset.add(2, 30)
        False
        >>> uset.size()
        2
        '''
        return self.siz

    def keys(self):
        '''Returns a list of keys in the USet.
        
        >>> uset = USet()
        >>> uset.keys()
        []
        >>> uset.add(1, 10)
        True
        >>> uset.add(2, 20)
        True
        >>> uset.keys()
        [1, 2]
        >>> uset.add(2, 30)
        False
        >>> uset.keys()
        [1, 2]
        '''
        NumKey=[]
        for i in self.uset:
            NumKey.append(i[0])
        return NumKey
