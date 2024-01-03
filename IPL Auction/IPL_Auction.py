import tkinter as tk
import customtkinter as ctk
from PIL import Image
from auction_lib import *
import mysql.connector
import random
import time
import sqlite3
import io
import base64
import gc

gc.disable()  # Disabling garbage collection

# Connecting to mysql database

connection = sqlite3.connect('iplauction_images.db')
cursor = connection.cursor()
x = "use iplplayers;"
cursor.execute(x)
cursor.execute("select * from auction;")
results = cursor.fetchall()


# Functions

def show_page2(page1,page2,page3,imgprof, image, Teamname, name):
    page1.pack_forget()
    page2.pack()
    page3.pack_forget()
    start_page.pack_forget
    imgprof.configure(image=image)
    Teamname.configure(text = name)
    bid_start()
    
def bid_start():
    global namep, y
    
    y = int(player_index.get())
    if y == 120 :
        show_page3(page1,page2,page3)
    namep = results[y][0]
    amou = results[y][1]
    am = str(float(amou)/10000000)+" Cr"
    
    try:
        new_image_path = results[y][2] 
        image = get_image(new_image_path)
        playerimage1.configure(image = image)
    except Exception as e:
        print(e)
    pn.set(namep)
    bidam.set(am)
    nbidam.set(str(round(float(amou)/10000000+0.1,1))+" Cr")
    y += 1
    player_index.set(y)
    window.update_idletasks()

def back():
    def yes1():
        list_team.append(team.get())
        y = 0
        cursor.execute("Delete from csk")
        cursor.execute("Delete from rcb")
        cursor.execute("Delete from mi")
        cursor.execute("Delete from srh")
        cursor.execute("Delete from rr")
        cursor.execute("Delete from kkr")
        cursor.execute("Delete from pk")
        cursor.execute("Delete from dc")
        connection.commit()

        show_page(page1, start_page, page2, page3)
        windowb.destroy()
    windowb = ctk.CTkToplevel()
    text = "You are about to leave the game. \nAre you sure you want to proceed?"
    warn(windowb, text, yes1)


bidl = 15  
def bid():
    def re(r):
        i = 1
        while i < 2:
                bidb.configure(state = "disabled")
                cursor.execute('select count(0) from %s'%d[r])
                if cursor.fetchall()[0][0] != 15:
                    cb2.configure(text = r)
                    i += 1
                    bidam.set(str(round(float(nbidam.get()[0:-3:]),1))+" Cr")
                    nbidam.set(str(round(float(nbidam.get()[0:-3:])+0.1,1))+" Cr")
                    text1 = "Another player has placed a bid for this player.\nDo you wish to rebid for this player"
                    rebid(windowc, text1, yes, no)
                    
                else:
                    list_team.remove(r)
                    r = random.choice(list_team)

    def cont():
        auto(list_team)
        windowb.destroy()
        show_page3(page1, page2, page3)

    def yes():
        t = team.get()
        cb2.configure(text = t)
        windowc.destroy()
        time.sleep(1)
        bidb.configure(state = "normal")
        bid()

    def no():
        cb2.configure(text = r)
        cursor.execute('insert into %s select * from auction where Name = "%s"' %(d[r],namep))
        connection.commit()
        windowc.destroy()
        time.sleep(1)
        bidb.configure(state = "normal")
        bid_start()

    x = int(bidno.get()) - 1
    t = team.get()
    cb2.configure(text = t)
    if x == 0:
        bidb.configure(state="disabled")
        windowb = ctk.CTkToplevel()
        text = "Congratulations you have successfully created your team.\nPlease wait until the other teams are formed.\nClick on continue to proceed."
        warn1(windowb, text, cont)
    
    l1 = [0, 1, 1]
    z = random.choice(l1)
    if z == 1:
        windowc = ctk.CTkToplevel()
        r = random.choice(list_team)
        time.sleep(1)
        re(r)

    else:
        bidno.set(x)
        tspent.set(str(round(float(bidam.get()[0:-3:]) + float(tspent.get()[0:-3:]),1))+" Cr")
        time.sleep(0.25)
        try:
            t = team.get()
            cb2.configure(text = t)
        except:
            pass

        name = team.get()
        for i in d:
            if name == i:
                cursor.execute('insert into %s select * from auction where Name = "%s"' %(d[name],namep))
                connection.commit()

        playernameif = ctk.CTkFrame(master = player_list_frame)
        playernameif.pack(padx=10,pady=5)
        e = pn.get()
        playernamei = ctk.CTkLabel(master = playernameif,text=e)
        pf(playernamei)
        playernamei.pack(padx=30,pady=10)

        bid_start()    

