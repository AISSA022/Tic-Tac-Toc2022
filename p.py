import tkinter as tkinter
import sqlite3
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from random import randint


def signin():
    """
    This method is for creating sigin page to enter your password and username that you created before
    """
    def login():
        # connecting to database
        db = sqlite3.connect('players.db')

        # creating a table if not exist in database
        db.execute( 'CREATE TABLE IF NOT EXISTS players(username TEXT,password TEXT,highs INTEGER)')

        # db.execute("INSERT INTO players(username,password)VALUES('admin','admin')")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM players WHERE username=? AND password=?",(userinput.get(),passwordinput.get()))
        
        #check all the data 
        # cursor.execute("SELECT * FROM players ")
        
        #Delete accounts from table
        # cursor.execute("""DELETE FROM players WHERE username=:username""",{'username':"admin"})

        row = cursor.fetchall()
        print(row)
        #Check the username and password if they exist in the table or not
        if row:
            loginp.destroy()
            main()
        else:
            messagebox.showerror('error', 'Login Faild')
        cursor.connection.commit()
        db.close()
        #  username = userinput.get()
        #  password = pass_input.get()
        #  wb =load_workbook('player.xlsx')
        #  ws = wb.active
        #  colomn=ws["A"]
        #  colomnb=ws["B"]
        #  for cell in colomn:
        # #   if username:
        #      if cell.value==username:
        #          loginp.destroy()
        #  main()
        #   else:
        #     messagebox.showerror('error', 'Login Faild')

    global user_input
    loginp = tkinter.Tk()
    loginp.title("tic tac toe | LOGIN")
    loginp.geometry('305x305')

    # Background image
    bgli = tkinter.PhotoImage(file="images/bgil.png")
    mylabel1 = tkinter.Label(loginp, image=bgli)
    mylabel1.place(x=0, y=0)
    # login title
    bgli1 = tkinter.PhotoImage(file="images/logint.png")
    mylabel2 = tkinter.Label(loginp, image=bgli1, bd=0, bg="#18132D")
    mylabel2.place(x=50, y=55)

    # creating input and buttons
    user_input = tkinter.StringVar()
    pass_input = tkinter.StringVar()

    image1 = Image.open("images/button.png")
    test = ImageTk.PhotoImage(image1)
    user = tkinter.Label(image=test, bd=0, bg="#863FDE")
    user.image = test
    user.place(x=55, y=155)
    userinput = tkinter.Entry(loginp, textvariable=user_input)
    userinput.place(x=155, y=165)

    pasimg = Image.open("images/passb.png")
    test1 = ImageTk.PhotoImage(pasimg)
    passw = tkinter.Label(image=test1, bd=0, bg="#863FDE")
    passw.image = test
    passw.place(x=55, y=190)
    passwordinput = tkinter.Entry(loginp, textvariable=pass_input, show='*')
    passwordinput.place(x=155, y=200)

    bg2 = tkinter.PhotoImage(file="images/LOGIN.png")
    b2 = tkinter.Button(loginp, text="hello", image=bg2,
                        bd=0, bg="#863FDE", command=login)
    b2.place(x=75, y=260)
    
    def back():
        """
        This method is for get back to the main page to create or sigin to  account
        """
        loginp.destroy()
        mainp()
    bg3 = tkinter.PhotoImage(file="images/backimg2.png")
    b3 = tkinter.Button(loginp, text="hello", image=bg3,
                        bd=0, bg="#863FDE", command=back)
    b3.place(x=10, y=5)
    loginp.mainloop()


