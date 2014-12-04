from projectors_personal_functions import *
from import_data import *
from convenient_objects import *
from hmgnzt_personal_functions import *
from numpy.linalg import inv


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

print
print "a ="
a = [ 1., 1., 1E4 ]
print a

k0 = E0/(3.*(1. - 2.*nu0))
mu0 = E0/(2.*(1. + nu0))
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
	
print
print "---------------------------------------------------------------------------"
	
Cvoigt_matrix = voigt_hmgnzt_2phases(v0, k0, k1, mu0, mu1 )
print
print "Cvoigt_matrix:"
for i in range(0, len(C0_matrix)):
	print Cvoigt_matrix[i]
Svoigt_matrix = inv( Cvoigt_matrix )
print
print "Svoigt_matrix:"
for i in range(0, len(Svoigt_matrix)):
	print Svoigt_matrix[i]

print
print "---------------------------------------------------------------------------"

Creuss_matrix = reuss_hmgnzt_2phases(v0, k0, k1, mu0, mu1 )
print
print "Creuss_matrix:"
for i in range(0, len(C0_matrix)):
	print Creuss_matrix[i]
Sreuss_matrix = inv( Creuss_matrix )
print
print "Sreuss_matrix:"
for i in range(0, len(Sreuss_matrix)):
	print Sreuss_matrix[i]
	
print
print "---------------------------------------------------------------------------"
	
C_MT_matrix = mori_tanaka( a, v0, C0_tensor4, C1_tensor4, zeta_csv, omega_csv )
C_MT_tensor4 = voigt4_to_tensor4( C_MT_matrix )
print
print "C_MT_matrix:"
for i in range(0, len(C_MT_matrix)):
	print C_MT_matrix[i]
S_MT_matrix = inv( C_MT_matrix )
print
print "S_MT_matrix:"
for i in range(0, len(S_MT_matrix)):
	print S_MT_matrix[i]
	
print
print "---------------------------------------------------------------------------"
print
print "Comparing results:"
print
print "E11: "
print "MT		", "Voigt		", "Reuss"
print 1./S_MT_matrix[0][0], 1./Svoigt_matrix[0][0], 1./Sreuss_matrix[0][0]
print
print "E22: "
print "MT		", "Voigt		", "Reuss"
print 1./S_MT_matrix[1][1], 1./Svoigt_matrix[1][1], 1./Sreuss_matrix[1][1]
print
print "E33: "
print "MT		", "Voigt		", "Reuss"
print 1./S_MT_matrix[2][2], 1./Svoigt_matrix[2][2], 1./Sreuss_matrix[2][2]
print
print "Gl: "
print "MT		", "Voigt		", "Reuss"
print 1./(2.*S_MT_matrix[3][3]), 1./(2.*Svoigt_matrix[3][3]), 1./(2.*Sreuss_matrix[3][3])
print
print "mu_l: "
print "MT		", "Voigt		", "Reuss"
print -S_MT_matrix[0][2]/(S_MT_matrix[2][2]), -Svoigt_matrix[0][2]/(Svoigt_matrix[2][2]), -Sreuss_matrix[0][2]/(Sreuss_matrix[2][2])
print
print "mu_t: "
print "MT		", "Voigt		", "Reuss"
print -S_MT_matrix[0][1]/(S_MT_matrix[1][1]), -Svoigt_matrix[0][1]/(Svoigt_matrix[1][1]), -Sreuss_matrix[0][1]/(Sreuss_matrix[1][1])
