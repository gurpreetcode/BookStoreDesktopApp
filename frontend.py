from tkinter import *
from tkinter import messagebox
import backend
import os

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)
    list1.insert(0,"ID | TITLE  |  AUTHOR  |  YEAR  |  ISBN/ASIN")
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    list1.insert(0,"ID | TITLE  |  AUTHOR  |  YEAR  |  ISBN/ASIN")
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(0,"ID | TITLE  |  AUTHOR  |  YEAR  |  ISBN/ASIN")
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())

def destroy_command():
    window.destroy()
    screen2.destroy()

def delete3():
    screen4.destroy()

def delete4():
    screen5.destroy()

def screen_destroy():
    screen.destroy()


def login_success():
    session()

def back():
    screen2.destroy()
    
def back1():
    screen1.destroy()

def session():

    global window, list1, sb1, title_text, author_text, year_text, isbn_text, selected_tuple
    global l1,l2,l3,l4,e1,e2,e3,e4,b1,b2,b3,b4,b5,b6
    
    window = Toplevel(screen2)
    window.attributes('-fullscreen',True)
    window.configure(background='SteelBlue1')

    l1=Label(window,text="BOOK  TITLE :",justify = CENTER,
             font = "Verdana 25 bold", bg = 'SteelBlue1')
    l1.grid(row=0,column=0)

    l2=Label(window,text="AUTHOR :",justify = CENTER,
             font = "Verdana 25 bold", bg = 'SteelBlue1')
    l2.grid(row=0,column=2)

    l3=Label(window,text="YEAR  PUBLISHED :",justify = CENTER,
             font = "Verdana 25 bold", bg = 'SteelBlue1')
    l3.grid(row=1,column=0)

    l4=Label(window,text="ISBN/ASIN :",justify = CENTER,
             font = "Verdana 25 bold", bg = 'SteelBlue1')
    l4.grid(row=1,column=2)

    title_text=StringVar()
    e1=Entry(window,textvariable=title_text,font = "Verdana 19",fg='navy')
    e1.grid(row=0,column=1)

    author_text=StringVar()
    e2=Entry(window,textvariable=author_text,font = "Verdana 19",fg='navy')
    e2.grid(row=0,column=3)

    year_text=StringVar()
    e3=Entry(window,textvariable=year_text,font = "Verdana 19",fg='navy')
    e3.grid(row=1,column=1)

    isbn_text=StringVar()
    e4=Entry(window,textvariable=isbn_text,font = "Verdana 19",fg='navy')
    e4.grid(row=1,column=3)

    list1=Listbox(window, height=25,width=60,font = "Verdana 15 ")
    list1.grid(row=2,column=0,rowspan=6,columnspan=2)
    list1.insert(0,"ID | TITLE  |  AUTHOR  |  YEAR  |  ISBN/ASIN")

    sb1=Scrollbar(window)
    sb1.grid(row=2,column=2,rowspan=6)

    list1.configure(yscrollcommand=sb1.set)
    sb1.configure(command=list1.yview)

    list1.bind('<<ListboxSelect>>',get_selected_row)

    b1=Button(window,text="VIEW ALL", width=12,activeforeground = "white",
              activebackground = "green",command=view_command,
              height = "1",font = "Verdana 30",bd = "4",bg='DodgerBlue4',fg='white')
    b1.grid(row=2,column=3)

    b2=Button(window,text="SEARCH", activeforeground = "white",
              activebackground = "green",width=12,command=search_command,
              height = "1",font = "Verdana 30",bd = "4",bg='DodgerBlue4',fg='white')
    b2.grid(row=3,column=3)

    b3=Button(window,text="ADD", activeforeground = "white",
              activebackground = "green",width=12,command=add_command,
              height = "1",font = "Verdana 30",bd = "4",bg='DodgerBlue4',fg='white')
    b3.grid(row=4,column=3)

    b4=Button(window,text="UPDATE",activeforeground = "white",
              activebackground = "green", width=12,command=update_command,
              height = "1",font = "Verdana 30",bd = "4",bg='DodgerBlue4',fg='white')
    b4.grid(row=5,column=3)
    
    b5=Button(window,text="DELETE",activeforeground = "white",
              activebackground = "green", width=12,command=delete_command,
              height = "1",font = "Verdana 30",bd = "4",bg='DodgerBlue4',fg='white')
    b5.grid(row=6,column=3)

    b6=Button(window,text="LOG OUT",activeforeground = "white",
              activebackground = "green", width=12,command=destroy_command,
              height = "1",font = "Verdana 30",bd = "4",bg='DodgerBlue4',fg='white')
    b6.grid(row=7,column=3)

def password_not_recognized():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Password Error")
    screen4.geometry("350x100")
    Label(screen4,text = "Password not recognized",font = "Verdana 20",fg='red').pack()
    Button(screen4,text = "OK",command = delete3,activeforeground = "white",
              activebackground = "green",font = "Verdana 15",bg='DodgerBlue4',fg='white').pack()

