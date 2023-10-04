#IMPORTING LIBRARIES
import random
import tkinter
from tkinter import*
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from tkinter.messagebox import *
from tkinter.filedialog import *
import os


#REGISTER DATABASE FUNCTION
def reg_database():
 
    #GETTING DATA FRO ENTRIES
    name = entry1.get()
    userd = entry2.get()
    email = entry3.get()
    dob = entry4.get()
    passd = entry5.get()
    conpass = entry6.get()
    
    #TURNING USER DATA TO TUPLE FOR SQL USE
    usertup = (userd,)

    #LOOP FOR CHECKING IF ALL ENTRIES ARE PROVIDED IN CORRECT WAY AND ALSO RUNNING MYSQL CONNECTOR
    if name == "" or userd == "" or email == "" or dob == "" or passd == "" or conpass == "":
        messagebox.showerror("Error", "All Feilds Are Required")
    elif passd != conpass:
        messagebox.showerror("Error", "Password and Confirmed Password are not same")
    else:
        
        db = mysql.connector.connect(host="localhost", user="root", passwd="123456", auth_plugin='mysql_native_password')
        create_bd = db.cursor()
        create_bd.execute("CREATE DATABASE IF NOT EXISTS MULTIVERSE")
        create_bd.execute("USE MULTIVERSE")
        create_bd.execute("create table if not exists records(user varchar(10) primary key, password varchar(10))")
        create_bd.execute("select * from records where user=%s",usertup)
        row = create_bd.fetchone()
        if row != None:
            messagebox.showerror("Error", "Username Already Exists")
        else:
            create_bd.execute("insert into records (user,password) values(%s, %s)",(userd, passd))
            db.commit()
            messagebox.showinfo("Sucess","Successfully Registered")
            register_screen.destroy()
            mainbody()
        db.commit()


#LOGIN DATABASE FUNCTION
def log_database():
    
    #GETTING DATA FROM ENTRIES
    loguser = entry7.get()
    logpass = entry8.get()

    #TURING THE DATA TO TUPLE FOR SQL USE
    log_tup = (loguser, logpass)

    #LOOP FOR CHECKING IF ALL ENTRIES ARE PROVIDED IN CORRECT WAY AND ALSO RUNNING MYSQL CONNECTOR
    if loguser == "" or logpass == "":
        messagebox.showerror("Error", "All Feilds Are Required")
    else:
        db = mysql.connector.connect(host="localhost", user="root", passwd="123456", auth_plugin='mysql_native_password')
        create_bd = db.cursor()
        create_bd.execute("CREATE DATABASE IF NOT EXISTS MULTIVERSE")
        create_bd.execute("USE MULTIVERSE")
        create_bd.execute("create table if not exists records(user varchar(10) primary key, password varchar(10))")
        create_bd.execute("select * from records where user=%s and password=%s",log_tup)
        row = create_bd.fetchone()
        if row == None:
            messagebox.showerror("Error","User Doesn't Exist")
        else:
            messagebox.showinfo("Success","Welcome Back")
            login_screen.destroy()
            mainbody()
        db.commit()


