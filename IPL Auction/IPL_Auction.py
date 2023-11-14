import tkinter as tk
from tkinter import ttk, PhotoImage
import customtkinter as ctk
import tkinter.font
from PIL import Image

# Functions
def show_page1():
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

def show_page2a():
    page1.pack_forget()
    page2.pack()
    imageprofile.configure(image=image1)
    Teamname.configure(text = "ROYAL\nCHALLENGERS\nBANGALORE")

def show_page2b():
    page1.pack_forget()
    page2.pack()
    imageprofile.configure(image=image2)
    Teamname.configure(text = "CHENNAI\nSUPER KINGS")

def show_page2c():
    page1.pack_forget()
    page2.pack()
    imageprofile.configure(image=image3)
    Teamname.configure(text = "MUMBAI\nINDIANS")

def show_page2d():
    page1.pack_forget()
    page2.pack()
    imageprofile.configure(image=image4)
    Teamname.configure(text = "SUNRISERS\nHYDERABAD")

def show_page2e():
    page1.pack_forget()
    page2.pack()
    imageprofile.configure(image=image5)
    Teamname.configure(text = "RAJASTHAN\nROYALS")

def show_page2f():
    page1.pack_forget()
    page2.pack()
    imageprofile.configure(image=image6)
    Teamname.configure(text = "KOLKATA\nKNIGHT RIDERS")

def show_page2g():
    page1.pack_forget()
    page2.pack()
    imageprofile.configure(image=image7)
    Teamname.configure(text = "PUNJAB\nKINGS")

def show_page2h():
    page1.pack_forget()
    page2.pack()
    imageprofile.configure(image=image8)
    Teamname.configure(text = "DELHI\nCAPITALS")

def bid():
    pass

def pas():
    pass

def back():
    def yes1():
        show_page1()
        windowb.destroy()
    windowb = ctk.CTkToplevel(window)
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
  

# Window

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

window = ctk.CTk()
window.title("IPL Auction Simulation")
window.geometry("1920x1080")
window.state('normal')

page1 = ctk.CTkFrame(window)
page1.grid_rowconfigure(0, weight=1)
page1.grid_rowconfigure(1, weight=1)
page1.grid_rowconfigure(2, weight=1)

page2 = ctk.CTkFrame(window)
page2.grid_rowconfigure(0)
page2.grid_columnconfigure(0, weight=1)
page2.grid_columnconfigure(1, weight=4)

# PAGE 1

# Title

title_label = ctk.CTkLabel(master = page1, text = "CHOOSE YOUR TEAM")
title_label.grid(row = 0,padx = 20,pady = 30)
hf(title_label)

# Row 1

containera = ctk.CTkFrame(master = page1)
containera.grid(row=1)
containera.grid_columnconfigure(0, weight=1)
containera.grid_columnconfigure(1, weight=1)
containera.grid_columnconfigure(2, weight=1)
containera.grid_columnconfigure(3, weight=1)

# RCB

container1 = ctk.CTkFrame(master = containera)

image1 = ctk.CTkImage(dark_image=Image.open(r"assets\RCB.png"),size=(230, 230))
image_label1 = ctk.CTkButton(master = container1, image = image1, text = "", command = show_page2a, fg_color = "transparent", hover_color = "#14375E")
image_label1.pack(padx = 20, pady = 10)

team1 = ctk.CTkButton(master = container1, command=show_page2a, text = "ROYAL\nCHALLENGERS\nBANGALORE", )
bf(team1)
team1.pack(pady=20)
container1.grid(column = 0, row = 0, padx = 105, pady = 40, sticky = 'nsew')

# CSK

container2 = ctk.CTkFrame(master = containera)

image2 = ctk.CTkImage(dark_image=Image.open(r"assets\CSK.png"),size=(230, 230))
image_label2 = ctk.CTkButton(master = container2, image=image2, text = "", command = show_page2b, fg_color = "transparent", hover_color = "#14375E")
image_label2.pack(padx = 20, pady = 20)

