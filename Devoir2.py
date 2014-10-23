from numpy import *
from tensor_personal_functions import *
from convenient_objects import *
from projectors_personal_functions import *
from numpy.linalg import inv

#====================================================
# Problem 2
# Problem 4
#====================================================

def problem2():
	#init_base = [ X, Y, Z ]
	init_base = [ [ 1, 0, 0],
		[ 0, 1, 0],
		[ 0, 0, 1]
		]


	final_base = [ [ 0.654, -0.082, -0.752 ],
		[ -0.540, -0.746, -0.389],
		[ -0.529, 0.661, -0.532 ]
		]
		
	A_voigt4 = [ [ 0.241, -0.202, -0.347, -0.848, 0.959, -0.023 ],
		[ -0.202, -0.678, 0.520, -0.600, 0.186, 0.861],
		[ -0.347, 0.520, 0.200, -0.473, -0.598, -0.927],
		[ -0.848, -0.600, -0.473, -0.214, -0.338, 0.201],
		[ 0.959, 0.186, -0.598, -0.338, 0.276, -0.392],
		[ -0.023, 0.861, -0.927, 0.201, -0.392, -0.719]
		]
	print "======================================================"
	print "Transformed A from voigt shape to tensorial shape."
	A_tensor4 = voigt4_to_tensor4( A_voigt4 )
	print "======================================================"

	print "Tensor minor symmetry is...", check_tensor_minor_symmetry( A_tensor4 )
	print "Tensor major symmetry is...",check_tensor_major_symmetry(A_tensor4 )

	P = generate_trans_matrix( init_base, final_base )
	print "======================================================"
	print "Generated transformation matrix P using initial and final base, P = "
	for i in range(0, 3):
		print P[i]


	A_tensor_in_new_base = tensorial_base_change( P, A_tensor4 )
	print "======================================================"
	print "Determined A_tensor in new base, A_voigt4_new_base..."
	A_voigt4_new_base = tensor4_to_voigt4( A_tensor_in_new_base )

	print "======================================================"
	print "======================================================"
	print "A_voigt4_new_base ="
	for i in range(0, 5):
		print A_voigt4_new_base[i]

		
def problem4():
	epsilon_ijk = generate_epsilon_ijk()
	
	print "======================================================"
	print "======================================================"
	print "Problem 04"
	print "======================================================"
	print "======================================================"
	print "epsilon_ijk ="
	
	for i in range(0, 3):
		print epsilon_ijk[i]
	
	print "======================================================"
	print "Question 1"
	print "epsilon_ijk[i][j][k]*epsilon_ijk[i][j][k] ?"
	print "------------------------------------------------------"
	#Question 1
	# epsilon_ijk[i][j][k]*epsilon_ijk[i][j][k] ?
	
	result = 0

	for i in range(0, 3):
		for j in range(0, 3):
			for k in range(0, 3):
				result = result + epsilon_ijk[i][j][k]*epsilon_ijk[i][j][k]
	
	print "epsilon_ijk[i][j][k]*epsilon_ijk[i][j][k] = ", result
	
	#Question 2
	# epsilon_ijk[i][j][k]*epsilon_ijk[m][j][k] ?
	
	print "======================================================"
	print "Question 2"
	print "epsilon_ijk[i][j][k]*epsilon_ijk[m][j][k] ?"
	print "------------------------------------------------------"
	
	result = initTensor(0, 3, 3)
	
	for i in range(0,3):
		for m in range(0,3):
			summation = 0
			for j in range(0,3):
				for k in range(0,3):
					result[i][m] = summation + epsilon_ijk[i][j][k]*epsilon_ijk[m][j][k]
	
	print "epsilon_ijk[i][j][k]*epsilon_ijk[m][j][k] = "
	for i in range(0,3):
		print result[i]
	
def problem10():
	S_voigt4 = initTensor( 0, 6, 6)
	El = 180 #GPa
	Et = 10 #GPa
	NuL = 0.28
	NuT = 0.4
	Gl = 7 #GPa
	#Axis x fiber direction

	S_voigt4[0][0] = 1./El
	S_voigt4[0][1] = -NuL/El
	S_voigt4[0][2] = -NuL/El
	
	S_voigt4[1][0] = -NuL/El
	S_voigt4[1][1] = 1./Et
	S_voigt4[1][2] = -NuT/Et
	
	S_voigt4[2][0] = -NuL/El
	S_voigt4[2][1] = -NuT/Et
	S_voigt4[2][2] = 1./Et
	
	S_voigt4[3][3] = (1.-NuT)/Et
	S_voigt4[4][4] = 1./(2*Gl)
	S_voigt4[5][5] = 1./(2*Gl)
	
	print "S_voigt4 = "
	for i in range(0, len(S_voigt4[0]) ):
		print S_voigt4[i]
		
	print "Now let's create P"	
	
	P = initTensor(0, 3, 3)
	#Rotation around Z by +37deg
	P[0][0] = cos(37*(pi/180))
	P[0][1] = -sin(37*(pi/180))
	P[0][2] = 0
	
	P[1][0] = sin(37*(pi/180))
	P[1][1] = cos(37*(pi/180))
	P[1][2] = 0
	
	P[2][0] = 0
	P[2][1] = 0
	P[2][2] = 1
	
	print "P = "
	for i in range(0, len(P[0]) ):
		print P[i]
	
	print "Now we need to convert S to a tensor 4"
	
	S_tensor4 = voigt4_to_tensor4( S_voigt4 )
	
	print "Then we perform a tensorial base change"
	
	S_tensor4_in_new_base = tensorial_base_change( P, S_tensor4 )
	
	print "We define Sigma the stress matrix"
	
	print "Sigma = "
	stress_matrix = initTensor(0, 3, 3)
	stress_matrix[0][0] = 100
	print "Sigma = "
	for i in range(0, len(stress_matrix[0]) ):
		print stress_matrix[i]
	
	print "We can now deduce the deofrmation which is S:Sigma"
	deformation_matrix = tensordot( S_tensor4_in_new_base, stress_matrix, 2)
	
	print "Convert it to Voigt notations"
	deformation_voigt = voigt_to_matrix( deformation_matrix )
	
	print "Deformation in voigt = "
	print deformation_voigt

