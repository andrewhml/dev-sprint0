# Polygon excercise from Week 0

# Name:Andrew Lee

import math


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()
bob.delay = 0.01	
ted = Turtle()
ted.color = 'green'
ted.delay = 0.01
judy = Turtle()
judy.color = 'yellow'
judy.delay = 0.01
duke = Turtle() 
duke.color = 'purple'
daisy = Turtle()
daisy.color = 'blue'
daisy.delay = 0.01
marla = Turtle()
marla.color = 'black'
marla.delay = 0.01



# This is where you put code to move bob

def square1():
	for i in range(4):
		fd(bob, 100)
		lt(bob)

def square2(name, distance):
	for i in range(4):
		fd(name, distance)
		lt(name)

#def polygon(name, n, distance):
	#angle = 360.0 / n
	#for i in range(n):
		#fd(name, distance)
		#lt(name, angle)
	

#def circle(name, radius):
	#polygon(name,(2*math.pi*radius)/360, 360)

#def circle(name, radius):
	#circumfrance = 2 * math.pi * radius
	#distance = int(circumfrance/3) + 1
	#length = circumfrance / distance
	#polygon(name, distance, length)

#def arc(name, radius, theta):
	#arc_length = 2 * math.pi * radius * theta / 360
	#n = int(arc_length / 3) + 1
	#step_length = arc_length / n
	#step_angle = float(theta) / n
	#for i in range(n):
		#fd(name, step_length)
		#lt(name, step_angle)

def polyline(name, n, distance, theta):
	for i in range(n):
		fd(name, distance)
		lt(name, theta)

def polygon(name, n, distance):
	theta = 360.0 / n
	polyline(name, n, distance, theta)

def arc (name, radius, theta):
	arc_length = 2 * math.pi * radius * theta / 360
	n = int(arc_length / 3) + 1
	step_length = arc_length / n
	step_angle = float(theta) / n
	polyline(name, n, step_length, step_angle)

def circle(name, radius):
	arc(name, radius, 360)


#print square1()
#print square2(ted, 200)
print polygon(judy, 50, 8)
print circle(duke, 75)
print arc(daisy, 50, 90)




wait_for_user()					
