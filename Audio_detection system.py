import tkinter as tk
from tkinter import *
from tkinter import messagebox
import speech_recognition as sr
from PIL import ImageTk,Image
from tkinter import ttk
import mysql.connector
import cv2


connection = mysql.connector.connect(host="localhost", user="root", password="welcome123456", db="Audio_detection")
cursor = connection.cursor()
cursor.execute("create table if not exists Login_table(Scode varchar(4) PRIMARY KEY, username varchar(30) NOT NULL, email varchar(80) NOT NULL, password varchar(30) NOT NULL, confirm_pwd varchar(30) NOT NULL, gender varchar(10) NOT NULL)")
with open('abi123.txt','r') as f:
    question_paper = f.read()

# Initialize the speech recognizer
r = sr.Recognizer()

# Define a function to perform speech recognition on audio input
def recognize_speech(audio):
    # Convert the recorded audio to text
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
        
        # Check for word matches with the question paper
        text = text.lower() # convert to lowercase for case-insensitive matching
        for word in text.split():
            if word in question_paper:
                # Display a prompt in the GUI
                root = tk.Tk()
                root.withdraw()
                messagebox.showwarning("Warning", "The person is trying to copy!")
                break
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


def start_recording():
    main_screen.destroy()
    with sr.Microphone() as source:
        root = tk.Tk()
        root.withdraw()
        messagebox.showwarning("Audio is being detected!")
        while True:
            try:
                audio = r.listen(source, timeout=1, phrase_time_limit=5) # listen for up to 5 seconds of audio at a time
                recognize_speech(audio)
            except sr.WaitTimeoutError:
                pass
            except KeyboardInterrupt:
                break




def Register():
  global Register
  Register_screen=Toplevel()
  Register_screen.geometry('800x450')
  Register_screen.config(bg="white")
  #Register_screen.iconbitmap(r"C:\Users\Dell\Desktop\Moonsun hospital\background\hospital-2_icon-icons.com_66067.ico")
  #Register_screen_img =ImageTk.PhotoImage(Image.open(r"C:\Users\Dell\Desktop\Moonsun hospital\background\Different Pills And Equipment At Paper.jpeg"))
  #lbl = Label(Register_screen,image =Register_screen_img)
  #lbl.image =Register_screen_img
  #lbl.grid(column=0, row=3)
  Register_screen.title('Account Register')

  username=StringVar()
  email=StringVar()
  password=StringVar()
  confirm_password=StringVar()
  ECODE1=StringVar()
  #var=StringVar()

  l_screen_img =ImageTk.PhotoImage(Image.open(r"3409297.jpg"))
  l = Label(Register_screen,image =l_screen_img)
  l.image =l_screen_img
  l.pack(side=RIGHT)
  
  Label(Register_screen, text="CODE",bg="white",font=("Times New Roman",10)).place(x=50,y=100)
  username_login_entry = Entry(Register_screen, textvariable=ECODE1)
  username_login_entry.place(x=200,y=100)
  Label(Register_screen, text="USERNAME",bg="white",font=("Times New Roman",10)).place(x=50,y=125)
  email_login_entry = Entry(Register_screen, textvariable=username)
  email_login_entry.place(x=200,y=125)
  Label(Register_screen, text="EMAIL",bg="white",font=("Times New Roman",10)).place(x=50,y=150)
  email_login_entry = Entry(Register_screen, textvariable=email)
  email_login_entry.place(x=200,y=150)
  Label(Register_screen, text="PASSWORD:",bg="white",font=("Times New Roman",10)).place(x=50,y=175)
  password__login_entry = Entry(Register_screen, textvariable=password, show= '*')
  password__login_entry.place(x=200,y=175)
  Label(Register_screen, text="CONFIRM PASSWORD:",bg="white",font=("Times New Roman",10)).place(x=50,y=200)
  confirmpassword__login_entry = Entry(Register_screen, textvariable=confirm_password, show= '*')
  confirmpassword__login_entry.place(x=200,y=200)
  gen=IntVar()
  Label(Register_screen, text="GENDER:",bg="white",font=("Times New Roman",10)).place(x=50,y=225)
  Radiobutton(Register_screen,text="Male",padx=5,variable=gen,value=1,font=("Times New Roman",10),bg="white").place(x=200,y=225)
  Radiobutton(Register_screen,text='Female',padx=10,variable=gen,value=2,font=("Times New Roman",10),bg="white").place(x=300,y=225)
  Label(Register_screen,text="REGISTER",font=("Times New Roman",20),bg="white").place(x=50,y=50)
  
  def submit():
    if password.get()==confirm_password.get():
        if gen.get() == 1:
            gender = "male"
        else:
            gender = "female"

        
        query="insert into Login_table(Scode,username,email,password,confirm_pwd,gender)values(%s,%s,%s,%s,%s,%s)"
        values1=(ECODE1.get(),username.get(),email.get(),password.get(),confirm_password.get(),gen.get())

        cursor.execute(query,values1)
        Register_screen.destroy()
        start_recording()
        
    else:
      messagebox.showerror("REGISTRATION ERROR","confirmation password and password doesnt match")
    connection.commit()
    cursor.close()
    connection.close()
  Label(Register_screen,text="Aldready have an account?",bg="white",font=("Times New Roman",10)).place(x=100,y=350)
  BUT1=Button(Register_screen,text="Register", height=2, width=8,bg="#AFF8DB",command=submit,borderwidth=0).place(x=175, y=265 )
  Button(Register_screen,text="SIGN IN",height=1,width=6,bg="white",borderwidth=0,command=login,fg="Blue").place(x=250,y=350)  


