from tkinter import *
#loginsys.py----creates a login system with no backend on a GUI window.
main_screen = Tk()

def main_user_screen():
    global main_screen 
    main_screen.geometry("1920x1080")
    main_screen.title('Account login form')


formLable = Label(text="choose login or regestration", bg="green", width="300", height="2",font=("calibri",13)).pack()
loginButton = Button(text="login", height="2", width="30", bg="yellow").pack()
regesterbutton = Button(text="Register", height="2", width="30", bg="red").pack()

# starting the GUI WINDOW
main_screen.mainloop()
# call the main_user_screen()function
main_user_screen()

