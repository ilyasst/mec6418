from projectors_personal_functions import *
from import_data import *
from convenient_objects import *
from hmgnzt_personal_functions import *



I_tensor4 = generate_I_tensor4()
I_matrix = tensor4_to_voigt4( I_tensor4 )

J_tensor4 = generate_J_tensor4()
J_matrix = tensor4_to_voigt4( J_tensor4 )

K_tensor4 = generate_K_tensor4()
K_matrix = tensor4_to_voigt4( K_tensor4 )

k = 1.
mu = 1.

print
print "==========================================================================="
print "==========================================================================="
print " Problem 07-01 "
print "==========================================================================="

C_tensor4 = dot( 3.*k, J_tensor4 ) + dot( 2.*mu, K_tensor4 )
C_matrix = tensor4_to_voigt4( C_tensor4 )
print
print "C_matrix:"
for i in range(0, len(C_matrix)):
	print C_matrix[i]

print
S_eshelby_th_tensor4 = dot( (3.*k/(3.*k+4.*mu) ), J_tensor4 ) + dot( (6.*(k + 2.*mu)/(5.*(3.*k + 4.*mu))), K_tensor4 )
S_eshelby_th_matrix = tensor4_to_voigt4( S_eshelby_th_tensor4 )
print
print "S_eshelby_th:"
print "This is the theoretical Eshelby tensor for spherical inclusions (known):"
for i in range(0, len(S_eshelby_th_matrix)):
	print S_eshelby_th_matrix[i]
	
print 
print "Let's now check if we find the same value by computing it ourselves"
a = [ 1. , 1. , 1. ]
print "a = ", a
zeta_csv = import_hmgnzt_quad( "zeta3_4points.csv" )
omega_csv = import_hmgnzt_quad( "omega_32points.csv" )


S_eshelby_quad_tensor4 = generate_eshelby_tensor( a, C_tensor4, zeta_csv, omega_csv )
S_eshelby_quad_tensor4 = clean_S_eshelby(S_eshelby_quad_tensor4)
S_eshelby_quad_matrix = tensor4_to_voigt4( S_eshelby_quad_tensor4 )

print 
print "S_eshelby_quad_matrix for zeta3 = 4, omega = 32:"
for i in range(0, len(S_eshelby_quad_matrix)):
	print S_eshelby_quad_matrix[i]

print 
print "----------------------------------------------------------------------------"
print "Fiber aligned along x3"
print "----------------------------------------------------------------------------"
print 

zeta_csv = import_hmgnzt_quad( "zeta3_4points.csv" )
omega_csv = import_hmgnzt_quad( "omega_512points.csv" )	

a = [ 1. , 1. , 10E4 ]
print "a = ", a

S_eshelby_quad_tensor4 = generate_eshelby_tensor( a, C_tensor4, zeta_csv, omega_csv )
S_eshelby_quad_tensor4 = clean_S_eshelby(S_eshelby_quad_tensor4)
S_eshelby_quad_matrix = tensor4_to_voigt4( S_eshelby_quad_tensor4 )

print 
print "S_eshelby_quad_matrix for zeta3 = 4, omega = 512, a = ", a, ":"
for i in range(0, len(S_eshelby_quad_matrix)):
	print S_eshelby_quad_matrix[i]