#CALCULATOR FUNCTION
def cal():

    #NUMBER FOR OPERATION
    global expression
    expression = ""
    
    # FUNCTION TO UPDATE 'expression'
    def press(num):
        global expression
        expression = expression + str(num)
        equation.set(expression)

    
    #FUNCTION TO EVALUATE 'expression'
    def equalpress():
        try:
            global expression
            total = str(eval(expression))
            equation.set(total)
            expression = ""

        except:

            equation.set(" error ")
            expression = ""

    #FUNCTION TO CLEAR THE ENTRY BOX
    def clear():
        global expression
        expression = ""
        equation.set("")

    # Window Code
    if __name__ == "__main__":
 
        #INITIALIZING SCREEN
        gui = Tk()

        #BACKGROUND COLOR
        gui.configure(background="light green")

        #SCREEN TITLE
        gui.title("Simple Calculator")

        #SCREEN SIZE
        gui.geometry("270x150")

        #ENTRY BOX
        equation = StringVar() 
        expression_field = Entry(gui, textvariable=equation)
        expression_field.grid(columnspan=4, ipadx=70)

        #bUTTONS
        button1 = Button(gui, text=' 1 ', fg='black', bg='red', command=lambda: press(1), height=1, width=7)
        button1.grid(row=2, column=0)

        button2 = Button(gui, text=' 2 ', fg='black', bg='red', command=lambda: press(2), height=1, width=7)
        button2.grid(row=2, column=1)

        button3 = Button(gui, text=' 3 ', fg='black', bg='red', command=lambda: press(3), height=1, width=7)
        button3.grid(row=2, column=2)

        button4 = Button(gui, text=' 4 ', fg='black', bg='red', command=lambda: press(4), height=1, width=7)
        button4.grid(row=3, column=0)

        button5 = Button(gui, text=' 5 ', fg='black', bg='red', command=lambda: press(5), height=1, width=7)
        button5.grid(row=3, column=1)

        button6 = Button(gui, text=' 6 ', fg='black', bg='red', command=lambda: press(6), height=1, width=7)
        button6.grid(row=3, column=2)

        button7 = Button(gui, text=' 7 ', fg='black', bg='red', command=lambda: press(7), height=1, width=7)
        button7.grid(row=4, column=0)

        button8 = Button(gui, text=' 8 ', fg='black', bg='red', command=lambda: press(8), height=1, width=7)
        button8.grid(row=4, column=1)

        button9 = Button(gui, text=' 9 ', fg='black', bg='red', command=lambda: press(9), height=1, width=7)
        button9.grid(row=4, column=2)

        button0 = Button(gui, text=' 0 ', fg='black', bg='red', command=lambda: press(0), height=1, width=7)
        button0.grid(row=5, column=0)

        plus = Button(gui, text=' + ', fg='black', bg='red', command=lambda: press("+"), height=1, width=7)
        plus.grid(row=2, column=3)

        minus = Button(gui, text=' - ', fg='black', bg='red', command=lambda: press("-"), height=1, width=7)
        minus.grid(row=3, column=3)

        multiply = Button(gui, text=' * ', fg='black', bg='red', command=lambda: press("*"), height=1, width=7)
        multiply.grid(row=4, column=3)

        divide = Button(gui, text=' / ', fg='black', bg='red', command=lambda: press("/"), height=1, width=7)
        divide.grid(row=5, column=3)

        equal = Button(gui, text=' = ', fg='black', bg='red', command=equalpress, height=1, width=7)
        equal.grid(row=5, column=2)

        clear = Button(gui, text='Clear', fg='black', bg='red', command=clear, height=1, width=7)
        clear.grid(row=5, column='1')

        Decimal = Button(gui, text='.', fg='black', bg='red', command=lambda: press('.'), height=1, width=7)
        Decimal.grid(row=6, column=0)

        #FINALIZING SCREEN
        gui.mainloop()


