# Hello excercise from Week 0

# Name: Andrew Lee


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				



# This is where you put code to move bob

# Draw the H
pu(bob)
bk(bob, 100)
lt(bob)
pd(bob)
fd(bob, 50)
bk(bob, 25)
rt(bob)
fd(bob, 25)
lt(bob)
fd(bob, 25)
bk(bob, 50)
rt(bob)

# Space
pu(bob)
fd(bob, 10)

# Draw the E
pd(bob)
lt(bob)
fd(bob, 50)
rt(bob)
fd(bob, 25)
rt(bob)
pu(bob)
fd(bob, 25)
rt(bob)
pd(bob)
fd(bob, 25)
lt(bob)
fd(bob, 25)
lt(bob)
fd(bob, 25)

# Draw Two L's with spaces

for i in range(2):
	pu(bob)
	fd(bob, 10)
	pd(bob)
	lt(bob)
	fd(bob, 50)
	bk(bob, 50)
	rt(bob)
	fd(bob, 25)

# Space
pu(bob)
fd(bob, 10)

#Draw the O
pd(bob)
fd(bob, 25)
lt(bob)
fd(bob, 50)
lt(bob)
fd(bob, 25)
lt(bob)
fd(bob, 50)

wait_for_user()					
