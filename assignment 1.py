
'''
This program is for CISC 121 assignment 1

Author: Wansi Liang
Student number: 20067725
'''

import random

'''
This function loads the set of puzzles into the program.
'''

def loadPuzzles(filename='wordblitzclues.txt'):
    fileClues = open(filename,'r')
    lisClues = []
    for line in fileClues:
        lisClues.append(line.rstrip()) #rstrip strips all chars from the end of the string.
    fileClues.close()
    return lisClues

'''
This function loads a random puzzle from the list of puzzles.
Removes any extra tabs that may be in the imported clue or word.
'''

def getRandomPuzzle(puzzleLis):
    randomIndex = random.randint(1,len(puzzleLis)-1)
    puzzle = puzzleLis[randomIndex].split('\t')
    for extraTab in puzzle:
        if extraTab == '':
            puzzle.remove('')
    puzzleClue = puzzle[0]
    secretWord = puzzle[1]
    return puzzleClue,secretWord

'''
Prints out 4 random puzzles at a time for demo purposes
'''

def puzzle():
    aList = []
    for i in range(1):
        puzzleLis = loadPuzzles() #Loads the puzzles into the program.
        puzzleClue,secretWord = getRandomPuzzle(puzzleLis) #Selects a random puzzle
        print("This is the clue:  " + str(puzzleClue)) 
        secretWord = secretWord.lower()
        for i in range(len(secretWord)): #split the secretWord and store each letter in a list
            aList.append(secretWord[i])
            i = i + 1
    return aList

'''
Asking the user wants to play with computer or huamn
'''

def start():
    flag = False
    while not flag:
        choice = input("Which one do you want to play with? Computer or human. Please enter 'computer' or 'human' ")
        if choice == "computer":
            flag = True
        elif choice == "human":
            flag = True
        else:
            print("You entered an invalid option")
            flag = False
    return choice

'''
Verifying if the user entered a valid word
'''

def name(choice):
    if choice == "human":
        nameC = input("Please enter another player's name: ")
    else:
        nameC = "computer"
    return nameC

'''
Asking which of the following option the user wants to choose and verifying if the user entered a valid number
'''

def option():
    flag = False
    while not flag: 
        print("1) Spin the wheel")
        print("2) Buy a vowel -- worth $25")
        print("3) Guess the word")
        print("4) Quit the game")
        num = int(input("Please enter a number for selecting your option "))
        try:
            if num > 4 or num < 1:
                raise ValueError
            flag = True
        except ValueError:
            print("You entered an invalid number")
    return num

'''
Random option for computer
'''

def optionC():
    print("1) Spin the wheel")
    print("2) Buy a vowel -- worth $25")
    print("3) Guess the word")
    print("4) Quit the game")
    numC = random.randint(1,2)
    print("Computer's option is", numC)
    return numC

'''
Option 1 for user
'''    
def spinP(wordList, nameO, nameP, length):
    con = ""
    numOfConP = 0
    aList = [] 
    positionList = []
    number = random.randint(0,21) #how much money does the user get
    if number == 0: #reset the money to zero
        print("Bankruptcy! Your money is reset to zero and your turn is over")
    elif number == 21: #round changed
        print("You lose your turn!")
    else:
        print("You get $", number)
        con = consonant() #asking for consonant
        con = con.lower()
        if con in wordList: 
            numOfConP = wordList.count(con) #how many position is replaced by the consonant
            for i in range(numOfConP): 
                wordPositionP = wordList.index(con) #showing the consonant's position(s)
                positionList.append(wordPositionP) #storing the position(s) of the consonant in the word
                wordList[wordPositionP] = " "   #replace the consonant's position(s) in the word by a space
        else:
            print("consonant '", con, "' not in the word") #when the consonant is not in the word, round changed
            number = 21
    aList.append(number)
    aList.append(positionList)
    aList.append(numOfConP)
    aList.append(con)
    return aList

'''
Option 1 for another player
'''

def spinO(wordList, nameO, nameP):
    con = ""
    numOfConO = 0
    aList = []
    positionList = []
    number = random.randint(0,21)
    if number == 0:
        print("Bankruptcy! Your money is reset to zero and your turn is over")
    elif number == 21:
        print("You lose your turn!")
    else:
        print("You get $", number)
        con = consonant()
        con = con.lower()
        if con in wordList:
            numOfConO = wordList.count(con)
            for i in range(numOfConO): 
                wordPositionO = wordList.index(con)
                positionList.append(wordPositionO)
                wordList[wordPositionO] = " "
        else:
            print("consonant '", con, "' not in the word")
            number = 21
    aList.append(number)
    aList.append(positionList)
    aList.append(numOfConO)
    aList.append(con)
    return aList

'''
Option 1 of computer
'''

