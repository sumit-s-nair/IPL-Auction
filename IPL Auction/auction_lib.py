# Functions for IPL AUCTION
import customtkinter as ctk
import tkinter as tk


def show_page1(page1,page2):
    page1.pack()
    page2.pack_forget()

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

def show_page2(page1,page2,imgprof, image, Teamname, name):
    page1.pack_forget()
    page2.pack()
    imgprof.configure(image=image)
    Teamname.configure(text = name)

def bid():
    pass

def pas():
    pass
