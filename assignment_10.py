import tkinter as tk
import webbrowser as wb

root = tk.Tk()

# Entry widget
entry = tk.Entry(root, font=("Times New Roman", 30), width=30)
entry.grid(row=0, column=0)

l1 = tk.Label(root, font=("Times New Roman", 20))
l1.grid(row=1, column=0)
def display():
    search = entry.get()
    print(search)
    if search:
        l1.config(text=f"Connecting to w3school-{search}...")
        
        wb.open(f"https://www.w3schools.com/{search}")
    else:
        print("Please enter something")


s_button = tk.Button(root, text="Search", font=("Times New Roman", 20),bg="#ff00ff", activebackground="#90fca7", command=display)
s_button.grid(row=3, column=0)

c_button = tk.Button(root, text="Close", font=("Times New Roman", 20),bg="#FE828C", activebackground="#cc8d7e", command=root.destroy)
c_button.grid(row=4, column=0)

root.mainloop()