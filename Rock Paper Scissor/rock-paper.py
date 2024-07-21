from tkinter import*
from PIL import Image,ImageTk
from random import randint

#2. configure and create main window
root = Tk() #initializing the module of tkinter 
root.title('Rock Paper Scissors')
root.configure(background="#9b59b6")


#3. pictures
rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissors_img = ImageTk.PhotoImage(Image.open("scissors-user.png"))
scissors_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))

#4. insert picture
user_label = Label(root,image=paper_img, bg="#9b59b6") #picture that will show initially
comp_label = Label(root,image=paper_img_comp, bg="#9b59b6")
comp_label.grid(row=1, column=0) #position
user_label.grid(row=1, column=4)

#4. scores
playerScore= Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computerScore= Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computerScore.grid(row=1,column=1)
playerScore.grid(row=1,column=3)

#6. indicators
user_indicator = Label(root,font=50,text="USER",bg="#9b59b6",fg="white")
comp_indicator = Label(root,font=50,text="COMPUTER",bg="#9b59b6",fg="white")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

#7. messages
msg = Label(root,font=50,bg="#9b59b6",fg="white")
msg.grid(row=3,column=2)

#9. update message
def updateMessage(x):
    msg['text'] = x

#10. update user score
def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

#11. update computer score
def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)

#12. check the winner
def checkWin(player,computer):
    if player == computer:
        updateMessage("It's a tie!!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("YOU LOSE")
            updateCompScore()
        else:
            updateMessage("YOU WIN!!")
            updateUserScore()
    elif player == "paper":
        if computer == "scissors":
            updateMessage("YOU LOSE")
            updateCompScore()
        else:
            updateMessage("YOU WIN!!")
            updateUserScore()
    elif player == "scissors":
        if computer == "rock":
            updateMessage("YOU LOSE")
            updateCompScore()
        else:
            updateMessage("YOU WIN!!")
            updateUserScore()
    else:
        pass

#8. update choices
choices = ["rock", "paper", "scissors"]
def updateChoice(x):
#choice for computer random
    compChoice = choices[randint(0,2)] 
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissors_img_comp)

#choice for user
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissors_img)
        
    checkWin(x,compChoice)

#5.buttons

rock= Button(root,width=20,height=2,text="ROCK",bg="#FF3E4D",fg="white",command = lambda:updateChoice("rock")).grid(row=2,column=1)
paper= Button(root,width=20,height=2,text="PAPER",bg="#FAD02E",fg="white",command = lambda:updateChoice("paper")).grid(row=2,column=2)
scissors= Button(root,width=20,height=2,text="SCISSORS",bg="#0ABDE3",fg="white",command = lambda:updateChoice("scissors")).grid(row=2,column=3)
root.mainloop()