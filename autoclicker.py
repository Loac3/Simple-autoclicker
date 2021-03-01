from pynput.mouse import Button, Controller
import time, keyboard, mouse, random
from random import uniform
import os
total_clicks = 0
print("""
Mouse LMB Autoclicker by Loac
@gvar3

Middle mouse button (scroll wheel) to click

Choose the timings, random timings to prevent anticheat from detecting you

press * to close the autoclicker
press / to show total clicks pressed
	""")


mouse2 = Controller()
time_each_click = input("Input random time between each click: ")
time_each_click2 = input("Input 2nd random time between each click: ")
try:
	time_each_click = float(time_each_click)
	time_each_click2 = float(time_each_click2)
except:
	print("Couldnt convert input to float... Have you entered a real number?")
	gone = input("Input enter to exit...")
	exit()


def autoclicker():
	global total_clicks
	random_click_speed = random.uniform(time_each_click, time_each_click2)
	time.sleep(random_click_speed)
	mouse2.click(Button.left, 1)
	total_clicks +=1

print("Autoclicker started")
while True:
	try:
		if keyboard.is_pressed('*'):
			exit()
	
		if keyboard.is_pressed('/'):
			time.sleep(0.1)
			print(total_clicks)
		while mouse.is_pressed(button='middle'):
			autoclicker()
	except:
		pass
