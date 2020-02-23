import math

x1 = int (input())
y1 = int (input())
x2 = int (input())
y2 = int (input())

Dx = (x1 - x2)**2
Dy = (y1 - y2)**2

D = math.sqrt (Dx + Dy)

if D<10:
	print ('perto')
else:
	print ('longe')
