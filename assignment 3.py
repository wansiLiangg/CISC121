
'''
This program is for CISC 121 assignment 3

Author: Wansi Liang
Student number: 20067725
'''

'''
Question 1: print numbers
'''
def printNums(nums):
    nums = str(nums)
    if len(nums) == 0: #base -- when the length of nums equal to zero
        return nums
    print(nums[0])
    printNums(nums[1:])

'''
Question 2: count vowels & print new string
'''
def numVowels(word):
    if len(word) == 0: #base -- when the length of word equal to zero
        return 0
    elif word[0] in ["a", "e", "i", "o", "u"]: #when the alphabet is a vowel
        return 1 + numVowels(word[1:])
    else:  
        return 0 + numVowels(word[1:])

#printing a new word without vowels
def remVowels(word):
    if len(word) == 0: #base -- when the length of word equal to zero
        return word
    else: 
        newWord = word[1:]
        if word[0] in ["a", "e", "i", "o", "u"]: #when the alphabet is a vowel
            return remVowels(newWord)
        else:
            return word[0] + remVowels(newWord) #printing the new word

'''
Question 3: find the specific product by splitting the list in half, and then multiply them together
'''
def multiply(n, m):
    mid = (n+m)//2 #getting the middle number
    if n > m: 
        return None
    if n == m:
        return m
    return multiply(n, mid) * multiply(mid+1, m)   

'''
Question 4: switch position
'''
def swapNeighbours(aList):
    if len(aList) < 2: #base -- when the number of elements in the list is less than 2
        return aList
    else: 
        return [aList[1], aList[0]] + swapNeighbours(aList[2:])
        
'''
Question 5: compare two lists
'''
def checkLists(bList, cList):
    if len(cList) != len(bList): #when bList does not contain the same number of elements in cList
        return False
    if len(bList) == len(cList) == 0: #when bList has the same elements as cList
        return True
    if bList[0] != cList[0]: #when the first element of bList is not equal to the first element in cList
        return False
    return checkLists(bList[1:], cList[1:])

'''
This function is testing all the functions above
'''
def tester(): 
    printNums(54321)
    print()
    printNums(987)
    print()
    printNums(4)
    print()
    print(numVowels("mnsty"))
    print(numVowels(""))
    print(numVowels("annn"))
    print(numVowels("nnnnna"))
    print(numVowels("canoe"))
    print(remVowels("mnsty"))
    print(remVowels(""))
    print(remVowels("annn"))
    print(remVowels("nnnnna"))
    print(remVowels("canoe")) 
    print(multiply(4, 7)) 
    print(multiply(2, 10))
    print(multiply(8, 2))
    print(swapNeighbours([2,3,4]))
    print(swapNeighbours([1])) 
    print(swapNeighbours([4,5,6,7])) 
    print(swapNeighbours([])) 
    print(checkLists([],[]))
    print(checkLists([2,5,7],[2,5,7]))
    print(checkLists([7,8,3],[7,8,2])) 
    print(checkLists([2,2],[2,2,2])) 
    print(checkLists([1],[1])) 
    print(checkLists([],[]))

tester()

'''
Part 2 -- complexity
'''
def find_max_a(lis):
     if len(lis) == 0: #O(2) -- get the length of lis and compare with 0
             return None #O(1) -- return None
     else:
            m = lis[0] #O(1) -- assign m
            for i in range(1, len(lis)): #O(n) -- run N times
                   if lis[i] > m: #O(2) -- get the i element from lis and compare it with m
                     m = lis[i] #O(1) -- assign m
            return m #O(1) -- return m
    #Therefore, the complexity of the function is O(n)
    
    

