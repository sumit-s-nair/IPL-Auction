import tkinter as tk
from tkinter import ttk, PhotoImage
import customtkinter as ctk
import tkinter.font
from PIL import Image, ImageTk
#from auction_lib import *
import datetime
import mysql.connector
import random
import time

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class TeamPage:
    def __init__(self, master, show_page2, show_page3):
        self.master = master
        self.show_page2 = show_page2
        self.show_page3 = show_page3

        # Variables
        self.selected_team = tk.StringVar()
        self.bid_player_index = 0

    def setup(self):
        page1 = ctk.CTkFrame(self.master)
        page1.grid_rowconfigure(0, weight=1)
        page1.grid_rowconfigure(1, weight=1)
        page1.grid_rowconfigure(2, weight=1)
        page1.pack()

        title_label = ctk.CTkLabel(master=page1, text="CHOOSE YOUR TEAM", font = ("Portico Rounded", 50))
        title_label.grid(row=0, padx=20, pady=30)

        containera = ctk.CTkFrame(master=page1)
        containera.grid(row=1)
        containera.grid_columnconfigure(3, weight=1)

        containerb = ctk.CTkFrame(master=page1)
        containerb.grid(row=2)
        containerb.grid_columnconfigure(3, weight=1)

        team_names = ["ROYAL\nCHALLENGERS\nBANGALORE", "CHENNAI\nSUPER KINGS", "MUMBAI\nINDIANS", "SUNRISERS\nHYDERABAD"]
        t = ["rcb", "csk", "mi", "srh"]
        for i, team_name in enumerate(team_names):
            team_path = t[i]
            container = TeamContainer(containera, i, team_name, team_path, self.show_page2)
            container.setup()

        team_names = ["RAJASTHAN\nROYALS", "KOLKATA\nKNIGHT RIDERS", "PUNJAB\nKINGS", "DELHI\nCAPITALS"]
        t = ["rr", "kkr", "pk", "dc"]
        for i, team_name in enumerate(team_names):
            team_path = t[i]
            container = TeamContainer(containerb, i, team_name, team_path, self.show_page2)
            container.setup()

class TeamContainer:
    def __init__(self, parent, index, team_name, team_path, show_page2_callback):
        self.parent = parent
        self.index = index
        self.team_name = team_name
        self.team_path = team_path
        self.show_page2_callback = show_page2_callback

    def setup(self):
        container = ctk.CTkFrame(master=self.parent)

        image = ctk.CTkImage(dark_image=Image.open(f"./IPL Auction/assets/{self.team_path.replace(' ', '')}.png"), size = (230,230))
        team_image = ctk.CTkButton(master=container, image=image, text="", command=self.show_page2, fg_color="transparent")
        team_image.configure(image = image)
        team_image.pack(padx=20, pady=10)

        team_button = ctk.CTkButton(master=container, text=self.team_name, command=self.show_page2)
        team_button.pack(pady=20)

        container.grid(column=self.index % 4, row=self.index // 4, padx=105, pady=40, sticky='nsew')

    def show_page2(self):
        self.show_page2_callback(image = f"./IPL Auction/assets/{self.team_path.replace(' ', '')}.png", team_name = self.team_name, team_path = self.team_path)

class AuctionPage(ctk.CTkFrame):
    def __init__(self, master, image, team_name, team_path,):
        super().__init__(master)
        #self.database = Database()
        self.bid_count = 15  # Initial bid count
        self.image = image
        self.team_name = team_name
        self.team_path = team_path
        self.create_widgets()

    def create_widgets(self):
        # Label to display the selected team
        team_label = ttk.Label(self, text=self.team_name, font=("Arial", 16, "bold"))
        team_label.grid(row=0, column=0, pady=10, sticky="w")

        # Label to display the bid count
        bid_count_label = ttk.Label(self, text=f"Bid Count: {self.bid_count}", font=("Arial", 16, "bold"))
        bid_count_label.grid(row=1, column=0, pady=10, sticky="w")

        # # Button to start bidding
        # start_bid_button = ttk.Button(self, text="Start Bidding", command=self.bid_start)
        # start_bid_button.grid(row=2, column=0, pady=10)

        # # Button to place a bid manually
        # bid_button = ttk.Button(self, text="Place Bid", command=self.bid)
        # bid_button.grid(row=3, column=0, pady=10)

        # # Button to pass the bid
        # pass_bid_button = ttk.Button(self, text="Pass Bid", command=self.pass_bid)
        # pass_bid_button.grid(row=4, column=0, pady=10)

        # # Button to enable auto-bid
        # auto_bid_button = ttk.Button(self, text="Enable Auto Bid", command=self.auto_bid)
        # auto_bid_button.grid(row=5, column=0, pady=10)

        # # Label to display bid status
        # self.bid_status_label = ttk.Label(self, text="", font=("Arial", 16, "bold"))
        # self.bid_status_label.grid(row=6, column=0, pady=10, sticky="w")

class IPL_Auction:
    def __init__(self):
        self.window = None
        self.team = None

        # Database connection details
        self.db_connection = mysql.connector.connect(host='127.0.0.1', database='iplplayers', user='root', password='admin')
        self.cursor = self.db_connection.cursor()
    
    def gui(self):
        self.window = ctk.CTk()
        self.window.title("IPL Auction Simulation")
        self.window.geometry("1920x1080")

    def team_page(self):
        team_page = TeamPage(self.window, self.show_auction_page, self.show_team_selection_page)
        team_page.setup()

    def auction_page(self):
        auction_page = AuctionPage(self.window, self.image, self.team_name, self.team_path,)
        auction_page.create_widgets()

    def run(self):
        self.gui()
        self.team_page()
        self.window.state("zoomed")
        self.window.mainloop()

    def show_team_selection_page(self, teampage, auctionpage):
        team_selection_page = TeamPage(self, self.show_auction_page,)
        team_selection_page.pack(fill="both", expand=True)
        self.current_page = team_selection_page

    def show_auction_page(self, image, team_name, team_path):
        auction_page = AuctionPage(master = self.window,image = image, team_name = team_name, team_path = team_path)
        auction_page.pack(fill="both", expand=True)
        self.current_page.pack_forget()
        self.current_page = auction_page





ipl_auction = IPL_Auction()
ipl_auction.run()