from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")

def restart_time():  
    os.system("shutdown /r /t 20")

def logout():
    os.system("shutdown -1")

def shutdown():
    os.system("shutdown /s /t 1")

start = Tk()
start.title("ShutDown App")
start.geometry("500x500")
start.config(bg="LightBlue")

restart_button = Button(start, 
                        text="Restart",
                        font=("Times New Roman", 20, "bold"),
                        relief=RAISED,  
                        cursor="plus",
                        command=restart)
restart_button.place(x=150, y=60, height=60, width=200)

restart_time_button = Button(start, 
                        text="Restart Time",
                        font=("Times New Roman", 20, "bold"),
                        relief=RAISED,  
                        cursor="plus",
                        command=restart_time)
restart_time_button.place(x=150, y=170, height=60, width=200)

logout_button = Button(start, 
                        text="Log-Out",
                        font=("Times New Roman", 20, "bold"),
                        relief=RAISED,  
                        cursor="plus",
                        command= logout)
logout_button.place(x=150, y=270, height=60, width=200)

shutdown_button = Button(start, 
                        text="ShutDown",
                        font=("Times New Roman", 20, "bold"),
                        relief=RAISED,  
                        cursor="plus",
                        command=shutdown)
shutdown_button.place(x=150, y=370, height=60, width=200)



start.mainloop()
