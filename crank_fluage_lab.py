from tensor_personal_functions import *
from projectors_personal_functions import *
from convenient_objects import *
from numpy.linalg import inv
from import_data import import_data_05_04
import matplotlib.pyplot as plt


def crankn_fluage(time_length, n, stress, k_0, k_1, k_2, u_0, u_1, u_2, lambda1, lambda2):
	#wi et lambdaio are positive
	print "================================================================================"
	print "================================================================================"
	print "n=", n
	print "time_length=", time_length
	h = float(time_length)/float(n)
	print "h=", h 
	
	J_tensor4 = generate_J_tensor4()
	
	I_tensor4 = generate_I_tensor4()
	
	K_tensor4 = generate_K_tensor4()

	J_matrix = tensor4_to_voigt4( J_tensor4 )

	K_matrix = tensor4_to_voigt4( K_tensor4 )
	
	#Matrices soupless
	S0 = dot(k_0/3., J_matrix) + dot(u_0/2., K_matrix)
	S1 = dot(k_1/3., J_matrix) + dot(u_1/2., K_matrix)
	S2 = dot(k_2/3., J_matrix) + dot(u_2/2., K_matrix)

	print "S0:"
	for i in range(0, len(S0)):
		print S0[i]
	print "S1:"
	for i in range(0, len(S1)):
		print S1[i]
	print "S2:"
	for i in range(0, len(S2)):
		print S2[i]

	A1 = S0
	A21 = linalg.cholesky( dot(S1,lambda1) )
	A22 = linalg.cholesky( dot(S2,lambda2) )
	print "A21:"
	for i in range(0, len(A21)):
		print A21[i]
	print "A22:"
	for i in range(0, len(A22)):
		print A22[i]
	
	A2 = initTensor( 0., 6, len(A21)+len(A22) )
	for k in range(0, 6):
		for j in range(0, 12):
			if j < 6:
				A2[k][j] = A21[k][j]
			elif j >= 6:
				A2[k][j] = A22[k][j-6]
	print "A2 = ( A21 | A22 ) :"
	for i in range(0, 6):
		print A2[i]
	
	A3 = initTensor( 0., 12, 12 )
	for i in range(0, 6):
		A3[i][i] = lambda1
	for i in range(6, 12):
		A3[i][i] = lambda2
	print "A3[r][r] = lambda1 for r(0,5); and lambda2 for r(6,12) :"
	for i in range(0, 12):
		print A3[i]
		
		
	#B = Identity
	B = indentity12_12()
	
	#W1 and W2
	W1_matrix = initTensor(0., 12, 12)
	W1_matrix = dot( inv( B + dot(h/2., dot( B, A3 ) ) ) , ( B - dot( dot( h/2., B ), A3 ) ) )
	print "W1 = inverse( B + h/2 * B * L3 ) * ( B - h/2 * B * L3 ) "
	for i in range(0, 12):
		print W1_matrix[i]
		
	W2_matrix = initTensor(0., 12, 12)
	
	W2_matrix = dot( dot( dot(-1.*(h/2.), inv( B + dot((h/2.), dot( B, A3 ) ) )),  inv(B)),  transpose(A2))
	print "W2 = - h/2 * inverse( B + h/2 * B *A3 ) * inverse(B) *transpose( A2 ) "
	print "Len( W2 ) =", len(W2_matrix), " * ", len(W2_matrix[0])
	for i in range(0, 12):
		print W2_matrix[i]
	
	#Euler
	x = initTensor( 0., n, 12 )
	deformation = initTensor( 0., n, 6 ) 
	print "len(deformation[0]):", len(deformation[0])
	
	#init
	print stress[0]
	x[0] = dot( W2_matrix, stress[0] )
	deformation[0] = dot( A1, stress[0] ) - dot( A2, x[0] )
	print "Deformation[0]", "x[0]"
	print deformation[0][0], x[0][0]
	
	for i in range( 1, n ):
		temp_stress = []
		for j in range(0, 6):
			temp_stress.append( stress[i][j] + stress[i-1][j] ) 
		#print "temp_stress;"
		#print temp_stress, len(temp_stress) 
		
		x[i] = dot( W1_matrix, x[i-1] ) + dot( W2_matrix, ( temp_stress ) )
		deformation[i] = dot( A1, stress[i] ) - dot( A2, x[i] )

		print deformation[i][0], deformation[i][1], deformation[i][2], x[i][0]

	return deformation

k_0 = 3.
k_1 = 2.
k_2 = 1.
u_0 = 7.
u_1 = 2.
u_2 = 3.
lambda0 = 0.
lambda1 = 2.
lambda2 = 1./130.

#time is a list
#stress is (n, 6) tensor !
time, stress = import_data_05_04( "05-06-histoire-contrainte.csv" )

n = len(time)
time_length = time[n-1]

#print "n =", n
#print "TIME=", time[len(time)-1]

deformation = crankn_fluage(time_length, n, stress, k_0, k_1, k_2, u_0, u_1, u_2, lambda1, lambda2)

deformation11 = []
for i in range(0, len(deformation)):
	deformation11.append( deformation[i][0] )

print "lengths:", len(time), len(deformation11)
plt.plot( time, deformation11, 'b--', label = "deformation")
plt.xlabel('time')
plt.title("05-06-histoire-contrainte")
plt.ylabel('deformation')
plt.legend()
plt.savefig('05_04_crankn_fluage.png')
plt.close()