team2 = ctk.CTkButton(master = container2, command=show_page2b, text = "CHENNAI\nSUPER KINGS")
bf(team2)
team2.pack(pady=20)
container2.grid(column = 1, row = 0, padx = 105, pady = 40, sticky = 'nsew')

# MI

container3 = ctk.CTkFrame(master = containera)

image3 = ctk.CTkImage(dark_image=Image.open(r"assets\MI.png"),size=(230, 230))
image_label3 = ctk.CTkButton(master = container3, image=image3, text = "", command = show_page2c, fg_color = "transparent", hover_color = "#14375E")
image_label3.pack(padx = 20, pady = 20)

team3 = ctk.CTkButton(master = container3, text = "MUMBAI\nINDIANS", command=show_page2c)
bf(team3)
team3.pack(pady=20)
container3.grid(column = 2, row = 0, padx = 105, pady = 40, sticky = 'nsew')

# SRH

container4 = ctk.CTkFrame(master = containera)

image4 = ctk.CTkImage(dark_image=Image.open(r"assets\SRH.png"),size=(230, 230))
image_label4 = ctk.CTkButton(master = container4, image=image4, text = "", command = show_page2d, fg_color = "transparent", hover_color = "#14375E")
image_label4.pack(padx = 20, pady = 20)

team4 = ctk.CTkButton(master = container4, text = "SUNRISERS\nHYDERABAD", command=show_page2d)
bf(team4)
team4.pack(pady=20)
container4.grid(column = 3, row = 0, padx = 105, pady = 40, sticky = 'nsew')

# Row 2

containerb = ctk.CTkFrame(master = page1)
containerb.grid(row=2)
containerb.grid_columnconfigure(0, weight=1)
containerb.grid_columnconfigure(1, weight=1)
containerb.grid_columnconfigure(2, weight=1)
containerb.grid_columnconfigure(3, weight=1)

# RR

container5 = ctk.CTkFrame(master = containerb)

image5 = ctk.CTkImage(dark_image=Image.open(r"assets\RR.png"),size=(230, 230))
image_label5 = ctk.CTkButton(master = container5, image=image5, text = "", command = show_page2e, fg_color = "transparent", hover_color = "#14375E")
image_label5.pack(padx = 20, pady = 20)

team5 = ctk.CTkButton(master = container5, text = "RAJASTHAN\nROYALS", command=show_page2e)
bf(team5)
team5.pack(pady=20)
container5.grid(column = 0, row = 0, padx = 105, pady = 40, sticky = 'nsew')

# KKR

container6 = ctk.CTkFrame(master = containerb)

image6 = ctk.CTkImage(dark_image=Image.open(r"assets\KKR.png"),size=(230, 230))
image_label6 = ctk.CTkButton(master = container6, image=image6, text = "", command = show_page2f, fg_color = "transparent", hover_color = "#14375E")
image_label6.pack(padx = 20, pady = 20)

team6 = ctk.CTkButton(master = container6, text = "KOLKATA\nKNIGHT RIDERS", command=show_page2f)
bf(team6)
team6.pack(pady=20)
container6.grid(column = 1, row = 0, padx = 105, pady = 40, sticky = 'nsew')

# PK

container7 = ctk.CTkFrame(master = containerb)

image7 = ctk.CTkImage(dark_image=Image.open(r"assets\PK.png"),size=(230, 230))
image_label7 = ctk.CTkButton(master = container7, image=image7, text = "", command = show_page2g, fg_color = "transparent", hover_color = "#14375E")
image_label7.pack(padx = 20, pady = 20)

team7 = ctk.CTkButton(master = container7, text = "PUNJAB\nKINGS", command=show_page2g)
bf(team7)
team7.pack(pady=20)
container7.grid(column = 2, row = 0, padx = 105, pady = 40, sticky = 'nsew')

# DC

container8 = ctk.CTkFrame(master = containerb)

