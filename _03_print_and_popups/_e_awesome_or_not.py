from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    w = Tk()
    # Hide the window using the window's .withdraw() method
    w.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
    n = random.randint(0,3)
    # 2. Print your variable to the console
    print(n)
    # 3. Get the user to enter something that they think is awesome
    simpledialog.askstring(title="",prompt="what do you think is awesome?")
    # 4. If your variable is  0
        # -- tell the user whatever they entered is awesome!
    if n == 0:
        messagebox.showinfo(message="that awesome")
        
    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
    elif n == 1:
        messagebox.showinfo(message="meh")
    
    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
    elif n == 2:
        messagebox.showinfo(message="Boring")
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
    elif n == 3:
        messagebox.showinfo(message="that worse than boring")
