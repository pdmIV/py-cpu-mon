import customtkinter as ctk
import tkinter
import psutil
from time import sleep


def start_monitoring(progressbar, label):
    while True:
        cpu_usage = psutil.cpu_percent()
        progressbar.set(cpu_usage)
        label.configure(text="CPU Usage: {:.2f}%".format(cpu_usage))
        root_tk.update()  # Update the GUI to reflect the changes
        sleep(0.5)  # Wait for a half-second before updating again

    # create main window with ctk theme
root_tk = tkinter.Tk()
root_tk.geometry("400x200")
root_tk.title("Resource Monitor")
root_tk.configure(bg="black")
ctk.set_default_color_theme("dark-blue")

    # create label
label = ctk.CTkLabel(master=root_tk, text="CPU Usage: ", font=ctk.CTkFont(family='calibri', size=30))
label.pack(pady=10)

    # create progressbar
progressbar = ctk.CTkProgressBar(master=root_tk, fg_color=("black"), width=200, height=10, corner_radius=20)
progressbar.set(0)
progressbar.pack(pady=10)

    # create button
button = ctk.CTkButton(master=root_tk, text="Start", command=lambda: start_monitoring(progressbar, label))
button.pack(pady=10)

# create ability to quit program with close button
root_tk.protocol("WM_DELETE_WINDOW", root_tk.destroy)



if __name__ == "__main__":
    root_tk.mainloop()





