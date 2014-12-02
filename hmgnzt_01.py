from projectors_personal_functions import *
from import_data import *


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

zeta_csv = import_hmgnzt_quad( "zeta3_4points.csv" )
omega_csv = import_hmgnzt_quad( "omega_32points.csv" )

S_eshelby_quad_tensor4 = generate_eshelby_tensor( a, C_tensor4, zeta_csv, omega_csv )




def generate_eshelby_tensor( a, C_tensor4, zeta_csv, omega_csv ):
	
	zetas = determining_zetas( zeta_csv, omega_csv )
	
def determining_zetas( zeta_csv, omega_csv ):

	zeta_3 = initTensor( 0., len( zeta_csv), len(omega_csv) )
	for i in range(0, len( zeta_csv) ):
		for j in range(0, len(omega_csv) ):
			zeta_3[i][j] = zeta_csv[i][0]
			print 
	
#q = length(omega_xls) ;
#p = length(zeta_xls) ;
#zeta3 = zeros(p,1,q);
#for pp = 1:p
    #for qq = 1:q
        #zeta3(pp,1,qq) = Zeta3(pp,1) ; 
    #end
#end