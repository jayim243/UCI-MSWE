#**TASK 1** hash class
import re #regular expression for splitting delimiters
#can we import random to use for compression function: scaling, prime numbers... etc?

class Hash():
    def __init__(self, capacity): 
        self.capacity = capacity #cap the bucket array
        self.keyCount = 0 #store number of unique keys in bucket array
        self.hashTable = [None] * capacity #fixed 1D array representing our bucket array
    

    def hash(self, x): #returns some integer e.g. 2131029, -12145, 6... 
        mask = (1 << 32) - 1 #cyclic-shift hash code from textbook readings
        h = 0
        x = ''.join(sorted(x)) #reasign x to sorted(x): by calling sorted on x, we can create a list of each characters sorted which will yield the same hash code when joined back
        for character in x:
            h = (h << 5 & mask) | (h >> 27)
            h += ord(character)
        return h #h = some int, we now use compression function to actually insert into our bucket array


    def compression(self, h): #compresses the integer from hash into an index for bucket array
        hashNum = self.hash(h) 
        anagram = x = ''.join(sorted(h))
        return (hashNum % self.capacity, anagram) #implementing MAD was a bit complicated

    
    def resize(self):
        print(f'{self.capacity} has been resized to {self.capacity * 2}')
        self.capacity = self.capacity * 2 #double capcity size
        self.hashTable += [None] * self.capacity #double bucket array size by concatenating [None]s


    def insert(self, x):
        index, anagram = self.compression(x)
        #resize if hash table is full
        if self.keyCount == self.capacity:
            self.resize()
        while self.hashTable[index] is not None:
            index = (index + 1) % self.capacity #linearly probing and possibly eventually wrapping

        if self.hashTable[index] == None: #if value is not None, then it should be the same anagram, in which case we do nothing
            self.keyCount += 1 #keep track of number of unique keys in bucket array


    def size(self):
        return self.keyCount
        

    
if __name__ == "__main__":
    #**TASK 2**
    h = Hash(31260)
    with open('pride-and-prejudice.txt', 'r') as file:
        for eachLine in file:
            line = file.readline()
            words = re.split(r'[^a-z-A-Z]', line) #regex to split lines by delimiters that are not alphanumeric
            for word in words:
                if word.isalnum(): #ignores whitespaces in words list
                    h.insert(word)
    print(h.size()) #task2 answer should be ab 6000..?