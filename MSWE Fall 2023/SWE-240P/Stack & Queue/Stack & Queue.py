#node class
class node:
    def __init__(self, element, next=None): #using LL to implement stack
        self.element = element
        self.next = next


#**TASK 1**
class stack:
    def __init__(self):
        self.currSize = 0
        self.head = None
        

    def isEmpty(self): #helper function to check if stack is empty and functions can raise error if empty
        if not self.head:
            return True
        return False


    def push(self, element): #push element to top of LL
        if not self.head: #if LL is empty
            self.head = node(element)
        else:
            nxt = self.head #else store the old top of stack so we can point the new head of the stack to it
            self.head = node(element, nxt)
        self.currSize += 1 #increment size of stack

    
    def pop(self):
        if self.isEmpty():
            raise AssertionError(f"Stack is empty")
        popped = self.head #save result to return
        self.head = self.head.next #setting new head to head.next
        popped.next = None
        self.currSize -= 1 #decrement size of stack
        return popped.element

    
    def peek(self):
        if self.isEmpty():
            raise AssertionError(f"Stack is empty")
        return self.head.element #return the element from the top of stack

    
    def size(self):
        return self.currSize #return size of stack that has been modified every push and pop



#**TASK 3**
class queue:
    def __init__(self, capacity):
        self.currSize = 0
        self.capacity = capacity #max capacity of queue
        self.head = 0 #keep track of next dequeue in the array (first in queue)
        self.tail = 0 #keep track of next enqueue placement in the array (next addition to queue)
        self.q = [0] * capacity #allocating enough space

    
    def enqueue(self, element):
        if self.currSize == self.capacity: #error if queue is full
            raise AssertionError(f'queue is full, cannot enqueue {element}')
        self.q[self.tail] = element
        self.currSize += 1 #incremenet size of queue
        self.tail = (self.tail+1) % self.capacity #circular queue using an array based implementation: update the next placement of enqueue
    

    def dequeue(self):
        if self.currSize == 0: #error if queue is empty
            raise AssertionError(f'queue is empty, cannot dequeue')
        self.currSize -= 1 #decrement size of queue
        res = self.q[self.head] #store result to return, no need to remove actual value from array, as next line will update the new "first" of queue, but will replace value with 0 for more clarity
        self.q[self.head] = 0
        self.head = (self.head+1) % self.capacity #update the "first" in queue
        return res
        
    
    def poll(self):
        if self.currSize == 0:
            raise AssertionError(f'queue is empty')
        return self.q[self.head]
    

    def size(self):
        return self.currSize



#**TASK 4**
class StackWithTwoQs:
    def __init__(self, capacity): #capacity of stack
        self.currSize = 0
        self.q1 = queue(capacity) #used to store actual stack in queue order
        self.q2 = queue(capacity) #used to hold new enqueue element and append remaining elements from q1 into here
        #swap q1 and q2 after computations are complete to still have q1 as stack


    def push(self, x):
        #algo visual:
            #q1 = [1] -> q1 = [ ] -> q1 = [1] -> q1 = [1] -> q1 = [ ] -> q1 = [2, 1] -> q1 = [2, 1] -> q1 = [ ] -> q1 = [3, 2, 1]
            #q2 = [ ] -> q2 = [1] -> q2 = [ ] -> q2 = [2] -> q2 = [2, 1] -> q2 = [ ] -> q2 = [3] -> q2 = [3, 2, 1] -> q2 = [ ]
        if self.q1.size() == 0: #if nothing in stack, just add into stack
            self.q1.enqueue(x)
        else:
            self.q2.enqueue(x) #add the "last(most recent)" element in stack to the front of queue2
            for i in range(self.q1.currSize): #add remaining elements from queue1 to queue2
                self.q2.enqueue(self.q1.dequeue())
            self.q1, self.q2 = self.q2, self.q1 #swap queues to continue algo
        self.currSize += 1


    def pop(self):
        if self.q1.size() == 0: #queue 1 empty means stack empty
            raise AssertionError(f'stack is empty')
        self.currSize -= 1
        return self.q1.dequeue()
        
    

    def peek(self):
        if self.q1.size() == 0: #queue 1 empty means stack empty
            raise AssertionError(f'stack is empty')
        return self.q1.poll()


    def size(self):
        return self.currSize # or len(self.q1) : same thing



