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



# Window

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

window = ctk.CTk()
window.title("IPL Auction Simulation")
window.geometry("1920x1080")

page1 = ctk.CTkFrame(window)
page1.grid_rowconfigure(0, weight=1)
page1.grid_rowconfigure(1, weight=1)
page1.grid_rowconfigure(2, weight=1)

page2 = ctk.CTkFrame(window)
page2.grid_rowconfigure(0)
page2.grid_columnconfigure(0, weight=1)
page2.grid_columnconfigure(1, weight=4)
page2.grid_columnconfigure(2, weight=1)

page3 = ctk.CTkFrame(window)
page3.grid_rowconfigure(0)
page3.grid_columnconfigure(0, weight=1)

profile_frame = ctk.CTkFrame(page2)
imageprofile = ctk.CTkLabel(profile_frame, text = "")
Teamname = ctk.CTkLabel(master = profile_frame, justify = "center", fg_color="transparent")

# PAGE 1

team = tk.StringVar(page2, )
list_team = ["ROYAL\nCHALLENGERS\nBANGALORE", "CHENNAI\nSUPER KINGS", "MUMBAI\nINDIANS", "SUNRISERS\nHYDERABAD", ]

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

image1 = ctk.CTkImage(dark_image=Image.open(r"./IPL Auction/assets/RCB.png"),size=(230, 230))

def fa() :
    show_page2(page1, page2, page3, imageprofile, image1, Teamname, name = "ROYAL\nCHALLENGERS\nBANGALORE")
    team = "ROYAL\nCHALLENGERS\nBANGALORE"
    return team

image_label1 = ctk.CTkButton(master = container1, image = image1, text = "", command = fa, fg_color = "transparent", hover_color = "#14375E")
image_label1.pack(padx = 20, pady = 10)

team1 = ctk.CTkButton(master = container1, command = fa, text = "ROYAL\nCHALLENGERS\nBANGALORE", )
bf(team1)
team1.pack(pady=20)
container1.grid(column = 0, row = 0, padx = 105, pady = 40, sticky = 'nsew')

# CSK

container2 = ctk.CTkFrame(master = containera)

image2 = ctk.CTkImage(dark_image=Image.open(r"./IPL Auction/assets/CSK.png"),size=(230, 230))

def fb() :
    show_page2(page1, page2, page3, imageprofile, image2, Teamname, name = "CHENNAI\nSUPER KINGS")
    team = "CHENNAI\nSUPER KINGS"
    return team
    
image_label2 = ctk.CTkButton(master = container2, image=image2, text = "", command = fb, fg_color = "transparent", hover_color = "#14375E")
image_label2.pack(padx = 20, pady = 20)

team2 = ctk.CTkButton(master = container2, command = fb, text = "CHENNAI\nSUPER KINGS")
bf(team2)
team2.pack(pady=20)
container2.grid(column = 1, row = 0, padx = 105, pady = 40, sticky = 'nsew')

# MI

container3 = ctk.CTkFrame(master = containera)

image3 = ctk.CTkImage(dark_image=Image.open(r"./IPL Auction/assets/MI.png"),size=(230, 230))

def fc() :
    show_page2(page1, page2, page3, imageprofile, image3, Teamname, name = "MUMBAI\nINDIANS")
    team = "MUMBAI\nINDIANS"
    return team

image_label3 = ctk.CTkButton(master = container3, image=image3, text = "", command = fc, fg_color = "transparent", hover_color = "#14375E")
image_label3.pack(padx = 20, pady = 20)

team3 = ctk.CTkButton(master = container3, text = "MUMBAI\nINDIANS", command = fc)
bf(team3)
team3.pack(pady=20)
container3.grid(column = 2, row = 0, padx = 105, pady = 40, sticky = 'nsew')

# SRH

container4 = ctk.CTkFrame(master = containera)

def fd() :
    show_page2(page1, page2, page3, imageprofile, image4, Teamname, name = "SUNRISERS\nHYDERABAD")
    team = "SUNRISERS\nHYDERABAD"
    return team

image4 = ctk.CTkImage(dark_image=Image.open(r"./IPL Auction/assets/SRH.png"),size=(230, 230))
image_label4 = ctk.CTkButton(master = container4, image=image4, text = "", command = fd, fg_color = "transparent", hover_color = "#14375E")
image_label4.pack(padx = 20, pady = 20)

team4 = ctk.CTkButton(master = container4, text = "SUNRISERS\nHYDERABAD", command = fd)
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

image5 = ctk.CTkImage(dark_image=Image.open(r"./IPL Auction/assets/RR.png"),size=(230, 230))

