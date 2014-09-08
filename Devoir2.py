from numpy import *


#Takes A_voigt(6,6) gives back A_tensor(4,4,4,4)
def voigt4_to_tensor4( A_voigt4 ):
	
	#A_tensor4 = [ [ [ [ 0 for l in range(3)] for k in range(3)] for i in range(3) ] for j in range(5) ]
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
				ip=0
				jp=1
				flaga= True

			if (b ==3):
				k=0
				l=1
				kp=0
				lp=1
				flagb= True	

			if (a == 4):
				i=1
				j=2
				ip=1
				jp=2
				flaga= True
	
			if (b == 4):
				k=1
				l=2
				kp=1
				lp=2
				flagb= True
	
			if (a == 5):
				i=0
				j=2
				ip=0
				jp=2
				flaga= True

			if (b == 5):
				k=0
				l=2
				kp=0
				lp=2
				flagb = True
			
			A_tensor4[i][j][k][l] = A_voigt4[a][b]
			print "A_voigt4[",a ,"][", b, "] = " , "A_tensor4[", i, "][", j, "][", k, "][", l, "]" 
			print A_tensor4[i][j][k][l], A_voigt4[a][b]
			print "-------------------------------------------------------------------"
			
			if (flaga is True):
				if (flagb is True):
					A_tensor4[ip][jp][k][l]=A_voigt4[a][b]/2.
					A_tensor4[i][j][kp][lp]=A_voigt4[a][b]/2.
					A_tensor4[ip][jp][kp][lp]=A_voigt4[a][b]/2.
				else:
					A_tensor4[ip][jp][k][l]=A_voigt4[a][b]/(sqrt(2))

			else:
				if (flagb is True):
					A_tensor4[i][j][kp][lp]=A_voigt4[a][b]/(sqrt(2))
					
	#Symmetry
	m = 0
	for i in range(len(A_tensor4)):
		for j in range(len(A_tensor4[i])):
			for k in range(len(A_tensor4[i][j])):
				for l in range(len(A_tensor4[i][j][k])):
					m = m + 1
					print m, i,j,k,l, A_tensor4[i][j][k][l]
					try:	
						A_tensor4[i][j][l][k] = A_tensor4[i][j][k][l]
						A_tensor4[j][i][k][l] = A_tensor4[i][j][k][l]
					except:
						print "Couldn't apply symmetry"

	return A_tensor4


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
	
	
A_voigt4 = [ [ 0.241, -0.202, -0.347, -0.848, 0.959, -0.023 ],
	     [ -0.202, -0.678, 0.520, -0.600, 0.186, 0.861],
	     [ -0.347, 0.520, 0.200, -0.473, -0.598, -0.927],
	     [ -0.848, -0.600, -0.473, -0.214, -0.338, 0.201],
	     [ 0.959, 0.186, -0.598, -0.338, 0.276, -0.392],
	     [ -0.023, 0.861, -0.927, 0.201, -0.392, -0.719]
	     ]

voigt4_to_tensor4( A_voigt4 )

