
'''
This program is for CISC 121 assignment 4

Author: Wansi Liang
Student number: 20067725
'''

'''
Build a binary search tree
'''
def createTree(fileName = "tree.txt"):
    tree = None
    file = open(fileName, "r")
    for i in file:
        i = i.replace(",", " ").split()
        i = [int(i[0])] + [float(j) for j in i[1:]]
        tree = insertTree(tree, i)   #insert values into the tree
    return tree

def insertTree(tree, value):    #This function is inserting values into the tree
    if tree == None:    #when the tree is empty
        return {"data":value, "left":None, "right":None}
    elif value < tree["data"]:  #when the value is less than the existing value
        tree["left"] = insertTree(tree["left"], value)
        return tree
    elif value > tree["data"]:  #when the value is greater than the existing value
        tree["right"] = insertTree(tree["right"], value)
        return tree
    else:
        return tree

'''
The first question -- add a new node to the tree
'''
def addNode(tree):  #This function is adding a new hotel and the hotel's marks
    hotelNum = enterHotelNum()  #asking for hotel number
    if searchTree(tree, hotelNum) == False:
        value = [hotelNum] + hotelInfo()
        insertTree(tree, value)     #adding new information 
        print("The information is added")

def enterHotelNum():  #This function is asking for hotel number and checking if the hotel number is eligible
    flag = False
    while not flag:
        hotelNum = int(input("Please enter a 4 digits hotel number "))
        try:
            if len(str(hotelNum)) != 4:   #when the hotel number is not a 4 digits number
                raise ValueError
            return hotelNum
            flag = True
        except ValueError:
            print("You entered an invalid hotel number")
                
def searchTree(tree, value):    #This function is searching if the hotel number is in the tree
    if tree == None:    #when the tree is empty
        return False
    elif tree['data'][0] == value:  #when the value is found
        return True
    elif tree['data'][0] > value:   #when the value is less than the existing value
        return searchTree(tree['left'], value)
    elif tree['data'][0] < value:   #when the value is greater than the existing value
        return searchTree(tree['right'], value)
    return False

def hotelInfo():  #This function is asking for new hotel's marks
    markList = []   #create a list to store all the marks
    
    #mark for location
    flag1 = False
    while not flag1:
        mark1 = float(input("Please enter the mark for location which is out of 25 "))
        try:
            if mark1 < 0 or mark1 >25:  #checking if the mark is within the range
                raise ValueError
            flag1 = True
        except ValueError:
            print("You entered an invalid mark")
    markList.append(mark1)

    #mark for reputation
    flag2 = False
    while not flag2:
        mark2 = float(input("Please enter the mark for reputation which is out of 25 "))
        try:
            if mark2 < 0 or mark2 >25:  #checking if the mark is within the range
                raise ValueError
            flag2 = True
        except ValueError:
            print("You entered an invalid mark")
    markList.append(mark2)

    #mark for cleanliness and comfort
    flag3 = False
    while not flag3:
        mark3 = float(input("Please enter the mark for cleanliness and comfort which is out of 15 "))
        try:
            if mark3 < 0 or mark3 >15:  #checking if the mark is within the range
                raise ValueError
            flag3 = True
        except ValueError:
            print("You entered an invalid mark")
    markList.append(mark3)

    #mark for amenities
    flag4 = False
    while not flag4:
        mark4 = float(input("Please enter the mark for amenities which is out of 20 "))
        try:
            if mark4 < 0 or mark4 >20:  #checking if the mark is within the range
                raise ValueError
            flag4 = True
        except ValueError:
            print("You entered an invalid mark")
    markList.append(mark4)

    #mark for price
    flag5 = False
    while not flag5:
        mark5 = float(input("Please enter the mark for price which is out of 20 "))
        try:
            if mark5 < 0 or mark5 >20:  #checking if the mark is within the range
                raise ValueError
            flag5 = True
        except ValueError:
            print("You entered an invalid mark")
    markList.append(mark5)

    #mark for luxury
    flag6 = False
    while not flag6:
        mark6 = float(input("Please enter the mark for luxury which is out of 35 "))
        try:
            if mark6 < 0 or mark6 >35:  #checking if the mark is within the range
                raise ValueError
            flag6 = True
        except ValueError:
            print("You entered an invalid mark")
    markList.append(mark6)

    #mark for overall average satisfaction of guests
    flag7 = False
    while not flag7:
        mark7 = float(input("Please enter the mark for overall average satisfaction of guests which is out of 65 "))
        try:
            if mark7 < 0 or mark7 >65:  #checking if the mark is within the range
                raise ValueError
            flag7 = True
        except ValueError:
            print("You entered an invalid mark")
    markList.append(mark7)

    return markList

