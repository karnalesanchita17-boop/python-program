import tkinter as tk
from tkinter import ttk, messagebox
root = tk.Tk()
root.title("Student Registration Form")
root.geometry("500x550")
root.configure(bg="#EAF2F8")
title = tk.Label(
    root,
    text="Student Registration Form",
    font=("Arial", 18, "bold"),
    bg="#EAF2F8",
    fg="#154360"
)
title.pack(pady=15)
form = tk.Frame(root, bg="white", padx=20, pady=15)
form.pack(padx=20, pady=10, fill="both", expand=True)
tk.Label(form, text="Full Name:", bg="white").grid(
    row=0, column=0, sticky="w", pady=8
)
name_entry = tk.Entry(form, width=28)
name_entry.grid(row=0, column=1, pady=8)
tk.Label(form, text="Email:", bg="white").grid(
    row=1, column=0, sticky="w", pady=8
)
email_entry = tk.Entry(form, width=28)
email_entry.grid(row=1, column=1, pady=8)
tk.Label(form, text="Course:", bg="white").grid(
    row=2, column=0, sticky="w", pady=8
)
course_box = ttk.Combobox(
    form,
    values=["Computer Science", "Information Technology",
            "Electronics", "Mechanical"],
    state="readonly",
    width=25
)
course_box.grid(row=2, column=1, pady=8)
course_box.set("Computer Science")
tk.Label(form, text="Gender:", bg="white").grid(
    row=3, column=0, sticky="w", pady=8
)
gender = tk.StringVar(value="Female")
tk.Radiobutton(
    form, text="Male", variable=gender,
    value="Male", bg="white"
).grid(row=3, column=1, sticky="w")
tk.Radiobutton(
    form, text="Female", variable=gender,
    value="Female", bg="white"
).grid(row=4, column=1, sticky="w")
tk.Label(form, text="Skills:", bg="white").grid(
    row=5, column=0, sticky="w", pady=8
)
python_skill = tk.BooleanVar()
java_skill = tk.BooleanVar()
tk.Checkbutton(
    form, text="Python", variable=python_skill,
    bg="white"
).grid(row=5, column=1, sticky="w")
tk.Checkbutton(
    form, text="Java", variable=java_skill,
    bg="white"
).grid(row=6, column=1, sticky="w")
def submit_form():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    course = course_box.get()
    if not name or not email:
        messagebox.showerror(
            "Error", "Please enter your name and email."
        )
        return
    skills = []
    if python_skill.get():
        skills.append("Python")
    if java_skill.get():
        skills.append("Java")
    if not skills:
        skills = ["None selected"]
    result = (
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Course: {course}\n"
        f"Gender: {gender.get()}\n"
        f"Skills: {', '.join(skills)}"
    )
    messagebox.showinfo("Registration Successful", result)
button_frame = tk.Frame(form, bg="white")
button_frame.grid(row=7, column=0, columnspan=2, pady=20)
tk.Button(
    button_frame,
    text="Submit",
    command=submit_form,
    bg="#2874A6",
    fg="white",
    width=12
).pack(side="left", padx=5)
def clear_form():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    course_box.set("Computer Science")
    gender.set("Female")
    python_skill.set(False)
    java_skill.set(False)
tk.Button(
    button_frame,
    text="Clear",
    command=clear_form,
    width=12
).pack(side="left", padx=5)
root.mainloop()
