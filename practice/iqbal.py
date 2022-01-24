import tkinter as tk
from tkinter import filedialog,Text
import os #allows us to run the apps

#this root like the body everything will be attached to it
root = tk.Tk()
apps =[]
def addApps():
    for widget in frame.winfo_children():
        widget.destroy()

    filename =filedialog.askopenfilename(initialdir="/", title=" Select File",
                                       filetypes=((" executables","*.exe"),("all files","*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app,bg ="gray")
        label.pack()
def runApps():
    for app in apps:
        os.startfile(app)




#used to add the structured graphics to the python application
canvas = tk.Canvas(root,height=600,width=600,bg="#5B2C6F")
#The pack() fill option is used to make a widget fill the entire frame
canvas.pack()
frame =tk.Frame(root,bg="white")
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
openFile = tk.Button(root,text="Open File", padx=10,pady=5, fg="white",bg="#5B2C6F" ,command =addApps)
openFile.pack()
runApps = tk.Button(root,text="Run Apps", padx=10,pady=5, fg="white",bg="#5B2C6F", command=runApps())
runApps.pack()
#This method listens for events,
#such as button clicks or keypresses, and blocks any code that comes after it
root.mainloop()