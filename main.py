#import modules
from tkinter import *
import random

#roll dice function, takes all dice vars and updates them based on button clicked and what random int it landed on
def roll(frame, dice_one, dice_two, dice_three, firstDiceFace, secondDiceface, thirdDiceFace, trueOne, trueTwo, trueThree, faceArray, total, totalLabel):
    one = random.randint(0, 5)
    pause_one = one
    two = random.randint(0, 5)
    pause_two = two
    three = random.randint(0, 5)
    pause_three = three

    if (trueOne == True and trueTwo == True and trueThree == True):
        firstDiceFace = faceArray[pause_one]
        secondDiceface = faceArray[pause_two]
        thirdDiceFace = faceArray[pause_three]
        dice_one.config(text=firstDiceFace)
        dice_two.config(text=firstDiceFace)
        dice_three.config(text=firstDiceFace)
        total= "Total: " + str(pause_one+pause_two+pause_three+3)

    elif((trueOne == True and trueTwo == True and trueThree == False)):
        firstDiceFace = faceArray[one]
        secondDiceface = faceArray[two]
        dice_one.config(text=firstDiceFace)
        dice_two.config(text=secondDiceFace)
        total="Total: " + str(pause_one + pause_two+ 2)
    else:
        firstDiceFace = faceArray[pause_one]
        dice_one.config(text=firstDiceFace)
        total = "Total: " + str(pause_one+1)

    totalLabel.config(text=total)



#should make all dice dissappear, does not work
def reset(frame, dice_one, dice_two, dice_three):
    dice_one.pack_forget()
    dice_two.pack_forget()
    dice_three.pack_forget()

#makes one Dice appear
def oneDice_clicked(frame, dice_one, dice_two, dice_three):
    trueOne = True
    trueTwo = False
    trueThree = False

    dice_one.place(x=225, y=75)


#makes two dice appear
def twoDice_clicked(frame, dice_one, dice_two, dice_three):
    trueOne = False
    trueTwo = True
    trueThree = True

    dice_one.place(x=160, y=75)
    dice_two.place(x=300, y=75)


#makes three dice appear
def threeDice_clicked(frame, dice_one, dice_two, dice_three):
    trueOne = True
    trueTwo = True
    trueThree = True

    dice_one.place(x=100, y=75)
    dice_two.place(x=225, y=75)
    dice_three.place(x=350, y=75)


#make frames
window = Tk()
top_frame = Frame(window, width=600, height=50, bg="gray")
top_frame.pack_propagate(False)
top_frame.pack()

bottom_frame = Frame(window, width= 600, height=50, bg="gray")
bottom_frame.pack_propagate(False)
bottom_frame.pack(side = BOTTOM)

#set size
window.geometry("600x300")

#change title
window.title("Dice Roller")

#change icon
icon = PhotoImage(file="dice.png")
window.iconphoto(True, icon)

#dice faces
diceFaces = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]

#sets dice face vars
firstDiceFace = diceFaces[0]
secondDiceFace = diceFaces[0]
thirdDiceFace = diceFaces[0]

#being used?
trueOne = False
trueTwo = False
trueThree = False

#labels
howMany = Label(top_frame, text="How many dice do you need?: ", padx=2, pady=2)
howMany.pack(side = LEFT)
totalOfDice = "0"
total = Label(bottom_frame, text="Total: " + totalOfDice, padx=25, pady=2)
total.place(x=330, y=12)
dice_one = Label(window, text = firstDiceFace, padx=25, pady=2, font=("Helvetica", 100))
dice_two = Label(window, text = secondDiceFace, padx=25, pady=2, font=("Helvetica", 100))
dice_three = Label(window, text = thirdDiceFace, padx=25, pady=2, font=("Helvetica", 100))

#buttons
oneDice = Button(top_frame, text = "1", padx=25, pady=2, command= lambda: [reset(window, dice_one, dice_two, dice_three), oneDice_clicked(window, dice_one, dice_two, dice_three)])
oneDice.place(x=250, y=10)
twoDice = Button(top_frame, text = "2", padx=25, pady=2, command= lambda: [reset(window, dice_one, dice_two, dice_three), twoDice_clicked(window, dice_one, dice_two, dice_three)])
twoDice.place(x=350, y=10)
threeDice = Button(top_frame, text = "3", padx=25, pady=2, command= lambda: [reset(window, dice_one, dice_two, dice_three), threeDice_clicked(window, dice_one, dice_two, dice_three)])
threeDice.place(x=450, y=10)
roll_button = Button(bottom_frame, text= "Roll", padx= 25, pady=2, command= lambda: roll(window, dice_one, dice_two, dice_three, firstDiceFace, secondDiceFace, thirdDiceFace, trueOne, trueTwo, trueThree, diceFaces, totalOfDice, total))
roll_button.place(x= 200, y=10)

#runs program
window.mainloop()