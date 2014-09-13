from numpy import *

def tensor4_to_voigt4( A_tensor4 ):
	A_voigt4 = initTensor(0, 6, 6)	
	
	for i in range( 0, 3 ):
		#print i
		for j in range( 0, 3 ):
			A_voigt4[i][j] = A_tensor4[i][i][j][j]
			
	for i in range( 0, 3 ):
		#print i
		A_voigt4[3][i] = sqrt(2) * A_tensor4[1][2][i][i]
		A_voigt4[4][i] = sqrt(2) * A_tensor4[2][0][i][i]
		A_voigt4[5][i] = sqrt(2) * A_tensor4[0][1][i][i]
		
	for j in range( 0, 3 ):
		#print j
		A_voigt4[j][3] = sqrt(2) * A_tensor4[j][j][1][2]
		A_voigt4[j][4] = sqrt(2) * A_tensor4[j][j][2][0]
		A_voigt4[j][5] = sqrt(2) * A_tensor4[j][j][0][1]
		
	A_voigt4[3][3] = 2 * A_tensor4[1][2][1][2]
	A_voigt4[4][3] = 2 * A_tensor4[2][0][1][2]
	A_voigt4[5][3] = 2 * A_tensor4[0][1][1][2]
	
	A_voigt4[3][4] = 2 * A_tensor4[1][2][2][0]
	A_voigt4[4][4] = 2 * A_tensor4[2][0][2][0]
	A_voigt4[5][4] = 2 * A_tensor4[0][1][2][0]

	A_voigt4[3][5] = 2 * A_tensor4[1][2][0][1]
	A_voigt4[4][5] = 2 * A_tensor4[2][0][0][1]
	A_voigt4[5][5] = 2 * A_tensor4[0][1][0][1]
	
	#print "AVOIGT4[0]:"
	#for i in range(len(A_voigt4[0])):
		#print A_voigt4[i]

	return A_voigt4
	
#Takes A_voigt(6,6) gives back A_tensor(4,4,4,4)
def voigt4_to_tensor4( A_voigt4 ):

	A_tensor4 = initTensor(0, 3, 3, 3, 3)
	
	a = 0
	b = 0
	A_voigt4_length = len( A_voigt4 )
	for a in range(0, A_voigt4_length ):
		for b in range(0, A_voigt4_length ):

			flaga = False
			flagb = False
			
			if (a == 0):
				i = 0
				j = 0
				
			if (b == 0):
				k=0
				l=0
				
			if (a == 1):
				i=1
				j=1
				
			if (b == 1):
				k=1
				l=1
				
			if (a == 2):
				i=2
				j=2

			if (b == 2):
				k=2
				l=2
				
			#Green area
			if (a == 3):
				i=0
				j=1
				ip=1
				jp=2
				flaga= True

			if (b ==3):
				k=0
				l=1
				kp=1
				lp=2
				flagb= True	

			if (a == 4):
				i=1
				j=2
				ip=2
				jp=0
				flaga= True
	
			if (b == 4):
				k=1
				l=2
				kp=2
				lp=0
				flagb= True
	
			if (a == 5):
				i=0
				j=2
				ip=0
				jp=1
				flaga= True

			if (b == 5):
				k=0
				l=2
				kp=0
				lp=1
				flagb = True
			
			A_tensor4[i][j][k][l] = A_voigt4[a][b]
			#print "A_voigt4[",a ,"][", b, "] = " , "A_tensor4[", i, "][", j, "][", k, "][", l, "]" 
			#print A_tensor4[i][j][k][l], A_voigt4[a][b]
			#print "-------------------------------------------------------------------"
			
			if (flaga is True):
				if (flagb is True):
					A_tensor4[ip][jp][k][l]=A_voigt4[a][b]/2.
					A_tensor4[i][j][kp][lp]=A_voigt4[a][b]/2.
					A_tensor4[ip][jp][kp][lp]=A_voigt4[a][b]/2.
				else:
					A_tensor4[ip][jp][k][l]=A_voigt4[a][b]/(sqrt(2))

			elif(flagb is True):
					A_tensor4[i][j][kp][lp]=A_voigt4[a][b]/(sqrt(2))

				
					
	#Symmetry
	m = 0
	for i in range(len(A_tensor4)):
		for j in range(len(A_tensor4[i])):
			for k in range(len(A_tensor4[i][j])):
				for l in range(len(A_tensor4[i][j][k])):
					m = m + 1
					#print m, i,j,k,l, A_tensor4[i][j][k][l]
					try:	
						A_tensor4[i][j][l][k] = A_tensor4[i][j][k][l]
						#print A_tensor4[i][j][l][k], A_tensor4[i][j][k][l]
						A_tensor4[j][i][k][l] = A_tensor4[i][j][k][l]

						
						A_tensor4[k][l][i][j] = A_tensor4[i][j][k][l]
						A_tensor4[j][i][l][k] = A_tensor4[i][j][k][l]

					except:
						print "Couldn't apply symmetry"

	return A_tensor4



