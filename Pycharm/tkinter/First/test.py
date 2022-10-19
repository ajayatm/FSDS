import tkinter as tk
import os

# Top level window
frame = tk.Tk()
frame.title("PDF Merger")
frame.geometry('1000x1000')

# Function for getting Input from textbox and printing it at label widget

def printinput():
    try:
        inp = inputtxt.get(1.0, "end-1c")
        filelist = os.listdir(inp)
        a = ''
        b = 0
        for i in filelist:
            a = a + i + '\n'
            if i[-4::] == '.pdf':
                b += 1

        print(a)
        lbl.config(text="Directory: " + inp + '\n\n'
                        + 'LIst of files in the directory are below' + '\n'
                        + a + '\n\n'
                        + 'Number of python files: ' + str(b) + '\n'
                   )
    except Exception as e:
        print(e)


# TextBox Creation
inputtxt = tk.Text(frame, height=1, width=100)
inputtxt.pack()

# Button Creation
printButton = tk.Button(frame,text="Print", command=printinput)
printButton.pack()

# Label Creation
lbl = tk.Label(frame, text="Please input your directory path in the above text box")
lbl.pack()

frame.mainloop()
