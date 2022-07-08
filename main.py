#! python3
#   Author      : jimi3640
#   GitHub      : https://github.com/jimi3640/DrawImageOnPaint
#   Youtube     : https://www.youtube.com/channel/UCoZG3afflQ5hj8WTuBe-49A
#   Year        : 2022
#   Description : This Script draws image that specified in line 54 in ms-paint using PyAutoGUI package.

import pyautogui
from PIL import Image
import pandas as pd

def set_color(R, G, B):
    pyautogui.PAUSE = 0.1
    try:
        _color_button_ = pyautogui.locateOnScreen('images/1.png')
        _location_ = pyautogui.center(_color_button_)
    except:
	print('cannot find change color button')
        pyautogui.PAUSE = 0.01
        return False

    if not pyautogui.click(_location_):
        pyautogui.typewrite('\t\t\t\t\t\t\t')
        pyautogui.write(str(R))
        pyautogui.typewrite('\t')
        pyautogui.write(str(G))
        pyautogui.typewrite('\t')
        pyautogui.write(str(B))
        pyautogui.typewrite('\n')

    pyautogui.PAUSE = 0.01
    return True

def paint():
    pyautogui.FAILSAFE = True
    # Location the start button
    _start_button_ = pyautogui.locateOnScreen('images/start_button.png')
    _location_ = pyautogui.center(_start_button_)

    # Clicking the start button
    if not pyautogui.click(_location_):
        print('Opened start menu successfully!')
    else:
        print('Failed to open start menu!')


    time.sleep(1)
    pyautogui.typewrite('paint')
    pyautogui.typewrite('\n')
    time.sleep(2)
    popup = pyautogui.getActiveWindow()
    popup.topleft = (0, 0)

    im = Image.open('images/google.png')  # Can be many different formats.
    pix = im.load()
    image_x, image_y = im.size  # Get the width and hight of the image for iterating over
    pyautogui.PAUSE = 0.01

    rows = []
    print('Image size:('+str(image_x)+' , '+str(image_y)+')')
    print('Loading image pixels')
    for i in range(0, image_x):
        for j in range(0, image_y):
            r, g, b, _ = im.getpixel((i,j))
            rows.append([(i,j), (r, g, b)])
    print('Image pixels loade successfully')
    df = pd.DataFrame(rows, columns=["pixel", "RGB"])

    df2 = df['RGB'].value_counts()
    paper_color = (255,255,255)
    x = 200
    y = 200
    for color, count in df2.items():
        if count>0:
            r,g,b = color
            if paper_color != (r,g,b):
                if not set_color(r, g, b):
		    continue
            else:
                continue
            mask = df.RGB.apply(lambda x: (r, g, b) == x)
            df3 = df[mask]
            for index, row in df3.iterrows():
                print('coloring pixel(' + str(row['pixel'][0]) + ',' + str(row['pixel'][1]) + ')   with color:  ' + str(color))
                pyautogui.click(x + int(row['pixel'][0]), y + int(row['pixel'][1]))



# Main function
if __name__ == '__main__':
    paint()

