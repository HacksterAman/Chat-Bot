import pyautogui
import time

text_input_coords = (756, 955)  
send_button_coords = (1853, 955)  

input_string = """Hello!
How are you?
This is a test message.
Goodbye!"""

lines = input_string.split('\n')
messages = [line.strip() for line in lines if line.strip()]

time.sleep(3)

for message in messages:
    # Type the message
    pyautogui.click(text_input_coords)
    pyautogui.write(message)

    # Click the Send button
    pyautogui.click(send_button_coords)