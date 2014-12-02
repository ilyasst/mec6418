from projectors_personal_functions import *

J_tensor4 = generate_J_tensor4()
J_matrix = tensor4_to_voigt4( J_tensor4 )

K_tensor4 = generate_K_tensor4()
K_matrix = tensor4_to_voigt4( K_tensor4 )

k = 1.
mu = 1.
C_tensor4 = dot( 3,dot(k,J_tensor4) ) + dot(2,dot(mu,K_tensor4))
C_matrix = tensor4_to_voigt4(C_tensor4)

print
print "C_matrix:"
for i in range(0, len(C_matrix)):
	print C_matrix[0]

print
S_eshelby_th_tensor4 = dot( (3.*k/(3.*k+4.*mu) ), J_tensor4 ) + dot( (6.*(k + 2.*mu)/(5.*(3.*k + 4.*mu))), K_tensor4 )
S_eshelby_th_matrix = tensor4_to_voigt4( S_eshelby_th_tensor4 )
print "S_eshelby_th:"
print "This is the theoretical Eshelby tensor for spherical inclusions (known):"
for i in range(0, len(S_eshelby_th_matrix)):
	print S_eshelby_th_matrix[0]
	
print 
print "Let's now check if we find the same value by computing it ourselves"
a = [ 1. , 1. , 1. ]
S_eshelby_quad_tensor4 = generate_eshelby_tensor( a, C_tensor4, zeta, omega )







def generate_eshelby_tensor( a, C_tensor4, zeta, omega ):
	