def fe() :
    show_page2(page1, page2, page3, imageprofile, image5, Teamname, name = "RAJASTHAN\nROYALS")
    team = "RAJASTHAN\nROYALS"
    return team

image_label5 = ctk.CTkButton(master = container5, image=image5, text = "", command = fe, fg_color = "transparent", hover_color = "#14375E")
image_label5.pack(padx = 20, pady = 20)

team5 = ctk.CTkButton(master = container5, text = "RAJASTHAN\nROYALS", command = fe)
bf(team5)
team5.pack(pady=20)
container5.grid(column = 0, row = 0, padx = 105, pady = 40, sticky = 'nsew')

# KKR

container6 = ctk.CTkFrame(master = containerb)

image6 = ctk.CTkImage(dark_image=Image.open(r"./IPL Auction/assets/KKR.png"),size=(230, 230))

def ff() :
    show_page2(page1, page2, page3, imageprofile, image6, Teamname, name = "KOLKATA\nKNIGHT RIDERS")

image_label6 = ctk.CTkButton(master = container6, image=image6, text = "", command = ff, fg_color = "transparent", hover_color = "#14375E")
image_label6.pack(padx = 20, pady = 20)

team6 = ctk.CTkButton(master = container6, text = "KOLKATA\nKNIGHT RIDERS", command = ff)
bf(team6)
team6.pack(pady=20)
container6.grid(column = 1, row = 0, padx = 105, pady = 40, sticky = 'nsew')

# PK

container7 = ctk.CTkFrame(master = containerb)

image7 = ctk.CTkImage(dark_image=Image.open(r"./IPL Auction/assets/PK.png"),size=(230, 230))

def fg() :
    show_page2(page1, page2, page3, imageprofile, image7, Teamname, name = "PUNJAB\nKINGS")

image_label7 = ctk.CTkButton(master = container7, image=image7, text = "", command = fg, fg_color = "transparent", hover_color = "#14375E")
image_label7.pack(padx = 20, pady = 20)

team7 = ctk.CTkButton(master = container7, text = "PUNJAB\nKINGS", command = fg)
bf(team7)
team7.pack(pady=20)
container7.grid(column = 2, row = 0, padx = 105, pady = 40, sticky = 'nsew')

# DC

container8 = ctk.CTkFrame(master = containerb)

image8 = ctk.CTkImage(dark_image=Image.open(r"./IPL Auction/assets/DC.png"),size=(230, 230))

def fh() :
    show_page2(page1, page2, page3, imageprofile, image8, Teamname, name = "DELHI\nCAPITALS")

image_label8 = ctk.CTkButton(master = container8, image=image8, text = "", command = fh, fg_color = "transparent", hover_color = "#14375E")
image_label8.pack(padx = 20, pady = 20)

team8 = ctk.CTkButton(master = container8, text = "DELHI\nCAPITALS", command = fh)
bf(team8)
team8.pack(pady=20)
container8.grid(column = 3, row = 0, padx = 105, pady = 40, sticky = 'nsew')


# PAGE 2

# Back

backim = ctk.CTkImage(dark_image=Image.open(r"./IPL Auction/assets/back.png"),size=(33, 35))
back_frame = ctk.CTkFrame(page2)
back_frame.grid(row = 0, column = 0,padx = 10, pady = 10, sticky = 'n')
back = ctk.CTkButton(master = back_frame, text = "", image = backim, command = back, width = 40)
back.pack(padx = 10, pady = 10)

# Profile

profile_frame.grid_rowconfigure(0,weight=1)
profile_frame.grid_columnconfigure(0, weight=1)
profile_frame.grid_rowconfigure(1,weight=4)
profile_frame.grid(row = 0,column=1, sticky = 'n')

# User Profile

imageprofile.grid(padx=20,pady=10)

bf(Teamname)
Teamname.grid(column=0, pady = 10, padx = 20)

# User Team

player_list_frame = ctk.CTkScrollableFrame(profile_frame, height = 590, width = 250, label_text = "Player List", label_font = ("Portico Rounded", 20), label_fg_color = "#1F538D", scrollbar_button_color = "#1F538D",scrollbar_button_hover_color = "#14375E")
player_list_frame.grid(column=0,padx=20,pady=20)

