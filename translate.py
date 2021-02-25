import sys
import math
import vertex as vert

def convertEquation(fromv, tov):
	print("This process does not yield correct answers yet")
	if fromv == tov:
		return "Not a valid conversion - Same to and from format... ending procees"
		pass
	vertex = [0, 0]
	yint = 0
	xint = [0, 0]
	if fromv == "vertex":
		print("Vertex form: y = a(x-h)^2 + k")
		a = float(input("a = "))
		h = float(input("h = "))
		k = float(input("k = "))
		vertex[0] = h
		vertex[1] = k
		yint = a * (0 - h) * (0 - h) + k
		if (0 - k) < 0:
			xint = [None, None]
		else:
			xint = [math.sqrt(0 - k) + h, 0 - math.sqrt(0 - k) + h]
	elif fromv == "standard":
		print("Standard form: y = ax^2 + bx + c")
		a = float(input("a = "))
		b = float(input("b = "))
		c = float(input("c = "))
		vertex = vert.vertex(a, b, c)
		yint = c
		xint = vert.xint(a, b, c)
	elif fromv == "xint":
		print("X intercept form: y = a(x - r)(x - s)")
		a = float(input("a = "))
		r = float(input("r = "))
		s = float(input("s = "))
		xint = [r, s]
		yint = a * (0 - r) * (0 - s)
		vertex[0] = (r - s) / 2
		vertex[1] = a * (vertex[0] - r) * (vertex[0] - s)
	else:
		print("Invalid input equation")
		pass
	print("Converting Equation...")
	if tov == "vertex":
		h = vertex[0]
		k = vertex[1]
		a = (yint - k) / ((0 - h) * (0 - h))
		if h < 0:
			return "Vertex Form: y = {}(x + {})^2 + {}".format(a, abs(h), k)
		elif h > 0:
			return "Vertex Form: y = {}(x - {})^2 + {}".format(a, abs(h), k)
		else: 
			return "Error: Miscalculation - try again - 01"
	elif tov == "standard":
		h = vertex[0]
		k = vertex[1]
		a = (yint - k) / ((0 - h) * (0 - h))
		b = 0 - h
		c = h + k
		return "Standard Form: y = {}x^2 + {}x + {}".format(a, b, c)
	elif tov == "xint":
		if xint == [None, None]:
			return "No X intercepts present - hence this equation form is not applicable"
		else:
			a = float(vertex[1]) / ((float(vertex[0]) - float(xint[0])) * (float(vertex[0])) - float(xint[1]))
			return "X Intercept Form: y = {}(x - {})(x - {})".format(a, (0 - xint[0]), (0 - xint[1]))