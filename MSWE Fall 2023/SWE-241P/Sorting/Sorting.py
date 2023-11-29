import random
def groupAnagram(array):
    d = {} #dictionary where keys are anagrams and values are lists of strings. We can append to the list of strings when we get a new anagram
    for i in array:
        anagram = sortString(i) #for each word, we call sortString method to receive a sorted anagram
        if anagram not in d:
            d[anagram] = [i]
        else:
            d[anagram].append(i)
    return list(d.values()) #all the anagram buckets will be stored in our dictionary


def sortString(str):
    # merge sort section
    def merge(left, right): #O(n) time complexity // merging each subarrays together takes n time
        #O(n) space complexitiy // need array of space n for each merge
        res = [0] * (len(left) + len(right)) #using array to store the sorted string because strings are immutable
        i = j = k = 0 # i pointer for left half, j pointer for right half, k pointer for res array
        while i < len(left) and j < len(right):
            if left[i] < right[j]: #comparing left half and right half
                res[k] = left[i]
                i += 1
            else:
                res[k] = right[j]
                j += 1
            k += 1
        while i < len(left): #if we have left or right half remaining, we append to our res array
            res[k] =  left[i]
            i += 1
            k += 1
        while j < len(right):
            res[k] =  right[j]
            j += 1
            k += 1
        return res
    

    def mergeSort(str): #O(log n) time complexity // splitting array by halves at each recursive level
        if len(str) <= 1: 
            return str
        m = len(str) // 2
        left, right = mergeSort(str[:m]), mergeSort(str[m:]) #recursive call to keep dividing str in halves
        return merge(left, right) #sorting each half and merging together
            
    return "".join(mergeSort(str)) #convert array back to str



    #quick sort section
    #quick sort source code: https://www.youtube.com/watch?v=9KBwdDEwal8
    # def quickSort(arr, left, right): #O(n log n) time complexitiy given pivot is properly chosen assuming random shuffle uniformally distributes array
    #     if left < right:
    #         pivot = partition(arr, left, right) #partition function gets index of pivot in the array
    #         #O(log n) space complexity // storing each left and right sort onto call stack, but could result in O(n) worst case time if pivot is chosen poorly
    #         quickSort(arr, left, pivot-1) #quick sorting left // from 0 to pivot
    #         quickSort(arr, pivot+1, right) #quick sorting right // from pivot to end of array
        

    # def partition(arr, left, right):
    #     i, j = left, right-1
    #     pivot = arr[right] #partitioning based on last index of randomized array
    #     while i < j:
    #         while i < right and arr[i] < pivot:
    #             i += 1
    #         while j > left and arr[j] > pivot:
    #             j -= 1
    #         if i < j:
    #             arr[i], arr[j] = arr[j], arr[i]
    #     if arr[i] > arr[right]:
    #         arr[i], arr[right] = arr[right], arr[i]
    #     return i

    # s = sorted(str) #randomize shuffle
    # random.shuffle(s)
    # quickSort(s, 0, len(s)-1)
    # return "".join(s)



if __name__ == "__main__":
    print(groupAnagram(["bucket","rat","mango","tango","ogtan","tar"]))
    print(groupAnagram([""]))
    print(groupAnagram(["a"]))