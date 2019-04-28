#!/usr/local/bin/python3
import pyautogui as pa
import time
pa.PAUSE = 1
pa.FAILSAFE = True
pa.size()
width, height = pa.size()
soundx = width - 420
desktop = width - 720
print(width)
print(height)
pa.click(soundx + 90,5)
time.sleep(1)
pa.click(soundx + 105, 60)
time.sleep(1)
pa.dragTo(soundx + 200,60,2)
time.sleep(1)
pa.click(soundx + 90,5)
time.sleep(1)
pa.click(soundx + 130, 60)
#pa.click(1670, 60)
time.sleep(1)
pa.rightClick(soundx + 330,50)
time.sleep(1)
pa.click(soundx + 320,55)
time.sleep(1)
pa.click(240,5)
time.sleep(1)
pa.click(240,180)
time.sleep(1)
pa.click(240,300)
time.sleep(1)
pa.click(390,5)
time.sleep(1)
pa.dragTo(390,1,5)
time.sleep(1)
pa.doubleClick(240,480)
pa.PAUSE = 1

