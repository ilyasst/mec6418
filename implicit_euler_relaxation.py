from tensor_personal_functions import *
from projectors_personal_functions import *
from convenient_objects import *
from numpy.linalg import inv
import matplotlib.pyplot as plt


def implicit_euler_relaxation(n, h, deformation, k0, k1, k2, u0, u1, u2, w1, w2):
	#wi et lambdaio are positive
	
	J_tensor4 = generate_J_tensor4()
	
	I_tensor4 = generate_I_tensor4()
	
	K_tensor4 = generate_K_tensor4()

	J_matrix = tensor4_to_voigt4( J_tensor4 )

	K_matrix = tensor4_to_voigt4( K_tensor4 )
	
	#Matrices rigid
	C0 = 3.*dot( k0, J_matrix) + 2.*dot( u0, K_matrix )
	C1 = 3.*dot( k1, J_matrix) + 2.*dot( u1, K_matrix )
	C2 = 3.*dot( k2, J_matrix) + 2.*dot( u2, K_matrix )
	print "C[0]:"
	for i in range(0, len(C0)):
		print C0[i]
	print "C[1]:"
	for i in range(0, len(C1)):
		print C1[i]
	print "C[2]:"
	for i in range(0, len(C2)):
		print C2[i]
		
	#Matrices internces
	L1 = C0 + C1 + C2
	print "L1:"
	for i in range(0, len(L1)):
		print L1[i]
	#L21
	L21 = linalg.cholesky( dot(w1, C1) )
	print "L21 = Cholesky(C1*w1):"
	for i in range(0, len(L21)):
		print L21[i]
	#L22
	L22 = linalg.cholesky( dot(w2, C2) )
	print "L22 = Cholesky(C2*w2):"
	for i in range(0, len(L22)):
		print L22[i]
		
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
	
	L3 = initTensor( 0., 12, 12 )
	for i in range(0, 6):
		L3[i][i] = w1
	for i in range(6, 12):
		L3[i][i] = w2
	print "L3[r][r] = w1 for r(0,5); and w2 for r(6,12) :"
	for i in range(0, 12):
		print L3[i]

	#B = Identity
	B = indentity12_12()

	#W1 and W2
	W1_matrix = initTensor(0., 12, 12)
	W1_matrix = inv( B + dot(h, dot( B, L3 ) ) )
	print "W1 = inverse( B + h * B * L3 )"
	for i in range(0, 12):
		print W1_matrix[i]
		
	W2_matrix = initTensor(0., 12, 12)
	W2_matrix = dot( dot( dot(-h, inv( B + dot(h, dot( B, L3 ) ) )),  inv(B)),  transpose(L2))
	print "W2 = - h * inverse( B + h * B * L3 ) * inverse(B) *transpose( L2 ) "
	print "Len( W2 ) =", len(W2_matrix), " * ", len(W2_matrix[0])
	for i in range(0, 12):
		print W2_matrix[i]
		
	#Euler
	x = initTensor( 0., n, 12 )
	stress = initTensor( 0., n, 6 ) 
	print "len(deformation[0]):", len(deformation[0])
	x[0] = dot( W2_matrix, deformation[0] )
	
	for i in range( 1, n ):
		x[i] = dot( W1_matrix, x[i-1] ) + dot( W2_matrix, deformation[i] )
		stress[i] = dot( L1, deformation[i] ) + dot( L2, x[i] )

	return stress



n = 1000
deformation = initTensor(0., n, 6)
eps0 = 0.01
for i in range(0, n):
	deformation[i][0] = eps0

#(n, h, deformation, k0, k1, k2, u0, u1, u2, w1, w2)
stress = implicit_euler_relaxation( 1000, 0.0050, deformation, 10., 10., 6., 4., 4., 1., 0.1, 0.0116 )
stress11 = []
time = []
for i in range(0, n):
	stress11.append( stress[i][0] )
	time.append( i*0.005 )
	
plt.plot( time, stress11, 'b--', label = "stress")
plt.xlabel('time')
plt.title("Stress")
plt.ylabel('stress')
plt.legend()
plt.savefig('05_01.png')
plt.close()