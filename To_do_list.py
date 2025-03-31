import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("To-Do List")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []


def add_task():
    task = task_entry.get()
    task_entry.delete(0, tk.END)
    if task:
        with open('tasklist.txt', 'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(tk.END, task)
        
def delete_task():
    global task_list
    task = str(listbox.get(tk.ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open('/Users/dhanyamanam/Desktop/To do list Project/tasklist.txt', 'w') as taskfile:
            for task in task_list:
                taskfile.write(task + '\n')
        listbox.delete(tk.ANCHOR)

def edit_task():
    global task_list
    try:
        selected_task_index = listbox.curselection()[0]  
        selected_task = listbox.get(selected_task_index)  

        task_entry.delete(0, tk.END)  
        task_entry.insert(0, selected_task)  
        task_list.remove(selected_task)
        listbox.delete(selected_task_index)

        with open('/Users/dhanyamanam/Desktop/To do list Project/tasklist.txt', 'w') as taskfile:
            for task in task_list:
                taskfile.write(task + '\n')

    except IndexError:
        print("⚠️ Please select a task to edit!")
         

def opentaskFile():
    try:
        global task_list
        with open("/Users/dhanyamanam/Desktop/To do list Project/tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()
        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(tk.END, task)
    except:
        file = open("/Users/dhanyamanam/Desktop/To do list Project/tasklist.txt", "w")
        file.close()








image_icon = tk.PhotoImage(file="/Users/dhanyamanam/Desktop/To do list Project/Image/task.png")
root.iconphoto(False, image_icon)


top_image = tk.PhotoImage(file="/Users/dhanyamanam/Desktop/To do list Project/Image/topbar.png")
tk.Label(root, image=top_image).pack()

dock_image = tk.PhotoImage(file="/Users/dhanyamanam/Desktop/To do list Project/Image/dock.png")
tk.Label(root, image=dock_image, bg="#32405b").place(x=30, y=25)

note_image = tk.PhotoImage(file='/Users/dhanyamanam/Desktop/To do list Project/Image/task.png')
tk.Label(root, image=note_image, bg="#32405b").place(x=340, y=25)


heading = tk.Label(root, text="ALL TASK", font=("Arial", 20, "bold"), fg="white", bg="#32405b")
heading.place(x=130, y=20)

frame = tk.Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=180)

task = tk.StringVar()
task_entry = tk.Entry(frame, width=17, font=("Arial", 20), bd=0)
task_entry.place(x=10, y=5)
task_entry.focus()




style = ttk.Style()
style.theme_use("clam")  

style.configure("Custom.TButton",
                font=("Arial", 17, "bold"),
                background="white",  
                foreground="white",
                borderwidth=0)

style.map("Custom.TButton",
          background=[("active", "#0056b3"), ("!disabled", "#007BFF")],
          foreground=[("pressed", "white"), ("active", "white")])


button = ttk.Button(frame, text="ADD",width=6, style="Custom.TButton",command=add_task)
button.place(x=300, y=5)

frame1 = tk.Frame(root, bd=3, width=700, height=280, bg="#223241")
frame1.pack(pady=(160, 0))

listbox = tk.Listbox(frame1,font = ('arial',12),width=40,height=16,bg='#32405b',fg='white',cursor='hand2',selectbackground='#5a95ff')
listbox.pack(side=tk.LEFT,fill=tk.BOTH,padx=2)

scrollbar = tk.Scrollbar(frame1)
scrollbar.pack(side=tk.RIGHT,fill=tk.BOTH)

opentaskFile()

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

Delete_icon = tk.PhotoImage(file="/Users/dhanyamanam/Desktop/To do list Project/Image/delete.png")
delete_button = tk.Button(root, image=Delete_icon, command=delete_task,bd=0)
delete_button.pack(side=tk.BOTTOM, padx=10, pady=13)  # Place at the bottom

Update_icon = tk.PhotoImage(file="/Users/dhanyamanam/Desktop/To do list Project/Image/Edit.png")
update_button = tk.Button(root, image=Update_icon,command=edit_task, bd=0)
update_button.place(x=270,y=580.5)
root.update_icon = Update_icon  




root.mainloop()
