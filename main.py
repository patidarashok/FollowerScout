import tkinter as tk
import customtkinter as ctk
import instaloader
from tkinter import filedialog, messagebox

L = instaloader.Instaloader()

class InstaFollowerFilterApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Follower Scout")
        self.geometry("400x500")

        self.label = ctk.CTkLabel(self, text="Login to Instagram")
        self.label.pack(pady=10)

        self.username_entry = ctk.CTkEntry(self, placeholder_text="Username")
        self.username_entry.pack(pady=5)

        self.password_entry = ctk.CTkEntry(self, placeholder_text="Password", show="*")
        self.password_entry.pack(pady=5)

        self.proxy_entry = ctk.CTkEntry(self, placeholder_text="Proxy (optional)")
        self.proxy_entry.pack(pady=5)

        self.login_button = ctk.CTkButton(self, text="Login", command=self.login)
        self.login_button.pack(pady=10)

        self.filter_button = ctk.CTkButton(self, text="Select File", command=self.select_file)
        self.filter_button.pack(pady=10)
        self.filter_button.configure(state="disabled")

        self.min_followers_entry = ctk.CTkEntry(self, placeholder_text="Min Followers")
        self.min_followers_entry.pack(pady=5)
        self.min_followers_entry.configure(state="disabled")

        self.max_followers_entry = ctk.CTkEntry(self, placeholder_text="Max Followers")
        self.max_followers_entry.pack(pady=5)
        self.max_followers_entry.configure(state="disabled")

        self.apply_filter_button = ctk.CTkButton(self, text="Apply Filter", command=self.apply_filter)
        self.apply_filter_button.pack(pady=10)
        self.apply_filter_button.configure(state="disabled")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        proxy = self.proxy_entry.get()

        if proxy:
            L.context.session.proxies = {'http': proxy, 'https': proxy}

        try:
            L.login(username, password)
            self.filter_button.configure(state="normal")
            messagebox.showinfo("Login Success", "Successfully logged in!")
        except Exception as e:
            messagebox.showerror("Login Error", str(e))

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
                        profile = instaloader.Profile.from_username(L.context, user)
                        followers_count = profile.followers

                        if min_followers <= followers_count <= max_followers:
                            file.write(user + "\n")
                    except Exception as e:
                        print(f"Error processing user {user}: {str(e)}")

            messagebox.showinfo("Success", "Filtered users saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    app = InstaFollowerFilterApp()
    app.mainloop()
