from numpy import *
from tensor_personal_functions import *
from convenient_objects import *

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
	
		
		
#problem2()
problem4()

