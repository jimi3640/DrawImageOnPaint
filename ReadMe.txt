Welcome

How to use code:
In the Images folder there is three images:
1- start_button.png : replace the image with your own start button image. best and easiest way is to use windows Snippin Tool.
2- 1.png : it is the change color bottum in ms-paint. if after the start of script, you saw 'cannot find change color buttom' in console,
 please replace 1.png image with your own image of change color. as note number 1, best and easiest way is windows Snipping Tool.
 remmeber to save it as 1.png or  change the file name in line 16 of script.
3- google.png : the image that script tries to draw it in ms-paint. you can change it to any custom image. 
but remember to keep the name as google.png or change the file name in script (line 55)

some notes:
- big size images may increase the drawing time. the more color ranges and more pixels make the process longer.
- before running script, just one time open the ms-paint and resize the drawing screen to desired size (as big as you can). 
although resize the windows (maybe maximazed is better) and close the window. This process will be saved in windows and next time
ms-paint will running in last sizes that you choosed.
- to stop running, just drang the mouse to top left corner of screen. because of "pyautogui.FAILSAFE = True" in line 36, 
if you place your mouse on position 0,0 the process will be terminated. position 0,0 is top left of screen.



leave comments if you have any problems.