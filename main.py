from pytesseract import pytesseract
import pyautogui
import time
from PIL import Image
import csv
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
import pynput
import os
from unidecode import unidecode

path_ = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

pytesseract.tesseract_cmd=path_

four_k=False

if four_k:
    t_w_i, t_h_i, t_w_f, t_h_f = 2626, 108, 3825, 150

    s_w_i, s_h_i, s_w_f, s_h_f = 3748, 195, 3823, 230

else:
    t_w_i, t_h_i, t_w_f, t_h_f = 1313, 54, 1912, 85

    s_w_i, s_h_i, s_w_f, s_h_f = 1876, 115, 1911, 140

def translate(title_):
    with open('names.csv', newline='', encoding='utf8') as f:
        reader = csv.reader(f, delimiter='|')
        for i in reader:
            if unidecode(i[1]) == unidecode(title_):
                return i[0]
    return title_

def removedash(text):
    x=-1
    for i in range(len(text)):
        if text[i]=='-':
            x=i
    text=text[0:x].strip()
    return text

def save_card(show_name=False):
    if four_k:
        c_w_i, c_h_i, c_w_f, c_h_f = 1432, 380, 2407, 1739

    else:
        c_w_i, c_h_i, c_w_f, c_h_f = 716, 190, 1203, 869

    title=pyautogui.screenshot('title.jpg', region=(t_w_i, t_h_i, t_w_f-t_w_i, t_h_f-t_h_i))

    set_=pyautogui.screenshot('set.jpg', region=(s_w_i, s_h_i, s_w_f-s_w_i, s_h_f-s_h_i))

    title=pytesseract.image_to_string(title, config='--psm 7', lang="por")

    set_=pytesseract.image_to_string(set_, config='-c load_system_dawg=0 -c load_freq_dawg=0 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 --psm 8').strip()

    double_card=False
    if '//' in title:
        if four_k:
            c_w_i, c_h_i, c_w_f, c_h_f = 1239, 571, 2600, 1547
        else:
            c_w_i, c_h_i, c_w_f, c_h_f = 620, 286, 1299, 773
        double_card=True

    title=removedash(title)

    if show_name:
        print(title, f'({set_})', end=' - ')

    if double_card:
        title=title.split('//')
        for i in range(len(title)):
            title[i]=translate(title[i].strip())
        title = ' - '.join(title)
    else:
        title = translate(title)

    if show_name:
        print(title, f'({set_})')

    card=pyautogui.screenshot(region=(c_w_i, c_h_i, c_w_f-c_w_i, c_h_f-c_h_i))
    if double_card:
        card=card.rotate(90, expand=True)

    try:
        os.mkdir('cards')
    except FileExistsError:
        ...
    
    if four_k:
        card=card.resize((975, 1360))
    else:
        card=card.resize((487, 679))

    # card.save(f'cards\\{title} ({set_}).jpg', format='JPEG', quality=100)
    card.save(f'cards\\{title} ({set_}).png', format='PNG', quality=100)

def on_click(x, y, button, pressed):
    if pressed and str(button)=='Button.middle':
        save_card()


if four_k:
    card_location=(3190,1570)
else:
    card_location=(1576,790)

toggle=False
def on_press(key):
    if not toggle and str(key)=='Key.ctrl_l':
        globals()['toggle']=True
        while True:

            pyautogui.click(card_location)
            pyautogui.scroll(clicks=1000)
            save_card()
            pyautogui.scroll(clicks=-1000)
            pyautogui.click(card_location)
            pyautogui.scroll(clicks=1000)
            save_card(show_name=True)
            pyautogui.scroll(clicks=-1000)
            pyautogui.press('down')

            title=pytesseract.image_to_string('title.jpg', config='--psm 7', lang="por")
            new_title=pyautogui.screenshot(region=(t_w_i, t_h_i, t_w_f-t_w_i, t_h_f-t_h_i))
            new_title=pytesseract.image_to_string(new_title, config='--psm 7', lang="por")

            title = removedash(title)
            new_title = removedash(new_title)
            # Checks if there are any new images
            if title==new_title:
                break

def on_release(key):
    if toggle:
        globals()['toggle']=False

keyboard_listener = KeyboardListener(on_press=on_press, on_release=on_release)
mouse_listener = MouseListener(on_click=on_click)

keyboard_listener.start()
mouse_listener.start()
keyboard_listener.join()
mouse_listener.join()