'''
The second question -- find average
'''
def option():   #This function is asking for the user which average does the user want to check
    print("Please choose one of the following option")
    print("1) Location")
    print("2) Reputation")
    print("3) Cleanliness and comfort")
    print("4) Amenities")
    print("5) Price")
    print("6) Luxury")
    print("7) Overall average satisfaction")
    flag = False
    while not flag:
        choice = int(input("Please enter an integer "))
        try:
            if choice not in [1, 2, 3, 4, 5, 6, 7]:     #checking if the choice valid
                raise ValueError
            else:
                return choice
        except ValueError:
            print("You entered an invalid integer")

def sumMarks(tree, choice):     #This function is calculating the sum of the specific position of marks
    if tree == None:
        return 0
    else:   #when the tree is not empty
        return tree["data"][choice] + sumMarks(tree["right"], choice) + sumMarks(tree["left"], choice)

def countNode(tree):    #This function is counting how many hotels have mark at that position
    counter = 0
    if tree == None:
        return 0
    else:   #when the tree is not empty
        counter = counter+1 + countNode(tree["right"]) + countNode(tree["left"])
        return counter
                
def average(tree):  #This function is calculating the average of the specific position of marks
    total = ["hotelNum", 25, 25, 15, 20, 20, 35, 65]
    position = ["hotelNum", "location", "reputation",  "cleanliness and comfort", "amenities", "price", "luxury", "overall average satisfaction"]
    choice = option()
    Sum = sumMarks(tree, choice)
    counter = countNode(tree)
    avg = (Sum / counter) / total[choice] * 100     
    print("The average is", avg)

'''
The third question -- prompt the user for a criterion
'''
def userMark(choice): #This function is asking for the minimum acceptable score
    if choice in [1, 2]:
        flag = False
        while not flag:
            mark = float(input("Please enter the minimum acceptable score which is out of 25: "))
            try:
                if mark < 0 or mark >25:  #checking if the mark is within the range
                    raise ValueError
                flag = True
            except ValueError:
                print("You entered an invalid mark")
    
    elif choice == 3:
        flag = False
        while not flag:
            mark = float(input("Please enter the minimum acceptable score which is out of 15: "))
            try:
                if mark < 0 or mark >15:  #checking if the mark is within the range
                    raise ValueError
                flag = True
            except ValueError:
                print("You entered an invalid mark")

    elif choice in [4, 5]:
        flag = False
        while not flag:
            mark = float(input("Please enter the minimum acceptable score which is out of 20: "))
            try:
                if mark < 0 or mark >20:  #checking if the mark is within the range
                    raise ValueError
                flag = True
            except ValueError:
                print("You entered an invalid mark")

    elif choice == 6:
        flag = False
        while not flag:
            mark = float(input("Please enter the minimum acceptable score which is out of 35: "))
            try:
                if mark < 0 or mark >35:  #checking if the mark is within the range
                    raise ValueError
                flag = True
            except ValueError:
                print("You entered an invalid mark")

    else:
        flag = False
        while not flag:
            mark = float(input("Please enter the minimum acceptable score which is out of 65: "))
            try:
                if mark < 0 or mark >65:  #checking if the mark is within the range
                    raise ValueError
                flag = True
            except ValueError:
                print("You entered an invalid mark")

    return mark