def login():
  global login
  username=StringVar()
  email=StringVar()
  password=StringVar()
  confirm_password=StringVar()
  ECODE1=StringVar()
  #var=StringVar()
  login_screen=Toplevel()
  login_screen.geometry('800x450')
  login_screen.title('Account Login')
  login_screen.config(bg="white")
  #login_screen.iconbitmap(r"C:\Users\Dell\Desktop\Moonsun hospital\background\hospital-2_icon-icons.com_66067.ico")
  login_screen_img =ImageTk.PhotoImage(Image.open(r"5135289.jpg"))
  lb2 = Label(login_screen,image =login_screen_img)
  lb2.image =login_screen_img
  lb2.pack(side=RIGHT)
  Label(login_screen,text="LOGIN",bg="white",font=("Times New Roman",20)).place(x=100,y=50)
  Label(login_screen,text="LOGIN",bg="white",font=("Times New Roman",10))
  Label(login_screen, text="USERNAME",bg="white",font=("Times New Roman",10)).place(x=100,y=100)
  username_login_entry = Entry(login_screen, textvariable="username",width=40)
  username_login_entry.place(x=100,y=125)
  Label(login_screen, text="PASSWORD",bg="white").place(x=100,y=150)
  ll=Label(login_screen,text='''Don't have an account?''',bg='white',font=("Times New Roman",10)).place(x=100,y=300)
  password__login_entry = Entry(login_screen, textvariable="password", show= '*',width=40)
  password__login_entry.place(x=100,y=175)
  def OK():
    username = username_login_entry.get()
    password = password__login_entry.get()
    
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="welcome123456",database="Audio_detection")
    cursor = mydb.cursor()
    
    savequery = "SELECT * FROM Login_table WHERE username=%s AND password=%s"
     # Get the records with these username and password ONLY
    cursor.execute(savequery,(username,password)) 
    myresult = cursor.fetchone() 
    
    if myresult: # If there is such a record, then success
        messagebox.showerror("LOGIN ERROR","LOGIN ERROR")
        # Whatever you want to do after user is authentic

    else:
        login_screen.destroy()
        start_recording()
        
    cursor.close()
    mydb.close()
  Button(login_screen,text="Login", height=2, width=8,bg="#A9A7A7",command=OK,borderwidth=0).place(x=250 , y = 200 )
  Button(login_screen,text="SIGN UP",height=1,width=6,bg="white",borderwidth=0,command=Register,fg="Blue").place(x=250,y=300)  



main_screen=Tk()
main_screen.geometry('800x450')
main_screen.config(bg = "white" )
#main_screen_HEADING = ImageTk.PhotoImage(Image.open(r"C:\Users\Dell\Desktop\Moonsun hospital\background\Untitled H.png"))
#Label(main_screen,image = main_screen_HEADING).pack()
#main_screen.iconbitmap(r"C:\Users\Dell\Desktop\Moonsun hospital\background\hospital-2_icon-icons.com_66067.ico")
main_screen.title("WELCOME TO AGM MANTRA")
main_screen_img = ImageTk.PhotoImage(Image.open(r"5559852.jpg"))
#login_button_img = ImageTk.PhotoImage(Image.open(r"C:\Users\Dell\Desktop\Moonsun hospital\background\icons8-login-32.png"))
#register_button_img= ImageTk.PhotoImage(Image.open(r"C:\Users\Dell\Desktop\Moonsun hospital\background\icons8-register-32.png"))
Label(text="",image = main_screen_img ,bg="white").pack(side=LEFT)
Button(main_screen,text="ADMIN", height=3, width=20,bg="#0080E5",compound="left",borderwidth=0,command=login).place(x=550,y=150)
Button(text="USER", height=3,bg="#A9A7A7", width=20,compound="left",borderwidth=0,command=login).place(x=550,y=220)
ll=Label(main_screen,text='''choose between two to login''',bg='white',font=("Times New Roman",12)).place(x=450,y=275)
l=Label(main_screen,text='''Welcome to AGM Mantra,Please put your login credentials
        below to start using the app''',bg='white',font=("Times New Roman",10)).place(x=450,y=100)
username=StringVar()
email=StringVar()
password=StringVar()
var=IntVar()
main_screen.mainloop()

