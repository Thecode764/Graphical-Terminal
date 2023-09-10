import tkinter as tk
import subprocess
import os

def run_command():
    command = entry.get()
    try:
        output = subprocess.check_output(command, shell=True, universal_newlines=True)
        output_text = f"Command: {command}\nOutput: {output}"
    except subprocess.CalledProcessError as e:
        output_text = f"Command: {command}\nError: {e.output}"
    
    output_text = output_text.strip()
    output_textbox.delete("1.0", tk.END)  # پاک کردن محتوای صفحه
    output_textbox.insert(tk.END, output_text + "\n")

root = tk.Tk()
root.title("Python Command Prompt")
root.configure(bg="black")

label = tk.Label(root, text="python@python~>", fg="green", bg="black")
label.pack()

entry = tk.Entry(root, fg="white", bg="black")
entry.pack()

button = tk.Button(root, text="Run", fg="black", bg="white", command=run_command)
button.pack()



output_textbox = tk.Text(root, fg="white", bg="black")
output_textbox.pack()

root.mainloop()