def pas():
    i = 1
    while i < 2:
            x = random.choice(list_team)
            cursor.execute('select count(0) from %s'%d[x])
            if cursor.fetchall()[0][0] != 15:
                cursor.execute('insert into %s select * from auction where Name = "%s"' %(d[x],namep))
                connection.commit()
                time.sleep(0.05)
                cb2.configure(text = x)
                bid_start()
                i += 1
                
            else:
                list_team.remove(x)

def nex():
    def yes1():
        list_team.append(team.get())
        auto(list_team)   
        show_page3(page1, page2, page3)
        windowb.destroy()

    windowb = ctk.CTkToplevel()
    text = "You are about to let the game auto form your team.\nAre you sure you want to proceed?"
    warn(windowb=windowb, text=text, cmd=yes1)

def show_page3(page1,page2,page3):
    page1.pack_forget()
    page2.pack_forget()
    start_page.pack_forget()
    page3.pack()
    frame_list = [rcb, csk, mi, srh, rr, kkr, pk, dc]
    q = 0
    for j in d:
        cursor.execute('select * from %s'%d[j])
        data = cursor.fetchall()
        for i in range(len(data)):
            n = data[i][0]
            new_image_path = data[i][2]
            new_image = get_image(new_image_path)
            player_detail_frame = ctk.CTkFrame(master=frame_list[q])
            playername = ctk.CTkLabel(master=player_detail_frame, text=n)
            playerimage = ctk.CTkLabel(master=player_detail_frame, text = "", image = new_image)
            mf(playername)
            player_detail_frame.pack(padx=50,pady=10, side = 'left')
            playerimage.pack(padx=20,pady=20)
            playername.pack(padx= 20, pady= 20)
        q += 1

def auto(lt):
    i=y
    while i < 120:
        x = random.choice(lt)
        cursor.execute('select count(0) from %s'%d[x])
        
        if cursor.fetchall()[0][0] != 15:
            cursor.execute('insert into %s select * from auction where Name = "%s"' %(d[x],namep))
            connection.commit()
            time.sleep(0.05)
            bid_start()
            i += 1
                
        else:
            list_team.remove(x) 

# Window

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

window = ctk.CTk()
window.title("IPL Auction Simulation")
window.geometry("1920x1080")

start_page = ctk.CTkFrame(window)

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

# Start page
def p():
    def yes2():
        windowb.destroy()
        show_page(page1, start_page, page2, page3)
        
    windowb = ctk.CTkToplevel()
    start(windowb, yes1=yes2)

bg = ctk.CTkImage(dark_image=Image.open(r"./IPL Auction/assets/bg1.png"), size = (1920,1080))
bg_label = ctk.CTkLabel(master = start_page, text = "", image = bg)
bg_label.grid(row = 0, column = 0)
Start_button = ctk.CTkButton(master = start_page, text = "START", fg_color="#1A3989", command=p, width = 200, height=50, bg_color="transparent", corner_radius = 0, border_width = 0)
Start_button.grid(row = 0, column = 0, pady=200, padx= 30, sticky = 's')
mf(Start_button)

# PAGE 1

# Vars

