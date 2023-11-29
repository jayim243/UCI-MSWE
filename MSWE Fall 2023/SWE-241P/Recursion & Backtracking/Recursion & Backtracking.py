# TASK 1
def task1(s1, s2):
    # backtrack brute force approach
    def backtrack(s): #// s = 'abc'
        perms = []
        if len(s) == 1: #base case: //returns 'c'
            return [s]

        for i in range(len(s)): #loops thru len(s): // s[i=0] = 'a', s[i=1] = 'b', s[i=2] = 'c'
            withoutI = s[:i] + s[i+1:] #every character before i and after i // withoutI = 'bc', withoutI = 'ac', withoutI = 'ab'

            for perm in backtrack(withoutI): #backtrack(withoutI) returns perms: ['bc', 'cb'], ['ac', 'ca'], ['ab', 'ba']
                perms.append(s[i] + perm) #// s[i]=a: 'a' + 'bc', 'a' + 'cb',   s[i]=b: 'b' + 'ac', 'b' + 'ca',   s[i]=c: 'c' + 'ab', 'c' + 'ba'

        return perms 

    if len(s1) == len(s2) == 0: #if s1 an s2 == ""
        return True
    for perm in backtrack(s1): #for each permutation of s1, we check if the permutation is in s2
        if perm in s2:
            return True
    return False


    # sliding window/hashmap approach
    # if len(s1) == len(s2) == 0:
    #     return True
    # left = 0
    # d1 = {}
    # for i in range(len(s1)):
    #     d1[s1[i]] = 1 + d1.get(s1[i], 0)
    # d2 = {}
    # for right in range(len(s2)):
    #     if sum(d2.values()) == len(s1):
    #         d2[s2[left]] -= 1
    #         if d2[s2[left]] == 0:
    #             del d2[s2[left]]
    #         left += 1
    #     d2[s2[right]] = 1 + d2.get(s2[right], 0)

    #     if d1 == d2:
    #         return True
    # return False



# TASK 2
def nQueens(line):    
    def isSafe(board, row, col):
        # rowSet = set() #checks safety for each row inside the column
        for r in range(len(board)):
            if board[r][col] == 1:
                return False
        
        # colSet = set() #checks safety for each column inside the row // don't need to check in terms of this problem
        if 1 in board[row]:
            return False

        # Check the diagonals: source chaptgpt
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)): #Top-Left to Bottom-Right
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row, len(board), 1), range(col, len(board), 1)): #Bottom-Left to Top-Right
            if board[i][j] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, len(board), 1)): #Top-Right to Bottom-Left
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row, len(board), 1), range(col, -1, -1)): #Bottom-Right to Top-Left
            if board[i][j] == 1:
                return False
            
        return True

        
    #backtracking for permutations of all valid boards
    def backtrack(board, row):
        if row == 8:
        # reached the end of board, so all queens are safe: add to solutions
            solutions.append([[1 if c == 1 else 0 for c in row] for row in board])
            return
        for col in range(8):
            if isSafe(board, row, col):
                board[row][col] = 1 #place queen
                backtrack(board, row + 1) #checks next row
                board[row][col] = 0 #backtracks by removing queen


    #board creation
    arr = line.split() #split input into array
    if len(arr) != 8:
        raise AssertionError('Length of input must equal 8')
    
    board = [[0 for c in range(8)] for r in range(8)] #building board to use backtrack on to find all valid boards
    board2 = [[0 for c in range(8)] for r in range(8)] #building given input board
    queen = 0 #queen counter to access arr[queen] to find out which column to place our next queen in
    for r in range(8):
        for c in range(8):
            if c == int(arr[queen])-1: #if col == queen, then update board with queen
                board2[c][r] = 1
        queen += 1 #increment queen counter 


    res = [] #hold steps from each valid board
    solutions = [] #holds all valid boards
    backtrack(board, 0) #backtracks to find all valid boards

    
    #my counting approach: after finding all valid boards, count the distance of queens vertically from given input to all valid boards
    for b in range(len(solutions)): #b = boards in solutions
        qPos = q2Pos = 0 #reset positions and step counts each game
        steps = 0
        for row in range(8): 
            qFound = q2Found = False #bool if both queens are found
            for col in range(8): 

                if board2[col][row] == 1 and not q2Found: #find position of queen on given input board
                    q2Pos = col
                    q2Found = True
                if solutions[b][col][row] == 1 and not qFound: #find position of queen on one of the valid boards
                    qPos = col
                    qFound = True
                if board2[col][row] == solutions[b][col][row] == 1: #if they are at the same spot, no need to move
                    qFound = q2Found = False #set found to False so steps does not increment
                # if (qFound and not q2Found) or (q2Found and not qFound): #entering next row, have to reset founds
                #     qFound = q2Found = False 
            if qFound and q2Found: #after going through all vertical spaces, add absolute difference between queens to steps
                steps += 1

            
        res.append(steps) #at the end of each game, add all steps taken from the game to res
    
    return min(res) #return smallest(quickest) steps of all valid boards from given input b oard

    



if __name__ == "__main__":
    # testing task 1
    print(task1(s1 = "ab", s2 = "eidbaooo")) #true
    print(task1(s1 = "ab", s2 = "3eidboaoo")) #false
    # print(task1(s1 = "", s2 = "")) #true
    # print(task1(s1 = " ", s2 = " ")) #true
    # print(task1(s1 = " a", s2 = " a")) #true
    # print(task1(s1 = " ", s2 = " a")) #true
    # print(task1(s1 = " a", s2 = " ")) #false
    # print(task1(s1 = " a ", s2 = "a  a  ")) #true


    # testing nQueens
    print(nQueens('6 4 7 1 8 2 5 3')) #0
    print(nQueens('1 2 3 4 5 6 7 8')) #7
    print(nQueens('1 1 1 1 1 1 1 1')) #7
    # print(nQueens('2 3 5 7 1 8 2 6 ')) #3
    # print(nQueens('3 4 6 5 7 1 2 8')) #5
    # print(nQueens('8 7 6 5 4 3 2 1')) #7

    # print(nQueens('1 2 3 4 5 6 7 8 9')) #assertion
    # print(nQueens('                 ')) #assertion
    # print(nQueens('')) #assertion