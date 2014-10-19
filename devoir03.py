from numpy import *
from tensor_personal_functions import *
from convenient_objects import *
from projectors_personal_functions import *


def problem1():
	C = initTensor(0., 6, 6)
	
	C[0][0] = 7.
	C[0][1] = 17.
	C[0][2] = 17.
	
	C[1][0] = 17.
	C[1][1] = 7.5
	C[1][2] = -4.5
	
	C[2][0] = 17.
	C[2][1] = -4.5
	C[2][2] = 7.5
	
	C[3][3] = 12.
	C[4][4] = 7.
	C[5][5] = 7.
	
	print "C ="
	for i in range(0, len(C[0])):
		print C[i]
	
	print "Eigen values:"
	print linalg.eigvals(C)
	
	for i in range(0, len( linalg.eigvals(C) ) ):
		if linalg.eigvals(C)[i] < 0:
			print "Eigen value", linalg.eigvals(C)[i], "is < 0"
			print "Not definite positive"
	
problem1()
	