#Also called extract projector parameters from isotropic transverse matrix
def problem13():
	S_voigt4 = initTensor(0, 6, 6)
	
	S_voigt4[0][0] = 5.56
	S_voigt4[0][1] = (-1.56)
	S_voigt4[0][2] = (-1.56)
	
	S_voigt4[1][0] = (-1.56)
	S_voigt4[1][1] = (100.)
	S_voigt4[1][2] = (-40)
	
	S_voigt4[2][0] = (-1.56)
	S_voigt4[2][1] = (-40.)
	S_voigt4[2][2] = (100.)
	
	S_voigt4[3][3] = (140.)
	S_voigt4[4][4] = (71.4)
	S_voigt4[5][5] = (71.4)
	
	for i in range(0, len(S_voigt4[0])):
		for j in range(0, len(S_voigt4[0])):
			S_voigt4[i][j] = pow(10, -6) * S_voigt4[i][j] 
			
	print "Initial S is:"
	for i in range(0, len(S_voigt4[0])):
		print S_voigt4[i]
	
	iT = generate_iT_matrix( 0 )
	
	EL = generate_EL_tensor( 0 )
	
	JT = generate_JT_tensor( iT )
	
	IT_6 = generate_IT_matrix( 0 )
	
	KE = generate_KE_tensor( 0, iT  )
	
	#IT_matrix wille be converted to a tensor in generate_KT_tensor
	KT = generate_KT_tensor( IT_6, JT  )
	
	KL = generate_KL_tensor( KT, KE )
	
	F_tensor = generate_F_tensor( 0, iT )
	
	F_matrix = tensor4_to_voigt4( F_tensor )
	
	F_matrix_transposed = transpose_matrix( F_matrix )
	
	#F is no symmetric !
	F_tensor_transposed = voigt4_to_tensor4_no_symmetry( F_matrix_transposed )
	
	print "F_Transposed_voigt is then:"
	for i in range(0, len(F_matrix_transposed[0])):
		print F_matrix_transposed[i]

		
	S_tensor4 = voigt4_to_tensor4( S_voigt4 )
	alpha = tensor4_contract4_tensor4( EL, S_tensor4 )
	print "Alpha =", alpha
	beta = tensor4_contract4_tensor4( JT, S_tensor4 )
	print "beta =", beta
	
	#GAMME IS WRONG
	gamma = tensor4_contract4_tensor4( F_tensor_transposed, S_tensor4 )
	print "gamma=", gamma
	
	gamma_prime = tensor4_contract4_tensor4( F_tensor, S_tensor4 )
	print "gamma_prime =", gamma_prime
	
	delta = tensor4_contract4_tensor4( KT, S_tensor4 )/2.
	print "delta =", delta
	
	delta_prime = tensor4_contract4_tensor4( KL, S_tensor4 )/2.
	print "delta_prime=", delta_prime
	
	print "The vector Omega is then:"
	omega = initTensor( 0., 2, 2 )
	omega[0][0] = alpha
	omega[0][1] = gamma_prime
	omega[1][0] = gamma
	omega[1][1] = beta
	print omega
	
	omega_inverse = inv( omega )
	print "And it's inverse is omega_invese:"
	print omega_inverse
	
	print "S-1 ="
	print omega_inverse[0][0], " * EL"
	print omega_inverse[1][1], " * JT"
	print omega_inverse[0][1], " * F_transpose"
	print omega_inverse[1][0], " * F"
	print 1./delta, " * KT"
	print 1./delta_prime, " * KL"

def problem06():
	
	init_base = [ [ 1, 0, 0],
		[ 0, 1, 0],
		[ 0, 0, 1]
		]

	final_base = initTensor( random.random_sample(), 3, 3 )

	P = generate_trans_matrix( init_base, final_base )

	rand_tensor = initTensor( random.random_sample(), 3, 3, 3, 3 )
	rand_matrix = tensor4_to_voigt4( rand_tensor)
	initial_trace = trace( rand_matrix )
	
	print "Initial trace:", initial_trace
	
	rand_tensor_base_changed = tensorial_base_change( P, rand_tensor )
	rand_matrix_base_changed = tensor4_to_voigt4( rand_tensor_base_changed )
	trace_after_rand_base_change = trace( rand_matrix_base_changed )
	
	print "trace_after_rand_base_change:", trace_after_rand_base_change
	
		
#problem2()
#problem4()

#PROBLEM with 10^(-3) CHECK IT SOMEDAY !
#problem10()

#problem13()

#CA MARCHE PAS
problem06()
