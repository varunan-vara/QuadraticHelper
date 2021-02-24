print("\n#############################################\n------------- Quadratics Helper -------------\n#############################################\n")

#Imports
import sys
import argparse

import vertex
import translate

#Setup args and opts
opts = [opt for opt in sys.argv[1:] if opt.startswith("--")]

#Testing Area



#Performer Functions
def vertexfinder():
	print("Finding Vertex:\nEquation formatted as: ax^2 + bx + c\n\n")
	a = float(input("a = "))
	b = float(input("b = "))
	c = float(input("c = "))
	coord = vertex.vertex(a, b, c)
	print("Vertex at: ({}, {})".format(coord[0], coord[1]))
def interceptfinder():
	print("Finding Vertex:\nEquation formatted as: ax^2 + bx + c\n\n")
	a = float(input("a = "))
	b = float(input("b = "))
	c = float(input("c = "))
	intercepts = vertex.xint(a, b, c)
	print("X intercepts at: ({}, {})".format(intercepts[0], intercepts[1]))
def equationconverter():
	print("Convert Equations from one form to another: \nUse the numbers in the legend for inputs:")
	print("1. Standard Equation\n2. Vertex Form Equation\n3. X Intercept Form Equation")
	fromequation = int(input("Original Equation: "))
	toequation = int(input("Convert Equation to: "))
	if fromequation < 1 or fromequation > 3 or toequation < 1 or toequation > 3:
		print("Proper Equation form was not given, terminating request.")
		pass
	else:
		keylist = ["placeholder", "standard", "vertex", "xint"]
		print(translate.convertEquation(keylist[fromequation], keylist[toequation]))

#Doer
if (len(opts) > 1):
	print("Please input one argument. Inputted argument: {}".format(opts))
	sys.exit()

if "--vertex" in opts:
	vertexfinder()
elif "--xint" in opts:
	interceptfinder()
elif "--equation" in opts:
	equationconverter()
elif "--help" in opts:
	#Argparse prep
	parser = argparse.ArgumentParser(description = "This is a command line tool to help solve quadratic style equations;   \nNo Dependencies Required; \nMade by Varunan Varathan")
	parser.add_argument("--vertex", help="Find the vertex of a quadratic equation")
	parser.add_argument("--xint", help="Find the x intercepts of a quadratic equation")
	parser.add_argument("--equation", help="Convert equations from one form to another")
	args = parser.parse_args()
	print(args.accumulate(args.integers))
	print("\n\n")