def spinC(wordList, nameO, nameP):
    conC = ""
    numOfConC = 0
    aList = []
    positionList = []
    number = random.randint(0,21)
    if number == 0:
        print("Bankruptcy! Your money is reset to zero and your turn is over")
    elif number == 21:
        print("You lose your turn!")
    else:
        print("You get $", number)
        conC = consonantC()
        conC = conC.lower()
        if conC in wordList:
            numOfConC = wordList.count(conC)
            for i in range(numOfConC): 
                wordPositionC = wordList.index(conC)
                positionList.append(wordPositionC)
                wordList[wordPositionC] = " "
        else:
            print("consonant '", conC, "' not in the word")
            number = 21
    aList.append(number)
    aList.append(positionList)
    aList.append(numOfConC)
    aList.append(conC)
    return aList

'''
Verifying if the user and player entered a valid consonant
'''

def consonant():
    flag = False
    while not flag:
        con = input("Please pick a consonant: ")
        if con in ["a", "e", "i", "o", "u"]:
            print("You entered a vowel")
            flag = False
        else:
            if len(con) == 1: 
                flag = True
            else:
                print("You entered more than one consonant")
                flag = False
    return con
'''
Random consonant for computer
'''

def consonantC():
    conC = random.choice("qwrtypsdfghjklzxcvbnm")
    return conC

'''
Option 2 for user and player
'''

def option2(wordList):
    numOfVP = 0
    aList = []
    positionList = []
    v = vowel()
    v = v.lower()
    if v in wordList:
        numOfVP = wordList.count(v)
        for i in range(numOfVP): 
            wordPositionP = wordList.index(v)
            positionList.append(wordPositionP)
            wordList[wordPositionP] = " "
    else:
        print("vowel '", v, "' not in the word")
    aList.append("")
    aList.append(positionList)
    aList.append(numOfVP)
    aList.append(v)
    return aList

'''
Option 2 for computer
'''

def option2C(wordList):
    numOfVC = 0
    aList = []
    positionList = []
    vC = vowelC()
    vC = vC.lower()
    if vC in wordList:
        numOfVC = wordList.count(vC)
        for i in range(numOfVC): 
            wordPositionC = wordList.index(vC)
            positionList.append(wordPositionC)
            wordList[wordPositionC] = " "
    else:
        print("vowel '", vC, "' not in the word")
    aList.append("")
    aList.append(positionList)
    aList.append(numOfVC)
    aList.append(vC)
    return aList

'''
Verifying if the user and player entered an valid vowel
'''

def vowel():
    flag = False
    while not flag:
        v = input("Please pick a vowel: ")
        if v not in ["a", "e", "i", "o", "u"]:
            print("You entered a consonant")
            flag = False
        else:
            if len(v) == 1: 
                flag = True
            else:
                print("You entered more than one vowel")
                flag = False
    return v

'''
Random vowel for computer
'''

def vowelC():
    vC = random.choice("aeiou")
    return vC

'''
Option 3 for user
'''

def guessP(wordList, nameO, nameP, length, com):
    word = input("Please enter the word you guess ")
    if len(word) == len(wordList): #verifying if the length of entered word is the same as secretWord
        for i in range(len(word)):
            if word[i] == wordList[i]: #verifying if the word entered is the same as secretWord
                i = i + 1
            else:
                print("The word you guess is incorrect")
                if com == "c":  #if another player is computer
                    gameC(nameO, nameP, wordList, length, com)
                else: 
                    gameO(nameO, nameP, wordList, length, com)
        print("Congratulations! You win the game!")
        print("Thanks for playing!")
        exit()
    else:
        print("The word you guess is incorrect")
        if com == "c":
            gameC(nameO, nameP, wordList, length,com)
        else: 
            gameO(nameO, nameP, wordList, length, com)
    return word

'''
Option 3 for player
'''

def guessO(wordList, nameO, nameP, length, com):
    word = input("Please enter the word you guess ")
    if len(word) == len(wordList): 
        for i in range(len(word)):
            if word[i] == wordList[i]:
                i = i + 1
            else:
                print("The word you guess is incorrect")
                gameP(nameP, nameO, wordList, length, com)
        print("Congratulaitons! You win the game!")
        print("Thanks for playing!")
        exit()
    else:
        print("The word you guess is incorrect")
        gameP(nameP, nameO, wordList, length, com)
    return word

'''
Game body for user
'''