player_index = tk.StringVar(value=0)
team = tk.StringVar()
d = {"ROYAL\nCHALLENGERS\nBANGALORE" : "rcb", "CHENNAI\nSUPER KINGS" : "csk", "MUMBAI\nINDIANS" : "mi", "SUNRISERS\nHYDERABAD" : "srh", "RAJASTHAN\nROYALS" : "rr", "KOLKATA\nKNIGHT RIDERS" : "kkr", "PUNJAB\nKINGS" : "pk", "DELHI\nCAPITALS" : "dc"}
list_team = ["ROYAL\nCHALLENGERS\nBANGALORE", "CHENNAI\nSUPER KINGS", "MUMBAI\nINDIANS", "SUNRISERS\nHYDERABAD", "RAJASTHAN\nROYALS", "KOLKATA\nKNIGHT RIDERS", "PUNJAB\nKINGS", "DELHI\nCAPITALS"]
bidno = tk.StringVar()
bidno.set(bidl)
bidam = tk.StringVar()
nbidam = tk.StringVar()
tspent = tk.StringVar()
inti = "0.0 Cr"
tspent.set(inti)
pn = tk.StringVar()


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
    team.set("ROYAL\nCHALLENGERS\nBANGALORE")
    list_team.remove("ROYAL\nCHALLENGERS\nBANGALORE")

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
    team.set("CHENNAI\nSUPER KINGS")
    list_team.remove("CHENNAI\nSUPER KINGS")
    
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
    team.set("MUMBAI\nINDIANS")
    list_team.remove("MUMBAI\nINDIANS")

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
    team.set("SUNRISERS\nHYDERABAD")
    list_team.remove("SUNRISERS\nHYDERABAD")

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
    team.set("RAJASTHAN\nROYALS")
    list_team.remove("RAJASTHAN\nROYALS")

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
    team.set("KOLKATA\nKNIGHT RIDERS")
    list_team.remove("KOLKATA\nKNIGHT RIDERS")

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
    team.set("PUNJAB\nKINGS")
    list_team.remove("PUNJAB\nKINGS")

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
    team.set("DELHI\nCAPITALS")
    list_team.remove("DELHI\nCAPITALS")

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
Totalam2 = ctk.CTkLabel(master = Totalam, text = "30 Cr")
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
Totalsp2 = ctk.CTkLabel(master = Totalsp, textvariable = tspent)
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
Bids2 = ctk.CTkLabel(master = Bids, textvariable=bidno, justify = "left")
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
playerimage1 = ctk.CTkLabel(master=player_detail_frame, text = "", image=image_player)
playerimage1.pack(padx=20,pady=20)
playername = ctk.CTkLabel(master=player_detail_frame, textvariable = pn)
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
ca2 = ctk.CTkLabel(master = ca_frame, textvariable = bidam)
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
cb2 = ctk.CTkLabel(master = cb_frame, text = "Current\nBidder")
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
nb2 = ctk.CTkLabel(master = nb_frame, textvariable = nbidam)
af(nb2)
nb3 = ctk.CTkLabel(master = nb_frame, text = "", image = imageam)
nb3.pack(side="left", padx = 10, pady = 10)
nb2.pack(padx=10,pady=20,side="left")

b_frame = ctk.CTkFrame(player_frame)
b_frame.grid(row=4,column=0, padx=20, pady = 20)

# Bid Button

bidb = ctk.CTkButton(master = b_frame, text = "   BID   ", command=bid, fg_color = "#2FA572", hover_color = "#177D51")
bidb.pack(side='left',pady=20,padx= 30)
mf(bidb)

# Pass Button

pasb = ctk.CTkButton(master = b_frame, text = " PASS ", command=pas, fg_color = "#840000", hover_color = "#630101")
pasb.pack(side='right',pady=20,padx =30)
mf(pasb)

# Next

next = ctk.CTkButton(master = b_frame, text = "   Auto   ", command = nex, width = 40)
mf(next)
next.pack(padx = 30, pady = 20)