def main():
    """
    This def create window  for the player to choose either play with the computer or play with friend
    """
    x = 1
    
    def recall():
        """
        recall():Is for quiting the page (choose) and open the page of the player 1
        """
        choose.destroy()
        opp()
    
    def recall2():
        """
        recall2():Is for quiting the page (choose) and open the page of the 2 players
        """
        choose.destroy()
        tp()
    # creating GUI
    choose = tkinter.Tk()
    choose.geometry('305x305')
    choose.title("tic tac toe | ")

    # Background image
    bg = tkinter.PhotoImage(file="images/bgi.png")
    mylabel = tkinter.Label(choose, image=bg)
    mylabel.place(x=0, y=0)

    # Button1
    bg1 = tkinter.PhotoImage(file="images/button1.png")
    b1 = tkinter.Button(choose, text="hello", image=bg1,
                        bd=0, bg="#764217", command=recall)
    b1.pack(pady=20)
    b1.place(x=35, y=230)
    # Button2
    bg2 = tkinter.PhotoImage(file="images/button2.png")
    b2 = tkinter.Button(choose, text="hello", image=bg2,
                        bd=0, bg="#764217", command=recall2)
    b2.pack(pady=20)
    b2.place(x=35, y=260)
    choose.mainloop()


player_char = ''
position = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
turn = 1
turns = 0
com_char = ''
game_over = False
global count
count = 0
global score
score = 0
global highs
highs = 0



