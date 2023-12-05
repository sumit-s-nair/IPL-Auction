# Functions for IPL AUCTION
import customtkinter as ctk
import tkinter as tk
import time
from PIL import Image
import io
import base64


def show_page1(page1,page2,page3):
    page1.pack()
    page2.pack_forget()
    page3.pack_forget()

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

def get_image(new_image_path):
    base64_data = base64.b64encode(new_image_path).decode('utf-8')
    imagep = Image.open(io.BytesIO(base64.b64decode(base64_data)))
    image = ctk.CTkImage(dark_image=imagep,size=(230,230))
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