from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.geometry('530x375')
root.title("                                                              Tic-Tac-Toe")
button1 = ttk.Button(root, text=" ", command=lambda:buttonPressed(1))
button1.grid(row=0, column=0, ipadx=50, ipady=50)

button2 = ttk.Button(root, text=" ", command=lambda:buttonPressed(2))
button2.grid(row=0, column=1, ipadx=50, ipady=50)

button3 = ttk.Button(root, text=" ", command=lambda:buttonPressed(3))
button3.grid(row=0, column=2, ipadx=50, ipady=50)

button4 = ttk.Button(root, text=" ", command=lambda:buttonPressed(4))
button4.grid(row=1, column=0, ipadx=50, ipady=50)

button5 = ttk.Button(root, text=" ", command=lambda:buttonPressed(5))
button5.grid(row=1, column=1, ipadx=50, ipady=50)

button6 = ttk.Button(root, text=" ", command=lambda:buttonPressed(6))
button6.grid(row=1, column=2, ipadx=50, ipady=50)

button7 = ttk.Button(root, text=" ", command=lambda:buttonPressed(7))
button7.grid(row=2, column=0, ipadx=50, ipady=50)

button8 = ttk.Button(root, text=" ", command=lambda:buttonPressed(8))
button8.grid(row=2, column=1, ipadx=50, ipady=50)

button9 = ttk.Button(root, text=" ", command=lambda:buttonPressed(9))
button9.grid(row=2, column=2, ipadx=50, ipady=50)

player = 1
count = 0
count1 = 0
count2 = 0


def newGame():
    MsgBox = messagebox.askquestion('Return', 'Do you want to play a new game?')
    if MsgBox == 'yes':
        startGame()
    else:
        root.destroy()


def checkWinner():
    global button1, button2, button3, button4, button5, button6, button7, button8, button9
    global count,count1,count2
    count = count+1
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
       button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
       button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
       button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
       button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
       button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X' or
       button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
       button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X'):
        count1 = count1+1
        messagebox._show("Winner of game", "Player X is winner \n Player X : " + str(count1) +
                         " \n Player Y : " + str(count2))
        count = 0
        newGame()

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
       button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
       button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
       button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
       button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
       button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O' or
       button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
       button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O'):
        count2 = count2+1
        messagebox._show("Winner of game", "Player O is winner \n Player X : " + str(count1) +
                         " \n Player Y : " + str(count2))
        count = 0
        newGame()

    if count == 9:
        messagebox._show("Draw", "Match is Draw \n Player X : " + str(count1) +
                         " \n Player Y : " + str(count2))
        count = 0
        newGame()


def startGame():
    global player
    global button1,button2,button3,button4,button5,button6,button7,button8,button9
    root.geometry('530x375')
    root.title("Tic-Tac-Toe")
    button1 = ttk.Button(root, text=" ", command=lambda:buttonPressed(1))
    button1.grid(row=0, column=0, ipadx=50, ipady=50)

    button2 = ttk.Button(root, text=" ", command=lambda:buttonPressed(2))
    button2.grid(row=0, column=1, ipadx=50, ipady=50)

    button3 = ttk.Button(root, text=" ", command=lambda:buttonPressed(3))
    button3.grid(row=0, column=2, ipadx=50, ipady=50)

    button4 = ttk.Button(root, text=" ", command=lambda:buttonPressed(4))
    button4.grid(row=1, column=0, ipadx=50, ipady=50)

    button5 = ttk.Button(root, text=" ", command=lambda:buttonPressed(5))
    button5.grid(row=1, column=1, ipadx=50, ipady=50)

    button6 = ttk.Button(root, text=" ", command=lambda:buttonPressed(6))
    button6.grid(row=1, column=2, ipadx=50, ipady=50)

    button7 = ttk.Button(root, text=" ", command=lambda:buttonPressed(7))
    button7.grid(row=2, column=0, ipadx=50, ipady=50)

    button8 = ttk.Button(root, text=" ", command=lambda:buttonPressed(8))
    button8.grid(row=2, column=1, ipadx=50, ipady=50)

    button9 = ttk.Button(root, text=" ", command=lambda:buttonPressed(9))
    button9.grid(row=2, column=2, ipadx=50, ipady=50)

    player = 1


def buttonPressed(buttonNumber):
    global player
    global button1, button2, button3, button4, button5, button6, button7, button8, button9
    if buttonNumber == 1 and player == 1 and button1['text'] == ' ':
        button1.config(text="X")
        player = 2
    elif buttonNumber == 2 and player == 1 and button2['text'] == ' ':
        button2.config(text="X")
        player = 2
    elif buttonNumber == 3 and player == 1 and button3['text'] == ' ':
        button3.config(text="X")
        player = 2
    elif buttonNumber == 4 and player == 1 and button4['text'] == ' ':
        button4.config(text="X")
        player = 2
    elif buttonNumber == 5 and player == 1 and button5['text'] == ' ':
        button5.config(text="X")
        player = 2
    elif buttonNumber == 6 and player == 1 and button6['text'] == ' ':
        button6.config(text="X")
        player = 2
    elif buttonNumber == 7 and player == 1 and button7['text'] == ' ':
        button7.config(text="X")
        player = 2
    elif buttonNumber == 8 and player == 1 and button8['text'] == ' ':
        button8.config(text="X")
        player = 2
    elif buttonNumber == 9 and player == 1 and button9['text'] == ' ':
        button9.config(text="X")
        player = 2
    elif buttonNumber == 1 and player == 2 and button1['text'] == ' ':
        button1.config(text="O")
        player = 1
    elif buttonNumber == 2 and player == 2 and button2['text'] == ' ':
        button2.config(text="O")
        player = 1
    elif buttonNumber == 3 and player == 2 and button3['text'] == ' ':
        button3.config(text="O")
        player = 1
    elif buttonNumber == 4 and player == 2 and button4['text'] == ' ':
        button4.config(text="O")
        player = 1
    elif buttonNumber == 5 and player == 2 and button5['text'] == ' ':
        button5.config(text="O")
        player = 1
    elif buttonNumber == 6 and player == 2 and button6['text'] == ' ':
        button6.config(text="O")
        player = 1
    elif buttonNumber == 7 and player == 2 and button7['text'] == ' ':
        button7.config(text="O")
        player = 1
    elif buttonNumber == 8 and player == 2 and button8['text'] == ' ':
        button8.config(text="O")
        player = 1
    elif buttonNumber == 9 and player == 2 and button9['text'] == ' ':
        button9.config(text="O")
        player = 1
    checkWinner()

root.mainloop()