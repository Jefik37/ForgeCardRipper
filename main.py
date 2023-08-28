from pytesseract import pytesseract
import pyautogui
import time
from PIL import Image
import csv
from pynput import mouse
import os

path_ = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

pytesseract.tesseract_cmd=path_

four_k=False

def translate(title_):
    with open('names.csv', newline='', encoding='utf8') as f:
        reader = csv.reader(f, delimiter='|')
        for i in reader:
            if i[1] == title_:
                return i[0]
    return title_

def save_card():
    if four_k:
        t_w_i, t_h_i, t_w_f, t_h_f = 2626, 108, 3825, 172

        s_w_i, s_h_i, s_w_f, s_h_f = 3748, 230, 3823, 281

        c_w_i, c_h_i, c_w_f, c_h_f = 1432, 380, 2407, 1739

    else:
        t_w_i, t_h_i, t_w_f, t_h_f = 1313, 54, 1912, 85

        s_w_i, s_h_i, s_w_f, s_h_f = 1876, 115, 1911, 140

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

    x=-1
    for i in range(len(title)):
        if title[i]=='-':
            x=i
    title=title[0:x].strip()

    print(title, f'({set_})', end=' - ')

    if double_card:
        title=title.split('//')
        for i in range(len(title)):
            title[i]=translate(title[i].strip())
        title = ' - '.join(title)
    else:
        title = translate(title)

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

# def on_scroll(x, y, dx, dy):
#     if dy==1:
#         save_card()

with mouse.Listener(on_click=on_click) as listener:
    listener.join()