# PAGE 3

team_list_frame = ctk.CTkScrollableFrame(page3, height = 900, width = 1900, label_text = "Final Teams", label_font = ("Portico Rounded", 30), scrollbar_button_color = "#1F538D",scrollbar_button_hover_color = "#14375E")
team_list_frame.grid(column=0,padx=20,pady=10)

# RCB

rcb = ctk.CTkScrollableFrame(team_list_frame, height = 350, width = 1800, label_text = "ROYAL CHALLENGERS BANGALORE", label_font = ("Portico Rounded", 20), label_fg_color = "transparent", scrollbar_button_color = "#1F538D",scrollbar_button_hover_color = "#14375E", orientation = "horizontal")
rcb.pack(padx=20,pady=10)

# CSK

csk = ctk.CTkScrollableFrame(team_list_frame, height = 350, width = 1800, label_text = "CHENNAI SUPER KINGS", label_font = ("Portico Rounded", 20), label_fg_color = "transparent", scrollbar_button_color = "#1F538D",scrollbar_button_hover_color = "#14375E", orientation = "horizontal")
csk.pack(padx=20,pady=10)

# MI

mi = ctk.CTkScrollableFrame(team_list_frame, height = 350, width = 1800, label_text = "MUMBAI INDIANS", label_font = ("Portico Rounded", 20), label_fg_color = "transparent", scrollbar_button_color = "#1F538D",scrollbar_button_hover_color = "#14375E", orientation = "horizontal")
mi.pack(padx=20,pady=10)

# SRH

srh = ctk.CTkScrollableFrame(team_list_frame, height = 350, width = 1800, label_text = "SUNRISERS HYDERABAD", label_font = ("Portico Rounded", 20), label_fg_color = "transparent", scrollbar_button_color = "#1F538D",scrollbar_button_hover_color = "#14375E", orientation = "horizontal")
srh.pack(padx=20,pady=10)

# RR

rr = ctk.CTkScrollableFrame(team_list_frame, height = 350, width = 1800, label_text = "RAJASTHAN ROYALS", label_font = ("Portico Rounded", 20), label_fg_color = "transparent", scrollbar_button_color = "#1F538D",scrollbar_button_hover_color = "#14375E", orientation = "horizontal")
rr.pack(padx=20,pady=10)

# KKR

kkr = ctk.CTkScrollableFrame(team_list_frame, height = 350, width = 1800, label_text = "KOLKATA KNIGHT RIDERS", label_font = ("Portico Rounded", 20), label_fg_color = "transparent", scrollbar_button_color = "#1F538D",scrollbar_button_hover_color = "#14375E", orientation = "horizontal")
kkr.pack(padx=20,pady=10)

# PK

pk = ctk.CTkScrollableFrame(team_list_frame, height = 350, width = 1800, label_text = "PUNJAB KINGS", label_font = ("Portico Rounded", 20), label_fg_color = "transparent", scrollbar_button_color = "#1F538D",scrollbar_button_hover_color = "#14375E", orientation = "horizontal")
pk.pack(padx=20,pady=10)

# DC

dc = ctk.CTkScrollableFrame(team_list_frame, height = 350, width = 1800, label_text = "DELHI CAPITALS", label_font = ("Portico Rounded", 20), label_fg_color = "transparent", scrollbar_button_color = "#1F538D",scrollbar_button_hover_color = "#14375E", orientation = "horizontal")
dc.pack(padx=20,pady=10)

# Run

window.state(newstate="zoomed")
show_page(start_page, page1, page2, page3)
window.mainloop()
cursor.execute("Delete from csk")
cursor.execute("Delete from rcb")
cursor.execute("Delete from mi")
cursor.execute("Delete from srh")
cursor.execute("Delete from rr")
cursor.execute("Delete from kkr")
cursor.execute("Delete from pk")
cursor.execute("Delete from dc")
connection.commit()
