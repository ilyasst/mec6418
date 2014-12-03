from projectors_personal_functions import *
from import_data import *
from convenient_objects import *




def generate_eshelby_tensor( a, C_tensor4, zeta_csv, omega_csv ):
	zetas = determining_zetas( zeta_csv, omega_csv )
	xis = determining_xis( a, zetas, len(zeta_csv), len(omega_csv) )
	print
	print "Retrieving data from xls files..."
	K_eshelby = determining_K_eshelby( C_tensor4, xis, len(zeta_csv), len(omega_csv) )
	print "Determining K_eshelby..."
	N_eshelby = determining_N_eshelby( K_eshelby, len(zeta_csv), len(omega_csv) )
	print "Determining N_eshelby..."
		
	D_eshelby = determining_D_eshelby( K_eshelby, len(zeta_csv), len(omega_csv) )
	print "Determining D_eshelby..."
	G_eshelby = determining_G_eshelby( xis, N_eshelby, D_eshelby, len(zeta_csv), len(omega_csv) )
	print "Determining G_eshelby..."
	W_eshelby = determining_W_eshelby( zeta_csv, omega_csv, len(zeta_csv), len(omega_csv) )
	print "Determining W_eshelby..."

	S_eshelby = initTensor( 0., 3, 3, 3, 3 )

	for i in range(0, 3):
		for j in range(0, 3):
			for k in range(0, 3):
				for l in range(0, 3):
					for o in range(0, len(zeta_csv)):
						for p in range(0, len(omega_csv) ):
							for m in range(0, 3):
								for n in range(0,3):
									S_eshelby[i][j][k][l] = S_eshelby[i][j][k][l] + (C_tensor4[m][n][k][l]/(8.*pi)) * ( G_eshelby[i][m][j][n][o][p] + G_eshelby[j][m][i][n][o][p] ) * W_eshelby[o][p]
	return S_eshelby
	
	
def clean_S_eshelby(S_eshelby):
	for i in range(0, 3):
		for j in range(0, 3):
			for k in range(0, 3):
				for l in range(0, 3):
					if abs( S_eshelby[i][j][k][l] ) < 0.01:
						S_eshelby[i][j][k][l] = 0.
	return S_eshelby

		
def determining_W_eshelby( zeta_csv, omega_csv, len_zeta_csv, len_omega_csv ):
	W_eshelby = initTensor( 0., len_zeta_csv, len_omega_csv )
	for i in range(0, len_zeta_csv):
		for j in range(0, len_omega_csv):
			W_eshelby[i][j] = zeta_csv[i][1]*omega_csv[j][1]
	return W_eshelby
	

def determining_G_eshelby( xis, N_eshelby, D_eshelby, len_zeta_csv, len_omega_csv ):
	G_eshelby = initTensor( 0., 3, 3, 3, 3, len_zeta_csv, len_omega_csv )
	for i in range(0, 3):									
		for j in range(0, 3):
			for k in range(0, 3):
				for l in range(0, 3):
					for m in range(0, len_zeta_csv):
						for n in range(0, len_omega_csv):
							G_eshelby[i][j][k][l][m][n] = xis[k][m][n]*xis[l][m][n]*N_eshelby[i][j][m][n]/D_eshelby[m][n]
	return G_eshelby

def determining_D_eshelby( K_eshelby, len_zeta_csv, len_omega_csv ):
	D_eshelby = initTensor( 0., len_zeta_csv, len_omega_csv )
	eps = generate_epsilon_ijk()
	for i in range(0, len_zeta_csv):
		for j in range(0, len_omega_csv ):
			for m in range(0, 3):
				for n in range(0, 3):
					for l in range(0, 3):
						D_eshelby[i][j] = D_eshelby[i][j] + eps[m][n][l]*K_eshelby[m][0][i][j]*K_eshelby[n][1][i][j]*K_eshelby[l][2][i][j]
		
	return D_eshelby


def determining_N_eshelby( K_eshelby, len_zeta_csv, len_omega_csv ):
	N_eshelby = initTensor( 0., 3, 3, len_zeta_csv, len_omega_csv )
	eps = generate_epsilon_ijk()
	for i in range(0, 3):
		for j in range(0, 3):
			for o in range(0, len_zeta_csv):
				for p in range(0, len_omega_csv):
					for k in range(0, 3):
						for l in range(0, 3):
							for m in range(0, 3):
								for n in range(0, 3):
									N_eshelby[i][j][o][p] = N_eshelby[i][j][o][p] + 0.5 * eps[i][k][l] * eps[j][m][n] * K_eshelby[k][m][o][p] * K_eshelby[l][n][o][p]
	return N_eshelby



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
			zeta_1[i][j] = sqrt( 1. - pow( zeta_3[i][j], 2 ) )* cos( omega_csv[j][0] )
			
	zeta_2 = initTensor( 0., len( zeta_csv), len(omega_csv) )
	for i in range(0, len( zeta_csv) ):
		for j in range(0, len(omega_csv) ):
			zeta_2[i][j] = sqrt( 1. - pow( zeta_3[i][j], 2 ) )* sin( omega_csv[j][0] )
	
	zetas = []
	zetas.append( zeta_1 )
	zetas.append( zeta_2 )
	zetas.append( zeta_3 )
	return zetas