#NOTEPAD FUNCTION
def note():
    class Notepad:

        #INITIALIZING SCREEN
        __root = Tk()

        #SCREEN SIZE
        __thisWidth = 300
        __thisHeight = 300
        __thisTextArea = Text(__root)
        __thisMenuBar = Menu(__root)
        __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
        __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
        __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)
        
        #ADDING SCROLLBAR
        __thisScrollBar = Scrollbar(__thisTextArea)	
        __file = None

        def __init__(self,**kwargs):
            try:
                    self.__root.wm_iconbitmap("Notepad.ico")
            except:
                    pass

            try:
                self.__thisWidth = kwargs['width']
            except KeyError:
                pass

            try:
                self.__thisHeight = kwargs['height']
            except KeyError:
                pass

            #SCREEN TITLE
            self.__root.title("Untitled - Notepad")

            #CENTERING THE SCREEN
            screenWidth = self.__root.winfo_screenwidth()
            screenHeight = self.__root.winfo_screenheight()
        
            #LEFT ALIGN THE TEXT
            left = (screenWidth / 2) - (self.__thisWidth / 2)
            
            #RIGHT ALIGN THE TEXT
            top = (screenHeight / 2) - (self.__thisHeight /2)
            
            #TOP AND BOTTOM ALIGN TEXT
            self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, self.__thisHeight, left, top))

            #MAKING THE TEXT AREA AUTO RRESIZE
            self.__root.grid_rowconfigure(0, weight=1)
            self.__root.grid_columnconfigure(0, weight=1)

            #ADDING CONTOLS
            self.__thisTextArea.grid(sticky = N + E + S + W)
            
            #NEW FILE
            self.__thisFileMenu.add_command(label="New", command=self.__newFile)
            
            #OPEN A FILE
            self.__thisFileMenu.add_command(label="Open", command=self.__openFile)
            
            #SAVE FILE
            self.__thisFileMenu.add_command(label="Save", command=self.__saveFile)

            #CREATING A LINE 	
            self.__thisFileMenu.add_separator()										
            self.__thisFileMenu.add_command(label="Exit", command=self.__quitApplication)
            self.__thisMenuBar.add_cascade(label="File", menu=self.__thisFileMenu)	
            
            #CUT FEATURE
            self.__thisEditMenu.add_command(label="Cut", command=self.__cut)			
        
            #COPY FEATURE
            self.__thisEditMenu.add_command(label="Copy", command=self.__copy)		
            
            #PASTE FEATURE
            self.__thisEditMenu.add_command(label="Paste", command=self.__paste)		
            
            #EDITING FEATURE
            self.__thisMenuBar.add_cascade(label="Edit", menu=self.__thisEditMenu)	
            
            #DESCRIPTION ABOUT NOTEPAD
            self.__thisHelpMenu.add_command(label="About Notepad", command=self.__showAbout)
            self.__thisMenuBar.add_cascade(label="Help",menu=self.__thisHelpMenu)

            self.__root.config(menu=self.__thisMenuBar)

            self.__thisScrollBar.pack(side=RIGHT,fill=Y)				
            
            #SCROLLER AUTO RESIZE	
            self.__thisScrollBar.config(command=self.__thisTextArea.yview)	
            self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)
        
        #EXIT
        def __quitApplication(self):
            self.__root.destroy()

        #DESCRIPTION
        def __showAbout(self):
            showinfo("Notepad","Mehyul, Krapanshu, Aaush")

        #OPEN FILE
        def __openFile(self):
            
            self.__file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

            if self.__file == "":
                
                # no file to open
                self.__file = None
            else:
                
                # Try to open the file
                self.__root.title(os.path.basename(self.__file) + " - Notepad")
                self.__thisTextArea.delete(1.0,END)

                file = open(self.__file,"r")

                self.__thisTextArea.insert(1.0,file.read())

                file.close()

        #NEW FILE  
        def __newFile(self):
            self.__root.title("Untitled - Notepad")
            self.__file = None
            self.__thisTextArea.delete(1.0,END)

        #SAVE FILE
        def __saveFile(self):

            if self.__file == None:
                # Save as new file
                self.__file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])

                if self.__file == "":
                    self.__file = None
                else:
                    
                    # Try to save the file
                    file = open(self.__file,"w")
                    file.write(self.__thisTextArea.get(1.0,END))
                    file.close()
                    
                    self.__root.title(os.path.basename(self.__file) + " - Notepad")
                    
                
            else:
                file = open(self.__file,"w")
                file.write(self.__thisTextArea.get(1.0,END))
                file.close()

        #CUT
        def __cut(self):
            self.__thisTextArea.event_generate("<<Cut>>")

        #COPY
        def __copy(self):
            self.__thisTextArea.event_generate("<<Copy>>")

        #PASTE
        def __paste(self):
            self.__thisTextArea.event_generate("<<Paste>>")

        def run(self):

            #FINALIZING SCREEN
            self.__root.mainloop()




    # Run main window
    notepad = Notepad(width=600,height=400)
    notepad.run()                                                                         


