#**TASK 1**
def task1(nums, target):   
    if type(target) != int:
        raise AssertionError('target must be an integer')
    leftMost = rightMost = -1 #return values: defaulted at -1 if we do not find a target
    l, r = 0, len(nums)-1
    while l <= r:
        m = (l+r)//2
        if target > nums[m]:
            l = m+1 
        elif target < nums[m]:
            r = m-1
        else: #"a target" found
            leftMost = m
            r = m-1 #keep looking to the left to see if m is already the left most

    # # second binary search to find right most
    l, r = 0, len(nums)-1
    while l <= r:
        m = (l+r)//2
        if target > nums[m]:
            l = m+1 
        elif target < nums[m]:
            r = m-1
        else: #"a target" found
            rightMost = m
            l = m+1 #look to the right to see if it is right most
    return [leftMost, rightMost]
    # runtime complexity: O(log n) + O(log n) = 2O(log n) or just O(log n)



#**TASK 2**
def task2(matrix, target):
    l, r = 0, len(matrix)-1 #binary search
    while l <= r:
        m = (l+r)//2
        if len(matrix[m]) < 1:
            raise AssertionError('One or more matrixes are empty')
        if target < matrix[m][0]: #if target is less than smallest number in inner matrix, we move r
            r = m-1
        elif target > matrix[m][-1]: #if target is greater than biggest number in inner matrix, we move l
            l = m+1

        # if target is between the smallest and biggest number in inner matrix, we perform inner binary search
        elif matrix[m][0] <= target <= matrix[m][-1]: 
            j, k = 0, len(matrix[m])-1 #binarch search 2
            innerMatrix = matrix[m] #regular array = [1, 2, 3, 4, 5]
            while j <= k:
                m2 = (j+k)//2
                if target < innerMatrix[m2]:
                    k = m2-1
                elif target > innerMatrix[m2]:
                    j = m2+1
                else: #target == innerMatrix[m2] so we can return True
                    return True
            return False #if while loop breaks and did not return True, that means target not found
    return False
    # runtime complexity: log(m) * log(n) == O(log(m*n)))



if __name__ == "__main__":
    print(task1(nums = [4,9,10,13,17,17,19,21], target = 17)) #output: [4, 5]
    print(task1(nums = [2,4,6,8,10,14,16], target = 12)) #output: [-1, -1]
    print(task1(nums = [], target = 0)) #output: [-1, -1]
    # print(task1(nums = [], target = '0')) #error

    print(task2(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3)) #true
    print(task2(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13)) #false
    # print(task2(matrix = [], target = 0)) #false
    # print(task2(matrix = [[],[],[]], target = 0)) #error