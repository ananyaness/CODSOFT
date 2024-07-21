#1.import module
from tkinter import *
from tkinter import messagebox

#5. create function
def newTask():
    task = my_entry.get() #this will take the info provided by user
    if task !="":
        lb.insert(END, task)
        my_entry.delete(0,"end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")  

def deleteTask():
    lb.delete(ANCHOR) #anchor is referred to the selected item(by default)       

#2. configure and create main window
#ws is a variable and it stands for workspace
ws = Tk() #initializing the module of tkinter 
ws.geometry('500x450+500+200')#height(400) and width(500) of application, position(500+200)
ws.title('To Do List')
ws.config(bg='#223441')
ws.resizable(width=False, height=False)#cannot resize the window

#4. create widgets(frame, listbox, scrollbar, Entry, button)
frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times',18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
)
lb.pack(side=LEFT, fill=BOTH)

task_list= [
    'Wake up early',
    'drink water',
    'Eat apple',
    'Go gym'
]

#to insert new tak
for item in task_list:
    lb.insert(END, item)

#scrollbar
sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)
  
lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('times', 24)
)
my_entry.pack(pady=20)

#buttons
button_frame = Frame(ws) #button_frame is used to place buttons parallel to each other
button_frame.pack(pady=20)

#button to add task
addTask_btn = Button(
    button_frame, #placed  button inside the frame
    text='Add Task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask #the thing that will happen when the bbutton will be clicked
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

#button to delete task
delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font =('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=TRUE, side=LEFT)

#3. create main loop
ws.mainloop()#infinite loop running



