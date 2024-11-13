import os
import tkinter as tk
from tkinter import ttk, simpledialog

def create_group():
    group_name = group_entry.get()
    password = simpledialog.askstring("Sudo Password", "Please enter your password:", show="*")
    if password is not None:
        os.system(f"echo '{password}' | sudo -S groupadd {group_name}")
        group_list.insert(tk.END, group_name)
        group_entry.delete(0, tk.END)

def add_user_to_group():
    group = group_list.get(group_list.curselection())
    user = user_entry.get()
    password = simpledialog.askstring("Sudo Password", "Please enter your password:", show="*")
    if password is not None:
        os.system(f"echo '{password}' | sudo -S usermod -a -G {group} {user}")
        user_entry.delete(0, tk.END)

def set_permissions():
    group = group_list.get(group_list.curselection())
    partition = partition_entry.get()
    password = simpledialog.askstring("Sudo Password", "Please enter your password:", show="*")
    if password is not None:
        os.system(f"echo '{password}' | sudo -S chown -R :{group} {partition}")
        os.system(f"echo '{password}' | sudo -S chmod -R g+rw {partition}")
        partition_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Partition Permission Manager")

# Group management
group_frame = ttk.LabelFrame(root, text="Manage Groups")
group_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

group_label = ttk.Label(group_frame, text="Group Name:")
group_label.grid(row=0, column=0, padx=5, pady=5)

group_entry = ttk.Entry(group_frame)
group_entry.grid(row=0, column=1, padx=5, pady=5)

group_button = ttk.Button(group_frame, text="Create Group", command=create_group)
group_button.grid(row=0, column=2, padx=5, pady=5)

group_list = tk.Listbox(group_frame, width=20)
group_list.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# User management
user_frame = ttk.LabelFrame(root, text="Manage Users")
user_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

user_label = ttk.Label(user_frame, text="Username:")
user_label.grid(row=0, column=0, padx=5, pady=5)

user_entry = ttk.Entry(user_frame)
user_entry.grid(row=0, column=1, padx=5, pady=5)

user_button = ttk.Button(user_frame, text="Add to Group", command=add_user_to_group)
user_button.grid(row=0, column=2, padx=5, pady=5)

# Partition management
partition_frame = ttk.LabelFrame(root, text="Manage Partition")
partition_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

partition_label = ttk.Label(partition_frame, text="Partition Path:")
partition_label.grid(row=0, column=0, padx=5, pady=5)

partition_entry = ttk.Entry(partition_frame)
partition_entry.grid(row=0, column=1, padx=5, pady=5)

partition_button = ttk.Button(partition_frame, text="Set Permissions", command=set_permissions)
partition_button.grid(row=0, column=2, padx=5, pady=5)

root.mainloop()