def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("User Error")
    screen5.geometry("350x100")
    Label(screen5,text = "User not recognized",font = "Verdana 20",fg='red').pack()
    Button(screen5,text = "OK",command = delete4,activeforeground = "white",
              activebackground = "green",font = "Verdana 15",bg='DodgerBlue4',fg='white').pack()

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info,"w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0,END)
    password_entry.delete(0,END)

    Label(screen1,text = "REGISTRATION SUCCESS",font = "Verdana 25 bold",
          bg = 'SteelBlue1',height = "2",width="300",fg = "green").pack()

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0,END)
    password_entry1.delete(0,END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1,"r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognized()
    else:
        user_not_found()

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("REGISTER")

    global username, password, username_entry, password_entry
    username = StringVar()
    password = StringVar()
    screen1.attributes('-fullscreen',True)
    screen1.configure(background='SteelBlue1')

    Label(screen1,  text = "Please enter New details below to REGISTER",fg = "white",
          bg = "IndianRed4",font = "Verdana 40 bold",height = "2",width="300").pack()
    Label(screen1, text = "", bg = "SteelBlue1").pack()
    Label(screen1, text = "", bg = "SteelBlue1").pack()
    Label(screen1, text = "", bg = "SteelBlue1").pack()
    Label(screen1, text = "Username * ",font = "Verdana 25 bold", bg = 'SteelBlue1').pack()
    username_entry = Entry(screen1, textvariable = username, font = "Verdana 20")
    username_entry.pack()
    Label(screen1, text = "", bg = "SteelBlue1").pack()
    Label(screen1, text = "", bg = "SteelBlue1").pack()
    Label(screen1, text = "", bg = "SteelBlue1").pack()
    Label(screen1, text = "Password * ",font = "Verdana 25 bold", bg = 'SteelBlue1').pack()
    password_entry = Entry(screen1, textvariable = password,font = "Verdana 20", show='*')
    password_entry.pack()
    password_entry.pack()
    Label(screen1, text = "", bg = "SteelBlue1").pack()
    Label(screen1, text = "", bg = "SteelBlue1").pack()
    Label(screen1, text = "", bg = "SteelBlue1").pack()    
    Button(screen1, text = "REGISTER", width = "10", height = "1",
           activeforeground = "white", bd="4",fg='white',font = "Verdana 30",
           bg='DodgerBlue4', activebackground = "green",
           command = register_user).pack()
    Label(screen1, text = "", bg = "SteelBlue1").pack();Label(screen1, text = "", bg = "SteelBlue1").pack()
    Button(screen1, text = "BACK",width = "10",height = "1",
           activeforeground = "white", bd = "4",fg='white',font = "Verdana 20",bg='DodgerBlue4',
           activebackground = "green", command = back1).pack()

def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("LOGIN")
    screen2.attributes('-fullscreen',True)
    screen2.configure(background='SteelBlue1')

    global username_verify, password_verify, username_entry1, password_entry1
    username_verify = StringVar()
    password_verify = StringVar()
    
    Label(screen2, text = "Please enter details below to LOGIN",fg = "white",
          bg = "IndianRed4",font = "Verdana 40 bold",height = "2",width="300").pack()
    Label(screen2, text = "", bg = "SteelBlue1").pack()
    Label(screen2, text = "", bg = "SteelBlue1").pack()
    Label(screen2, text = "", bg = "SteelBlue1").pack()
    Label(screen2, text = "Username * ",font = "Verdana 25 bold", bg = 'SteelBlue1').pack()
    username_entry1 = Entry(screen2, textvariable = username_verify,font = "Verdana 20")
    username_entry1.pack()
    Label(screen2, text = "", bg = "SteelBlue1").pack()
    Label(screen2, text = "", bg = "SteelBlue1").pack()
    Label(screen2, text = "", bg = "SteelBlue1").pack()
    Label(screen2, text = "Password * ",font = "Verdana 25 bold", bg = 'SteelBlue1').pack()
    password_entry1 = Entry(screen2, textvariable = password_verify, font = "Verdana 20", show = '*')
    password_entry1.pack()
    Label(screen2, text = "", bg = "SteelBlue1").pack()
    Label(screen2, text = "", bg = "SteelBlue1").pack()
    Label(screen2, text = "", bg = "SteelBlue1").pack()
    Button(screen2, text = "LOGIN",width = "10",height = "1",
           activeforeground = "white", bd = "4",fg='white',font = "Verdana 30",bg='DodgerBlue4',
           activebackground = "green", command = login_verify).pack()
    Label(screen2, text = "", bg = "SteelBlue1").pack();Label(screen2, text = "", bg = "SteelBlue1").pack()
    Button(screen2, text = "BACK",width = "10",height = "1",
           activeforeground = "white", bd = "4",fg='white',font = "Verdana 20",bg='DodgerBlue4',
           activebackground = "green", command = back).pack()    

    
def main_screen():
    global screen
    screen = Tk()
    screen.attributes('-fullscreen',True)
    screen.title("BOOK STORE")
    screen.configure(background='SteelBlue1')
    Label(screen, text = "BOOK  STORE",fg = "white", bg = "IndianRed4",
          font = "Verdana 50 bold",height = "2",width="300").pack()
    Label(screen, text = "", bg = "SteelBlue1").pack()
    Label(screen, text = "", bg = "SteelBlue1").pack()
    Label(screen, text = "", bg = "SteelBlue1").pack()
    Button(screen, text = "LOGIN",height = "1",width = "10",fg='white',
           activeforeground = "white",font = "Verdana 30",bg='DodgerBlue4',
           bd = "4", activebackground = "green",command = login).pack()
    Label(screen, text = "", bg = "SteelBlue1").pack()
    Label(screen, text = "", bg = "SteelBlue1").pack()
    Label(screen, text = "", bg = "SteelBlue1").pack()
    Button(screen, text = "REGISTER",height = "1",width = "10",fg='white',
           activeforeground = "white",font = "Verdana 30",bg='DodgerBlue4',
           bd = "4", activebackground = "green",command = register).pack()
    Label(screen, text = "", bg = "SteelBlue1").pack()
    Label(screen, text = "", bg = "SteelBlue1").pack()
    Label(screen, text = "", bg = "SteelBlue1").pack()
    Button(screen, text = "CLOSE",height = "1",width = "10",fg='white',
           activeforeground = "white",font = "Verdana 30",bg='DodgerBlue4',
           bd = "4", activebackground = "green",command = screen_destroy).pack()

    screen.mainloop()
    
    
main_screen()
