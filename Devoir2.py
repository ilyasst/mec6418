from numpy import *


#Takes A(6,6) gives back A(4,4,4,4)
def voigt4_to_tensor4( A_voigt4 ):
	
	A_tensor4 = [ [ 0 for i in range(6) ] for j in range(6) ]
			
	for i in range( len( A_voigt4 )):
		for j in range( len( A_voigt4[i] ) ):
			print A_voigt4[i][j]
	
	
A_voigt4 = [ [ 0.241, -0.202, -0.347, -0.848, 0.959, -0.023 ],
	     [ -0.202, -0.678, 0.520, -0.600, 0.186, 0.861],
	     [ -0.347, 0.520, 0.200, -0.473, -0.598, -0.927],
	     [ -0.848, -0.600, -0.473, -0.214, -0.338, 0.201],
	     [ 0.959, 0.186, -0.598, -0.338, 0.276, -0.392],
	     [ -0.023, 0.861, -0.927, 0.201, -0.392, -0.719]
	     ]

voigt4_to_tensor4( A_voigt4 )