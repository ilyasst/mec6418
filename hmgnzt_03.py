from import_data import *
from hmgnzt_personal_functions import *
from tensor_personal_functions import *
from projectors_personal_functions import *
from numpy import *

def problem07_03_transverse_case():
	zeta_csv = import_hmgnzt_quad( "zeta3_8points.csv" )
	omega_csv = import_hmgnzt_quad( "omega_64points.csv" )
	
	print 
	print "Transverse isotropy"
	print
	
	J_tensor4 = generate_J_tensor4()
	J_matrix = tensor4_to_voigt4( J_tensor4 )

	K_tensor4 = generate_K_tensor4()
	K_matrix = tensor4_to_voigt4( K_tensor4 )

	E0 = 3000.
	nu0 = 0.3
	E1 = 70000.
	nu1 = 0.3
	
	v0 = 0.7
	v1 = 1. - v0 
	
	k0 = E0/(3.*(1. - 2.*nu0)) 
	mu0 = E0/(2.*(1. + nu0)) 
	C0_tensor4 = dot( 3.*k0, J_tensor4 ) + dot( 2.*mu0, K_tensor4 )
	C0_matrix = tensor4_to_voigt4( C0_tensor4 )
	print
	print "C0_matrix:"
	for i in range(0, len(C0_matrix)):
		print C0_matrix[i]
	
	
	k1 = E1/(3.*(1 - 2.*nu1)) 
	mu1 = E1/(2.*(1. + nu1)) 
	C1_tensor4 = dot( 3.*k1, J_tensor4 ) + dot( 2.*mu1, K_tensor4 )
	C1_matrix = tensor4_to_voigt4( C1_tensor4 )
	print
	print "C1_matrix:"
	for i in range(0, len(C1_matrix)):
		print C1_matrix[i]
	
	#Mori Tanaka is necessary for C0
	a = [ 1., 1., 1E4 ]
	C_MT_matrix = mori_tanaka( a, v0, C0_tensor4, C1_tensor4, zeta_csv, omega_csv )
	C_MT_tensor4 = voigt4_to_tensor4( C_MT_matrix )
	print
	print "C_MT_matrix:"
	for i in range(0, len(C_MT_matrix)):
		print C_MT_matrix[i]
	
	#AC scheme
	tolerance = 1E-5
	max_iter = 1000
	
	#Initial value C0 = C_MT
	C_matrix = C_MT_matrix
	C_tensor4 = C_MT_tensor4
	C_temp_tensor4 = initTensor( 0., 3, 3, 3, 3 )
	C_temp_matrix = tensor4_to_voigt4( C_temp_tensor4 )
	C_list = []
	
	I_tensor4 = generate_I_tensor4()
	I_matrix = tensor4_to_voigt4( I_tensor4 )
	
	C_difference = initTensor( 0., 6, 6 )
	C_fixed_difference = initTensor( 0., 6, 6 )
	
	for k in range( 0, max_iter ):
		
		for i in range(0, len(C0_matrix)):
			for j in range(0, len(C0_matrix)):
				C_difference[i][j] = C1_matrix[i][j] - C_matrix[i][j]
				
		for i in range(0, len(C0_matrix)):
			for j in range(0, len(C0_matrix)):
				C_fixed_difference[i][j] = C1_matrix[i][j] - C0_matrix[i][j]
		
		C_tensor4 = voigt4_to_tensor4( C_matrix )
		S_eshelby_tensor = generate_eshelby_tensor( a, C_tensor4, zeta_csv, omega_csv )
		S_eshelby_matrix = tensor4_to_voigt4( S_eshelby_tensor )
		
		Ar_matrix = inv( I_matrix + dot( S_eshelby_matrix, dot( inv(C_matrix), C_difference ) ) )
	
		C_temp_matrix = C0_matrix + dot( v1 ,dot( C_difference, Ar_matrix ) )
		
		C_list.append( C_temp_matrix )
		C_matrix = C_temp_matrix
		
		if k > 1:
			print "Iteration:", len(C_list)
			error_0 = 0.
			error_1 = 0.
			norm_C_matrix = 0.
			for i in range(0, len(C_matrix)):
				for j in range(0, len(C_matrix[0])):
					error_0 = error_0 + pow( C_list[k][i][j] - C_list[k-1][i][j], 2) 
					error_1 = error_1 + pow( C_list[k][i][j] - C_list[k-1][i][j], 2) 
					norm_C_matrix = norm_C_matrix + pow( C_matrix[i][j] , 2 )
			error_0 = sqrt( error_0 )
			error_1 = sqrt( error_1 )
			norm_C_matrix = sqrt( norm_C_matrix )
			error_1 = error_1/norm_C_matrix
			print "Error 0:", error_0
			print "Error 1:", error_1
					
			if error_0 < tolerance and error_1 < tolerance:
				print
				print "Convergence reached (normalized) !"
				break
			
	print
	print "Auto-coherent scheme done !"
	print
	C_AC_matrix = clean_matrix( C_matrix )
	print "C_AC_Matrix:"
	for i in range(0, len(C_AC_matrix)):
		print C_AC_matrix[i]
			
			
			
		
		
		
	

