print("\n#############################################\n------------- Quadratics Helper -------------\n#############################################\n")

#Imports
import sys
import vertex
import argparse

#Setup args and opts
opts = [opt for opt in sys.argv[1:] if opt.startswith("--")]

#Testing Area



#Performer Functions
def vertexfinder():
	print("Finding Vertex:\nEquation formatted as: ax^2 + bx + c\n\n")
	a = int(input("a = "))
	b = int(input("b = "))
	c = int(input("c = "))
	coord = vertex.vertex(a, b, c)
	print("Vertex at: ({}, {})".format(coord[0], coord[1]))
def interceptfinder():
	print("Finding Vertex:\nEquation formatted as: ax^2 + bx + c\n\n")
	a = int(input("a = "))
	b = int(input("b = "))
	c = int(input("c = "))
	intercepts = vertex.xint(a, b, c)
	print("X intercepts at: ({}, {})".format(intercepts[0], intercepts[1]))
#Doer
if (len(opts) > 1):
	print("Please input one argument. Inputted argument: {}".format(opts))
	sys.exit()

if "--vertex" in opts:
	vertexfinder()
elif "--xint" in opts:
	interceptfinder()
elif "--help" in opts:
	#Argparse prep
	parser = argparse.ArgumentParser(description = "This is a command line tool to help solve quadratic style equations;   \nNo Dependencies Required; \nMade by Varunan Varathan")
	parser.add_argument("--vertex", help="Find the vertex of a quadratic equation")
	parser.add_argument("--xint", help="Find the x intercepts of a quadratic equation")
	args = parser.parse_args()
	print(args.accumulate(args.integers))


