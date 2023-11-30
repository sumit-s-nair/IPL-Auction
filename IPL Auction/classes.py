import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

class AuctionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Player Auction")

        # Database connection details
        self.db_connection = mysql.connector.connect(host='127.0.0.1', database='iplplayers', user='root', password='admin')
        self.cursor = self.db_connection.cursor()

        # Variables
        self.selected_team = tk.StringVar()
        self.bid_player_index = 0

        # Team selection page
        self.team_selection_page()

    def team_selection_page(self):
        label = tk.Label(self.root, text="Select Team:")
        label.pack(pady=10)

        teams = ["Team A", "Team B", "Team C"]
        team_dropdown = ttk.Combobox(self.root, textvariable=self.selected_team, values=teams)
        team_dropdown.pack(pady=10)

        next_button = tk.Button(self.root, text="Next", command=self.bid_page)
        next_button.pack(pady=10)

    def bid_page(self):
        team_name = self.selected_team.get()
        if not team_name:
            messagebox.showwarning("Warning", "Please select a team.")
            return

        # Fetch players from the database for bidding
        self.cursor.execute("SELECT Name, BASEPRICE, Image FROM auction")
        players = self.cursor.fetchall()

        # Bid page
        self.root.destroy()
        bid_root = tk.Tk()
        bid_root.title(f"Bid for Players - {team_name}")

        player_name_var = tk.StringVar(value=players[self.bid_player_index][0])
        base_price_var = tk.StringVar(value=players[self.bid_player_index][1])
        bid_var = tk.DoubleVar()

        player_label = tk.Label(bid_root, text="Player:")
        player_label.grid(row=0, column=0, padx=10, pady=10)
        player_entry = tk.Entry(bid_root, textvariable=player_name_var, state='readonly')
        player_entry.grid(row=0, column=1, padx=10, pady=10)

        base_price_label = tk.Label(bid_root, text="Base Price:")
        base_price_label.grid(row=1, column=0, padx=10, pady=10)
        base_price_entry = tk.Entry(bid_root, textvariable=base_price_var, state='readonly')
        base_price_entry.grid(row=1, column=1, padx=10, pady=10)

        # Load and display player image
        image_path = players[self.bid_player_index][2]
        image = Image.open(image_path)
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)

        image_label = tk.Label(bid_root, image=photo)
        image_label.image = photo  # Keep reference to the image to prevent garbage collection
        image_label.grid(row=0, column=2, rowspan=3, padx=10, pady=10)

        bid_label = tk.Label(bid_root, text="Your Bid:")
        bid_label.grid(row=2, column=0, padx=10, pady=10)
        bid_entry = tk.Entry(bid_root, textvariable=bid_var)
        bid_entry.grid(row=2, column=1, padx=10, pady=10)

        def place_bid():
            nonlocal player_name_var, base_price_var, bid_var
            nonlocal players

            bid_amount = bid_var.get()
            if bid_amount >= players[self.bid_player_index][1]:
                messagebox.showinfo("Bid Placed", f"Bid of {bid_amount}$ placed for {player_name_var.get()}")
                # Add logic to update team/player details in the database

                # Move to the next player
                self.bid_player_index += 1

                if self.bid_player_index < len(players):
                    # Update player details
                    player_name_var.set(players[self.bid_player_index][0])
                    base_price_var.set(players[self.bid_player_index][1])

                    # Load and display new player image
                    new_image_path = players[self.bid_player_index][2]
                    new_image = Image.open(new_image_path)
                    new_image = new_image.resize((100, 100))
                    new_photo = ImageTk.PhotoImage(new_image)
                    image_label.configure(image=new_photo)
                    image_label.image = new_photo  # Keep reference to the image

                    bid_var.set("")
                else:
                    messagebox.showinfo("Auction Completed", "All players have been auctioned.")
                    bid_root.destroy()
                    self.display_teams_page()

            else:
                messagebox.showwarning("Invalid Bid", "Bid must be greater than or equal to the base price.")

        bid_button = tk.Button(bid_root, text="Place Bid", command=place_bid)
        bid_button.grid(row=3, column=1, pady=10)

    def display_teams_page(self):
        # Display teams page
        teams_page = tk.Tk()
        teams_page.title("Teams")

        # Fetch teams and players from the database and display them in a Treeview
        self.cursor.execute("SELECT team_name, player_name FROM teams")
        team_data = self.cursor.fetchall()

        tree = ttk.Treeview(teams_page, columns=("Team Name", "Player Name"), show="headings")
        tree.heading("Team Name", text="Team Name")
        tree.heading("Player Name", text="Player Name")

        for row in team_data:
            tree.insert("", "end", values=row)

        tree.pack(padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = AuctionApp(root)
    root.mainloop()