def opp():
    """
    This method is used to create the page of the one player to play with computer by choosing the player_char
    """
    
    def check_winner(poss):
        """
        This method is for chechking every time if there is a winner or a no
        If the player_char equal to the winner char the score will increament 
        """
        global score
        global game_over
        global highs
        global count
        if poss[0]+poss[1]+poss[2] == 'XXX' or \
                poss[3]+poss[4]+poss[5] == 'XXX' or \
                poss[6]+poss[7]+poss[8] == 'XXX' or \
                poss[0]+poss[3]+poss[6] == 'XXX' or \
                poss[1]+poss[4]+poss[7] == 'XXX' or \
                poss[2]+poss[5]+poss[8] == 'XXX' or \
                poss[0]+poss[4]+poss[8] == 'XXX' or \
                poss[2]+poss[4]+poss[6] == 'XXX':

            if player_char == "X":
                score += 5
                if highs < score:
                    highs = score
                    conn = sqlite3.connect('players.db')
                    c = conn.cursor()
                    # print(user_input)

                    # Updating the high score in the table if score is greater than highs
                    c.execute("""UPDATE  players SET highs=:highs WHERE username=:username""", {
                              'highs': highs, 'username': user_input.get()})
                    row=c.fetchall()
                    print(row)
                    conn.commit()
                    c.close()
                    conn.close()
            else:
                score-=5
            game_over = True
            win_label = tkinter.Label(
                root, text="X-Wins!").grid(row=8, column=1)
            scorel = tkinter.Label(root, text=score).grid(row=9, column=1)
        if poss[0]+poss[1]+poss[2] == 'OOO' or \
                poss[3]+poss[4]+poss[5] == 'OOO' or \
                poss[6]+poss[7]+poss[8] == 'OOO' or \
                poss[0]+poss[3]+poss[6] == 'OOO' or \
                poss[1]+poss[4]+poss[7] == 'OOO' or \
                poss[2]+poss[5]+poss[8] == 'OOO' or \
                poss[0]+poss[4]+poss[8] == 'OOO' or \
                poss[2]+poss[4]+poss[6] == 'OOO':
            game_over = True
            if player_char == "O":
                score += 5
                if highs < score:
                    highs = score
                    conn = sqlite3.connect('players.db')
                    c = conn.cursor()
                    # print(user_input)

                    # Updating the high score in the table if score is greater than highs
                    c.execute("""UPDATE  players SET highs=:highs WHERE username=:username""", {
                              'highs': highs, 'username': user_input.get()})
                    # c.execute("SELECT * FROM players WHERE username=? AND password=?",(user_input.get(),pass_input.get()))
                    row=c.fetchall()
                    print(row)
                    conn.commit()
                    c.close()
                    conn.close()
            else:
                score-=5
            win_label = tkinter.Label(
                root, text="O-Wins!").grid(row=8, column=1)
            scorel = tkinter.Label(root, text=score).grid(row=9, column=1)
        elif count == 9:
            game_over = False
            win_label = tkinter.Label(
                root, text="Draw!!!").grid(row=8, column=1)
        return game_over

    
    def changestate():
        """
        changestate():Is for disabling all the buttons ,if you click on the button no change take place
        """
        buttons = [t1, t2, t3, t4, t5, t6, t7, t8, t9]
        for x in range(len(buttons)):
            buttons[x].config(state="disabled")
    
    def com_turn():
        """
        com_turn():This is for the turn of the computer that get an random index of the array(postion) and check if the index is empty and fill it by
                   player_char else get another number for index
        """
        global turn
        global turns
        global position
        global game_over
        global count
        while turn == 0 and turns < 9 and game_over == False:

            com_select = randint(0, 8)
            if position[com_select] == ' ':
                position[com_select] = com_char
                if 0 <= com_select <= 2:
                    r = 5
                elif 3 <= com_select <= 5:
                    r = 6
                else:
                    r = 7
                if com_select == 0 or com_select == 3 or com_select == 6:
                    c = 0
                elif com_select == 1 or com_select == 4 or com_select == 7:
                    c = 1
                else:
                    c = 2
                nw = tkinter.Button(root, height=8, width=14, bg="#863FDE",
                                    text=position[com_select]).grid(row=r, column=c)
                game_over = check_winner(position)
                turn = 1
                turns += 1
                count += 1

    
    def select_x():
        """
        select_x():IS called if the user choose X
        """
        global com_char
        global player_char
        player_char = "X"
        com_char = 'O'
        labelp = tkinter.Label(root, font=('Times New Roman', 17, 'bold'), fg="white", bg="black", text="You have selected " +
                               player_char).place(x=60, y=170)
        start = tkinter.Button(root, text="Start!", bg="#863FDE",
                               border=5, width=7, height=3, command=db).place(x=130, y=250)

    
    def select_o():
        """
        select_o():IS called if the user choose o
        """
        global com_char
        global player_char
        player_char = "O"
        com_char = 'X'
        labelp = tkinter.Label(root, font=('Times New Roman', 17, 'bold'), fg="white", bg="black", text="You have selected " +
                               player_char).place(x=60, y=170)
        start = tkinter.Button(root, text="Start!", bg="#863FDE",
                               border=5, width=7, height=3, command=db).place(x=130, y=250)

    
    def plyaer_pos(pos):
        """
        player_pos():Is for the player postion that he choose to fill it by his choosen character 
        """
        global turn
        global turns
        global game_over
        global count
        if 0 <= pos <= 2:
            r = 5
        elif 3 <= pos <= 5:
            r = 6
        else:
            r = 7
        if pos == 0 or pos == 3 or pos == 6:
            c = 0
        elif pos == 1 or pos == 4 or pos == 7:
            c = 1
        else:
            c = 2
        if turn == 1 and turns < 9 and game_over == False:
            if position[pos] == ' ':
                position[pos] = player_char
                nw = tkinter.Button(root, height=8, width=14,
                                    text=position[pos], bg="#9D1D7F").grid(row=r, column=c)
                game_over = check_winner(position)
                turn = 0
                turns += 1
                count += 1
                com_turn()
    
    def rest():
        """
        rest():Is to restart the gaming by creating a new db which is the GUI of the X/O
        """
        db()
        win_label = tkinter.Label(
            root, text="            ").grid(row=8, column=1)

    
    def db():
        """
        db():Is for creating the x/o GUI buttons
        """
        global position
        global turn
        global turns
        global game_over
        global count
        game_over = False
        turn = 1
        turns = 0
        count = 0
        position = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

        t1 = tkinter.Button(root, text=position[0], height=8, width=14, command=lambda: plyaer_pos(
            0)).grid(row=5, column=0)
        t2 = tkinter.Button(root, text=position[1], height=8, width=14, command=lambda: plyaer_pos(
            1)).grid(row=5, column=1)
        t3 = tkinter.Button(root, text=position[2], height=8, width=14, command=lambda: plyaer_pos(
            2)).grid(row=5, column=2)
        t4 = tkinter.Button(root, text=position[3], height=8, width=14, command=lambda: plyaer_pos(
            3)).grid(row=6, column=0)
        t5 = tkinter.Button(root, text=position[4], height=8, width=14, command=lambda: plyaer_pos(
            4)).grid(row=6, column=1)
        t6 = tkinter.Button(root, text=position[5], height=8, width=14, command=lambda: plyaer_pos(
            5)).grid(row=6, column=2)
        t7 = tkinter.Button(root, text=position[6], height=8, width=14, command=lambda: plyaer_pos(
            6)).grid(row=7, column=0)
        t8 = tkinter.Button(root, text=position[7], height=8, width=14, command=lambda: plyaer_pos(
            7)).grid(row=7, column=1)
        t9 = tkinter.Button(root, text=position[8], height=8, width=14, command=lambda: plyaer_pos(
            8)).grid(row=7, column=2)
        
        def back1():
            """
            back1():This method destroy the page of the db and open hs1
            """
            score = 0
            root.destroy()
            hs1()
        restart = tkinter.Button(root, text="Restart", command=rest, bg="#863FDE", border=5, width=7, height=1, font=(
            "COMIC SANS MS", 10, "bold"), foreground="white").grid(row=8, column=0)
        backim = tkinter.PhotoImage(file="images/backimg.png")
        back = tkinter.Button(root, text="Back", bg="#863FDE", command=back1, border=5, width=7,
                              height=1, foreground="white", font=("COMIC SANS MS", 10, "bold")).grid(row=8, column=2)

    root = tkinter.Tk()
    root.title("tic tac toe | Two Players")
    root.geometry("325x480")

    score = 0
    highs = 0

    # Background image
    bgli = tkinter.PhotoImage(file="images/bgil2.png")
    mylabel1 = tkinter.Label(root, image=bgli)
    mylabel1.place(x=0, y=0)

    # creating x/o buttons to let the user choose
    x = tkinter.PhotoImage(file="images/x.png")
    o = tkinter.PhotoImage(file="images/o.png")

    x_button = tkinter.Button(
        root, text="X", image=x, bd=0, bg="#863FDE", command=select_x).place(x=55, y=80)
    orr = tkinter.Label(root, text="OR", fg="white", bg="black", font=(
        'Times New Roman', 17, 'bold')).place(x=150, y=95)
    o_button = tkinter.Button(
        root, text="O", image=o, bd=0, bg="#863FDE", command=select_o).place(x=250, y=80)

    root.mainloop()


