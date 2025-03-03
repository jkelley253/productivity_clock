# Step 1: imports 

# GUI library for creating clock window 
import tkinter as tk
# Handle time 
import datetime
# Ensures GUI remains responsive while updating the clock 
import threading
# text-to-speach 
import pyttsx3



# Step 2: Create GUI 

# Create main window 
window = tk.Tk()
window.title("Productivity Clock")

# Create lable to display the time 
time_label = tk.Label(window, text="00:00:00", font=("Arial", 40))
time_label.pack(pady=20) # space around the label 

# Create the Start button
start_button = tk.Button(window, text="Start", font=("Arial", 14))
start_button.pack(pady=5)

# Create Stop button
stop_button = tk.Button(window, text="Stop", font=("Arial", 14))
stop_button.pack(pady=5)


# Step 5: Text-to-Speech 

# Set up text-to-speech
tts_engine = pyttsx3.init()

# Set speech rate 
tts_engine.setProperty("rate", 150)

# Set voice 
voices = tts_engine.getProperty('voices')
tts_engine.setProperty('voice', voices[164].id)

# Variable to control if clock is running 
running = False 
# Variable to track the last announce hour 
last_announce_hour = None


def announce_time():
    """
    announce the current hour 
    """
    
    # Get the current hour 
    current_hour = datetime.datetime.now().strftime("%I %p")
    
    # Create message 
    message = f"It is {current_hour}"
    
    # Use text-to-speach to announce the time 
    tts_engine.say(message)
    tts_engine.runAndWait()



# Step 3: Create function to udpate time 

def update_time():
    """
    Fetch and update time every second while True
    """
    
    global last_announce_hour
    
    if running:
        # Get the current time 
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        current_hour = datetime.datetime.now().hour
        
        # Update the label to show the new time 
        time_label.config(text=current_time)
        
        # Check if the hour has changed and announce it
        if current_hour != last_announce_hour:
            announce_time()
            last_announce_hour = current_hour
        
        # Make sure the function runs after every second 
        window.after(1000, update_time)
        
def start_clock():
    """
    Start updating the clock when start is clicked
    """
    global running
    # Prevent multiple starts
    if not running:
        running = True
        # Start the time update loop
        update_time()

def stop_clock():
    """
    Stop updating the clock when Stop is clicked
    """
    global running
    # Stop update time from running again
    running = False

# Link the buttons to their functions 
start_button.config(command=start_clock)
stop_button.config(command=stop_clock)



# Step 4: Tkinter loop 
window.mainloop()
