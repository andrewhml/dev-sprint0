# Flower excercise (4.2) from Week 0

# Name: Andrew Lee

import math

from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()
bob.color = 'blue'
bob.delay = 0.01		



# This is where you put code to move bob

# Use polyline and arc from sib_polygon.py
def polyline(name, n, distance, theta):
	for i in range(n):
		fd(name, distance)
		lt(name, theta)

def arc (name, radius, theta):
	arc_length = 2 * math.pi * radius * theta / 360
	n = int(arc_length / 3) + 1
	step_length = arc_length / n
	step_angle = float(theta) / n
	polyline(name, n, step_length, step_angle)

#define a petal
#takes a Turtle(), a radius and number of petals in flower

def flower (name, radius, petals):
	#calculate how much to rotate the turtle
	theta = int(360 / petals)
	#loop for the number of desired petals
	for i in range(petals):
		arc(name, radius, theta)
		lt(bob, 180-theta)
		arc(name, radius, theta)
		rt(name, 180)

#unique function to create an overlaping flower
def overlap (name, n, radius, petals):
	for i in range (n):
		petal(name, radius, petals)
		rt(bob, 180 / petals)

#petal(bob, 100, 5)
#lt(bob, 36)
#petal(bob, 100, 5)

flower(bob, 80, 7)
pu(bob)
fd(bob, 200)
pd(bob)
overlap(bob, 2, 60, 5)
pu(bob)
lt(bob, 75)
fd(bob, 200)
pd(bob)
flower(bob, 200, 20)


wait_for_user()					

