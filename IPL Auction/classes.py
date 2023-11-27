import tkinter as tk
from tkinter import ttk, PhotoImage
import customtkinter as ctk
import tkinter.font
from PIL import Image
from auction_lib import *
import datetime
import mysql
import random

# Functions

def back():
    def yes1():
        show_page1(page1, page2, page3)
        windowb.destroy()
    windowb = ctk.CTkToplevel()
    windowb.title("Warning")
    windowb.geometry("400x150")
    windowb.grid_rowconfigure(1)
    frame = ctk.CTkFrame(master = windowb)
    frame.grid_columnconfigure(1)
    warn = ctk.CTkLabel(master = windowb, text = "You are about to leave the game.\nAre you sure you want to proceed?", font = ("Product Sans",18))
    yes = ctk.CTkButton(master = frame, command=yes1, text = "Yes",)
    yes.grid(row = 0, column = 1, sticky = 'nsew', padx = 10, pady = 10)
    no = ctk.CTkButton(master = frame, command=windowb.destroy, text = "No",)
    no.grid(row = 0, column = 0, sticky = 'nsew', padx = 10, pady = 10)
    warn.grid(row = 0, column = 0, sticky = 'ew', padx = 10, pady = 10)
    frame.grid(row = 1, column = 0, sticky = 'ew', padx = 10, pady = 10)
    windowb.attributes('-topmost',True)
    windowb.mainloop()

    
def bid():
    pass

def pas():
    pass

def nex():
    def yes1():
        show_page3(page1, page2, page3)
        windowb.destroy()
    windowb = ctk.CTkToplevel()
    windowb.title("Warning")
    windowb.geometry("415x150")
    windowb.grid_rowconfigure(1)
    frame = ctk.CTkFrame(master = windowb)
    frame.grid_columnconfigure(1)
    warn = ctk.CTkLabel(master = windowb, text = "You are about to let the game auto form your team.\nAre you sure you want to proceed?", font = ("Product Sans",18))
    yes = ctk.CTkButton(master = frame, command=yes1, text = "Yes",)
    yes.grid(row = 0, column = 1, sticky = 'ew', padx = 10, pady = 10)
    no = ctk.CTkButton(master = frame, command=windowb.destroy, text = "No",)
    no.grid(row = 0, column = 0, sticky = 'ew', padx = 10, pady = 10)
    warn.grid(row = 0, column = 0, sticky = 'ew', padx = 10, pady = 10)
    frame.grid(row = 1, column = 0, sticky = 'ew', padx = 10, pady = 10)
    windowb.attributes('-topmost',True)
    windowb.mainloop()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")



class IPLAuctionSimulation:
    def __init__(self):
        self.ctk = None
        self.team = None

    def setup_gui(self):
        self.ctk = ctk.CTk()
        self.ctk.title("IPL Auction Simulation")
        self.ctk.geometry("1920x1080")

    def create_team_page(self):
        team_page = TeamPage(self.ctk, self.show_page2, self.show_page3)
        team_page.setup()

    def run(self):
        self.setup_gui()
        self.create_team_page()
        self.ctk.state("zoomed")
        self.ctk.mainloop()

    def show_page2(self, image, team_name):
        # Implementation for showing page 2
        pass

    def show_page3(self):
        # Implementation for showing page 3
        pass

class TeamPage:
    def __init__(self, ctk, show_page2, show_page3):
        self.ctk = ctk
        self.show_page2 = show_page2
        self.show_page3 = show_page3

    def setup(self):
        page1 = tk.Frame(self.ctk)
        page1.grid_rowconfigure(0, weight=1)
        page1.grid_rowconfigure(1, weight=1)
        page1.grid_rowconfigure(2, weight=1)

        title_label = tk.Label(master=page1, text="CHOOSE YOUR TEAM")
        title_label.grid(row=0, padx=20, pady=30)

        containera = tk.Frame(master=page1)
        containera.grid(row=1)
        containera.grid_columnconfigure(0, weight=1)
        containera.grid_columnconfigure(1, weight=1)
        containera.grid_columnconfigure(2, weight=1)
        containera.grid_columnconfigure(3, weight=1)

        team_names = ["ROYAL\nCHALLENGERS\nBANGALORE", "CHENNAI\nSUPER KINGS", "MUMBAI\nINDIANS", "SUNRISERS\nHYDERABAD"]
        for i, team_name in enumerate(team_names):
            container = TeamContainer(containera, i, team_name, self.show_page2)
            container.setup()

        # ... Continue with the rest of your code for page 1

class TeamContainer:
    def __init__(self, parent, index, team_name, show_page2_callback):
        self.parent = parent
        self.index = index
        self.team_name = team_name
        self.show_page2_callback = show_page2_callback

    def setup(self):
        container = tk.Frame(master=self.parent)

        image = ctk.CTkImage(dark_image=Image.open(f"./IPL Auction/assets/{self.team_name.replace(' ', '')}.png"))
        image_label = tk.Button(master=container, image=image, text="", command=self.show_page2)
        image_label.configure(image = image)
        image_label.pack(padx=20, pady=10)

        team_button = tk.Button(master=container, text=self.team_name, command=self.show_page2)
        team_button.pack(pady=20)

        container.grid(column=self.index % 4, row=self.index // 4, padx=105, pady=40, sticky='nsew')

    def show_page2(self):
        self.show_page2_callback(f"./IPL Auction/assets/{self.team_name.replace(' ', '')}.png", self.team_name)

# Other classes and methods can be similarly refactored

if __name__ == "__main__":
    ipl_auction = IPLAuctionSimulation()
    ipl_auction.run()