image8 = ctk.CTkImage(dark_image=Image.open(r"assets\DC.png"),size=(230, 230))
image_label8 = ctk.CTkButton(master = container8, image=image8, text = "", command = show_page2h, fg_color = "transparent", hover_color = "#14375E")
image_label8.pack(padx = 20, pady = 20)

team8 = ctk.CTkButton(master = container8, text = "DELHI\nCAPITALS", command=show_page2h)
bf(team8)
team8.pack(pady=20)
container8.grid(column = 3, row = 0, padx = 105, pady = 40, sticky = 'nsew')

# PAGE 2

# Back

backim = ctk.CTkImage(dark_image=Image.open(r"assets\back.png"),size=(33, 35))
back_frame = ctk.CTkFrame(page2)
back_frame.grid(row = 0, column = 0,padx = 10, pady = 10, sticky = 'n')
back = ctk.CTkButton(master = back_frame, text = "", image = backim, command = back, width = 40)
back.pack(padx = 10, pady = 10)

# Profile

profile_frame = ctk.CTkFrame(page2)
profile_frame.grid_rowconfigure(0,weight=1)
profile_frame.grid_columnconfigure(0, weight=1)
profile_frame.grid_rowconfigure(1,weight=4)
profile_frame.grid(row = 0,column=1, sticky = 'n')

# User Profile

imageprofile = ctk.CTkLabel(profile_frame, text = "")
imageprofile.grid(padx=20,pady=10)

Teamname = ctk.CTkLabel(master = profile_frame, justify = "center", fg_color="transparent")
bf(Teamname)
Teamname.grid(column=0, pady = 10, padx = 20)

# User Team

player_list_frame = ctk.CTkScrollableFrame(profile_frame, height = 590, width = 250, label_text = "Player List", label_font = ("Portico Rounded", 20), label_fg_color = "#1F538D", scrollbar_button_color = "#1F538D",scrollbar_button_hover_color = "#14375E")
player_list_frame.grid(column=0,padx=20,pady=10)

playername1f = ctk.CTkFrame(master = player_list_frame)
playername1f.pack(padx=10,pady=5)
playername1 = ctk.CTkLabel(master = playername1f,text="Player 1")
pf(playername1)
playername1.pack(padx=30,pady=10)

playername2f = ctk.CTkFrame(master = player_list_frame)
playername2f.pack(padx=10,pady=5)
playername2 = ctk.CTkLabel(master = playername2f,text="Player 2")
pf(playername2)
playername2.pack(padx=30,pady=10)

playername3f = ctk.CTkFrame(master = player_list_frame)
playername3f.pack(padx=10,pady=5)
playername3 = ctk.CTkLabel(master = playername3f,text="Player 3")
pf(playername3)
playername3.pack(padx=30,pady=10)

playername4f = ctk.CTkFrame(master = player_list_frame)
playername4f.pack(padx=10,pady=5)
playername4 = ctk.CTkLabel(master = playername4f,text="Player 4")
pf(playername4)
playername4.pack(padx=30,pady=10)

playername5f = ctk.CTkFrame(master = player_list_frame)
playername5f.pack(padx=10,pady=5)
playername5 = ctk.CTkLabel(master = playername5f,text="Player 5")
pf(playername5)
playername5.pack(padx=30,pady=10)

playername6f = ctk.CTkFrame(master = player_list_frame)
playername6f.pack(padx=10,pady=5)
playername6 = ctk.CTkLabel(master = playername6f,text="Player 6")
pf(playername6)
playername6.pack(padx=30,pady=10)

playername7f = ctk.CTkFrame(master = player_list_frame)
playername7f.pack(padx=10,pady=5)
playername7 = ctk.CTkLabel(master = playername7f,text="Player 7")
pf(playername7)
playername7.pack(padx=30,pady=10)

playername8f = ctk.CTkFrame(master = player_list_frame)
playername8f.pack(padx=10,pady=5)
playername8 = ctk.CTkLabel(master = playername8f,text="Player 8")
pf(playername8)
playername8.pack(padx=30,pady=10)

