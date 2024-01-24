import tkinter as tk
import ttkbootstrap as ttk
import pyautogui
import time
import threading
import random
from pynput.keyboard import Controller
import string

continue_flag = False
keyboard = Controller()

def mouse_move():
    global continue_flag
    while continue_flag:
        mouse_checked = mouse_check_var.get()
        keyboard_checked = keyboard_check_var.get()
        print(str(mouse_checked) + " " + str(keyboard_checked))
        if(mouse_checked):
            x, y = pyautogui.position()
            distance = int(distance_slider.get())  # Convert the slider value to an integer
            distance_x = random.randint(-distance, distance)  # Random distance for x between -distance and distance
            distance_y = random.randint(-distance, distance)  # Random distance for y between -distance and distance
            steps = random.randint(-100, 100)  
            for i in range(steps):
                move_distance_x = distance_x / steps
                move_distance_y = distance_y / steps
                duration = random.uniform(0.1, 0.5)  # Random duration between 0.1 and 0.5
                pyautogui.move(move_distance_x, move_distance_y, duration=duration)
                time.sleep(0.1)
            
        if(keyboard_checked):
                # Randomly type a letter
            if random.randint(0, 1):  # 50% chance to type a letter
                letter = random.choice(string.ascii_letters)  # Choose a random letter
                keyboard.type(letter)  # Type the letter
        time.sleep(90)

def start_stop():
    global continue_flag
    continue_flag = not continue_flag
    if continue_flag:
        t = threading.Thread(target=mouse_move)
        t.daemon = True  # Set the thread as a daemon thread
        t.start()
        status_label.config(text="Status: Running", foreground='green')
        start_button.pack_forget()
        stop_button.pack(pady=10, ipadx=20, ipady=10)
    else:
        status_label.config(text="Status: Stopped", foreground='red')
        stop_button.pack_forget()
        start_button.pack(pady=10, ipadx=20, ipady=10)

#main window
mywindow = ttk.Window(themename='darkly')
mywindow.minsize(300, 100)
mywindow.title('MouseMove')

#vars
myint = ttk.IntVar()
mouse_check_var = ttk.BooleanVar()
keyboard_check_var = ttk.BooleanVar()

# Heading
heading = ttk.Label(mywindow, text="Make my mouse move!", font=("Arial", 13))
heading.pack()

# Status Label
status_label = ttk.Label(mywindow, text="Status: Stopped", font=("Arial", 10), foreground='red')
status_label.pack()

#Warn lable
warn_label = ttk.Label(mywindow, text="Warning: \nThis program will move your mouse and type random letters.\nPlease make sure to select the desktop while using!", font=("Arial", 10), foreground='red')
warn_label.pack()

# Checkboxes
checkbox_frame = ttk.Frame(mywindow, padding="10 10 10 10")  # Add padding to the frame

# Add a title
title = ttk.Label(checkbox_frame, text="Options", font=("Arial", 12))
title.pack()

mouse_check = ttk.Checkbutton(checkbox_frame, text="AutoMouse", variable=mouse_check_var)
keyboard_check = ttk.Checkbutton(checkbox_frame, text="AutoKeyboard", variable=keyboard_check_var)

mouse_state = bool(mouse_check_var.get())
keyboard_state = bool(keyboard_check_var.get())

mouse_check.pack(side=ttk.LEFT, padx=5, pady=5)  # Add padding to the checkboxes
keyboard_check.pack(side=ttk.LEFT, padx=5, pady=5)  # Add padding to the checkboxes
checkbox_frame.pack()

def update_label(*args):
    distance_label.config(text=f"Mouse Distance: {int(distance_slider.get())}")

# Distance Slider
slider_value = tk.IntVar()
distance_slider = ttk.Scale(mywindow, from_=0, to=500, orient='horizontal', length=200, variable=slider_value)
distance_slider.set(100)  # Set the initial value
slider_value.trace("w", update_label)

distance_label = ttk.Label(mywindow, text=f"Mouse Distance: {distance_slider.get()}", font=("Arial", 10))
distance_label.pack()
distance_slider.pack(pady=10)

# Button
# Start Button
start_button = ttk.Button(mywindow, text="Start", command=start_stop, style='success.TButton')

# Stop Button
stop_button = ttk.Button(mywindow, text="Stop", command=start_stop, style='danger.TButton')

# Initially, only the start button is visible
start_button.pack(pady=10, ipadx=20, ipady=10)


#Window Loop
mywindow.mainloop()