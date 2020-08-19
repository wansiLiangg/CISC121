
'''
This program is for CISC 121 assignment 2

Author: Wansi Liang
Student number: 20067725
'''

'''
This function is getting commands from the file
'''
def readFile(fileName = "PATH_TO_FILE.txt"):
    commandFile = open(fileName, "r")
    commandList = {}    #create a linked list
    ptr = commandList
    for l in commandFile:
        job = l.split()
        ptr["data"] = job  #adding information line by line to the linked list
        ptr["next"] = {}
        ptr = ptr["next"]
    return commandList

'''
This function is to get the length of the command list
'''
def length(commandList): 
    ptr = commandList
    number = 0
    while ptr != {}:
        ptr = ptr["next"]
        number = number + 1
    return number

'''
This function is adding jobs to a new linked list
'''
def received(ptr, linkedList):
    ptrN = linkedList
    while ptrN != {}: #getting the correct possition -- adding node to the end of the linked list
        ptrN = ptrN["next"]
    ptrN["data"] = ptr["data"]
    ptrN["next"] = {}
    print("Adding order", ptr["data"][1], "to the queue.", ptr["data"][2], "is the priority of the call. Job", ptr["data"][1], "is", ptr["data"][3], "type")
    return linkedList 

'''
This function is showing there are how many jobs left and the average of priority of these jobs
'''
def show(linkedList):
    ptr = linkedList
    number = 0
    total = 0
    while ptr != {}: #run through the whole list
        total = total + int(ptr["data"][2]) #getting the total priority 
        ptr = ptr["next"]
        number = number + 1 #calculating how many jobs in the list
    average = total / number #calculating the average of priority
    print("There are", number, "jobs currently in the queue. The average priority of all of the calls is", average)

'''
This function is showing the details of a specific job
'''
def details(ptr, linkedList):
    ptrN = linkedList
    while ptrN["data"][1] != ptr["data"][1]: #getting the specific job from the list
        if ptrN != {}:
            ptrN = ptrN["next"]
        else: #if the job is not in the list
            print(ptr["data"][1], "is not in list")
            return linkedList
    print("Call ID:", ptrN["data"][1], ", priority:", ptrN["data"][2], ", type:", ptrN["data"][3])

'''
This function is used to modify the priority
'''
def modify(ptr, linkedList):
    ptrN = linkedList
    while ptrN["data"][1] != ptr["data"][1]: #getting the specific job from the list
        if ptrN["next"] != {}:
            ptrN = ptrN["next"]
        else: #if the job is not in the list
            print(ptr["data"][1], "is not in list")
            return linkedList
    ptrN["data"][2] = ptr["data"][2] #modifying the priority
    return linkedList

'''
This function is showing the completed job
'''
def respond(linkedList):
    ptrN = linkedList
    print("Responding to job", ptrN["data"][1])
    ptrN = ptrN["next"] #remove the first node of the list
    if ptrN == {}: #if there is no job left
        print("No current emergencies -- time for a coffee break!")
    return ptrN

'''
This function is showing all the uncompleted jobs in the list and their type
'''
def statistics(linkedList):
    ptrN = linkedList
    while ptrN != {}: #run through the whole list
        print("Call ID:", ptrN["data"][1], ", job type:", ptrN["data"][-1])
        ptrN = ptrN["next"]

'''
This functiton is removing a specific job from the list
'''
def remove(linkedList, ptr):
    ptrN = linkedList
    if ptrN["data"][1] == ptr["data"][1]: #when the job is located at the first node
        ptrN = ptrN["next"] #remove the first node
        return ptrN
    else:
        while ptrN["next"]["data"][1] != ptr["data"][1]: #getting the specific node position
            if ptrN["next"] != {}:
                ptrN = ptrN["next"]
            else: #if the node is not in the list
                print(ptr["data"][1], "is not in list")
                return ptrN
        print("ID", ptr["data"][1], "has been removed")
        ptrN["next"] = ptrN["next"]["next"]
        return linkedList
    
    
'''
This function is used to combine all the functions above
'''
def main():
    commandList = readFile(fileName = "PATH_TO_FILE.txt") #getting all the commands and store them in a linked list
    number = length(commandList) #getting the length of the command list
    ptr = commandList 
    linkedList = {} #create a new linked list to complete all the commands
    for i in range(number): #go through all the commands
        if ptr["data"][0] == "received": #when the command is "received"
            received(ptr, linkedList)
        elif ptr["data"][0] == "show": #when the command is "show"
            show(linkedList)
        elif ptr["data"][0] == "details": #when the command is "details"
            details(ptr, linkedList)
        elif ptr["data"][0] == "modify": #when the command is "modify"
            modify(ptr, linkedList)
        elif ptr["data"][0] == "respond": #when the command is "respond"
            linkedList = respond(linkedList)
        elif ptr["data"][0] == "statistics": #when the command is "statistics"
            statistics(linkedList)
        elif ptr["data"][0] == "remove": #when the command is "remove"
            linkedList = remove(linkedList, ptr)
        ptr = ptr["next"]
main()
