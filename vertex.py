import sys 
import math
# Find the vertex of a parabola
def vertex(a, b, c):
	xcord = 0 - (b / (2 * a))
	ycord = (a * xcord * xcord) + (b * xcord) + c
	return [xcord, ycord]

# Find x intercepts
def xint(a, b, c):
	vertexcoord = vertex(a, b, c)
	firstcoord = a + b + c
	if (vertexcoord[1] > 0):
		if (firstcoord > vertexcoord[1]):
			return [None, None]
			pass
	else:
		if firstcoord < vertexcoord[1]:
			return [None, None]
			pass
	intercept1 = ((0 - b) + math.sqrt((b * b) - (4 * a * c))) / (2 * a)
	intercept2 = ((0 - b) - math.sqrt((b * b) - (4 * a * c))) / (2 * a)
	return [intercept1, intercept2]

# Find y intercepts
def yint(a, b, c):
	return c

def intersection(a1, b1, c1, a2, b2, c2):
	pass

def slopeequation(a, b, c):
	pass