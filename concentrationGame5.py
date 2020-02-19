#concentration3Pt0.py

'''
Traceback (most recent call last):
  File "/home/william/pythonClass Dell E6430/programs/concentration Game/ModularConcentration/concentration4pt0.py", line 236, in <module>
    nextLoop()
  File "/home/william/pythonClass Dell E6430/programs/concentration Game/ModularConcentration/concentration4pt0.py", line 175, in nextLoop
    listofPossibles[countLOP].delete()
AttributeError: 'str' object has no attribute 'delete'

how to delete from a list?  use del listname[index] or listname.pop(index)
how to redo the same square over and over? it is reversing the two options? after
the first turning and returning


'''

from random import randint
import turtle
from turtle import *
import tkinter.font
from tkinter import *
import drawBoardLarger
import startingData
import sys

screen = Screen()
screen.setup(width=800, height=800, startx=10, starty=10)


root = Tk()
root.title("Concentration Game for Binary and Hexadecimal Numbers!")
x = (root.winfo_screenwidth() - root.winfo_reqwidth() + 480) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight() -20) / 2
root.geometry("+%d+%d" % (x, y))

def erasableWrite(tortoise, name, font, align, reuse=None):
    eraser = turtle.Turtle() if reuse is None else reuse
    eraser.hideturtle()
    eraser.up()
    eraser.setposition(tortoise.position())
    eraser.write(name, font=font, align=align)
    return eraser
'''
this creates this list
eraseble = [<turtle.Turtle object at 0x7f2f24513340>,
<turtle.Turtle object at 0x7f2f24513580>.....]
'''

def printBoard():
    global t, eraseble
    counter = 0
    startX = -280
    startY = -295
    textValue = ''
    for i in range(5):
        for k in range(5):
            textValue = CList[counter][1]
            t.penup()
            t.goto(startX, startY)
            t.pendown()
            #if len(textValue) <= 3:
            eraseble.append(erasableWrite(t, textValue, font=("New Times Roman", 18, "normal"), align="center"))
            #    print('printBoard counter = {} eraseble = {}'.format(counter, eraseble[counter]))
            #else:
            #   eraseble.append(erasableWrite(t, textValue, font=("New Times Roman", 14, "normal"), align="center"))
            #print('printBoard counter = {} eraseble = {}'.format(counter, eraseble[counter]))
            startX += 140
            counter +=1
        startY += 140
        startX = -280
       

index = []
eraseble = []
t = turtle.Turtle()
t.hideturtle()
turtle.speed(0)
drawBoardLarger
CList = startingData.startingData()
count1 = 0
for i in CList:
        indexEntry = [CList[count1][0], CList[count1][1]]
        index.append(indexEntry)
        count1 +=1
printBoard()
matchCount = 0
guessCount = 0 # this is for wild card handling
wildCardCount = 0
pastGuesses = []
listofPossibles = ['00', '01', '02', '03', '04', '10', '11', '12', '13', '14', '20', '21', '22', '23', '24', '30', '31', '32', '33', '34', '40', '41', '42', '43', '44']
thisGameListofPs = listofPossibles

def getFirst():
    textInput = screen.textinput("Concentration Game", "type your first choice")
    
    return textInput

def getSecond():
    textInput = screen.textinput("Concentration Game", "type your second choice")
    guessCount = 1
    return textInput

def validate(stringNumber, choice):
    global thisGameListofPs
    if stringNumber in thisGameListofPs:
        return stringNumber
    elif choice == 1:
        getFirst()
    else:
        getSecond()

def updatethisGameListofPs():
    global thisGameListofPs, choice1, choice2
    
            
    
def gotAMatch():
    global matchCount
    messagebox.showinfo('A Match!', 'Excellent : > )')
    matchCount += 1
    #updatethisGameListofPossibles()
    
def NotAMatch():
    messagebox.showinfo('NOT a match!', 'sorry : > (')

def startAgain(root):
    nextLoop()

