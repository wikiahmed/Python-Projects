# Import necessary libraries
import os
import pygame
from tkinter import *
import random

# Initialize Pygame mixer
pygame.mixer.init()

# Define constants
WIDTH = 1200
HEIGHT = 600

# Create a Tkinter GUI
root = Tk()
root.title("Simple Piano")
root.geometry(f"{WIDTH}x{HEIGHT}") # Use f-string for formatting
root.config(bg="#f0f4f8") # Light gray-blue background

# Define color palettes
Background = ["#0ff", "#0fa", "#00f", "#0af", "#d08", "#da0", "#fff", "#000"]
Main_Background = ["#e74c3c", "#2ecc71", "#9b59b6", "#1abc9c", "#16a085", "#27ae60", "#2980b9", "#2c3e50"]
Special_Background = ["#700", "#090", "#8a0", "#0a9", "#a80", "#a08"]

# Function to change background color
def change_background():
    background_random = random.choice(Background)
    root.config(bg=background_random)
    header_canvas.itemconfig(header_canvas.find_all()[0], fill=background_random)

# Function to change main buttons color
def change_main_buttons_color():
    main_background = random.choice(Main_Background)
    for button in Main_buttons:
        button.config(bg=main_background, fg="white")

# Function to change special buttons color
def change_special_buttons_color():
    special_background = random.choice(Special_Background)
    for button in Special_buttons:
        button.config(bg=special_background, fg="white")

# Function to play music for a short duration using channels
def play_music(sound):
    channel = pygame.mixer.find_channel() # Find an unused channel
    if channel:
        channel.play(sound) # Play the sound on the found channel
        root.after(1000, lambda: stop_music(channel)) # Stop the sound after 1 second

# Function to stop music
def stop_music(channel):
    channel.stop() # Stop the individual sound

# Define buttons and their positions
list_of_buttons = ["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5", "D5", "E5", "F5"]
sites = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950, 1050]
special_buttons = ["C#", "D#", "", "F#", "G#", "A#", "", "C5#", "D5#", "", "F5#"]

# Define music folders
music1 = r"C:\Users\Waqas Ahmed\Desktop\images\Music\Music1"
music2 = r"C:\Users\Waqas Ahmed\Desktop\images\Music\Music2"

# Get list of files in music folders
list_of_files1 = sorted(os.listdir(music1))
list_of_files2 = sorted(os.listdir(music2))

# Initialize lists to store buttons
Main_buttons = []
Special_buttons = []

# Add main buttons
for i in range(11):
    file_path = os.path.join(music1, list_of_files1[i])
    sound = pygame.mixer.Sound(file_path) # Load as a Sound object
    button = Button(
        root,
        text=list_of_buttons[i],
        bg="#3b82f6", # Soft blue
        fg="#ffffff", # White text
        font=('Helvetica', 12, 'bold'),
        relief="sunken",
        command=lambda sound=sound: play_music(sound),
        height=2,
        width=10,
        bd=5
    )
    button.place(x=sites[i] , y=350, width=80, height=200)
    Main_buttons.append(button)

# Add special buttons
for i in range(11):
    if i in [2, 6, 9]:
        continue
    file_path = os.path.join(music2, list_of_files2[i])
    sound = pygame.mixer.Sound(file_path) # Load as a Sound object
    S_button = Button(
        root,
        text=special_buttons[i],
        bg="#9333ea", # Vivid violet
        fg="#ffffff", # White text
        font=('Helvetica', 12, 'bold'),
        relief="sunken",
        command=lambda sound=sound: play_music(sound),
        height=2,
        width=10,
        bd=5
    )
    S_button.place(x=sites[i] + 50, y=250, width=80, height=150)
    Special_buttons.append(S_button) 

# Create header canvas

header_canvas = Canvas(root, bg="#a35722", highlightthickness=0) # Orange header
header_canvas.place(y=0, x=350, width=500, height=100)
header_canvas.create_text(
    250, 50,
    text="Simple Piano",
    font=("Aerial", 40, "bold"),
    fill="#ffffff", # White text
    angle=0
)

Change_button = Button(
    root,
    text="Change BG",
    bg="#38a081", # Emerald green
    fg="#ffffff", # White text
    font=('Helvetica', 12, 'bold'),
    relief="sunken",
    command=change_background,
    height=2, width=10, bd=5
)
Change_button.place(x=14, y=18, width=250, height=80)

Change_color1 = Button(
    root,
    text="B1",
    bg="#50a051", # Emerald green
    fg="#ffffff", # White text
    font=('Helvetica', 12, 'bold'),
    relief="sunken",
    command=change_main_buttons_color,
    height=2, width=10, bd=5
)
Change_color1.place(x=880, y=14, width=150, height=80)

Change_color2 = Button(
    root,
    text="B2",
    bg="#50a051", # Emerald green
    fg="#ffffff", # White text
    font=('Helvetica', 12, 'bold'),
    relief="sunken",
    command=change_special_buttons_color,
    height=2, width=10, bd=5
)
Change_color2.place(x=1040, y=14, width=150, height=80)

# Start the Tkinter main loop
root.mainloop()