def searchMin(choice, mark, tree): #This function is searching for hotels which achieve the minimum acceptable score
    if tree == None:
        return ""
    elif (tree["data"][choice]) > mark: #the specific mark is greater than the minimum acceptable score
        print("Hotel ID:", tree["data"][0], "'s", choice, "score achieves your minimum acceptable score")
        return searchMin(choice, mark, tree["right"]) + searchMin(choice, mark, tree["left"])
    else:
        return searchMin(choice, mark, tree["right"]) + searchMin(choice, mark, tree["left"])
    
def userCriterion(tree):
    choice = option()
    mark = userMark(choice)
    searchMin(choice, mark, tree)
    
'''
The forth question -- count how many hotels got less than 70% on the 'overall average satisfaction of guests' criteria
'''
def under70(tree):   #This function is counting how many hotels got less than 70% on the 'overall average satisfaction of guests' criteria
    counter = 0
    if tree == None:
        return 0
    elif (tree["data"][7]/65) < 0.7:    #hotels got less than 70%
        counter = counter+1 + under70(tree["right"]) + under70(tree["left"])
    else:   #hotels got more than 70%
        counter = counter + under70(tree["right"]) + under70(tree["left"])
    return counter

def result(tree):   #This function is representing the result 
    counter = under70(tree)
    print("There are", counter, "hotels less than 70% on the 'overall average satisfaction of guests' criteria")

'''
The fifth question -- marks for a particular hotel
'''
def printNode(tree, value):     #This function is similar with searchTree function, but this function record the information from the specific node
    if tree == None:
        return False
    elif tree['data'][0] == value:
        return tree["data"]     #keeping the information 
    elif tree['data'][0] > value:
        return printNode(tree['left'], value)
    elif tree['data'][0] < value:
        return printNode(tree['right'], value)
    return False

def hotelMarks(tree):     #This function is checking if the hotel is in the list and representing marks of the specific hotel
    #checking if the hotel is in the tree
    flagHotel = False
    while not flagHotel:
        try:
            hotelNum = enterHotelNum()
            if searchTree(tree, hotelNum) == False:   #when the hotel is in the list
                raise ValueError
            flagHotel = True
        except ValueError:  #when the hotel is not in the list
            print("This hotel does not exist")

    #representing marks
    result = printNode(tree, hotelNum)
    if result == False:
        print("This hotel does not exist")
    else:
        print("Marks for hotel", hotelNum, ":")
        print("Location is", result[1], "out of 25")
        print("Reputation is", result[2], "out of 25")
        print("Cleanliness and comfort is", result[3], "out of 15")
        print("Amenities is", result[4], "out of 20")
        print("Price is", result[5], "out of 20")
        print("Luxury is", result[6], "out of 35")
        print("Overall average satisfaction of guests is", result[7], "out of 65")
        
'''
menu -- asking user for their option
'''
def menu(tree):     #This function is a menu function that asking what does the user want to do
    keepGoing = "yes"
    print("Welcome to the program")
    print("There are 5 options")
    while keepGoing == "yes":   #when the user want to keep using the program
        print("1) Add a new hotel and that hotel's marks")
        print("2) Find the average of one of the marks")
        print("3) Prompt the user for a criterion")
        print("4) Count the number of hotel got less than 70% on the 'overall average satisfaction of guests'")
        print("5) Look up the marks for a particular hotel")
        number = int(input("Please enter an integer for your option "))     #asking which function does the user want to use
        if number == 1:     
            addNode(tree)
        elif number == 2:
            average(tree)
        elif number == 3:
            userCriterion(tree)
        elif number == 4:
            result(tree)
        elif number == 5:
            hotelMarks(tree)
        else:   #when the user entered an invalid number
            print("You entered an invalid number")
            
        keepGoing = input("Please enter 'yes' if you want to keep using the program, or enter others to exit ")     #asking if the user want to keep running the program

    print("Thanks for using")   

def main():
    tree = createTree()
    print(tree)
    #menu(tree)

main()
