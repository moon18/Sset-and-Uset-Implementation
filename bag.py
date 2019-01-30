from uset import USet

# Adapted from Exercise 1.5 in the book.

class Bag:
    def __init__(self):
        '''Initializes member variables.
        >>> bag = Bag()
        '''
        self.uset = USet()  # this is the underlying data structure.
        self.siz =0

    def __str__(self):
        '''Returns a string representation of an object for printing.
        >>> bag = Bag()
        >>> print(bag)  # prints bag.__str__()
        '''
        pass

    def add(self, key, val):
        '''Adds the pair (key, val) to the Bag.
        >>> bag = Bag()
        >>> bag.add(1, 10)
        >>> bag.size()
        1
        >>> bag.add(1, 10)
        >>> bag.size()
        2
        >>> bag.add(1, 20)
        >>> bag.size()
        3
        >>> bag.add(2, 20)
        >>> bag.size()
        4
        '''
        founded_item = self.uset.remove(key)
        if (founded_item != None):
            if type(founded_item[1])==list :
                founded_item[1].append(val)
                self.siz +=1
                self.uset.add(founded_item[0],founded_item[1])
            else:
                temp_list =[founded_item[1],val]
                self.uset.add(founded_item[0],temp_list)
                self.siz +=1
        else:
            self.uset.add(key,val)
            self.siz +=1
        print(self.uset.uset,self.siz)            




            
        
        

    def remove(self, key):
        '''Removes a pair with key from the Bag and returns it.
        Returns None if no such pair exsits.
        >>> bag = Bag()
        >>> bag.add(1, 10)
        >>> bag.add(1, 10)
        >>> bag.add(1, 20)
        >>> bag.add(2, 20)
        >>> bag.remove(1)
        (1,10)  # could be any of the 3 pairs with key == 1.
        >>> bag.remove(2)
        (2,20)
        >>> bag.remove(20)
        >>>
        '''
        founded_item = self.uset.remove(key)
        if founded_item != None:
            if(type(founded_item[1]) == list):
                temp_val = founded_item[1].pop()
                self.siz-=1
                if (len(founded_item[1])!= 1):
                    self.uset.add(founded_item[0],founded_item[1])
                    print(self.uset.uset,self.siz)
                else:
                    self.uset.add(founded_item[0],founded_item[1][0])
                    print(self.uset.uset,self.siz)
                return (founded_item[0],temp_val)
            else:
                self.siz -=1
                return founded_item
            
        return None
            

    def find(self, key):
        '''Returns a pair from the Bag that contains key; None if no
        such pair exists.
        >>> bag = Bag()
        >>> bag.add(1, 10)
        >>> bag.add(1, 10)
        >>> bag.add(1, 20)
        >>> bag.add(2, 20)
        >>> bag.find(1)
        (1,10)  # could be any of the 3 pairs with key == 1.
        >>> bag.find(2)
        (2,20)
        >>> bag.find(20)
        >>>
        '''
        temp_item = self.uset.find(key)
        if(temp_item!=None):
            if(type(temp_item[1])==list):
                return (temp_item[0],temp_item[1][0])
            else:
                return temp_item
        else:
            return temp_item
    def size(self):
        '''Returns the number of pairs currently in the Bag.
        
        >>> bag = Bag()
        >>> bag.size()
        0
        >>> bag.add(1, 10)
        >>> bag.add(2, 20)
        >>> bag.size()
        2
        >>> bag.add(2, 30)
        >>> bag.size()
        3
        '''
        return self.siz

    def keys(self):
        '''Returns a list of keys in the Bag.
        >>> bag = Bag()
        >>> bag.add(1, 10)
        >>> bag.add(1, 10)
        >>> bag.add(1, 20)
        >>> bag.add(2, 20)
        >>> bag.keys()
        [1, 2]
        '''
        return self.uset.keys()

    def find_all(self,key):
        founded_item = self.uset.find(key)
        r_list = []
        if(founded_item != None ):
            if(type(founded_item[1])==list):
                for i in founded_item[1]:
                    r_list.append((founded_item[0],i))
            else:
                r_list.append(founded_item)
        return r_list
        
