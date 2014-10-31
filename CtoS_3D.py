from tensor_personal_functions import *
from numpy.linalg import inv, svd
from projectors_personal_functions import *


def CtoS_interconversion3D( C0, C1, C2, rho ):
	# Compute the internal matrices associated with the relaxation modulus
	# 2
	L1 = initTensor( 0., 6, 6 )
	for i in range(0, len(L1)):
		for j in range(0, len(L1)):
			L1[i][j] = C0[i][j] + C1[i][j] + C2[i][j]
	
	print "L1"
	for i in range(0, len(L1)):
		print L1[i]
		
	# 3
	L21 = linalg.cholesky( dot(rho[0], C1) )
	L22 = linalg.cholesky( dot(rho[1], C2) )
	L2 = initTensor( 0., 6, len(L21)+len(L22) )
	for k in range(0, 6):
		for j in range(0, 12):
			if j < 6:
				L2[k][j] = L21[k][j]
			elif j >= 6:
				L2[k][j] = L22[k][j-6]
	print "L2 = ( L21 | L22 ) :"
	for i in range(0, 6):
		print L2[i]
		
	# 4
	print "L3:"
	L3 = initTensor(0, 12, 12)
	for i in range(0, 12):
		for j in range(0, 12):
			if i<6 and j<6:
				L3[i][j] = rho[0]
			elif i>=6 and j>=6:
				L3[i][j] = rho[1]
	for i in range(0, 12):
		print L3[i]
	
	# 5
	B = eye(6*len(rho))

	# Compute the internal matrices associated with the creep compliance
	
	#7
	A1 = inv(L1)
	print "A1:"
	print A1

	#8
	A2 = transpose( dot( transpose(L2) , inv(L1) ) )
	print "A2:"
	print A2
	 
	#9 THERE IS A BUG RIGHT HERE
	A3 = L3 -  dot( dot( transpose( L2 ), inv( L1 ) ) , L2 )
	print "A3:"
	for i in range(0, len(A3)):
		print A3[i]
		
	# 10 Diagonalize
	# 11 Compute the eigenvectores P and eigenvalues D of A with singular value decomposition
	# 12
	P, A3s, Q = linalg.svd(A3, full_matrices=True)
	print "Matrix P:"
	print P
	print "A3*:"
	print A3s
	print "Lambdas ="
	lambdas = linalg.eigvals( A3 )
	print lambdas
	
	# 13
	A2s = transpose( dot( transpose( P ), transpose( A2 ) ) )
	
	#14
	
	#ALERT STOPPED HERE
	#S0 = A1
	#for m in range( 0, 6*len(rho)):
		#S[
	
	
C0 = [ 136.8, 1.546, 0.996, 1.209, 0.408, 0.026, 100.9, -3.455, -4.792, 5.692,  1.367, 51.18,  48.78, -20.04, -15.27, 75.10, -37.96, 4.752, 235.3,  12.08, 189.1 ]
C0 = generate_symmetric_matrix66_from_list( dot( 0.1, C0) )

C1 = [ 44.76, 0.560, 1.741, 0.173, 2.033, 2.467, 
      116.9, -27.11,  35.68, 11.87, -10.81,  55.8, -3.398,   5.29, -9.681, 51.97, -30.22, 18.29, 95.46, -50.67, 88.94 ]
C1 = generate_symmetric_matrix66_from_list( dot( 0.1, C1 ) )

C2 = [ 25.73,-12.29,-9.826,-6.928,-1.113,-2.627, 
      119.2, -53.04, -57.93,-4.033,  18.40, 147.4, -31.91, -56.97, -16.33, 198.1,  61.87,-32.13, 155.0,  23.37, 97.59 ]
C2 = generate_symmetric_matrix66_from_list( dot( 0.1, C2 ) )

rho = [ 14.514, 368.88 ]

CtoS_interconversion3D( C0, C1, C2, rho )




	
