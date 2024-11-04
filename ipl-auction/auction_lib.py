# Functions for IPL AUCTION
import customtkinter as ctk
import tkinter as tk
import time
from PIL import Image
import io
import base64


def show_page(page1,page2,page3, page4):
    page1.pack()
    page2.pack_forget()
    page3.pack_forget()
    page4.pack_forget()


def hf(label):
    hf = ctk.CTkFont( family = "Portico Rounded", size = 50, weight = "bold")
    label.configure(font = hf)

def bf(button):
    bf = ctk.CTkFont( family = "Portico Rounded", size = 20, weight = "bold")
    button.configure(font = bf)

def pf(button):
    pf = ctk.CTkFont( family = "Portico Rounded", size = 15, weight = "bold")
    button.configure(font = pf)

def af(button):
    af = ctk.CTkFont( family = "Portico Light", size = 15, weight = "bold")
    button.configure(font = af)

def sf(button):
    af = ctk.CTkFont( family = "Portico Light", size = 20, weight = "bold")
    button.configure(font = af)

def mf(button):
    af = ctk.CTkFont( family = "Portico light", size = 25, weight = "normal")
    button.configure(font = af)

def get_image_from_path(image_path):
    imagep = Image.open(r"./ipl-auction"+ image_path)  # Directly loading from the file system
    image = ctk.CTkImage(dark_image=imagep, size=(230, 230))
    return image

def warn(windowb, text, cmd):
    windowb.title("Warning")
    windowb.geometry("415x150")
    windowb.grid_rowconfigure(1)
    frame = ctk.CTkFrame(master = windowb)
    frame.grid_columnconfigure(1)
    warn = ctk.CTkLabel(master = windowb, text = text, font = ("Product Sans",18))
    yes = ctk.CTkButton(master = frame, command=cmd, text = "Yes",)
    yes.grid(row = 0, column = 0, sticky = 'ew', padx = 10, pady = 10)
    no = ctk.CTkButton(master = frame, command=windowb.destroy, text = "No",)
    no.grid(row = 0, column = 1, sticky = 'ew', padx = 10, pady = 10)
    warn.grid(row = 0, column = 0, sticky = 'ew', padx = 10, pady = 10)
    frame.grid(row = 1, column = 0, sticky = 'ew', padx = 10, pady = 10)
    windowb.attributes('-topmost',True)
    windowb.mainloop()

def warn1(windowb, text, cmd):
    windowb.title("Warning")
    windowb.geometry("500x150")
    warn = ctk.CTkLabel(master = windowb, text = text, font = ("Product Sans",18))
    warn.pack(padx = 10, pady = 10)
    cont = ctk.CTkButton(master = windowb, command=cmd, text = "Continue",)
    cont.pack(padx = 10, pady = 10)
    windowb.attributes('-topmost',True)
    windowb.mainloop()

def rebid(windowb, text, cmd, cmd1):
    windowb.title("Warning")
    windowb.geometry("415x150")
    windowb.grid_rowconfigure(1)
    frame = ctk.CTkFrame(master = windowb)
    frame.grid_columnconfigure(1)
    warn = ctk.CTkLabel(master = windowb, text = text, font = ("Product Sans",18))
    yes = ctk.CTkButton(master = frame, command=cmd, text = "Yes",)
    yes.grid(row = 0, column = 0, sticky = 'ew', padx = 10, pady = 10)
    no = ctk.CTkButton(master = frame, command=cmd1, text = "No",)
    no.grid(row = 0, column = 1, sticky = 'ew', padx = 10, pady = 10)
    warn.grid(row = 0, column = 0, sticky = 'ew', padx = 10, pady = 10)
    frame.grid(row = 1, column = 0, sticky = 'ew', padx = 10, pady = 10)
    windowb.attributes('-topmost',True)
    windowb.mainloop()

def start(windowb, yes1):
    windowb.title("Rules")
    windowb.geometry("900x700")
    windowb.grid_rowconfigure(1)
    text =""" 1. Click continue to start the game. Read all rules before doing so.
        \n 2. On clicking continue you will be asked to choose a team.
        \n 3. You will taken to the the auction page.
        \n 4. Max number of bids are set to 15.
        \n 5. The BID button will let you place a bid of the displayed player.
        \n Note: Other players may have a higher bid for the same player and you will recieve a prompt to bid again
        \n 6. If you are the highest bidder the player will be added to the player list which is under ther profile picture
        \n 7. If you do not wish to place a bid on the player you have an option of PASS
        \n Note: Pass will not let you bid for the player again.
        \n 8. The last option is AUTO, this option allows the game to automatically sort the remainingplayers into teams
        \n Note: You will not be able to stop this function once it has been started to choose it wisely
        \n 9. Once you have successfully completed you team, you will reach the final page where all teams are displayed"""
    
    rule = ctk.CTkLabel(master = windowb, text = "Rules" , font = ("Product Sans",36))  
    warn = ctk.CTkLabel(master = windowb, text = text, font = ("Product Sans",18), justify = "left")
    yes = ctk.CTkButton(master = windowb, command=yes1, text = "Continue",)
    yes.grid(row = 2, column = 0, sticky = 'ew', padx = 10, pady = 10)
    warn.grid(row = 1, column = 0, sticky = 'ew', padx = 10, pady = 10)
    rule.grid(row = 0, column = 0, sticky = 'ew', padx = 10, pady = 10)
    windowb.attributes('-topmost',True)
    windowb.mainloop()