playername9f = ctk.CTkFrame(master = player_list_frame)
playername9f.pack(padx=10,pady=5)
playername9 = ctk.CTkLabel(master = playername9f,text="Player 9")
pf(playername9)
playername9.pack(padx=30,pady=10)

playername10f = ctk.CTkFrame(master = player_list_frame)
playername10f.pack(padx=10,pady=5)
playername10 = ctk.CTkLabel(master = playername10f,text="Player 10")
pf(playername10)
playername10.pack(padx=30,pady=10)

playername11f = ctk.CTkFrame(master = player_list_frame)
playername11f.pack(padx=10,pady=5)
playername11 = ctk.CTkLabel(master = playername11f,text="Player 11")
pf(playername11)
playername11.pack(padx=30,pady=10)

# Auction

auction_frame = ctk.CTkFrame(page2)
auction_frame.grid(row=0, column=2,sticky='n', padx= 20, pady= 20)

amount_frame = ctk.CTkFrame(auction_frame)
amount_frame.grid_columnconfigure(0,weight=1)
amount_frame.grid_columnconfigure(1,weight=1)
amount_frame.grid_columnconfigure(2,weight=1)
amount_frame.grid_rowconfigure(0)
amount_frame.pack(padx= 20, pady= 20)

# Total Amount

Totalam = ctk.CTkFrame(master=amount_frame, width=200, height=100)
Totalam1 = ctk.CTkLabel(master = Totalam, text = "TOTAL AMOUNT")
Totalam1.pack(side="top", padx = 20, pady = 10)
af(Totalam1)
imageam = ctk.CTkImage(dark_image=Image.open(r"assets\x.png"),size=(50, 50))
Totalam3 = ctk.CTkLabel(master = Totalam, text = "", image = imageam)
Totalam3.pack(side="left", padx = 10, pady = 10)
Totalam2 = ctk.CTkLabel(master = Totalam, text = "30,00,00,000")
af(Totalam2)
Totalam2.pack(side="right", padx = 10, pady = 10)
Totalam.grid(row=0, column=0,sticky='nsew', pady=30, padx=50)

# Total Spent

Totalsp = ctk.CTkFrame(master=amount_frame, width=200, height=100)
Totalsp1 = ctk.CTkLabel(master = Totalsp, text = "TOTAL SPENDING")
af(Totalsp1)
Totalsp1.pack(side="top", padx = 20, pady = 10)
imagets = ctk.CTkImage(dark_image=Image.open(r"assets\down.png"),size=(50, 50))
Totalsp3 = ctk.CTkLabel(master = Totalsp, text = "", image = imagets)
Totalsp3.pack(side="left", padx = 10, pady = 10)
Totalsp2 = ctk.CTkLabel(master = Totalsp, text = "TOTAL SPENDING")
af(Totalsp2)
Totalsp2.pack(side="right", padx = 10, pady = 10)
Totalsp.grid(row=0,column=1,sticky='nsew',padx= 50, pady=30)

# Total Bids

Bids = ctk.CTkFrame(master=amount_frame, width=200, height=100)
Bids1 = ctk.CTkLabel(master = Bids, text = "BIDS LEFT")
af(Bids1)
Bids1.pack(side="top", padx = 30, pady = 10)
imagebid = ctk.CTkImage(dark_image=Image.open(r"assets\bid.png"),size=(50, 50))
bid3 = ctk.CTkLabel(master = Bids, text = "", image = imagebid)
bid3.pack(side="left", padx = 10, pady = 10)
Bids2 = ctk.CTkLabel(master = Bids, text = "11", justify = "left")
af(Bids2)
Bids2.pack(side="left", padx = 10, pady = 10)
Bids.grid(row=0,column=2,sticky='nsew',padx= 50, pady=30)

# Player Details Frame

player_frame = ctk.CTkFrame(auction_frame)
player_frame.grid_rowconfigure(0,weight=1)
player_frame.grid_rowconfigure(1,weight=1)
player_frame.grid_rowconfigure(2,weight=1)
player_frame.grid_rowconfigure(3,weight=1)
player_frame.grid_rowconfigure(4,weight=1)
player_frame.grid_rowconfigure(0)
player_frame.pack(padx= 20, pady= 10)

