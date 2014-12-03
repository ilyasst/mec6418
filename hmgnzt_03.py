from import_data import *
from hmgnzt_personal_functions import *
from tensor_personal_functions import *
from projectors_personal_functions import *
from numpy import *




zeta_csv = import_hmgnzt_quad( "zeta3_4points.csv" )
omega_csv = import_hmgnzt_quad( "omega_32points.csv" )

E0 = 3.
nu0 = 0.3
E1 = 70.
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

tolerance = 1E-5 
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
	