if __name__ == "__main__":
    #**TASK 1 TESTING**
    # s = stack()
    # s.push(1)
    # s.push(2)
    # s.push(3)
    # for i in range(5):
    #     s.push(i)
    #     print(s.size())
    # print(s.peek())
    # print(s.pop())
    

    
    #**TASK 2**
    def task2(input):
        operators = '+-/*' #global operators


        #infix portion
        def infixHelper(input): #infix to postfix concept from: https://www.youtube.com/watch?v=kKSENzdu7bE. Implementation is done solo
            
            infix = [] #infix = [10, '+', 20, '*', 2]
            numCreator = ''
            pointer = 0
            while pointer < len(input): #creating infix


                #validating arithmetic expression of infix:
                i = 0  #even indexes must be operands, odd indexes must be operators
                while i < len(infix):
                    if i % 2 == 0:
                        if type(infix[i]) != int:
                            raise AssertionError(f'invalid arithmetic expression: {input}')
                    else:
                        if infix[i] not in operators:
                            raise AssertionError(f'invalid arithmetic expression: {input}')
                    i += 1


                character = input[pointer]
                if character == ' ': #ignoring white spaces
                    pointer += 1
                    continue
                elif character.isnumeric(): #operand: add to numCreator
                    numCreator += character
                elif character in operators: #operator: add the complete integer and operator to infix array
                    if character == '-': #account for negative number:
                        if len(numCreator) > 0 and (-2**31) <= int(numCreator) <= (2**31-1): #checking num bounds. if character = '-': then we check if there is numCreator, if so then we know '-' is a minus sign, otherwise it is a negative sign
                            infix.append(int(numCreator))
                            numCreator = ''
                            infix.append('-')
                        else:
                            numCreator = '-' #else negative sign so we can add to the front of numCreator to make our next number negative
                    
                    elif len(numCreator) == 0: #validating arithmetic expression
                        raise AssertionError(f'invalid arithmetic expression: {input}')

                    elif (-2**31) <= int(numCreator) <= (2**31-1): #checking num bounds
                        if len(infix) > 0 and infix[-1] not in operators: #since we are adding operands and then operators, the previous index will always be an operator
                            raise AssertionError(f'invalid arithmetic expression: {input}')
                        infix.append(int(numCreator)) #join and add integers to infix
                        infix.append(character) #add operator to infix
                        numCreator = '' #resetting numCreator for the next number
                    else:
                        raise AssertionError(f'number: {numCreator} not between (-2^31) and (2^31-1)')
                else:
                    raise AssertionError(f'invalid arithmetic expression: {input}')
                pointer += 1

            if len(numCreator) > 0: #handles if last infix input is an integer(not an operator)
                infix.append(int(numCreator))
                numCreator = ''

            #once infix is completed, must validate one more time to see if last index is actually an operand or not
            if len(infix) > 0 and type(infix[-1]) != int: #if last index not an operand: invalid
                    raise AssertionError(f'invalid arithmetic expression: {input}')
                    
            return infix

# this is what i want postfix = [10, -2, 3, '/', 100, '*', '-', -6, '+']
        #infix to postfix using stack portion
        def postfixHelper(infix):
            s = stack() #stack used to store operators
            postfix = [] #postfix result
            highPrecedence = '*/'
            lowPrecedence = '+-'
            for i in infix:
                if type(i) == int: #add to postfix if integer
                    postfix.append(i)
                else: #else: operators
                    if s.isEmpty(): #if stack empty, append
                        s.push(i)
                    elif i in lowPrecedence: #perform operators from left to right: since operator is lowPrecendence, we need to perform most left operator regardless, thus pop from stack
                        while s.size() > 0: #pop all operators because i is lowPrecedence and most right operator currently
                            postfix.append(s.pop())
                        s.push(i) #push most right lowPrecedence operator
                    elif i in highPrecedence: 
                        if s.peek() in lowPrecedence: #perform highPrecedence operator before low, so we can just push to the top of stack
                            s.push(i)
                        else:
                            postfix.append(s.pop()) #if both are highPrecendence, perform most left, thus pop most left highPrecendence and append right operator to stack
                            s.push(i)
                
            while s.size() > 0: #empties remaining operators from stack to complete the postfix
                postfix.append(s.pop())
            
            return postfix


        def operatorHelper(n1, n2, op): #helper function to convert and perform operator strings
            if op == '+':
                return n1 + n2
            elif op == '-':
                return n1 - n2
            elif op == '*':
                return n1 * n2
            elif op == '/':
                return n1 / n2


        #arithmetic expression using stack portion
        def arithmeticExpression(postfix):
            resStack = stack()
            for i in postfix:
                if type(i) == int: #push to stack if integer
                    resStack.push(i)
                else: #pop last two integers to perform operator on
                    num2 = resStack.pop()
                    num1 = resStack.pop()
                    resStack.push(operatorHelper(num1, num2, i)) #call on helper to perform operation since operator is a string: '+', '*'...
            return resStack.pop() #once all operations are complete, the final(result) integer should be in stack


        #task2 will perform multiple inner function calls to return result
        return arithmeticExpression(postfixHelper(infixHelper(input))) 



    #**TASK 2 TESTING**
    # print(task2('6 + 2 - 4 / 6 * 14'))
    # print(6 + 2 - 4 / 6 * 14)
    # print(task2('10 - -2 / 3 * 100 +- 6 + 1 - 4'))
    # print((10 - -2 / 3 * 100 +- 6 + 1 - 4))
    # print(task2('10 - -2/3 * 100 +- 6'))
    # print(10 - -2/3 * 100 +- 6)
    # print(task2('-10 + -2'))
    # print(-10 + -2)

    #arithmetic expression tests
    # print(task2('10 + 2/')) #invalid
    # print(task2('10 +* 2')) #invalid
    # print(task2('10 +* ')) #invalid
    # print(task2('+ 2')) #invalid
    # print(task2('10 + -2-')) #invalid





    #**TASK 3 TESTING**
    # q = queue(3)
    # q.enqueue(1)
    # q.enqueue(2)
    # q.enqueue(3)
    # q.enqueue(4)
    # q.dequeue()
    # q.enqueue(4)
    # q.dequeue()
    # q.enqueue(5)
    # q.dequeue()
    # q.enqueue(6)
    # q.dequeue()
    # print('poll: ', q.poll())
    # print('size: ', q.size())
    # for i in range(3):
    #     print(q.q[i])



    #**TASK 4 TESTING**
    # q = StackWithTwoQs(5)
    # q.push(1)
    # q.push(2)
    # q.push(3)
    # q.pop()
    # q.pop()
    # q.push(4)
    # q.pop()
    # q.push(5)
    # q.push(6)
    # print(q.size())
    # print(q.peek())
    # for i in range(q.currSize):
    #     print(q.pop())
