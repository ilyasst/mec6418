from projectors_personal_functions import *
from import_data import *
from convenient_objects import *



def generate_eshelby_tensor( a, C_tensor4, zeta_csv, omega_csv ):
	zetas = determining_zetas( zeta_csv, omega_csv )
	xis = determining_xis( a, zetas, len(zeta_csv), len(omega_csv) )
	K_eshelby = determining_K_eshelby( C_tensor4, xis, len(zeta_csv), len(omega_csv) )
	N_eshelby = determining_N_eshelby( K_eshelby, len(zeta_csv), len(omega_csv) )

def determining_N_eshelby( K_eshelby, len_zeta_csv, len_omega_csv ):
	N_eshelby = initTensor( 0., 3, 3, len_zeta_csv, len_omega_csv )
	for i in range(0, 3):
#Nf(Ke,p,q)
#y = zeros(3,3,p,q);
#for i = 1:3
    #for j = 1:3
        #for pp = 1:p
            #for qq = 1:q
                #for k = 1:3
                    #for l = 1:3
                        #for m = 1:3
                            #for n = 1:3
                                #y(i,j,pp,qq) = y(i,j,pp,qq) +...
                                    #0.5*eps(i,k,l)*eps(j,m,n)*...
                                    #Ke(k,m,pp,qq)*Ke(l,n,pp,qq) ;
                            #end
                        #end
                    #end
                #end
            #end
        #end
    #end
#end

def determining_K_eshelby( C_tensor4, xis, len_zeta_csv, len_omega_csv ):
	K = initTensor( 0., 3, 3, len_zeta_csv, len_omega_csv )
	for i in range(0, 3):
		for k in range(0, 3):
			for m in range(0, len_zeta_csv):
				for n in range(0, len_omega_csv):
					for j in range(0, 3):
						for l in range(0, 3):
							K[i][k][m][n] = K[i][k][m][n] + C_tensor4[i][j][k][l]*xis[j][m][n]*xis[l][m][n]
	return K


def determining_xis( a, zetas, len_zeta_csv, len_omega_csv ):
	xi_1 = initTensor( 0., len_zeta_csv, len_omega_csv )
	for i in range(0, len_zeta_csv):
		for j in range(0, len_omega_csv):
			xi_1[i][j] = zetas[0][i][j]/a[0]

	xi_2 = initTensor( 0., len_zeta_csv, len_omega_csv )
	for i in range(0, len_zeta_csv):
		for j in range(0, len_omega_csv):
			xi_2[i][j] = zetas[1][i][j]/a[1]
			
	xi_3 = initTensor( 0., len_zeta_csv, len_omega_csv )
	for i in range(0, len_zeta_csv):
		for j in range(0, len_omega_csv):
			xi_3[i][j] = zetas[2][i][j]/a[2]

	xis = []
	xis.append( xi_1 )
	xis.append( xi_2 )
	xis.append( xi_3 )
	return xis

def determining_zetas( zeta_csv, omega_csv ):
	
	zeta_3 = initTensor( 0., len( zeta_csv), len(omega_csv) )
	for i in range(0, len( zeta_csv) ):
		for j in range(0, len(omega_csv) ):
			zeta_3[i][j] = zeta_csv[i][0]
			
	zeta_1 = initTensor( 0., len( zeta_csv), len(omega_csv) )
	for i in range(0, len( zeta_csv) ):
		for j in range(0, len(omega_csv) ):
			zeta_1[i][j] = sqrt( 1. - pow( zeta_3[i][j], 2 ) )* cos( omega_csv[i][0] )
			
	zeta_2 = initTensor( 0., len( zeta_csv), len(omega_csv) )
	for i in range(0, len( zeta_csv) ):
		for j in range(0, len(omega_csv) ):
			zeta_2[i][j] = sqrt( 1. - pow( zeta_3[i][j], 2 ) )* sin( omega_csv[i][0] )
	
	zetas = []
	zetas.append( zeta_1 )
	zetas.append( zeta_2 )
	zetas.append( zeta_3 )
	return zetas






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