for i in range(1,16):
    playernameif = ctk.CTkFrame(master = player_list_frame)
    playernameif.pack(padx=10,pady=5)
    playernamei = ctk.CTkLabel(master = playernameif,text="Player %i" %i)
    pf(playernamei)
    playernamei.pack(padx=30,pady=10)

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
imageam = ctk.CTkImage(dark_image=Image.open(r"./IPL Auction/assets/x.png"),size=(50, 50))
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
imagets = ctk.CTkImage(dark_image=Image.open(r"./IPL Auction/assets/down.png"),size=(50, 50))
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
imagebid = ctk.CTkImage(dark_image=Image.open(r"./IPL Auction/assets/bid.png"),size=(50, 50))
bid3 = ctk.CTkLabel(master = Bids, text = "", image = imagebid)
bid3.pack(side="left", padx = 10, pady = 10)
Bids2 = ctk.CTkLabel(master = Bids, text = "15", justify = "left")
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

image_player = ctk.CTkImage(dark_image=Image.open(r"./IPL Auction/assets/profile.png"),size=(230, 230))
player_detail_frame = ctk.CTkFrame(player_frame)
player_detail_frame.grid(row=1, padx=50,pady=10)
playerimage = ctk.CTkLabel(master=player_detail_frame, text = "")
playerimage.configure(image = image_player)
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
cbim = ctk.CTkImage(dark_image=Image.open(r"./IPL Auction/assets/pro.png"),size=(50, 50))
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

# Next

next = ctk.CTkButton(master = b_frame, text = "   Auto   ", command = nex, width = 40)
mf(next)
next.pack(padx = 30, pady = 20)

# PAGE 3

team_list_frame = ctk.CTkScrollableFrame(page3, height = 900, width = 1900, label_text = "Final Teams", label_font = ("Portico Rounded", 30), scrollbar_button_color = "#1F538D",scrollbar_button_hover_color = "#14375E")
team_list_frame.grid(column=0,padx=20,pady=10)

# RCB

rcb_team_list_frame = ctk.CTkScrollableFrame(team_list_frame, height = 350, width = 1800, label_text = "ROYAL CHALLENGERS BANGALORE", label_font = ("Portico Rounded", 20), label_fg_color = "transparent", scrollbar_button_color = "#1F538D",scrollbar_button_hover_color = "#14375E", orientation = "horizontal")
rcb_team_list_frame.pack(padx=20,pady=10)

for i in range(1,16):
    player_detail_frame = ctk.CTkFrame(rcb_team_list_frame)
    player_detail_frame.pack(padx=50,pady=10, side = 'left')
    playerimage = ctk.CTkLabel(master=player_detail_frame, text = "")
    playerimage.configure(image = image_player)
    playerimage.pack(padx=20,pady=20)
    playername = ctk.CTkLabel(master=player_detail_frame, text="Player Name")
    mf(playername)
    playername.pack(padx= 20, pady= 20)
    
# CSK

csk_team_list_frame = ctk.CTkScrollableFrame(team_list_frame, height = 350, width = 1800, label_text = "CHENNAI SUPER KINGS", label_font = ("Portico Rounded", 20), label_fg_color = "transparent", scrollbar_button_color = "#1F538D",scrollbar_button_hover_color = "#14375E", orientation = "horizontal")
csk_team_list_frame.pack(padx=20,pady=10)

for i in range(1,16):
    player_detail_frame = ctk.CTkFrame(csk_team_list_frame)
    player_detail_frame.pack(padx=50,pady=10, side = 'left')
    playerimage = ctk.CTkLabel(master=player_detail_frame, text = "")
    playerimage.configure(image = image_player)
    playerimage.pack(padx=20,pady=20)
    playername = ctk.CTkLabel(master=player_detail_frame, text="Player Name")
    mf(playername)
    playername.pack(padx= 20, pady= 20)

# MI

mi_team_list_frame = ctk.CTkScrollableFrame(team_list_frame, height = 350, width = 1800, label_text = "MUMBAI INDIANS", label_font = ("Portico Rounded", 20), label_fg_color = "transparent", scrollbar_button_color = "#1F538D",scrollbar_button_hover_color = "#14375E", orientation = "horizontal")
mi_team_list_frame.pack(padx=20,pady=10)

for i in range(1,16):
    player_detail_frame = ctk.CTkFrame(mi_team_list_frame)
    player_detail_frame.pack(padx=50,pady=10, side = 'left')
    playerimage = ctk.CTkLabel(master=player_detail_frame, text = "")
    playerimage.configure(image = image_player)
    playerimage.pack(padx=20,pady=20)
    playername = ctk.CTkLabel(master=player_detail_frame, text="Player Name")
    mf(playername)
    playername.pack(padx= 20, pady= 20)

# SRH

