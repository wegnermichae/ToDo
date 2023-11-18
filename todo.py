import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        list_tasks_box.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove_task():
    selected = list_tasks_box.curselection()
    if selected:
        list_tasks_box.delete(selected)

root = tk.Tk()
root.title("Todo List GUI")
root.geometry("250x350")

entry = tk.Entry(root)
entry.pack(pady=10)

add_task_button = tk.Button(root, text="Add Task", command=add_task)
add_task_button.pack(pady=5)

remove_task_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_task_button.pack(pady=5)

list_tasks_box = tk.Listbox(root)
list_tasks_box.pack(pady=10)

root.mainloop()
