import numpy as np
import math

# C and rho should be lists
def CtoS_interconversion1D( C, rho ):
	# Compute the internal matrices associated with the relaxation modulus
	N = len( rho )
	
	#2
	L1 = 0
	for Ci in C :
		L1 = L1 + Ci
	print "(1) 	L = %s" % L1
	print "(1th) 	L = %s" % 17
	
	#3
	l = np.zeros(shape=(1, N))
	for index in xrange( 0, N ) :
		l[ 0, index ] = math.sqrt( C[ index +1 ]*rho[ index ] )
	print "(2) 	l = %s" % l
	print "(2th) 	l = [", math.sqrt(6) , "," , 2./math.sqrt(35) ,"]"

	#4 
	L = np.zeros(shape=(N, N))
	for j in xrange( 0, N ):
		L[j, j] = rho[j]
	print "(3) 	L = %s" % L
	print "(3th) 	L = [[2 , 0] , [0, ", 1/35. ,"]]"

	#5
	B = np.identity(N)
	print "(4) 	B = %s" % B

	# Compute the internal matrices associated with the creep compliance
	#7
	A1 = 1/L1
	print "(7) 	A1 = %s" % A1
	print "(7th) 	A1 = %s" % (1/17.)

	#8
	a = ( np.dot( l.transpose(), A1 ) ).transpose()
	print "(8) 	a = %s" % a
	print "(8th) 	a = %s" % "[", math.sqrt(6)/17. ,",", 2./(17*math.sqrt(35) ) ,"]" 

	lxl = np.zeros(shape=(N, N))
	for k in xrange(0, N ):
		for q in xrange( 0, N):
			lxl[ k, q ] = l[ 0, k ] * l[ 0, q ]
	#9
	A = L - A1*( lxl )
	print "(9) 	A = %s" % A 
	print "(9th) 	A = [[ ", 28./17. ,",", -2./17.*math.sqrt( 6./35. ) ," ], [", -2./17*math.sqrt( 6./35. ) ,",", 13./595. , "]]" 

	# Diagonalization : 
	# Compute the eigenvectores P and eigenvalues D of A with singular value decomposition
	D, P = np.linalg.eigh( A )
	print "(11) 	P = %s and D = %s" % ( P, D )
	print "(11th) 	P = [[ -0.02993, -0.9996 ], [-0.9996, 0.02993]]"

	#12
	Astar = np.dot( np.dot( P.transpose(), A ) , P )
	print "(12) 	A* = %s" % Astar
	print "(12th) 	A* = [[ 0.0204, 0 ], [ 0, 1.649 ]]"
	#13
	astar = ( np.dot( P.transpose(), a.transpose() ) ).transpose()
	print "(13) 	a* = %s" % astar
	print "(13th) 	a* = [ -0.0242, -0.1434 ]"

	#14
	S0 = A1
	print "(14) S0 = %s " % S0
	S = [ S0 ]
	Lambda = []
	for m in xrange( 0, N ):
		print "m=%s" % m
		Sm = pow( astar[ 0, m ], 2 ) / Astar[ m, m ]
		print "(17)(m=%s) Sm = %s " % ( m, Sm )
		S.append( Sm )
		Lambdam = Astar[ m, m ] / B[ m, m ]
		print "(17)(m=%s) Lambdam = %s " % ( m, Lambdam )
		Lambda.append( Lambdam )

	return { "S" : S, "Lambda" : Lambda }

def StoC_interconversion1D( S, Lambda ):
	# Compute the internal matrices associated with the relaxation modulus
	M = len( Lambda )
	#2
	A1 = S[0]
	
	#3
	a = np.zeros(shape=(1, M))
	for index in range( 1, M ) :
		a[ 0, index ] = math.sqrt( Lambda[index-1]*S[index] )
	#print "(3) a = %s" % a
	#print "(3th) 	a = %s" % "[", math.sqrt(6)/17. ,",", 2./(17*math.sqrt(35) ) ,"]" 

	#4 
	A = np.zeros(shape=(M, M))
	for j in xrange( 0, M ):
		A[j, j] = Lambda[j]
	#print "(4) 	A = %s" % A
	#print "(4th) 	A = [[ ", 28./17. ,",", -2./17.*math.sqrt( 6./35. ) ," ], [", -2./17*math.sqrt( 6./35. ) ,",", 13./595. , "]]" 

	#5
	B = np.identity(M)
	#print "(4) 	B = %s" % B

	# Compute the internal matrices associated with the relaxation modulus
	#7
	L1 = 1/A1
	#print "(7) 	L1 = %s" % L1

	#8
	l = ( a.transpose()*L1 ).transpose()
	#print "(8) 	l = %s" % l

	axa = np.zeros(shape=(M, M))
	for k in xrange(0, M ):
		for q in xrange( 0, M):
			axa[ k, q ] = a[ 0, k ] * a[ 0, q ]
	#9
	L = A + L1*( axa )
	#print "(9) 	A = %s" % A 

	# Diagonalization : 
	# Compute the eigenvectores P and eigenvalues D of A with singular value decomposition
	D, P = np.linalg.eigh( L )
	#print "(11) 	P = %s and D = %s" % ( P, D )

	#12
	Lstar = np.dot( np.dot( P.transpose(), L ) , P )
	#print "(12) 	L* = %s" % Lstar
	#13
	lstar = ( np.dot( P.transpose(), l.transpose() ) ).transpose()
	#print "(13) 	l* = %s" % lstar

    	C0 = L1
	C = [ ]

	rho = []
	for m in xrange( 0, M ):
		Cm = pow( lstar[ 0, m ], 2 ) / Lstar[ m, m ]
		#print "(17)(m=%s) Cm = %s " % ( m, Cm )
		C.append( Cm )
		rhom = Lstar[ m, m ] / B[ m, m ]
		#print "(17)(m=%s) rhom = %s " % ( m, rhom )
		rho.append( rhom )
		
	#15
	for Ci in C :
		C0 = C0 - Ci
	C[0] = C0
	#print "(15) 	C0 = %s" % C0

	return { "C" : C, "rho" : rho }

# C = [ 
# 	10.,
# 	3.,
# 	4. 
# ]
# 
# rho = [
# 	2.,
# 	1/35.
# ]

#C = [ 
	#10.,
	#2.,
	#5. 
#]

#rho = [
	#1.,
	#10.
#]

#retour = CtoS_interconversion1D( C, rho )
#S = retour[ "S" ]
#Lambda = retour[ "Lambda" ]
#print "S is : %s \nLambda is : %s" % ( S, Lambda )

# Sprime = [
# 	0.0588,
# 	0.0287,
# 	0.01248
# ]
# Lambdaprime = [
# 	0.0204,
# 	1.649
# ]
# 
# retour_inverse = StoC_interconversion1D( Sprime, Lambdaprime )
# Cretour = retour_inverse[ "C" ]
# rhoRetour = retour_inverse[ "rho" ]
# print "C & rho RETURNS : %s ; %s" % ( Cretour, rhoRetour )