#STONE,PAPER SCISSOR FUNCTION
def sps():
	#INITALIZING SCREEN
	toot = Tk()

	#SCREEN SIZE
	toot.geometry("300x300")

	#SCREEN TITLE
	toot.title("Rock Paper Scissor Game")

	#VALUES FOR ROCK, PAPER AND SCISSOR
	computer_value = {
		"0": "Rock",
		"1": "Paper",
		"2": "Scissor"
	}

	#RESTART
	def reset_game():
		b1["state"] = "active"
		b2["state"] = "active"
		b3["state"] = "active"
		l1.config(text="Player")
		l3.config(text="Computer")
		l4.config(text="")

	#DISABLE FUNCTION
	def button_disable():
		b1["state"] = "disable"
		b2["state"] = "disable"
		b3["state"] = "disable"

	#RULE IF PLAYER PLAYED ROCK
	def isrock():
		c_v = computer_value[str(random.randint(0, 2))]
		if c_v == "Rock":
			match_result = "Match Draw"
		elif c_v == "Scissor":
			match_result = "Player Win"
		else:
			match_result = "Computer Win"
		l4.config(text=match_result)
		l1.config(text="Rock		 ")
		l3.config(text=c_v)
		button_disable()

	#RULE IF PLAYER PLAYED PAPER
	def ispaper():
		c_v = computer_value[str(random.randint(0, 2))]
		if c_v == "Paper":
			match_result = "Match Draw"
		elif c_v == "Scissor":
			match_result = "Computer Win"
		else:
			match_result = "Player Win"
		l4.config(text=match_result)
		l1.config(text="Paper		 ")
		l3.config(text=c_v)
		button_disable()

	#RULE IF PLAYER PLAYED SCISSOR
	def isscissor():
		c_v = computer_value[str(random.randint(0, 2))]
		if c_v == "Rock":
			match_result = "Computer Win"
		elif c_v == "Scissor":
			match_result = "Match Draw"
		else:
			match_result = "Player Win"
		l4.config(text=match_result)
		l1.config(text="Scissor		 ")
		l3.config(text=c_v)
		button_disable()

	#ADDING LABLES, FRAMES AND BUTTONS 
	Label(toot, text="Rock Paper Scissor", font="normal 20 bold", fg="blue").pack(pady=20)

	frame = Frame(toot)
	frame.pack()

	l1 = Label(frame,text="Player			 ",font=10)

	l2 = Label(frame,text="VS			 ",font="normal 10 bold")

	l3 = Label(frame, text="Computer", font=10)

	l1.pack(side=LEFT)
	l2.pack(side=LEFT)
	l3.pack()

	l4 = Label(toot, text="", font="normal 20 bold", bg="white", width=15, borderwidth=2, relief="solid")
	l4.pack(pady=20)

	frame1 = Frame(toot)
	frame1.pack()

	b1 = Button(frame1, text="Rock", font=10, width=7, command=isrock)

	b2 = Button(frame1, text="Paper ", font=10, width=7, command=ispaper)

	b3 = Button(frame1, text="Scissor", font=10, width=7, command=isscissor)

	b1.pack(side=LEFT, padx=10)
	b2.pack(side=LEFT, padx=10)
	b3.pack(padx=10)

	Button(toot, text="Reset Game", font=10, fg="red", bg="black", command=reset_game).pack(pady=20)

	#FINALIZING SCREEN
	toot.mainloop()


