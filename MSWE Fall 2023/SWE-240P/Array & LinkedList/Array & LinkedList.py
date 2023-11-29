class node:
    def __init__(self, user, id, next):
        #node class
        self.user = user #giving user info to node attributes
        self.name = self.user[0] 
        self.address = self.user[1]
        self.social = self.user[2]
        self.deposit = self.user[3]
        self.next = next
        self.id = id


class bankOfOrangeCounty:
    def __init__(self):
        #singly LL class
        self.head = None
        self.size = 0


    def getSize(self): #return size of LL
        return self.size

    
    def validId(self, ID): #validates ID to test edge cases
        curr = self.head
        while curr:
            if curr.id == ID:
                return True
            curr = curr.next
        return False


    def addUser(self, user):
        if not self.head: #check for head, add user regularly to the end of LL ensuring to point to Null
                self.head = node(user, 0, None)
                self.currentId = 1
                self.size = 1
        elif not self.head.name: #if first user is None
            self.head = node(user, 0, self.head.next)
            self.size += 1
        else:
            prev = None
            curr = self.head
            while curr and curr.next:
                if not curr.name: # if users anywhere else is None
                    tempID = curr.id
                    tempNext = curr.next 
                    prev.next = node(user, tempID, tempNext) 
                    self.size += 1
                    return 
                prev = curr
                curr = curr.next

            if not curr.name: #if last user is None
                tempID = curr.id
                tempNext = curr.next 
                prev.next = node(user, tempID, tempNext) 
                self.size += 1
                return                 

            curr.next = node(user, self.currentId, None) #adding to tail of LL
            self.currentId += 1
            self.size += 1

    
    def deleteUser(self, ID):
        if not self.validId(ID):
            raise AssertionError(f'user ID: {ID} does not exist in bank')

        curr = self.head
        while curr:
            if curr.id == ID:
                curr.user = curr.name = curr.address = curr.social = curr.deposit = None #set all node attributes to None besides ID and next pointer
                self.size -= 1 #decremenet size of LL
                return
            curr = curr.next
        
                     

    def payUserToUser(self, payerID, payeeID, amount):
        if not self.validId(payerID):
            raise AssertionError(f'user ID: {payerID} does not exist in bank')
        if not self.validId(payeeID):
            raise AssertionError(f'user ID: {payeeID} does not exist in bank')

        
        
        curr = self.head
        paid = received = False #determines if first instance of both payerID and payeeID are found
        while curr:
            if paid and received:
                return 
            if curr.id == payerID and not paid:
                if curr.deposit >= amount:
                    curr.deposit -= amount #subtract amount from payer
                    paid = True
                else:
                    raise AssertionError(f'user ID: {curr.id} insufficient funds') #raise error instead of withdrawing as much as possible because a real bank will decline
            if curr.id == payeeID and not received:
                curr.deposit += amount #add amount to payee
                received = True
            curr = curr.next


    def getMedian(self): #since our LL is already in increasing sorted order by ID:
        slow, fast = self.head, self.head.next #flyod tortoise and hare to find middle of LL
        while fast and fast.next:
            slow = slow.next #slow pointer will end at either middle of LL or first of the two middle nodes
            fast = fast.next.next
        if self.size % 2 == 0: #if even, return avg
            return (slow.id + slow.next.id) / 2
        else:
            return slow.id #else median
    

    def mergeAccounts(self, ID1, ID2):
        if not self.validId(ID1):
            raise AssertionError(f'user ID: {ID1} does not exist in bank')
        if not self.validId(ID2):
            raise AssertionError(f'user ID: {ID2} does not exist in bank')

        curr = self.head
        smallerID = min(ID1, ID2) #identify which ID is smaller
        firstFound = secondFound = False
        while curr:
            if curr.id == ID1 and not firstFound: #finding first ID in LL
                firstAccount = curr
                firstFound = True
            if curr.id == ID2 and not secondFound: #finding second ID in LL
                secondAccount = curr
                secondFound = True
            curr = curr.next
        if firstFound and secondFound: #if both IDs are found in LL compare if users are actually the same
            if firstAccount.user[:3] == secondAccount.user[:3]: #comparison
                if firstAccount.id == smallerID: #if first account ID is smaller, merge onto first account and delete second
                    self.payUserToUser(secondAccount.id, firstAccount.id, secondAccount.deposit)
                    self.deleteUser(secondAccount.id)
                else:
                    self.payUserToUser(firstAccount.id, secondAccount.id, firstAccount.deposit) #vice versa
                    self.deleteUser(firstAccount.id)
            
    
    def mergeBanks(self, bankOfOrangeCounty, bankOfLosAngeles):
        curr = self.head
        while curr and curr.next:
            curr = curr.next #reach end of OC LL
        headLa = bankOfLosAngeles.head
        prevId = curr.id #store prev ID to increment and change all LA IDs
        while headLa:
            headLa.id = prevId + 1 #going through LA LL and changing all IDs to previous ID + 1
            prevId = headLa.id #update prevId
            headLa = headLa.next
        curr.next = bankOfLosAngeles.head #appending head of LA LL to end of OC LL
        return self.head #return head of OC LL (OC -> LA -> None)




if __name__ == "__main__":
    # **OC TEST CASES**
    users = [['jay', '123 street', 12345, 0], #input [[user info], [user info], [user info]...]
        ['josh', '456 street', 43123, 321312], 
        ['joe', '789 street', 00000, 123], 
        ['yongjun', '471 street', 34810, 999]]

    LL = bankOfOrangeCounty() #initialize LL and test functions
    for user in users:
        LL.addUser(user)

    # LL.deleteUser(0)
    # LL.addUser(['anh', '2313 st', 3215, 0])
    # LL.deleteUser(2)
    # LL.addUser(['jax', '2313 st', 3215, 0])
    # LL.addUser(['hannah', '2313 st', 3215, 50])
    # LL.addUser(['angel', '2313 st', 3215, 200])
    # LL.payUserToUser(4, 0, 50)
    # LL.mergeAccounts(4, 5)

    # curr = LL.head #print results
    # while curr:
    #     print(curr.name, curr.deposit, curr.id)
    #     curr = curr.next
    
    # print(LL.getMedian())
    # print(LL.getSize())
    


    # **LA TEST CASES**
    laUsers = [['may', '123 street', 12345, 0], #input [[user info], [user info], [user info]...]
        ['julian', '456 street', 43123, 321312], 
        ['ephraim', '789 street', 00000, 123], 
        ['kole', '471 street', 34810, 999]]
        
    LA = bankOfOrangeCounty()
    for user in laUsers:
        LA.addUser(user)

    # currLa = LA.head #print results
    # while currLa:
    #     print(currLa.name, currLa.id)
    #     currLa = currLa.next


    # **BSC TEST CASE**
    # Bank_of_Southern_California = LL.mergeBanks(LL, LA) #create new LL(bank) BSC by merging OC and LA
    # while Bank_of_Southern_California:
    #     print(Bank_of_Southern_California.name, Bank_of_Southern_California.id)
    #     Bank_of_Southern_California = Bank_of_Southern_California.next