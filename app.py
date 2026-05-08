import tkinter as tk
from tkinter import messagebox

appointments = []

def schedule_appointment():
    name = name_entry.get()
    date = date_entry.get()
    time = time_entry.get()

    if name == "" or date == "" or time == "":
        messagebox.showwarning("Missing Info", "Please fill out all fields.")
        return
    
    for appt in appointments:
        if appt["date"] == date and appt["time"] == time:
            messagebox.showerror("Unavailable", "Appointment already booked.")
            return
        
    appointments.append({
        "name": name,
        "date": date,
        "time": time
    })

    appointment_list.insert(
        tk.END,
        f"{name} {date} {time}"
    )

    name_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)


def delete_appointment():
    selected = appointment_list.curselection()

    if not selected:
        messagebox.showwarning("No Selection", "Please select an appointment to delete.")
        return

    index = selected[0]
    appointment_list.delete(index)
    appointments.pop(index)

def sort_appointments():
    appointments.sort(key=lambda x: x["date"])

    appointment_list.delete(0, tk.END)

    for appt in appointments:
        appointment_list.insert(
            tk.END,
            f'{appt["name"]} {appt["date"]} {appt["time"]}'
        )

root = tk.Tk()
root.title("Clinical Scheduling System")
root.geometry("500x500")

title = tk.Label(root, text="Clinical Scheduling System", font=("Arial, 19"))
title.pack(pady=10)

tk.Label(root, text="Patient Name").pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack()

tk.Label(root, text="Date").pack()
date_entry = tk.Entry(root, width=40)
date_entry.pack()

tk.Label(root, text="Time").pack()
time_entry = tk.Entry(root, width=40)
time_entry.pack()

schedule_button = tk.Button(
    root,
    text="Schedule Appointment",
    command=schedule_appointment
)
schedule_button.pack(pady=10)

delete_button = tk.Button(
    root,
    text="Delete Selected Appointment",
    command=delete_appointment
)
delete_button.pack(pady=5)

sort_button = tk.Button(
    root,
    text="Sort by Date",
    command=sort_appointments
)
sort_button.pack(pady=5)

tk.Label(root, text="Appointments").pack(pady=10)

appointment_list = tk.Listbox(root, width=60)
appointment_list.pack(pady=20)

root.mainloop()