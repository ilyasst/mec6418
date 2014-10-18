from numpy import *
from tensor_personal_functions import *

#Tenseur alternateur
def generate_epsilon_ijk():
	epsilon_ijk = initTensor( 0, 3, 3, 3)
	
	for i in range(0, len(epsilon_ijk) ):
		for j in range(0, len(epsilon_ijk[0]) ):
			for k in range(0, len(epsilon_ijk[0][0]) ):
				
				if (i == j) or (j == k) or (i == k):
					epsilon_ijk[i][j][k] = 0
				if (`i`+`j`+`k` == "012") or (`i`+`j`+`k` == "120") or (`i`+`j`+`k` == "201"):
					epsilon_ijk[i][j][k] = 1
				if (`i`+`j`+`k` == "021") or (`i`+`j`+`k` == "102") or (`i`+`j`+`k` == "210"):
					epsilon_ijk[i][j][k] = -1
			
	return epsilon_ijk

	
def kronecker( i, j ):
	if ( i == j ):
		return 1.
	else:
		return 0.
		
def generate_I_tensor4():
	I_tensor4 = initTensor(0., 3, 3, 3, 3)
	for i in range( len( I_tensor4[0][0][0] ) ):
		for j in range( len( I_tensor4[0][0][0] ) ):
			for k in range( len( I_tensor4[0][0][0] ) ):
				for l in range( len( I_tensor4[0][0][0] ) ):
					I_tensor4[i][j][k][l]=(1./2.)*( kronecker(i,k)*kronecker(j,l)+kronecker(i,l)*kronecker(j,k) )
					
	return I_tensor4
	
def generate_J_tensor4():
	J_tensor4 = initTensor(0., 3, 3, 3, 3)
	for i in range( len( J_tensor4[0][0][0] ) ):
		for j in range( len( J_tensor4[0][0][0] ) ):
			for k in range( len( J_tensor4[0][0][0] ) ):
				for l in range( len( J_tensor4[0][0][0] ) ):
					J_tensor4[i][j][k][l]=(1./3.)*kronecker(i,j)*kronecker(k,l)
	return J_tensor4
	
def generate_K_tensor4():
	I_tensor4 = generate_I_tensor4()
	J_tensor4 = generate_J_tensor4()
	K_tensor4 = initTensor(0., 3, 3, 3, 3)
	for i in range( len( K_tensor4[0][0][0] ) ):
		for j in range( len( K_tensor4[0][0][0] ) ):
			for k in range( len( K_tensor4[0][0][0] ) ):
				for l in range( len( K_tensor4[0][0][0] ) ):
					K_tensor4[i][j][k][l]= (I_tensor4[i][j][k][l]-J_tensor4[i][j][k][l])
	return K_tensor4
	