def gameP(nameP, nameO, wordList, length, com):
    counterP = 0 #money in each round
    counterPT = 0   #money in total game
    print("It's", nameP, "'s turn!")
    print(nameP, "'s balance in this round is", counterP)
    print(nameP, "'s balance in total is", counterPT)
    num = option() #asking for option
    while num != 4:
        counterP = 0
        if num == 1: #otpion 1
            aList = spinP(wordList, nameO, nameP, length) #asking for consonant
            if int(aList[0]) == 0: #bankruptcy
                counterP = 0
                if num != 4:
                    if com == "c":
                        gameC(nameO, nameP, wordList, length, com)
                    else: 
                        gameO(nameO, nameP, wordList, length, com)
            elif int(aList[0]) == 21: #lose a turn
                if num != 4:
                    if com == "c":
                        gameC(nameO, nameP, wordList, length, com)
                    else: 
                        gameO(nameO, nameP, wordList, length, com)
            else:
                if aList[1] == []: 
                    counterP = counterP + int(aList[0])
                else:
                    counterP = counterP + int(aList[0])*len(aList[1])
                if len(aList[1]) != 0:
                    for i in range(len(aList[1])):
                        length[aList[1][i]] = aList[3]
                    for j in range(len(length)):
                        print(length[j], end = "")
        elif num == 2: #option 2
            bList = option2(wordList) #asking for vowel
            counterP = counterP - 25
            if len(bList[1]) != 0:
                for i in range(len(bList[1])):
                    length[bList[1][i]] = bList[3]
                for j in range(len(length)):
                    print(length[j], end = "")
                return length
        else: #option 3
            word = guessP(wordList, nameO, nameP, length, com)
        counterPT = counterPT + counterP
        print(" It's", nameP, "'s turn!")
        print(nameP, "'s balance in this round is", counterP)
        print(nameP, "'s balance in total is", counterPT)
        num = option()
    print("Thanks for playing!")
    exit()

'''
Game body for another player
'''

def gameO(nameO, nameP, wordList, length, com):
    counterO = 0
    counterOT = 0
    print("It's", nameO, "'s turn!")
    print(nameO, "'s balance in this round is", counterO)
    print(nameO, "'s balance in total is", counterOT)
    num = option()
    while num != 4:
        counterO = 0
        if num == 1:
            aList = spinO(wordList, nameO, nameP)
            if int(aList[0]) == 0:
                counterO = 0
            elif int(aList[0]) == 21:
                if num != 4: 
                    gameP(nameP, nameO, wordList, length, com)
            else:
                if aList[1] == []:
                    counterO = counterO + int(aList[0])
                else:
                    counterO = counterO + int(aList[0])*len(aList[1])
                if len(aList[1]) != 0:
                    print(length)
                    for i in range(len(aList[1])):
                        length[aList[1][i]] = aList[3]
                        print(length)
                    for j in range(len(length)):
                        print(length[j], end = "")
        elif num == 2:
            bList = option2(wordList)
            counterO = counterO - 25
            if len(bList[1]) != 0:
                print(length)
                for i in range(len(bList[1])):
                    length[bList[1][i]] = bList[3]
                    print(length)
                for j in range(len(length)):
                    print(length[j], end = "")
        else:
            word = guessO(wordList, nameO, nameP, length, com)
        counterOT = counterOT + counterO
        print(" It's", nameO, "'s turn!")
        print(nameO, "'s balance in this round is", counterO)
        print(nameO, "'s balance in total is", counterOT)
        num = option()
    print("Thanks for playing!")
    exit()

'''
Game body for computer
'''

def gameC(nameO, nameP, wordList, length, com):
    counterC = 0
    counterCT = 0
    print("It's", nameO, "'s turn!")
    print(nameO, "'s balance in this round is", counterC)
    print(nameO, "'s balance in total is", counterCT)
    num = optionC()
    while num != 4:
        counterC = 0
        if num == 1:
            aList = spinC(wordList, nameO, nameP)
            if int(aList[0]) == 0:
                counterC = 0
            elif int(aList[0]) == 21:
                if num != 4: 
                    gameP(nameP, nameO, wordList, length, com)
            else:
                if aList[1] == []:
                    counterC = counterC + int(aList[0])
                else:
                    counterC = counterC + int(aList[0])*len(aList[1])
                if len(aList[1]) != 0:
                    print(length)
                    for i in range(len(aList[1])):
                        length[aList[1][i]] = aList[3]
                        print(length)
                    for j in range(len(length)):
                        print(length[j], end = "")
        elif num == 2:
            bList = option2C(wordList)
            counterC = counterC - 25
            if len(bList[1]) != 0:
                print(length)
                for i in range(len(bList[1])):
                    length[bList[1][i]] = bList[3]
                    print(length)
                for j in range(len(length)):
                    print(length[j], end = "")
        else:
            word = guessO(wordList, nameO, nameP, length, com)
        counterCT = counterCT + counterC
        print(" It's", nameO, "'s turn!")
        print(nameO, "'s balance in this round is", counterC)
        print(nameO, "'s balance in total is", counterCT)
        num = optionC()
    print("Thanks for playing!")
    exit()
    
def main():
    print("Welcome to Word Blitz!")
    choice = start() # who the user wants to play with
    nameP = input("Please enter your name: ") #asking for user's name
    nameO = name(choice) #asking for another player's name
    if nameO == "computer":
        com = "c"
    else:
        com = "o"
    wordList = puzzle() #getting secretWord
    if " " in wordList:
        wordList.remove(" ") #remove space if the secretWord has
    length = "_ " * len(wordList) #printing underline to show how long the word is
    print(length)
    n = 2
    length = [length[i:i+n] for i in range(0, len(length), n)] #store underline one by one to a list
    print(length)
    gameP(nameP, nameO, wordList, length, com) #game
      

main()