#COLOR GAME FUNCTION
def color_game():

    #LIST OF COLORS
    colours = ['Red', 'Blue', 'Green', 'Pink', 'Black','Yellow', 'Orange', 'White', 'Purple', 'Brown']

    global score
    global timeleft
 
    score = 0

    #STARTIMG TIME
    timeleft = 30

    #FUNCTION TO START THE GAME
    def startGame(event):

        if timeleft == 30:

            #START THE TIMER
            countdown()

        #STARTING FUNCTION TO CHOOSE COLOR
        nextColour()

    
    #FUNCTION TO CHOOSE COLOR
    def nextColour():
        global score
        global timeleft

        if timeleft > 0:
            e.focus_set()

            #LOOP FOR GIVING SCORE
            if e.get().lower() == colours[1].lower():
                score += 1

            #CLEARING TEXTBOX
            e.delete(0, tkinter.END)

            random.shuffle(colours)

            #CHANGING THE TEXT TO RANDOM COLOR
            label.config(fg=str(colours[1]), text=str(colours[0]))

            #UPDATING SCORE
            scoreLabel.config(text="Score: " + str(score))

    #TIME FUNCTION
    def countdown():
        global timeleft
        if timeleft > 0:

            #DECREASING TIME
            timeleft -= 1

            #UPDATING TIME LABLE
            timeLabel.config(text="Time left: "+ str(timeleft))

            #REPAT THE FUNCTION AGAIN IN 1 SECOND
            timeLabel.after(1000, countdown)

    # INITIALIZING SCREEN
    boot = tkinter.Tk()

    #SCREEN TITLE
    boot.title("COLORGAME")

    #SCREEN SIZE
    boot.geometry("375x200")

    #ADDING RULES
    instructions = tkinter.Label(boot, text="Type in the colour""of the words, and not the word text!",font=('Helvetica', 12))
    instructions.pack()

    #ADDING SCORE
    scoreLabel = tkinter.Label(boot, text="Press enter to start",font=('Helvetica', 12))
    scoreLabel.pack()

    #ADDING TIMELEFT 
    timeLabel = tkinter.Label(boot, text="Time left: "+str(timeleft), font=('Helvetica', 12))
    timeLabel.pack()

    #ADDING TITLE FOR FEILD
    label = tkinter.Label(boot, font=('Helvetica', 60))
    label.pack()

    #ADDING ENTRY 
    e = tkinter.Entry(boot)

    #RUN THE 'startGame' FUNCTION
    boot.bind('<Return>', startGame)
    e.pack()

    #SETIING FOCUS ON ENTRY
    e.focus_set()

    #FINALIZING SCREEN
    boot.mainloop()


#REGISTER SCREEN FUNCTION
def register():
    
    #INITIALIZING SCREEN
    global register_screen
    register_screen = tk.Tk()
    
    #SIZE AND TITLE OF SCREEN
    size = register_screen.geometry("1280x720+0+0")
    name = register_screen.title("Multiverse")

    #ADDIN BACKGROUND IMAGE
    img = ImageTk.PhotoImage(file="images/back.jpg",master=register_screen)
    bglb = tk.Label(register_screen, image=img)
    bglb.place(x=0,y=0, relheight=1, relwidth=1)

    #ADDING AREA FOR FEILDS
    frame1 = Frame(register_screen, bg="white")
    frame1.place(x=480, y=100, width=700, height=500)

    #ADDING BACKGROUND
    log_img = ImageTk.PhotoImage(file='images/log.png',master=register_screen)
    log_place = Label(register_screen,image=log_img)
    log_place.place(x=80, y=100, width=400, height=500)

    #ADDING TITLE FOR FEILD 
    global username
    global password
    username = StringVar()
    password = StringVar()
    title1 = Label(frame1, text="REGISTER HERE", bg="white", fg="green",font=("times new roman", 20, "bold")).place(x=50, y=48)
    feild1 = Label(frame1, text="FULL NAME", bg="white", fg="black",font=("times new roman", 10, "bold")).place(x=50, y=128)
    feild2 = Label(frame1, text="USER NAME", bg="white", fg="black",font=("times new roman", 10, "bold")).place(x=400, y=128)
    feild3 = Label(frame1, text="EMAIL", bg="white", fg="black",font=("times new roman", 10, "bold")).place(x=50, y=208)
    feild4 = Label(frame1, text="DATE OF BIRTH", bg="white", fg="black",font=("times new roman", 10, "bold")).place(x=400, y=208)
    feild5 = Label(frame1, text="PASSWORD", bg="white", fg="black",font=("times new roman", 10, "bold")).place(x=50, y=288)
    feild6 = Label(frame1, text="COMFIRM PASSWORD", bg="white", fg="black", font=("times new roman", 10, "bold")).place(x=400, y=288)
    
    #ADDING PLACE TO ENTER THE FEILDS
    global entry1
    global entry2
    global entry3
    global entry4
    global entry5
    global entry6
    entry1 = Entry(frame1, font=('times new roman', 15),bg='lightgrey')
    entry1.place(x=50, y=158, width=250)
    entry2 = Entry(frame1,textvariable=username,font=('times new roman', 15),bg='lightgrey')
    entry2.place(x=400, y=158, width=250)
    entry3 = Entry(frame1, font=('times new roman', 15),bg='lightgrey')
    entry3.place(x=50, y=238, width=250)
    entry4 = Entry(frame1, font=('times new roman', 15),bg='lightgrey')
    entry4.place(x=400, y=238, width=250)
    entry5 = Entry(frame1,textvariable=password,show='*',font=('times new roman', 15),bg='lightgrey')
    entry5.place(x=50, y=318, width=250)
    entry6 = Entry(frame1, font=('times new roman', 15),bg='lightgrey')
    entry6.place(x=400, y=318, width=250)

    #ADDING AGREE TO TERMS AND CONDITIONS BUTTON
    agreebutton = Checkbutton(frame1, text="I Agree To All The Terms And Conditions", onvalue=1, offvalue=0, font=('times new roman', 14), bg='white', cursor='hand2')
    agreebutton.place(x=50, y=378)

    #ADDING THE REGISTER BUTTON
    reg_img = ImageTk.PhotoImage(file='images/button.jpg',master=register_screen)
    reg_but = Button(frame1, image=reg_img,command=lambda:[reg_database()], bd=0,cursor='hand2').place(x=400, y=400)

    #ADDING LOGIN BUTTON
    log_info = Label(register_screen, text='If You Already Have An Account, Please Login Below', font=('times new roman', 10), bg='black', fg='orange').place(x=160, y=460)
    log_button = Button(register_screen, text='Login',command=login, font=('times new roman', 15),bg='black', fg='orange', bd=0, cursor='hand2').place(x=235, y=500)
    
    #DESTROYING PREVIOUS SCREEN
    root.destroy()

    #FINALIZING SCREEN
    register_screen.mainloop()


