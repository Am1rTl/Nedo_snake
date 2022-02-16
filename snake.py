import time
import random
import keyboard
import os
os.system("mode con cols=100 lines=50")

speed = 1
a = []
for i in range(25):
	a.append([])
	for _ in range(50):
		a[i].append(' ')
x = random.randint(0,49)
y = random.randint(0,24)
a[y][x] = '0'
nullik = 0
score = 0

while ((x>=0 and y>=0) and (x<=49 and y<=24)):
	for i in range(25):
		for b in range(50):
			if a[i][b] == '+':
				nullik = 1
	if nullik == 0:
		x1 = random.randint(0,49)
		y1 = random.randint(0,24)
		while x1 == x and y1 == y :
			x1 = random.randint(0,49)
			y1 = random.randint(0,24)
		a[y1][x1] = '+'
		score+= 1
	
	print('score :',score)
	nullik = 0
		
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	pole = ''
	for i in range(25):
		for j in range(50):
			pole+= a[i][j]
		print('|',pole,'|')
		pole = ''
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	time.sleep(0.1)
	if keyboard.is_pressed('Up'):
			a[y-1][x] = '0'
			a[y][x] = ' '
			y -= 1
	elif keyboard.is_pressed('Left'):
			a[y][x-1] = '0'
			a[y][x] = ' '
			x -= 1
	elif keyboard.is_pressed('Right'):
			a[y][x+1] = '0'
			a[y][x] = ' '
			x += 1
	elif keyboard.is_pressed('Down'):
			a[y+1][x] = '0'
			a[y][x] = ' '
			y += 1
	
			
	
	
