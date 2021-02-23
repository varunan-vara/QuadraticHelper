import sys 
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
			return "No x interecepts present"
			pass
	else:
		if firstcoord < vertexcoord[1]:
			return "No x interecepts present"
			pass
	

# Find y intercepts
def yint(a, b, c):
	return c

