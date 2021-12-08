import tkinter
from tkinter import *
from tkinter import ttk

# main
window = tkinter.Tk()
window.title("Python Voice Chat")


# creates a new window
def openNewWindow():
    newWindow = Toplevel(window)
    # title
    newWindow.title("Python Voice Chat-Server")
    #color
    newWindow.configure(background="white")
    # photo
    banner = PhotoImage(file="pinkFlow.gif")
    header = tkinter.Label(newWindow, image=banner, bg="white")
    header.image = banner
    header.grid(row=0, column=0, sticky=W)
    Label(newWindow, text="You've entered the server!", bg="white", fg="black", font="Raleway 22 bold")\
        .grid(row=1, column=0, sticky=S)




# click function will collect text from the text box
def click():
    entered_text = textentry.get()
    openNewWindow()


# window background color
window.configure(background="white")

# insert photo
photo = PhotoImage(file="flowerSize.gif")
Label(window, image=photo, bg="white").grid(row=0, column=0, sticky=N)

# creating label/text, bg= box color around text, fg= text color
Label(window, text="Voice Chat Info", bg="white", fg="black", font="Raleway 22 bold").grid(row=0, column=0,
                                                                                           sticky=N, pady=50)
# text box for name and server ip
name = tkinter.Label(window, text="Username:", bg="white", fg="black", font="Raleway 14")
name.grid(row=0, column=0, sticky=N)
name.place(x=220, y=100)

textentry = Entry(window, bg="#ebebeb", borderwidth=0, highlightthickness=0)
textentry.grid(row=0, column=0)
textentry.place(height=30, x=220, y=125)

ipadd = tkinter.Label(window, text="IP address:", bg="white", fg="black", font="Raleway 14")
ipadd.grid(row=0, column=0, sticky=N, pady=50)
ipadd.place(x=220, y=175)

ipentry = Entry(window, bg="#ebebeb", borderwidth=0, highlightthickness=0)
ipentry.grid(row=0, column=0)
ipentry.place(height=30, x=220, y=200)

# submit button
submit = tkinter.Button(window, text="Submit", width=6, command=click, highlightthickness=0,
                        highlightbackground="white")
submit.grid(row=0, column=0, sticky=S)
submit.place(x=250, y=250)

# run main
window.mainloop()
