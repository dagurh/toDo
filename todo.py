import tkinter as tk
from tkinter import *
import os

root = tk.Tk()

texts = []

if os.path.isfile('saveTasks.txt'):
  with open('saveTasks.txt', 'r') as f:
    tempTexts = f.read()
    tempTexts = tempTexts.split(',')
    texts = [x for x in tempTexts if x.strip()]

def addTask():
  canvas.pack_forget()
  addTaskButton.pack_forget()
  clearFirstTask.pack_forget()
  frame.place_forget()
  frameCheckBox.place_forget()
  canvasText.pack()
  confirmButton.pack(fill = X)

def clearAll():
  del texts[:]
  with open('saveTasks.txt', 'r') as fin:
    data = fin.read().splitlines(True)
  with open('saveTasks.txt', 'w') as fout:
    fout.writelines(data[1:])
  for widget in frame.children.values():
    widget.destroy()
    for widget1 in frameCheckBox.children.values():
      widget1.destroy()

    
def confirmTask():

  for widget in frame.winfo_children():
    widget.destroy()

  texts.append(canvasText.get(1.0, END))

  canvasText.delete(1.0, END)

  for text in texts:
    label = tk.Label(frame, text=text, borderwidth=2, relief="sunken", bg="white", font=("Helvetica", 12), anchor=W)
    label.pack(fill=X)
    
  check = Checkbutton(frameCheckBox)
  check.deselect()
  check.pack(anchor=E, padx=23, pady=9)

  canvasText.pack_forget()
  confirmButton.pack_forget()

  frameCheckBox.place(relwidth=0.1, relheight=0.8, relx=0.8, rely=0.1)
  canvas.pack()
  addTaskButton.pack(fill = X)
  clearFirstTask.pack(fill = X)
  frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

canvasText = Text(root, height=4, width=60, bg="white", font=("Helvetica", 20))

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.7, relheight=0.8, relx=0.1, rely=0.1)

frameCheckBox = tk.Frame(root, bg="white")
frameCheckBox.place(relwidth=0.1, relheight=0.8, relx=0.8, rely=0.1)

addTaskButton = tk.Button(root, text="Add task", padx=10, pady=5, fg="white", bg="#263D42", command=addTask)
addTaskButton.pack(fill = X)

clearFirstTask = tk.Button(root, text="Clear first task", padx=10, pady=5, fg="white", bg="#263D42", command=clearAll)
clearFirstTask.pack(fill = X)

confirmButton = tk.Button(text="Confirm", padx=10, pady=5, fg="white", bg="#263D42", command=confirmTask)


for text in texts:
  label = tk.Label(frame, text=text, borderwidth=2, relief="sunken", bg="white", font=("Helvetica", 12), anchor=W)
  label.pack(fill=X)
  check = Checkbutton(frameCheckBox, padx=23, pady=9)
  check.deselect()
  check.pack(anchor=E)

root.mainloop()

with open('saveTasks.txt', 'w') as f:
    for text in texts:
      f.write(text + ',')