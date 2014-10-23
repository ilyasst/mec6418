from tensor_personal_functions import *
from projectors_personal_functions import *
from convenient_objects import *
from numpy.linalg import inv


def implicit_euler_fluage(k0, u0):
	#wi et lambdai are positive
	
	J_tensor4 = generate_J_tensor4()
	
	I_tensor4 = generate_I_tensor4()
	
	K_tensor4 = generate_K_tensor4()

	J_matrix = tensor4_to_voigt4( J_tensor4 )

	K_matrix = tensor4_to_voigt4( K_tensor4 )
	
	#Matrices soupless
	S0 = dot(k0/3., J_matrix) + dot(u0/2., K_matrix)
	print S0

	
	
	
implicit_euler_fluage(10., 4.)