#LOGIN IN SCREEN FUNCTION
def login():

    #INITIALIZING SCREEN
    global login_screen
    login_screen = tk.Tk()
    
    #SIZE AND TITLE OF SCREEN
    size = login_screen.geometry("1280x720+0+0")
    name = login_screen.title("Multiverse")

    #ADDIN BACKGROUND IMAGE
    img = ImageTk.PhotoImage(file="images/back.jpg", master=login_screen)
    bglb = tk.Label(login_screen, image=img)
    bglb.place(x=0, y=0, relheight=1, relwidth=1)

    #ADDING AREA FOR FEILDS
    frame1 = Frame(login_screen, bg="white")
    frame1.place(x=480, y=100, width=700, height=500)

    #ADDING BACKGROUND
    log_img = ImageTk.PhotoImage(file='images/log.png', master=login_screen)
    log_place = Label(login_screen, image=log_img)
    log_place.place(x=80, y=100, width=400, height=500)

    #ADDING TITLE FOR THE FEILDS
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    title1 = Label(frame1, text="LOGIN", bg="white", fg="green", font=("times new roman", 20, "bold")).place(x=50, y=48)
    feild1 = Label(frame1, text="USER NAME", bg="white", fg="black", font=("times new roman", 10, "bold")).place(x=50, y=128)
    feild2 = Label(frame1, text="PASSWORD", bg="white", fg="black", font=("times new roman", 10, "bold")).place(x=50, y=221)
    
    #ADDING PLACE TO ENTER THE FEILDS
    global entry7
    global entry8
    entry7 = Entry(frame1, font=('times new roman', 15),bg='lightgrey',textvariable=username_verify)
    entry7.place(x=50, y=158, width=250)
    entry8 = Entry(frame1, font=('times new roman', 15),bg='lightgrey',textvariable=password_verify,show='*')
    entry8.place(x=50, y=251, width=250)

    #ADDING AGREE TO TERMS AND CONDITIONS BUTTON
    agreebutton = Checkbutton(frame1, text="I Agree To All The Terms And Conditions", onvalue=1, offvalue=0, font=('times new roman', 14), bg='white', cursor='hand2').place(x=50, y=321)

    #ADDING THE LOGIN BUTTON
    reg_img = ImageTk.PhotoImage(file='images/log.jpeg',master=login_screen)
    reg_but = Button(frame1, image=reg_img,command=lambda:[log_database()], bd=0,cursor='hand2').place(x=410, y=400)

    #ADDING REGISTER BUTTON
    log_info = Label(login_screen, text='If You Dont Have An Account, Please Create Below', font=('times new roman', 10), bg='black', fg='orange').place(x=160, y=460)
    log_button = Button(login_screen,command=register, text='SIGN IN', font=('times new roman', 15),bg='black', fg='orange', bd=0, cursor='hand2').place(x=235, y=500)

    #DESTROYING PREVIOUS SCREEN
    root.destroy()

    #FINALIZING THE SCREEN
    login_screen.mainloop()


