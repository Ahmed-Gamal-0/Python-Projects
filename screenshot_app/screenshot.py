#-----------------------------------------------------------------------
# to install virtual environment write in terminal 'pip install virtualenv'  
#  it used to make your project in isolated environment
#  if you downloaded any packges in virtual environment 
#  it will not be exist in you original system           
# pip install pyautogui --> it will help us to take screen shots
#-----------------------------------------------------------------------
import time
import pyautogui
import tkinter as tk # used to make GUI

def screenshot():
    
    #to generate a random name for the img
    name = int(round(time.time() * 1000))
    
    #to add the file path to save imgs in, and to add extention to the name of img
    name = f"D:/courses/Programming/projects/python/screenshot_app/saved_imgs/{name}.png"


    # to take name of img from user
    # name = input("image Name: ")
    # name = f"{name}.png"


   # to make the programm wait for 5 second before taking screenshot
   # time.sleep(.25)  
   
   

    
    img = pyautogui.screenshot(name)
    img.show() 


# GUI
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text = "Take screenshot",
    command = screenshot
)

button.pack(side=tk.LEFT)
close = tk.Button(
    frame,
    text = "Quit",
    command = quit
)
close.pack(side=tk.LEFT)

root.mainloop()
    
    
    
screenshot()

