#Made my Moonis Rasheed
#For more check out my Github Account https://github.com/moon18

class SSet:
    def __init__(self):
        '''Initializes member variables.
        >>> sset = SSet()
        '''
        self.set = []   #set is a list we made to work in our data structure
        self.siz = 0

    def __str__(self):
        '''Returns a string representation of an object for printing.

        >>> sset = SSet()
        >>> print(sset)  # prints sset.__str__()
        '''
        pass

    def add(self, key, val):
        '''Adds the pair (key, val) to the SSet if no pair with key
        already exists in the SSet, and returns True. Returns False if a
        pair with key already exists in the SSet.
        
        >>> sset = SSet()
        >>> sset.add(1, 10)
        True
        >>> sset.add(2, 20)
        True
        >>> sset.add(2, 30)
        False
        '''
        #checking for existing key 
        for i in self.set:
            if i[0]==key:
                return False

        self.set.append((key,val))
        self.set.sort()
        self.siz += 1
        return True
    

    def remove(self, key):
        '''Removes the pair with key from the SSet and returns it.
        Returns None if no such pair exsits.

        >>> sset = SSet()
        >>> sset.add(1, 10)
        True
        >>> sset.add(2, 20)
        True
        >>> sset.remove(1)
        (1, 10)
        >>> sset.remove(10)
        >>>
        '''
        index = 0
        for i in self.set:
            if i[0]==key:
                self.siz-=1
                return self.set.pop(index)
            index+=1
        return None

    def find(self, key):
        '''Returns the pair from the SSet that contains key. If no such
        pair exists, returns the pair from the SSet that contains the
        successor of key. Returns None if no such pair exists.

        >>> sset = SSet()
        >>> sset.add(1, 10)
        True
        >>> sset.add(2, 20)
        True
        >>> sset.find(1)
        (1, 10)
        >>> sset.find(1.5)
        (2, 20)
        >>> sset.find(3)
        >>> 
        '''
        
        for i in self.set:
            if i[0]>=key:
                return i
        return None

    def size(self):
        '''Returns the number of pairs currently in the SSet.
        
        >>> sset = SSet()
        >>> sset.size()
        0
        >>> sset.add(1, 10)
        True
        >>> sset.add(2, 20)
        True
        >>> sset.size()
        2
        >>> sset.add(2, 30)
        False
        >>> sset.size()
        2
        '''
       
        return  self.siz

    def keys(self):
        '''Returns a list of keys in the SSet.
        
        >>> sset = SSet()
        >>> sset.keys()
        []
        >>> sset.add(1, 10)
        True
        >>> sset.add(2, 20)
        True
        >>> sset.keys()
        [1, 2]
        >>> sset.add(2, 30)
        False
        >>> sset.keys()
        [1, 2]
        '''
        NumKey=[]
        for i in self.set:
            NumKey.append(i[0])
        return NumKey