clicked = True
count = 0


def tp():
    tp = Tk()
    tp.title("tic tac toe | Two Players")
    tp.geometry("320x480")
    tp.configure(bg="#863FDE")
    global score1
    global score2
    score1 = 0
    score2 = 0
    # Quit button
    quiti = PhotoImage(file="images/quit.png")
    exitButton = tkinter.Button(text="Quit", image=quiti, bg="#863FDE", command=quit, font=(
        "COMIC SANS MS", 10, "bold"), foreground="white")
    exitButton.grid(row=0, column=2)

    
    def restart():
        """
        restart():to restart the game
        """ 
        global clicked, count
        buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
        for x in range(len(buttons)):
            buttons[x].config(text=" ")
            buttons[x].config(bg="white")
            buttons[x].config(state="normal")
        x = 1
        if x == 1:
            clicked = True
            count = 0

        l1 = Label(text="PLAYER: 1(X)", height=3, bg="#863FDE", font=(
            "COMIC SANS MS", 10, "bold"), foreground="white").grid(row=0, column=0)
    # get back to the choose page

    def back():

        tp.destroy()
        main()
    l1 = Label(text="PLAYER: 1(X)", height=3, bg="#863FDE", font=(
        "COMIC SANS MS", 10, "bold"), foreground="white").grid(row=0, column=0)
    # restart button
    restarti = PhotoImage(file="images/restart.png")
    restart = tkinter.Button(text="restart", image=restarti, bg="#863FDE", command=restart, font=(
        "COMIC SANS MS", 10, "bold"), foreground="white").grid(row=0, column=1)
    # Label that shows the score
    l1 = Label(text="X:"+str(score1)+"-"+str(score2)+":O", bg="#863FDE",
               height=3, font=("COMIC SANS MS", 10, "bold"), foreground="white")
    l1.grid(row=5, column=1)
    # Back button
    backim = tkinter.PhotoImage(file="images/backimg.png")
    back = Button(image=backim, bd=0, bg="#863FDE",
                  command=back).grid(row=5, column=0)
    
    def changestate():
        """
        This method to disable all the buttons
        """
        buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
        for x in range(len(buttons)):
            buttons[x].config(state="disabled")

    
    def checkWinner():
        """
        Check the winner of the game and update the score 
        """
        global score1
        global score2

        # X winnes
        if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
            messagebox.showinfo("Winner!!!", "Player1 Wins!!!")
            changestate()
            score1 += 1
            l1.config(text="X:"+str(score1)+"-"+str(score2)+":O")

        elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
            messagebox.showinfo("Winner!!!", "Player1 Wins!!!")
            changestate()
            score1 += 1
            l1.config(text="X:"+str(score1)+"-"+str(score2)+":O")
        elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
            messagebox.showinfo("Winner!!!", "Player1 Wins!!!")
            changestate()
            score1 += 1
            l1.config(text="X:"+str(score1)+"-"+str(score2)+":O")
        elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
            messagebox.showinfo("Winner!!!", "Player1 Wins!!!")
            changestate()
            score1 += 1
            l1.config(text="X:"+str(score1)+"-"+str(score2)+":O")
        elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
            messagebox.showinfo("Winner!!!", "Player1 Wins!!!")
            changestate()
            score1 += 1
            l1.config(text="X:"+str(score1)+"-"+str(score2)+":O")
        elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
            messagebox.showinfo("Winner!!!", "Player1 Wins!!!")
            changestate()
            score1 += 1
            l1.config(text="X:"+str(score1)+"-"+str(score2)+":O")
        elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
            messagebox.showinfo("Winner!!!", "Player1 Wins!!!")
            changestate()
            score1 += 1
            l1.config(text="X:"+str(score1)+"-"+str(score2)+":O")
        elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
            messagebox.showinfo("Winner!!!", "Player1 Wins!!!")
            changestate()
            score1 += 1
            l1.config(text="X:"+str(score1)+"-"+str(score2)+":O")
        elif count == 9:
            messagebox.showinfo("What A Game!!!", "Draw!")

        # O Winnes
        if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
            messagebox.showinfo("Winner!!!", "Player2 Wins!!!")
            changestate()
            score2 += 1
            l1.config(text="X:"+str(score1)+"-"+str(score2)+":O")
        elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
            messagebox.showinfo("Winner!!!", "Player2 Wins!!!")
            changestate()
            score2 += 1
            l1.config(text="X:"+str(score1)+"-"+str(score2)+":O")
        elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
            messagebox.showinfo("Winner!!!", "Player2 Wins!!!")
            changestate()
            score2 += 1
            l1.config(text="X:"+str(score1)+"-"+str(score2)+":O")
        elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
            messagebox.showinfo("Winner!!!", "Player2 Wins!!!")
            changestate()
            score2 += 1
            l1.config(text="X:"+str(score1)+"-"+str(score2)+":O")
        elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
            messagebox.showinfo("Winner!!!", "Player2 Wins!!!")
            changestate()
            score2 += 1
            l1.config(text="X:"+str(score1)+"-"+str(score2)+":O")
        elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
            messagebox.showinfo("Winner!!!", "Player2 Wins!!!")
            changestate()
            score2 += 1
            l1.config(text="X:"+str(score1)+"-"+str(score2)+":O")
        elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
            messagebox.showinfo("Winner!!!", "Player2 Wins!!!")
            changestate()
            score2 += 1
            l1.config(text="X:"+str(score1)+"-"+str(score2)+":O")
        elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
            messagebox.showinfo("Winner!!!", "Player2 Wins!!!")
            changestate()
            score2 += 1
            l1.config(text="X:"+str(score1)+"-"+str(score2)+":O")

    
    def b_click(b):
        """
        b_click(b): b=the name of the button where it change the text of the button if it was empty 
        """
        global clicked, count
        if b["text"] == " " and clicked == True:
            l1 = Label(text="PLAYER: 2(O)", height=3, bg="#863FDE",
                       font=("COMIC SANS MS", 10, "bold"), foreground="white")
            l1.grid(row=0, column=0)
            b["text"] = "X"
            b.configure(bg="#863FDE")
            clicked = False
            count += 1
            checkWinner()
        elif b["text"] == " " and clicked == False:
            l1 = Label(text="PLAYER: 1(X)", height=3, font=(
                "COMIC SANS MS", 10, "bold"), bg="#863FDE", foreground="white").grid(row=0, column=0)
            b["text"] = "O"
            b.configure(bg="#9D1D7F")
            clicked = True
            count += 1
            checkWinner()
        else:
            messagebox.showerror("Error", "This Box is already is choosen")
    # creating buttons
    b1 = Button(tp, text=" ", font=("Helvetica", 20), height=3,
                width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
    b2 = Button(tp, text=" ", font=("Helvetica", 20), height=3,
                width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
    b3 = Button(tp, text=" ", font=("Helvetica", 20), height=3, width=6,
                bg="SystemButtonFace", command=lambda: b_click(b3))

    b4 = Button(tp, text=" ", font=("Helvetica", 20), height=3,
                width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
    b5 = Button(tp, text=" ", font=("Helvetica", 20), height=3,
                width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
    b6 = Button(tp, text=" ", font=("Helvetica", 20), height=3,
                width=6, bg="SystemButtonFace", command=lambda: b_click(b6))

    b7 = Button(tp, text=" ", font=("Helvetica", 20), height=3,
                width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
    b8 = Button(tp, text=" ", font=("Helvetica", 20), height=3,
                width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
    b9 = Button(tp, text=" ", font=("Helvetica", 20), height=3,
                width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

    b1.grid(row=2, column=0)
    b2.grid(row=2, column=1)
    b3.grid(row=2, column=2)
    b4.grid(row=3, column=0)
    b5.grid(row=3, column=1)
    b6.grid(row=3, column=2)
    b7.grid(row=4, column=0)
    b8.grid(row=4, column=1)
    b9.grid(row=4, column=2)

    tp.mainloop()


def hs1():
    """
    hs1:Display a window that contain the high score 
    """
    root = tkinter.Tk()
    root.title("tic tac toe ")
    root.geometry("325x480")

    # Background image
    bgli = tkinter.PhotoImage(file="images/bgil2.png")
    mylabel1 = tkinter.Label(root, image=bgli)
    mylabel1.place(x=0, y=0)
    # creating buttons
    highrs = tkinter.Label(root, text="Your High score is :", fg="white", bg="black", font=(
        'Times New Roman', 17, 'bold')).place(x=80, y=100)

    score11 = tkinter.Label(root, text=highs, fg="white", bg="black", font=(
        'Times New Roman', 17, 'bold')).place(x=130, y=140)
    quiti = PhotoImage(file="images/quit1.png")
    """
    back():close hs1 window and open main()
    """
    def back():
        root.destroy()
        main()
    backim = PhotoImage(file="images/backimg.png")
    # back button
    back = tkinter.Button(text="Quit", image=backim, height=40, width=70, bg="#863FDE",
                          command=back, font=("COMIC SANS MS", 10, "bold"), foreground="white")
    back.place(x=55, y=240)
    # exit button
    exitButton = tkinter.Button(text="Quit", image=quiti, bg="#863FDE", command=quit, font=(
        "COMIC SANS MS", 10, "bold"), foreground="white")
    exitButton.place(x=165, y=240)
    root.mainloop()





def create():
    """
    Create():This method create a window for creating an account
    """
    root = tkinter.Tk()
    root.title("Tic Tac Toe")
    root.geometry("305x305")

    def create():
        db = sqlite3.connect('players.db')
        db.execute(
            'CREATE TABLE IF NOT EXISTS players(username TEXT,password TEXT,highs INTEGER)')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM players where username=? AND password=?",
                       (user_inputc.get(), pass_inputc.get()))
        # cursor.execute("""DELETE FROM players WHERE username=:username""",{'username':"admin"})

        row = cursor.fetchall()
        # print(row)
        if row:
            messagebox.showerror('error', 'This username already exist')

        else:

            db.execute("INSERT INTO players(username,password)VALUES(?,?)",
                       (user_inputc.get(), pass_inputc.get()))
            root.destroy()
            mainp()
        cursor.connection.commit()
        db.close()
    # Background image
    bgli = tkinter.PhotoImage(file="images/bgil.png")
    mylabel1 = tkinter.Label(root, image=bgli)
    mylabel1.place(x=0, y=0)

    bgli1 = tkinter.PhotoImage(file="images/create.png")
    mylabel2 = tkinter.Label(root, image=bgli1, bd=0, bg="#18132D")
    mylabel2.place(x=50, y=55)

    # creating input and buttons
    user_inputc = tkinter.StringVar()
    pass_inputc = tkinter.StringVar()
    
    image1 = Image.open("images/button.png")
    test = ImageTk.PhotoImage(image1)
    user = tkinter.Label(image=test, bd=0, bg="#863FDE")
    user.image = test
    user.place(x=55, y=155)
    userinputc = tkinter.Entry(root, textvariable=user_inputc)
    userinputc.place(x=155, y=165)

    pasimg = Image.open("images/passb.png")
    test1 = ImageTk.PhotoImage(pasimg)
    passw = tkinter.Label(image=test1, bd=0, bg="#863FDE")
    passw.image = test
    passw.place(x=55, y=190)
    passwordinput = tkinter.Entry(root, textvariable=pass_inputc, show='*')
    passwordinput.place(x=155, y=200)

    bg2 = tkinter.PhotoImage(file="images/createacc.png")
    b2 = tkinter.Button(root, text="hello", image=bg2,
                        bd=0, bg="#863FDE", command=create)
    b2.place(x=55, y=260)

    def back():
        root.destroy()
        mainp()
    bg3 = tkinter.PhotoImage(file="images/backimg2.png")
    b3 = tkinter.Button(root, text="hello", image=bg3,
                        bd=0, bg="#863FDE", command=back)
    b3.place(x=10, y=5)

    root.mainloop()


def mainp():
    """
    shows the window that contain create an account and signin by your account
    """
    root = tkinter.Tk()
    root.title("Tic Tac Toe")
    root.geometry("305x305")
    # Background image
    bgli = tkinter.PhotoImage(file="images/bgil.png")
    mylabel1 = tkinter.Label(root, image=bgli)
    mylabel1.place(x=0, y=0)

    bgli1 = tkinter.PhotoImage(file="images/welcome.png")
    mylabel2 = tkinter.Label(root, image=bgli1, bd=0, bg="#18132D")
    mylabel2.place(x=50, y=55)

    def recalll1():
        root.destroy()
        create()

    def recall1():
        root.destroy()
        signin()
    bg2 = tkinter.PhotoImage(file="images/createacc.png")
    b2 = tkinter.Button(root, text="hello", image=bg2,
                        bd=0, bg="#863FDE", command=recalll1)
    b2.place(x=55, y=220)

    bg3 = tkinter.PhotoImage(file="images/SIGNUP2.png")
    b3 = tkinter.Button(root, text="hello", image=bg3,
                        bd=0, bg="#863FDE", command=recall1)
    b3.place(x=55, y=160)

    root.mainloop()


mainp()
