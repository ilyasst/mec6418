from numpy import *
from tensor_personal_functions import *

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


A_tensor4 = voigt4_to_tensor4( A_voigt4 )

print "Tensor minor symmetry is...", check_tensor_minor_symmetry( A_tensor4 )
print "Tensor major symmetry is...",check_tensor_major_symmetry(A_tensor4 )

#P = generate_trans_matrix( init_base, final_base )
#print P
#A_tensor_in_new_base = tensorial_base_change( P, A_tensor4 )
#A_voigt4_new_base = tensor4_to_voigt4( A_tensor_in_new_base )

#print "======================================================"
#print "======================================================"
#print "RESULT:"
print "A_tensor4 ="
for i in range(len(A_tensor4[0][0][0])):
	for j in range(len(A_tensor4[0][0][0])):
		for k in range(len(A_tensor4[0][0][0])):
			for l in range(len(A_tensor4[0][0][0])):
				print i,j,k,l, A_tensor4[i][j][k][l]