srh_team_list_frame = ctk.CTkScrollableFrame(team_list_frame, height = 350, width = 1800, label_text = "SUNRISERS HYDERABAD", label_font = ("Portico Rounded", 20), label_fg_color = "transparent", scrollbar_button_color = "#1F538D",scrollbar_button_hover_color = "#14375E", orientation = "horizontal")
srh_team_list_frame.pack(padx=20,pady=10)

for i in range(1,16):
    player_detail_frame = ctk.CTkFrame(srh_team_list_frame)
    player_detail_frame.pack(padx=50,pady=10, side = 'left')
    playerimage = ctk.CTkLabel(master=player_detail_frame, text = "")
    playerimage.configure(image = image_player)
    playerimage.pack(padx=20,pady=20)
    playername = ctk.CTkLabel(master=player_detail_frame, text="Player Name")
    mf(playername)
    playername.pack(padx= 20, pady= 20)

# RR

rr_team_list_frame = ctk.CTkScrollableFrame(team_list_frame, height = 350, width = 1800, label_text = "RAJASTHAN ROYALS", label_font = ("Portico Rounded", 20), label_fg_color = "transparent", scrollbar_button_color = "#1F538D",scrollbar_button_hover_color = "#14375E", orientation = "horizontal")
rr_team_list_frame.pack(padx=20,pady=10)

for i in range(1,16):
    player_detail_frame = ctk.CTkFrame(rr_team_list_frame)
    player_detail_frame.pack(padx=50,pady=10, side = 'left')
    playerimage = ctk.CTkLabel(master=player_detail_frame, text = "")
    playerimage.configure(image = image_player)
    playerimage.pack(padx=20,pady=20)
    playername = ctk.CTkLabel(master=player_detail_frame, text="Player Name")
    mf(playername)
    playername.pack(padx= 20, pady= 20)

# KKR

kkr_team_list_frame = ctk.CTkScrollableFrame(team_list_frame, height = 350, width = 1800, label_text = "KOLKATA KNIGHT RIDERS", label_font = ("Portico Rounded", 20), label_fg_color = "transparent", scrollbar_button_color = "#1F538D",scrollbar_button_hover_color = "#14375E", orientation = "horizontal")
kkr_team_list_frame.pack(padx=20,pady=10)

for i in range(1,16):
    player_detail_frame = ctk.CTkFrame(kkr_team_list_frame)
    player_detail_frame.pack(padx=50,pady=10, side = 'left')
    playerimage = ctk.CTkLabel(master=player_detail_frame, text = "")
    playerimage.configure(image = image_player)
    playerimage.pack(padx=20,pady=20)
    playername = ctk.CTkLabel(master=player_detail_frame, text="Player Name")
    mf(playername)
    playername.pack(padx= 20, pady= 20)

# PK

pk_team_list_frame = ctk.CTkScrollableFrame(team_list_frame, height = 350, width = 1800, label_text = "PUNJAB KINGS", label_font = ("Portico Rounded", 20), label_fg_color = "transparent", scrollbar_button_color = "#1F538D",scrollbar_button_hover_color = "#14375E", orientation = "horizontal")
pk_team_list_frame.pack(padx=20,pady=10)

for i in range(1,16):
    player_detail_frame = ctk.CTkFrame(pk_team_list_frame)
    player_detail_frame.pack(padx=50,pady=10, side = 'left')
    playerimage = ctk.CTkLabel(master=player_detail_frame, text = "")
    playerimage.configure(image = image_player)
    playerimage.pack(padx=20,pady=20)
    playername = ctk.CTkLabel(master=player_detail_frame, text="Player Name")
    mf(playername)
    playername.pack(padx= 20, pady= 20)

# DC

dc_team_list_frame = ctk.CTkScrollableFrame(team_list_frame, height = 350, width = 1800, label_text = "DELHI CAPITALS", label_font = ("Portico Rounded", 20), label_fg_color = "transparent", scrollbar_button_color = "#1F538D",scrollbar_button_hover_color = "#14375E", orientation = "horizontal")
dc_team_list_frame.pack(padx=20,pady=10)

for i in range(1,16):
    player_detail_frame = ctk.CTkFrame(dc_team_list_frame)
    player_detail_frame.pack(padx=50,pady=10, side = 'left')
    playerimage = ctk.CTkLabel(master=player_detail_frame, text = "")
    playerimage.configure(image = image_player)
    playerimage.pack(padx=20,pady=20)
    playername = ctk.CTkLabel(master=player_detail_frame, text="Player Name")
    mf(playername)
    playername.pack(padx= 20, pady= 20)


# Run

show_page1(page1,page2,page3)
window.state("zoomed")
window.mainloop()
