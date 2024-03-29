from tkinter import *  #* means importing everything from tkinter. tkinter is a python library used for developing GUI
from tkinter import messagebox
from mydb1 import Database
from myAPI import API
import json


class NLPApp:
    def __init__(self):
        # login ka gui load karna
        self.dbo = Database()
        self.apio=API()
        self.root = Tk()  # this is Tk class ka object. Root is a variable of NLPApp class and it is also the object of Tk
        self.root.title("NLPApp")  #using methods from Tk class
        self.root.iconbitmap("Resources/favicon.ico")  #we have to convert the png into favicon.ico
        self.root.geometry("350x600")
        self.root.configure(bg='#c9dd65')

        self.login_gui()
        self.root.mainloop()  # mainloop ki wajah se GUI hold rahega screen par

    def login_gui(self):          #making loggin function
        self.clear()
        heading = Label(self.root, text="NLP App", bg='#c9dd65', fg='red')   #Label is a class in tkinter
        heading.pack(pady=(30, 30))
        heading.configure(font=("verdana", 35, 'italic'))

        label1 = Label(self.root, text='Enter email', bg='#c9dd65')  # Label is a class
        label1.pack(pady=(10, 10))
        label1.configure(font=("verdana", 17, 'bold'))

        self.email_input = Entry(self.root, width=50)  # Entry is a class
        self.email_input.pack(pady=(10, 10), ipady=5)

        label2 = Label(self.root, text='Enter password', bg='#c9dd65')
        label2.pack(pady=(10, 10))
        label2.configure(font=('verdana', 17, 'bold'))

        self.password_input = Entry(self.root, width=50, show='*')
        self.password_input.pack(pady=(10, 10), ipady=5)
        login_btn = Button(self.root, text='Login', width=30, height=2, bg='yellow',command=self.perform_login)
        login_btn.pack(pady=(10, 10))
        login_btn.configure(font=('verdana', 10, 'bold'))

        label3 = Label(self.root, text='Not a member?', bg='#c9dd65', fg='red')
        label3.pack(pady=(10, 10))
        label3.configure(font=('verdana', 8, 'italic'))

        register_btn_input = Button(self.root, text="Register Now", width=30, height=2, bg="#c9dd65", fg='red',
                                    command=self.register_gui)
        register_btn_input.pack(pady=(5, 10))

    def register_gui(self):
        self.clear()
        heading = Label(self.root, text="NLP App", bg='#c9dd65', fg='red')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 34, 'italic'))

        label0 = Label(self.root, text='Enter name', bg='#c9dd65', fg='white')
        label0.pack(pady=(10, 10))
        label0.configure(font=('verdana', 17, 'bold'))
        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(10, 10), ipady=5)

        label1 = Label(self.root, text='Enter email', bg='#c9dd65', fg='white')  # Label is a class
        label1.pack(pady=(10, 10))
        label1.configure(font=("verdana", 17, 'bold'))
        self.email_input = Entry(self.root, width=50)  # Entry is a class
        self.email_input.pack(pady=(10, 10), ipady=5)

        label2 = Label(self.root, text='Enter password', bg='#c9dd65')
        label2.pack(pady=(10, 10))
        label2.configure(font=('verdana', 17, 'bold'))
        self.password_input = Entry(self.root, width=50, show='*')
        self.password_input.pack(pady=(10, 10), ipady=5)

        register_btn = Button(self.root, text='Register', width=30, height=2, bg='yellow',
                              command=self.perform_registration)
        register_btn.pack(pady=(10, 10))
        register_btn.configure(font=('verdana', 10, 'bold'))

        label3 = Label(self.root, text='Already a member?', bg='#c9dd65', fg='white')
        label3.pack(pady=(10, 10))
        label3.configure(font=('verdana', 8, 'italic'))

        register_btn_input = Button(self.root, text="Login Now", width=30, height=2, bg="#c9dd65", fg='white',
                                    command=self.login_gui)
        register_btn_input.pack(pady=(5, 10))

    # clearing the gui

    def clear(self):
        for i in self.root.pack_slaves():  # self.root.pack_slaves is a method which have every attribute and method regarding the current gui
            i.destroy()

    def perform_registration(self):
        # fetching data from gui
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        res = self.dbo.add_data(name, email, password)
        if res:
            messagebox.showinfo('Success',"Registration successful.You can now login")
        else:
            messagebox.showerror('Error',"Email already exists")

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()
        res=self.dbo.search(email,password)
        if res:
            messagebox.showinfo('Success','Logging in')
            self.home_gui()
        else:
            messagebox.showerror('Error','Invalid login credentials')

    def home_gui(self):
        self.clear()
        heading=Label(self.root,text='NLP App',bg='#c9dd65',fg='red')
        heading.pack(pady=(30,30))
        heading.configure(font=("verdana",34,'italic'))

        sentiment_btn=Button(self.root,text='Sentiment Analysis',width=30,height=3,command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10,30))
        sentiment_btn.configure(font=('verdana',18,'bold'))

        ner_btn = Button(self.root, text='Name Entity Recognition', width=30, height=3,command=self.ner_gui)
        ner_btn.pack(pady=(10, 30))
        ner_btn.configure(font=('verdana', 18, 'bold'))

        emotion_btn = Button(self.root, text='Emotion Prediction', width=30, height=3,command=self.emotion_gui)
        emotion_btn.pack(pady=(10, 30))
        emotion_btn.configure(font=('verdana', 18, 'bold'))

        logout_btn=Button(self.root,text='Logout',width=10,height=2,command=self.login_gui)
        logout_btn.pack(pady=(10,10))
        logout_btn.configure(font=('verdana',10))

    def sentiment_gui(self):
       self.clear()
       heading = Label(self.root, text='NLP App', bg='#c9dd65', fg='red')
       heading.pack(pady=(30, 30))
       heading.configure(font=("verdana", 34, 'italic'))

       heading2 = Label(self.root, text='Sentiment Analysis', bg='white', fg='black')
       heading2.pack(pady=(10, 30))
       heading2.configure(font=("verdana", 20, 'italic'))

       label1=Label(self.root,text='Enter text',bg='white',fg='black')
       label1.pack(pady=(10,30))
       label1.configure(font=('verdana',10,'italic'))

       self.text_input=Entry(self.root,width=30)
       self.text_input.pack(pady=(10,10),ipady=15)

       analyze_btn = Button(self.root, text='Analyze text', width=10, height=2, command=self.do_sentiment_analysis)
       analyze_btn.pack(pady=(10, 10))
       analyze_btn.configure(font=('verdana', 10))

       self.sentiment_result= Label(self.root, text='', bg='#c9dd65')
       self.sentiment_result.pack(pady=(10,10))
       self.sentiment_result.configure(font=('verdana',10))

       goback_btn = Button(self.root, text='Go Back!', width=8, height=2, command=self.home_gui)
       goback_btn.pack(pady=(10, 10))
       goback_btn.configure(font=('verdana', 10))

    def do_sentiment_analysis(self):
        text=self.text_input.get()
        result=self.apio.sentiment_analysis(text)
        txt=""
        for i in result['sentiment']:
            txt=txt+ i+'>--'+str(result['sentiment'][i])+"\n"

        self.sentiment_result['text']=txt

    def ner_gui(self):
        self.clear()
        heading = Label(self.root, text='NLP App', bg='#c9dd65', fg='red')
        heading.pack(pady=(30, 30))
        heading.configure(font=("verdana", 34, 'italic'))

        heading2 = Label(self.root, text='Name Entity Recognition', bg='white', fg='black')
        heading2.pack(pady=(10, 30))
        heading2.configure(font=("verdana", 20, 'italic'))

        label1 = Label(self.root, text='Enter text', bg='white', fg='black')
        label1.pack(pady=(10, 30))
        label1.configure(font=('verdana', 10, 'italic'))

        self.text_input = Entry(self.root, width=30)
        self.text_input.pack(pady=(10, 10), ipady=15)

        analyze_btn = Button(self.root, text='Analyze text', width=10, height=2, command=self.do_ner_analysis)
        analyze_btn.pack(pady=(10, 10))
        analyze_btn.configure(font=('verdana', 10))

        self.ner_result = Label(self.root, text='', bg='#c9dd65')
        self.ner_result.pack(pady=(10, 10))
        self.ner_result.configure(font=('verdana', 10))

        goback_btn = Button(self.root, text='Go Back!', width=8, height=2, command=self.home_gui)
        goback_btn.pack(pady=(10, 10))
        goback_btn.configure(font=('verdana', 10))

    def do_ner_analysis(self):
        text = self.text_input.get()
        result = self.apio.ner(text)
        txt=""
        for i in result['entities']:
            for j in i:                       #j is key of dictionary i
              txt=txt+j+ "<--" + str(i[j])+"\n"

        self.ner_result['text']=txt

    def emotion_gui(self):
        self.clear()
        heading = Label(self.root, text='NLP App', bg='#c9dd65', fg='red')
        heading.pack(pady=(30, 30))
        heading.configure(font=("verdana", 34, 'italic'))

        heading2 = Label(self.root, text='Emotion Prediction', bg='white', fg='black')
        heading2.pack(pady=(10, 30))
        heading2.configure(font=("verdana", 20, 'italic'))

        label1 = Label(self.root, text='Enter text', bg='white', fg='black')
        label1.pack(pady=(10, 30))
        label1.configure(font=('verdana', 10, 'italic'))

        self.text_input = Entry(self.root, width=30)
        self.text_input.pack(pady=(10, 10), ipady=15)

        analyze_btn = Button(self.root, text='Analyze text', width=10, height=2, command=self.do_emotion_analysis)
        analyze_btn.pack(pady=(10, 10))
        analyze_btn.configure(font=('verdana', 10))

        self.emotion_result = Label(self.root,text="", bg='#c9dd65')
        self.emotion_result.pack(pady=(10, 10))
        self.emotion_result.configure(font=('verdana', 10))

        goback_btn = Button(self.root, text='Go Back!', width=8, height=2, command=self.home_gui)
        goback_btn.pack(pady=(10, 10))
        goback_btn.configure(font=('verdana', 10))

    def do_emotion_analysis(self):
        text = self.text_input.get()
        result = self.apio.emotion(text)
        txt= ""
        for i in result['emotion']:
            txt=txt+i+ "<---" + str(result['emotion'][i])+"\n"

        self.emotion_result['text']=txt









nlp = NLPApp()