from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    w = Tk()
    # Hide the window using the window's .withdraw() method
    w.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question
    one = simpledialog.askstring(title= '',prompt= 'what is 57-8')
    #      // 3.  Use an if statement to check if their answer is correct
    if one == '49':
        score = score + 1
        correct = messagebox.showinfo(title="", message='correct')
    else:
        incorrect = messagebox.showinfo(title="",message='incorrect')
        score = score - 1
    #      // 4.  if the user's answer was correct, add one to their score

    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    two = simpledialog.askstring(title="", prompt="what is the capital of the USA")
    if two == "washington DC":
        score = score + 1
        messagebox.showinfo(title="", message='correct')
    else:
        score = score - 1
        messagebox.showinfo(title="", message='incorrect')
    three = simpledialog.askstring(title="", prompt="who is the author of the harry potter series?")
    if three == "JK rowling":
        score = score + 1
        messagebox.showinfo(title="", message='correct')
    else:
        score = score - 1
        messagebox.showinfo(title="", message='incorrect')

    # After all the questions have been asked, tell the user their final score
    messagebox.showinfo(message= "Score = "+ str(score))
    # remember to convert your variable to a string using the str() function 
    