cplayer = ctk.CTkLabel(master = player_frame, text = "Current Player")
sf(cplayer)
cplayer.grid(row=0,padx=50,pady=10,sticky='w')

# Player Card

player_detail_frame = ctk.CTkFrame(player_frame)
player_detail_frame.grid(row=1, padx=50,pady=10)
playerimage = ctk.CTkLabel(master=player_detail_frame, text = "")
playerimage.configure(image = image1)
playerimage.pack(padx=20,pady=20)
playername = ctk.CTkLabel(master=player_detail_frame, text="Player Name")
mf(playername)
playername.pack(padx= 20, pady= 20)

# Details

dplayer = ctk.CTkLabel(master = player_frame, text = "Player Details")
sf(dplayer)
dplayer.grid(row=2,padx=50,pady=10,sticky='w')

# Bid Details

details_frame = ctk.CTkFrame(player_frame)
details_frame.grid_columnconfigure(0,weight=1)
details_frame.grid_columnconfigure(1,weight=1)
details_frame.grid_columnconfigure(2,weight=1)
details_frame.grid_rowconfigure(0)
details_frame.grid(row=3,padx= 20, pady= 10)

# Current Bid Amount

ca_frame = ctk.CTkFrame(details_frame)
ca_frame.grid(row=0,column=0, padx=20, pady = 20)
ca1 = ctk.CTkLabel(master = ca_frame, text = "CURRENT BID AMOUNT")
af(ca1)
ca1.pack(padx=20,pady=20,side="top")
ca2 = ctk.CTkLabel(master = ca_frame, text = "Current Bid Amount")
af(ca2)
ca3 = ctk.CTkLabel(master = ca_frame, text = "", image = imageam)
ca3.pack(side="left", padx = 10, pady = 10)
ca2.pack(padx=10,pady=20,side="left")

# Current Bidder

cb_frame = ctk.CTkFrame(details_frame)
cb_frame.grid(row=0,column=1, padx=20, pady = 20)
cb1 = ctk.CTkLabel(master = cb_frame, text = "CURRENT BIDDER")
af(cb1)
cb1.pack(padx=20,pady=20,side="top")
cb2 = ctk.CTkLabel(master = cb_frame, text = "Current Bidder")
af(cb2)
cbim = ctk.CTkImage(dark_image=Image.open(r"assets\pro.png"),size=(50, 50))
cb3 = ctk.CTkLabel(master = cb_frame, text = "", image = cbim)
cb3.pack(side="left", padx = 10, pady = 10)
cb2.pack(padx=10,pady=20,side="left")

# Next Bid Amount

nb_frame = ctk.CTkFrame(details_frame)
nb_frame.grid(row=0,column=2, padx=20, pady = 20)
nb1 = ctk.CTkLabel(master = nb_frame, text = "NEXT BID AMOUNT")
af(nb1)
nb1.pack(padx=20,pady=20,side="top")
nb2 = ctk.CTkLabel(master = nb_frame, text = "Next Bid Amount")
af(nb2)
nb3 = ctk.CTkLabel(master = nb_frame, text = "", image = imageam)
nb3.pack(side="left", padx = 10, pady = 10)
nb2.pack(padx=10,pady=20,side="left")

# Buttons

b_frame = ctk.CTkFrame(player_frame)
b_frame.grid(row=4,column=0, padx=20, pady = 20)

# Bid Button

bid = ctk.CTkButton(master = b_frame, text = "   BID   ", command=bid, fg_color = "#2FA572", hover_color = "#177D51")
bid.pack(side='left',pady=20,padx= 30)
mf(bid)

# Pass Button

pas = ctk.CTkButton(master = b_frame, text = " PASS ", command=pas, fg_color = "#840000", hover_color = "#630101")
pas.pack(side='right',pady=20,padx =30)
mf(pas)

# PAGE 3



# Run

show_page1()
window.state("zoomed")
window.mainloop()