#MAIN SCREEN FUNCTION
def mainbody():

    #INITIALIZING SCREEN
    global select_screen
    select_screen = tk.Tk()
    
    #SIZE AND TITLE OF SCREEN
    size = select_screen.geometry("1280x720+0+0")
    name = select_screen.title("Multiverse")

    #ADDIN BACKGROUND IMAGE
    img = ImageTk.PhotoImage(file="images/back.jpg", master=select_screen)
    bglb = tk.Label(select_screen, image=img)
    bglb.place(x=0, y=0, relheight=1, relwidth=1)

    #ADDING AREA FOR FEILDS
    frame1 = Frame(select_screen, bg="white")
    frame1.place(x=80, y=100, width=1100, height=500)
    
    #ADDING TITLE
    title1 = Label(frame1, text="SELECT YOUR OPERATIONS", bg="white", fg="green",font=("times new roman", 20, "bold")).place(x=50, y=48)

    #ADDING BUTTONS FOR OPERTIONS
    but1 = Button(frame1, text="Calculator", command=lambda: [cal()], font=('times new roman', 40), fg='Red').place(x=50, y=150)
    but2 = Button(frame1, text="Color Game", command=lambda:[color_game()],font=('times new roman', 40), fg='Blue').place(x=400, y=150)
    but3 = Button(frame1, text="Notepad", command=lambda: [note()], font=('times new roman', 40), fg='Black').place(x=800, y=150)
    but4 = Button(frame1, text="Stone, Paper, Scissor", command=lambda: [sps()], font=('times new roman', 40), fg='Orange').place(x=100, y=300)
    
    #FINALIZING SCREEN
    select_screen.mainloop()


#STARTING SCREEN FUNCTION
def main_screen():
    
    #INITIATING SCREEN
    global root
    root = tk.Tk()
    
    #SIZE AND TITLE OF SCREEN
    size = root.geometry("1280x720+0+0")
    name = root.title("Multiverse")

    #ADDIN BACKGROUND IMAGE
    img = ImageTk.PhotoImage(file='images/back.jpg')
    back = Label(image=img)
    back.place(x=0, y=0, relwidth=1, relheight=1)

    #ADDING AREA FOR FEILDS
    frame1 = Frame(root, bg="white")
    frame1.place(x=480, y=100, width=700, height=500)

    #ADDING BACKGROUND
    log_img = ImageTk.PhotoImage(file='images/log.png')
    log_place = Label(image=log_img)
    log_place.place(x=80, y=100, width=400, height=500)

    #ADDING TITLE TO THE ABOVE CREATED AREA AND ASLO ADDING FEILD NAMES TO IT
    title1 = Label(frame1, text="Select Your Choice", bg="white", fg="green",font=("times new roman", 20, "bold")).place(x=240, y=48)

    #ADDING THE REGISTER AND LOGIN BUTTONS
    reg_but = Button(frame1,text="REGISTER",font=('times new roman',40),bd=0,cursor='hand2',command=register).place(x=200, y=150)
    log_but = Button(frame1, text="LOGIN", font=('times new roman', 40), bd=0, cursor='hand2',width=10,command=login).place(x=200, y=330)
    root.mainloop()


#STARTING THE CODE
main_screen()
