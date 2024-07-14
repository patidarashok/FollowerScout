import tkinter as tk
import customtkinter as ctk
import requests
from bs4 import BeautifulSoup
from tkinter import filedialog, messagebox

class InstaFollowerFilterApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Follower Scout")
        self.geometry("400x500")

        self.label = ctk.CTkLabel(self, text="Select File and Filter Criteria")
        self.label.pack(pady=10)

        self.filter_button = ctk.CTkButton(self, text="Select File", command=self.select_file)
        self.filter_button.pack(pady=10)

        self.min_followers_entry = ctk.CTkEntry(self, placeholder_text="Min Followers")
        self.min_followers_entry.pack(pady=5)
        self.min_followers_entry.configure(state="disabled")

        self.max_followers_entry = ctk.CTkEntry(self, placeholder_text="Max Followers")
        self.max_followers_entry.pack(pady=5)
        self.max_followers_entry.configure(state="disabled")

        self.apply_filter_button = ctk.CTkButton(self, text="Apply Filter", command=self.apply_filter)
        self.apply_filter_button.pack(pady=10)
        self.apply_filter_button.configure(state="disabled")

    def select_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if self.file_path:
            self.min_followers_entry.configure(state="normal")
            self.max_followers_entry.configure(state="normal")
            self.apply_filter_button.configure(state="normal")

    def apply_filter(self):
        try:
            with open(self.file_path, 'r') as file:
                users = file.read().splitlines()

            try:
                min_followers = int(self.min_followers_entry.get())
                max_followers = int(self.max_followers_entry.get())
            except ValueError:
                messagebox.showerror("Input Error", "Please enter valid numbers for followers range.")
                return

            output_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
            if not output_file:
                messagebox.showinfo("Cancelled", "Save operation was cancelled.")
                return

            with open(output_file, 'w') as file:
                for user in users:
                    try:
                        followers_count = self.get_followers_count(user)

                        if followers_count is not None and min_followers <= followers_count <= max_followers:
                            file.write(user + "\n")
                            file.flush()  # Ensure the data is written to disk immediately
                    except Exception as e:
                        print(f"Error processing user {user}: {str(e)}")

            messagebox.showinfo("Success", "Filtered users saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def get_followers_count(self, username):
        url = f"https://www.instagram.com/{username}/"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            meta_tag = soup.find('meta', attrs={'name': 'description'})
            if meta_tag:
                description = meta_tag['content']
                followers_text = description.split('-')[0].split()[0]
                followers_count = self.parse_followers(followers_text)
                print(followers_count)
                return followers_count
        return None

    def parse_followers(self, followers_text):
        followers_text = followers_text.lower()
        if 'k' in followers_text:
            return int(float(followers_text.replace('k', '')) * 1000)
        elif 'm' in followers_text:
            return int(float(followers_text.replace('m', '')) * 1000000)
        else:
            return int(followers_text.replace(',', ''))

if __name__ == "__main__":
    app = InstaFollowerFilterApp()
    app.mainloop()
