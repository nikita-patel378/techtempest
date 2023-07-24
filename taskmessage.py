import pyautogui
import keyboard
import time
import pywhatkit as w
import json

with open('tasks.json') as f:
    tasks = json.load(f)

# Function to generate the message
def generate_message(week_dict):
    date = week_dict['Date']
    video_group = week_dict['Video']
    fun_activity_group = week_dict['Fun Activity']

    message = f"Hi! For this Sunday, {date}, here are the following groups with their respective tasks: {video_group} for Video and {fun_activity_group} for Fun Activity. Thank you so much for your help!"
    return message

# Generate message for the first week
week = tasks['monthly_sessions']['Week'][0]
message = generate_message(week)

def send_group_message(group_name, message):
    w.sendwhatmsg_to_group_instantly(group_name, message)
    
msg=message

#Enter Whatsapp group name and send the message
send_group_message('group_name',msg)
pyautogui.click(1050, 950)
time.sleep(2)
keyboard.press_and_release('enter')

