import tkinter as tk
import time


splash = tk.Tk()
splash.title("Loading...")
splash.geometry("300x200")
splash.config(bg="lightblue")

label = tk.Label(splash, text="Loading Calculator...", font=("Arial", 16), bg="lightblue")
label.pack(expand=True)

splash.update()
time.sleep(2)  # 2-second loading screen
splash.destroy()


root = tk.Tk()
root.title("Calculator")
root.geometry("490x400")
root.config(bg="lightgray")

entry = tk.Entry(root, width=20, font=("Arial", 18), bd=5, relief="ridge", bg="lightyellow")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)



def click(button_text):
    if button_text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)



buttons = [
    ("7", "skyblue"), ("8", "skyblue"), ("9", "skyblue"), ("/", "orange"),
    ("4", "skyblue"), ("5", "skyblue"), ("6", "skyblue"), ("*", "orange"),
    ("1", "skyblue"), ("2", "skyblue"), ("3", "skyblue"), ("-", "orange"),
    ("0", "skyblue"), (".", "skyblue"), ("=", "lightgreen"), ("+", "orange"),
    ("C", "tomato")
]

row_val = 1
col_val = 0

for (text, color) in buttons:
    action = lambda x=text: click(x)
    btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                    bg=color, fg="black", command=action)
    btn.grid(row=row_val, column=col_val, padx=5, pady=5)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()