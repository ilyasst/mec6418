from projectors_personal_functions import *
from import_data import *
from convenient_objects import *
from hmgnzt_personal_functions import *



zeta_csv = import_hmgnzt_quad( "zeta3_4points.csv" )
omega_csv = import_hmgnzt_quad( "omega_512points.csv" )

I_tensor4 = generate_I_tensor4()
I_matrix = tensor4_to_voigt4( I_tensor4 )

J_tensor4 = generate_J_tensor4()
J_matrix = tensor4_to_voigt4( J_tensor4 )

K_tensor4 = generate_K_tensor4()
K_matrix = tensor4_to_voigt4( K_tensor4 )

print
print "Getting materials' properties..."
E0 = 3000.
nu0 = 0.3
E1 = 70000.
nu1 = 0.3

v0 = 0.7
v1 = 1. - v0

k0 = E0/(3.*(1. - 2.*nu0))
mu0 = E0/(2.*(.1 + nu0))
C0_tensor4 = dot( 3.*k0, J_tensor4 ) + dot( 2.*mu0, K_tensor4 )
C0_matrix = tensor4_to_voigt4( C0_tensor4 )
print
print "C0_matrix:"
for i in range(0, len(C0_matrix)):
	print C0_matrix[i]
	

k1 = E1/(3.*(1. - 2.*nu1)) 
mu1 = E1/(2.*(1. + nu1)) 
C1_tensor4 = dot( 3.*k1, J_tensor4 ) + dot( 2.*mu1, K_tensor4 )
C1_matrix = tensor4_to_voigt4( C1_tensor4 )
print
print "C1_matrix:"
for i in range(0, len(C1_matrix)):
	print C1_matrix[i]