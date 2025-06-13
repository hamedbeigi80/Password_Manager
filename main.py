#!/usr/bin/env python3
"""
Password Manager - A simple desktop password manager
Author: Hamed Ahmadbeigi
Date: 2025
Description: Generate, store, and retrieve passwords with a user-friendly GUI
"""

from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
import os

# Constants
DATA_FILE = "data.json"
LOGO_FILE = "logo.png"
DEFAULT_EMAIL = "your.email@example.com"  # Change this to your email


class PasswordManager:
    """Main Password Manager Class"""

    def __init__(self):
        self.setup_ui()

    def password_generator(self):
        """Generate a strong random password"""
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                   'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                   'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        # Generate password components
        password_letters = [choice(letters) for _ in range(randint(8, 10))]
        password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
        password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

        # Combine and shuffle
        password_list = password_letters + password_symbols + password_numbers
        shuffle(password_list)
        password = "".join(password_list)

        # Clear previous password and insert new one
        self.password_entry.delete(0, END)
        self.password_entry.insert(0, password)

        # Copy to clipboard
        pyperclip.copy(password)
        messagebox.showinfo("Success", "Password generated and copied to clipboard!")

    def save_password(self):
        """Save password to JSON file"""
        website_name = self.website_entry.get().strip()
        password = self.password_entry.get()
        email = self.email_entry.get().strip()

        # Validation
        if not website_name or not password:
            messagebox.showwarning("Input Error", "Please don't leave Website or Password fields empty!")
            return

        if not email:
            messagebox.showwarning("Input Error", "Please enter an email address!")
            return

        # Confirm save
        is_ok = messagebox.askokcancel(
            title=website_name,
            message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it ok to save?"
        )

        if is_ok:
            new_data = {
                website_name: {
                    "email": email,
                    "password": password
                }
            }

            try:
                # Try to read existing data
                with open(DATA_FILE, "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                # Create new file if it doesn't exist
                with open(DATA_FILE, "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Update existing data
                data.update(new_data)
                with open(DATA_FILE, "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                # Clear entries after saving
                self.website_entry.delete(0, END)
                self.password_entry.delete(0, END)
                messagebox.showinfo("Success", f"Password for {website_name} saved successfully!")

    def find_password(self):
        """Search for saved password"""
        website = self.website_entry.get().strip()

        if not website:
            messagebox.showwarning("Input Error", "Please enter a website name to search!")
            return

        try:
            with open(DATA_FILE, "r") as data_file:
                content = data_file.read().strip()
                if not content:  # File is empty
                    raise FileNotFoundError("Empty data file")
                data_file.seek(0)  # Reset file pointer
                data = json.load(data_file)
        except (FileNotFoundError, json.JSONDecodeError):
            messagebox.showerror("Error", "No password data found or file is corrupted. Save some passwords first!")
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                # Copy password to clipboard
                pyperclip.copy(password)
                messagebox.showinfo(
                    title=website,
                    message=f"Email: {email}\nPassword: {password}\n\nPassword copied to clipboard!"
                )
            else:
                messagebox.showinfo("Not Found", f"No password found for {website}")

    def setup_ui(self):
        """Setup the user interface"""
        # Main window
        self.window = Tk()
        self.window.title("Password Manager")
        self.window.config(padx=50, pady=50, bg="white")
        self.window.resizable(False, False)

        # Logo
        self.canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
        if os.path.exists(LOGO_FILE):
            try:
                self.logo_img = PhotoImage(file=LOGO_FILE)
                self.canvas.create_image(100, 100, image=self.logo_img)
            except:
                # If logo fails to load, create a simple text logo
                self.canvas.create_text(100, 100, text="🔐", font=("Arial", 50))
        else:
            # Create a simple text logo if no image file
            self.canvas.create_text(100, 100, text="🔐", font=("Arial", 50))

        self.canvas.grid(column=1, row=0, pady=(0, 20))

        # Website
        self.website_label = Label(text="Website:", font=("Arial", 10), bg="white")
        self.website_label.grid(column=0, row=1, sticky="e", padx=(0, 5))

        self.website_entry = Entry(width=21, font=("Arial", 10))
        self.website_entry.grid(column=1, row=1, padx=(0, 5))
        self.website_entry.focus()

        self.search_button = Button(
            text="Search",
            width=13,
            command=self.find_password,
            font=("Arial", 10),
            bg="#4CAF50",
            fg="white",
            cursor="hand2"
        )
        self.search_button.grid(column=2, row=1)

        # Email
        self.email_label = Label(text="Email/Username:", font=("Arial", 10), bg="white")
        self.email_label.grid(column=0, row=2, sticky="e", padx=(0, 5), pady=(10, 0))

        self.email_entry = Entry(width=35, font=("Arial", 10))
        self.email_entry.grid(column=1, row=2, columnspan=2, pady=(10, 0))
        self.email_entry.insert(0, DEFAULT_EMAIL)

        # Password
        self.password_label = Label(text="Password:", font=("Arial", 10), bg="white")
        self.password_label.grid(column=0, row=3, sticky="e", padx=(0, 5), pady=(10, 0))

        self.password_entry = Entry(width=21, font=("Arial", 10))
        self.password_entry.grid(column=1, row=3, padx=(0, 5), pady=(10, 0))

        self.generate_button = Button(
            text="Generate Password",
            command=self.password_generator,
            font=("Arial", 10),
            bg="#2196F3",
            fg="white",
            cursor="hand2"
        )
        self.generate_button.grid(column=2, row=3, pady=(10, 0))

        # Add button
        self.add_button = Button(
            text="Add Password",
            width=36,
            command=self.save_password,
            font=("Arial", 10, "bold"),
            bg="#FF9800",
            fg="white",
            cursor="hand2"
        )
        self.add_button.grid(column=1, row=4, columnspan=2, pady=(20, 0))

        # Status label
        self.status_label = Label(
            text="Ready to manage your passwords!",
            font=("Arial", 8),
            fg="gray",
            bg="white"
        )
        self.status_label.grid(column=1, row=5, columnspan=2, pady=(10, 0))

        # Start the GUI
        self.window.mainloop()


def main():
    """Main function to run the password manager"""
    try:
        app = PasswordManager()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
