#Import the required libraries :
from tkinter import *
import random

root = Tk()
root.configure(bg="#000000")
root.geometry('+0+0')
root.title("Rock-Paper-Scissor")
root.resizable(width=False,height=False)
#Hand images :
rockHandPhoto = PhotoImage(file="rHand.png")
paperHandPhoto = PhotoImage(file="pHand.png")
scissorHandPhoto = PhotoImage(file="sHand.png")

#Graphical images :
rockPhoto = PhotoImage(file="rock.png")
paperPhoto = PhotoImage(file="paper.png")
scissorPhoto = PhotoImage(file="scissors.png")

#Decision image :
decisionPhoto = PhotoImage(file="ds.png")

#Result images :
winPhoto = PhotoImage(file="win.png")
losePhoto = PhotoImage(file="loose.png")
tiePhoto = PhotoImage(file="tie.png")



#Initialize the button variables :
rockHandButton = " "
paperHandButton = " "
scissorHandButton = " "
resultButton = " "
#Create the result button :
resultButton = Button(root,image=decisionPhoto)

#Set the variable to True
click = True

def play():
    global rockHandButton,paperHandButton,scissorHandButton,resultButton
    global comp_score,player_score
    #Set images and commands for buttons :
    rockHandButton = Button(root,image = rockHandPhoto, command=lambda:youPick("Rock"))
    paperHandButton = Button(root,image = paperHandPhoto, command=lambda:youPick("Paper"))
    scissorHandButton = Button(root,image = scissorHandPhoto, command=lambda:youPick("Scissor"))
    #Place the buttons on window :
    rockHandButton.grid(row=0,column=0)
    paperHandButton.grid(row=0,column=1)
    scissorHandButton.grid(row=0,column=2)
    
    #Add space :
    root.grid_rowconfigure(1, minsize=50) 
    
    #Place result button on window : 
    resultButton.grid(row=1,column=0,columnspan=5)

def computerPick():
    choice = random.choice(["Rock","Paper","Scissor"])
    return choice    
def youPick(yourChoice):
    global click
    
    compPick = computerPick()
    
    
    if click==True:
        
        if yourChoice == "Rock":
            
            rockHandButton.configure(image=rockPhoto)
            
            if compPick == "Rock":
                paperHandButton.configure(image=rockPhoto)
                resultButton.configure(image=tiePhoto)
                scissorHandButton.grid_forget()
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                click = False
            
            elif compPick == "Paper":
                paperHandButton.configure(image=paperPhoto)
                scissorHandButton.grid_forget()
                resultButton.configure(image=losePhoto)
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                click = False
            
            else :
                paperHandButton.configure(image=scissorPhoto)
                scissorHandButton.grid_forget()
                resultButton.configure(image=winPhoto)
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                click = False
                
            
                
                
        elif yourChoice == "Paper":
            rockHandButton.configure(image=paperPhoto)
            
            if compPick == "Rock":
                paperHandButton.configure(image=rockPhoto)
                resultButton.configure(image=losePhoto)
                scissorHandButton.grid_forget()
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                click = False
        
            elif compPick == "Paper":
                paperHandButton.configure(image=paperPhoto)
                resultButton.configure(image=tiePhoto)
                scissorHandButton.grid_forget()
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                click = False
            
            else:
                paperHandButton.configure(image=scissorPhoto)
                resultButton.configure(image=losePhoto)
                scissorHandButton.grid_forget()
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                click = False            
                
                
        else:
            rockHandButton.configure(image=scissorPhoto)
            if compPick == "Rock":
                paperHandButton.configure(image=rockPhoto)
                resultButton.configure(image=losePhoto)
                scissorHandButton.grid_forget()
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                click = False
            
            elif compPick == "Paper":
                paperHandButton.configure(image=paperPhoto)
                resultButton.configure(image=winPhoto)
                scissorHandButton.grid_forget()
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                click = False
            
            else:
                paperHandButton.configure(image=scissorPhoto)
                resultButton.configure(image=tiePhoto)
                scissorHandButton.grid_forget()
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                click = False 
                
    else:
        #To reset the game :
        if yourChoice=="Rock" or yourChoice=="Paper" or yourChoice=="Scissor":
            rockHandButton.configure(image=rockHandPhoto)
            paperHandButton.configure(image=paperHandPhoto)
            scissorHandButton.configure(image=scissorHandPhoto)
            resultButton.configure(image=decisionPhoto)
            
            #Get back the deleted buttons :
            scissorHandButton.grid(row=0,column=1)

            #Set click = True :
            click=True
#Calling the play function :
play()

#Enter the main loop :
root.mainloop()            