def flipCard(choice):
    global wildCardCount, gameTupleList, index, eraseble, CList, gameTupleList
    gameTupleList = CList
    firstInt = 0
    counti = 0
    count1 = 0
    textValue = ''
    for x in index:
        if x[1] == choice:
            firstInt = index[counti][0]
        counti +=1
    newEntry = (gameTupleList[firstInt])
    nextStep = (newEntry[0], newEntry[2], newEntry[1], newEntry[3])
    gameTupleList[firstInt] = nextStep
    counter = newEntry[0]
    counterX = counter % 5
    counterY = int(counter/5)
    startX = -280
    startY = -295
    startY += 140 * counterY
    startX += 140 * counterX
    t.penup()
    t.goto(startX, startY)
    #print('eraseble = {}'.format(eraseble))
    eraseble[counter].clear()
    textValue = nextStep[1]
    if textValue == 'Wild\nCard' and guessCount == 0:
        wildCardCount = 1
        if len(textValue) <= 3:
            eraseble[counter] = eraseble.append(erasableWrite(t, textValue, font=("New Times Roman", 18, "normal"), align="center"))
        else:
            eraseble[counter] = eraseble.append(erasableWrite(t, textValue, font=("New Times Roman", 14, "normal"), align="center"))
    elif textValue == 'Wild\nCard' or wildCardCount ==1:
        wildCardCount = 0
        if len(textValue) <= 3:
            eraseble[counter] = (erasableWrite(t, textValue, font=("New Times Roman", 18, "normal"), align="center"))
        else:
            eraseble[counter] = (erasableWrite(t, textValue, font=("New Times Roman", 14, "normal"), align="center"))
            gotAMatch()
    else:
        if len(textValue) <= 3:
            eraseble[counter] = (erasableWrite(t, textValue, font=("New Times Roman", 18, "normal"), align="center"))
        else:
            eraseble[counter] = (erasableWrite(t, textValue, font=("New Times Roman", 14, "normal"), align="center"))
    return nextStep

def unFlipCards():
    global indexEntry, choice1, choice1
        

def nextLoop():
    global choice1, choice2, matchCount, CList, thisGameListofPs, gameTupleList, index, a, eraseble
    while matchCount <= 11:
        choice1 = getFirst()
        choice1 = validate(choice1, 1)
        card1 = flipCard(choice1)
        #print('card1[3] = {}'.format(card1[3]))
        choice2 = getSecond()
        choice2 = validate(choice2, 2)
        card2 = flipCard(choice2)
        #print('card2[3] = {}'.format(card2[3]))
        if card1[3] == card2[3] or card1[3] == 1000 or card2[3] == 1000:
            countLOP = 0
            for n in thisGameListofPs:
                if n == choice1 or n == choice2:
                    del thisGameListofPs[countLOP]
                    countLOP +=1
                else:
                    countLOP +=1
            matchCount +=1
            # print('length of thisGameListofPossibles'.format(len(thisGameListofPossibles)))
            print('thisGameListofPs is {}'.format(thisGameListofPs))
            CList = gameTupleList
            gotAMatch()
        else:
            NotAMatch()
            listReset = [choice1, choice2]
            print('list reset = {}'.format(listReset))
            counter = 0
            gameTupleList = CList
            for a in listReset:
                for item in index:
                    if item[1] == a:
                        counter = item[0]
                        break
                #print('gameTupleList[counter] is {} choice (that is a) = {} counter = {}'.format(gameTupleList[counter], a, counter))
                counterX = counter % 5
                counterY = int(counter/5)
                startX = -280
                startY = -295
                startY += 140 * counterY
                startX += 140 * counterX
                t.penup()
                t.goto(startX, startY)
                print('length of eraseble is {}.'.format(len(eraseble)))
                print('in next loop eraselbe = {}'.format(eraseble))
                print('in next loop counter = {}, eraseble[counter] = {}.'.format(counter, eraseble[counter]))
                if eraseble[counter] != None:
                    eraseble[counter].clear()
                print('in next loop past eraseble clear')
                textValue = CList[counter][2]
                eraseble[counter] = (erasableWrite(t, textValue, font=("New Times Roman", 18, "normal"), align="center"))


def goForIt(choice):
    global numberOfGuesses
    numberOfGuesses +=1
    pastGuesses.append(choice)
    #print('goForIt choice = {}'.format(choice))
    flipCard(choice)
    if numberOfGuesses % 2 == 1:
        sec(root)
    else:
        print('got to match in goForIt()')
        match()
           
def done():
    global firstChoice, secondChoice
    frame_Main.destroy()
    root.destroy()
    sys.exit()


def endThis(root):
    b4 = Button(frame_Main, text="Click here to Exit Game", command=done)
    b4.grid(row =0, column=1)


nextLoop()

root.mainloop()
