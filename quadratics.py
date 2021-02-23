print("\n#############################################\n------------- Quadratics Helper -------------\n#############################################\n")

#Imports
import sys
import vertex
import argparse

#Setup args and opts
opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]

#Testing Area

#Argparse prep
parser = argparse.ArgumentParser(description = "Solve Quadratic Equations.")
parser.add_argument("--vertex", dest="accumulator", action="store_const", const=sum, default=max, help="Find the vertex of a quadratic equation, given ax^2 + bx + c")
args = parser.parse_args()
print(args.accumulate(args.integers))

#Performer Functions
def vertexfinder():
	print("Finiding Vertex:\nEquation formatted as: ax^2 + bx + c\n\n")
	a = int(input("a = "))
	b = int(input("b = "))
	c = int(input("c = "))
	coord = vertex.vertex(a, b, c)
	print("Vertex at: ({}, {})".format(coord[0], coord[1]))
def helpy():
	print("This is a command line tool to help solve quadratic style equations.\nTo see what type of commands are available, run without any arguments\nNo Dependencies Required\nMade by Varunan Varathan")

#Doer
if (len(opts) > 1):
	print("Please input one argument. Inputted argument: {}".format(opts))
	sys.exit()

if "-vertex" in opts:
	vertexfinder()
elif "-help" in opts:
	helpy()