def generate_trans_matrix( init_base, final_base ):
	P = initTensor(0, 3, 3)
	for i in range(len(init_base)):
		for j in range(len(init_base)):
			#print "--------------------------"
			#print init_base[i], final_base[j]
			P[i][j] = vector_dot_vector( init_base[i], final_base[j] )
			#print i, j, P[i][j]
			
	return P

	
def vector_dot_vector( vectora, vectorb ):
	sumdot = 0
	for i in range(len(vectora)):
		sumdot = sumdot + vectora[i] * vectorb[i]
		#print vectora[i], " * ", vectorb[i]
	#print vectora, " times ", vectorb, " = ", sumdot
	return sumdot
	


#Generate a tensor, any order, any size
def initTensor(value, *lengths):
	list = []
	dim = len(lengths)
	if dim == 1:
		for i in range(lengths[0]):
			list.append(value)
	elif dim > 1:
		for i in range(lengths[0]):
			list.append(initTensor(value, *lengths[1:]))
	return list

#! Square matrix
def matrix_dot_matrix( matrixa, matrixb ):
	C = initTensor( 0, 3, 3)
	
	for i in range( len(matrixc) ):
		for j in range( len(matrixc)):
			for k in range( len( matrixa )):
				C[i][j] = C[i][j] + matrixa[i][k]*matrix[k][j]
	return C
			

def kronecker( i, j ):
	if ( i == j ):
		return 1
	else:
		return 0
	
	

def tensorial_base_change( P, tensorA ):
	tensorB = initTensor( 0, 3, 3, 3, 3)
	for m in range( len( tensorA[0][0][0] ) ):
		for n in range( len( tensorA[0][0][0] ) ):
			for o in range( len( tensorA[0][0][0] ) ):
				for p in range( len( tensorA[0][0][0] ) ):
					
					for i in range( len( tensorA[0][0][0] ) ):
						for j in range( len( tensorA[0][0][0] ) ):
							for k in range( len( tensorA[0][0][0] ) ):
								for l in range( len( tensorA[0][0][0] ) ):
									tensorB[m][n][o][p] = tensorB[m][n][o][p] + P[i][m]*P[j][n]*P[k][o]*P[l][p]*tensorA[i][j][k][l]
	return tensorB

def check_tensor_minor_symmetry( tensor ):
	for i in range(len(tensor[0][0][0])):
		for j in range(len(tensor[0][0][0])):
			for k in range(len(tensor[0][0][0])):
				for l in range(len(tensor[0][0][0])):
					
					if (tensor[i][j][k][l] != tensor[j][i][k][l]):
						print "[check_tensor_minor_symmetry] Tensor is not symmetrical "
						print i,j,k,l, tensor[i][j][k][l], tensor[j][i][k][l]
						return False
						
					if (tensor[i][j][k][l] != tensor[i][j][l][k]):
						print "[check_tensor_minor_symmetry] Tensor is not symmetrical "
						print i,j,k,l, tensor[i][j][k][l], tensor[i][j][l][k]
						return False
						
					if (tensor[i][j][k][l] != tensor[j][i][l][k]):
						print "[check_tensor_minor_symmetry] Tensor is not symmetrical "
						print i,j,k,l, tensor[i][j][k][l], tensor[j][i][l][k]
						return False
	return True


def check_tensor_major_symmetry( tensor ):
	for i in range(len(tensor[0][0][0])):
		for j in range(len(tensor[0][0][0])):
			for k in range(len(tensor[0][0][0])):
				for l in range(len(tensor[0][0][0])):
					
					if (tensor[i][j][k][l] != tensor[k][l][i][j]):
						print "[check_tensor_major_symmetry] Tensor is not symmetrical "
						print i,j,k,l, tensor[i][j][k][l], tensor[k][l][i][j]
						return False
	return True
						

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

