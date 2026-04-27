import tkinter as tk
from tkinter import messagebox

def calculate_result():
    try:
        name = entry_name.get()
        m1 = int(entry_m1.get())
        m2 = int(entry_m2.get())
        m3 = int(entry_m3.get())

        total = m1 + m2 + m3
        percentage = total / 3

        if percentage >= 80:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 40:
            grade = "C"
        else:
            grade = "Fail"

        result = f"Name: {name}\nTotal: {total}\nPercentage: {percentage:.2f}%\nGrade: {grade}"
        label_result.config(text=result)

    except:
        messagebox.showerror("Error", "Please enter valid numbers")

root = tk.Tk()
root.title("Student Result Calculator")
root.geometry("350x400")

tk.Label(root, text="Student Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Marks 1").pack()
entry_m1 = tk.Entry(root)
entry_m1.pack()

tk.Label(root, text="Marks 2").pack()
entry_m2 = tk.Entry(root)
entry_m2.pack()

tk.Label(root, text="Marks 3").pack()
entry_m3 = tk.Entry(root)
entry_m3.pack()

tk.Button(root, text="Calculate Result", command=calculate_result).pack(pady=10)

label_result = tk.Label(root, text="", fg="blue")
label_result.pack()

root.mainloop()