def problem07_03_isotropic_case():
	zeta_csv = import_hmgnzt_quad( "zeta3_4points.csv" )
	omega_csv = import_hmgnzt_quad( "omega_32points.csv" )
	print 
	print "Isotropic Case"
	print

	E0 = 3000.
	nu0 = 0.3
	E1 = 70000.
	nu1 = 0.3

	v0 = 0.7
	v1 = 1. - v0 

	x = []
	k0 = E0/(3.*(1. - 2.*nu0)) 
	x.append( k0 )
	mu0 = E0/(2.*(1. + nu0)) 
	x.append( mu0 )
	k1 = E1/(3.*(1 - 2.*nu1)) 
	mu1 = E1/(2.*(1. + nu1)) 

	tolerance = 1E-3
	max_iter = 1000 

	J_tensor4 = generate_J_tensor4()
	J_matrix = tensor4_to_voigt4( J_tensor4 )

	K_tensor4 = generate_K_tensor4()
	K_matrix = tensor4_to_voigt4( K_tensor4 )

	C_tensor4 = []
	S_eshelby_tensor4 = []
	x_list = []
	for k in range(0, max_iter):
		x_temp = []
		C_tensor4.append( dot( 3.*x[0], J_tensor4) + dot( 2.*x[1], K_tensor4 ) ) 

		S_eshelby_tensor4.append( dot( (3.*x[0]/(3*x[0]+4.*x[1])), J_tensor4 ) + dot( (6*(x[0] + 2.*x[1])/(5.*(3.*x[0] + 4.*x[1]))), K_tensor4 ) )
		S_eshelby_matrix = tensor4_to_voigt4( S_eshelby_tensor4[k] )
		alpha_eshelby, beta_eshelby = extract_isotropic_parameters( S_eshelby_matrix )
		
		x_temp.append( k0 + v1*(x[0]*(k1 - k0))/(x[0] + alpha_eshelby*(k1 - x[0])) )
		x_temp.append( mu0 + v1*(x[1]*(mu1 - mu0))/(x[1] + beta_eshelby*(mu1 - x[1])) )
		x_list.append( x_temp )
		
		x[0] = x_temp[0]
		x[1] = x_temp[1]
		
		if k > 1:
			error_0 = sqrt( pow( x_list[k][0], 2) - pow( x_list[k-1][0], 2) )
			error_1 = sqrt( pow( x_list[k][1], 2) - pow( x_list[k-1][1], 2) )
			
			if error_0 < tolerance or error_1 < tolerance:
				print
				print "Convergence reached !"
				break

	print
	print "Iterations:", len(x_list)
	print 
	print "k	", "mu		"
	for i in range(0, len(x_list)):
		print x_list[i][0], x_list[i][1]
	print 


#problem07_03_isotropic_case()	
problem07_03_transverse_case()