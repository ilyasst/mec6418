from import_data import *
from numpy import *
from tensor_personal_functions import *
from hmgnzt_personal_functions import *


def moyenne_orientation( Cm, angle0pi, angle02pi, N ):
	print
	print "Starting moyenne orientation..."
	print
	C = voigt4_to_tensor4(Cm)
	mx = 16*pow( 2, (N-1) )
	print "N=", N
	print "Max:", mx
	Pm = initTensor( 0., 3, 3 )
	C_matrix_moy = Cm
	#C_tensor4_moy = initTensor( 0., 3, 3, 3, 3)
	#print 

	
	for theta in range( 0, mx ):
		for phi in range( 0, mx ):
			for beta in range( 0, mx ):
				Pm[0][0] = cos(angle0pi[N][theta][0])*cos(angle02pi[N][phi][0])*cos(angle02pi[N][beta][0])-sin(angle02pi[N][phi][0])*sin(angle02pi[N][beta][0])
				Pm[0][1] = -cos(angle0pi[N][theta][0])*cos(angle02pi[N][phi][0])*sin(angle02pi[N][beta][0])-sin(angle02pi[N][phi][0])*sin(angle02pi[N][beta][0])
				Pm[0][2] = sin(angle0pi[N][theta][0])*cos(angle02pi[N][phi][0])
				
				Pm[1][0] = cos(angle0pi[N][theta][0]) * sin(angle02pi[N][phi][0]) * cos(angle02pi[N][beta][0])  + cos(angle02pi[N][phi][0]) * sin(angle02pi[N][beta][0])
				Pm[1][1] = -cos(angle0pi[N][theta][0])*sin(angle02pi[N][phi][0])*sin(angle02pi[N][beta][0]) + cos(angle02pi[N][phi][0])*cos(angle02pi[N][beta][0])
				Pm[1][2] = sin(angle0pi[N][theta][0])*sin(angle02pi[N][phi][0])
				
				Pm[2][0] = - sin(angle0pi[N][theta][0]) * cos(angle02pi[N][beta][0])
				Pm[2][1] = sin(angle0pi[N][theta][0])*sin(angle02pi[N][beta][0])
				Pm[2][2] = cos(angle0pi[N][theta][0])
				
	
				for i in range(0, 3):
					for j in range(0, 3):
						for k in range(0, 3):
							for l in range(0, 3):
								#for m in range(0, 3):
									#for n in range(0, 3):
										#for o in range(0, 3):
											#for p in range(0, 3):
												#C_tensor4_moy[m][n][o][p] = C_tensor4_moy[m][n][o][p] + ( (1./(8.*pow( pi,2)))*Pm[i][m]*Pm[j][n]*Pm[k][o]*Pm[l][p]*C[i][j][k][l]*sin(angle0pi[N][theta][0])*angle0pi[N][theta][1]*angle02pi[N][phi][1]*angle02pi[N][beta][1])
								C_matrix_moy[0][0] = C_matrix_moy[0][0] + ( (1./(8.*pow( pi,2)))*Pm[i][0]*Pm[j][0]*Pm[k][0]*Pm[l][0]*C[i][j][k][l]*sin(angle0pi[N][theta][0])*angle0pi[N][theta][1]*angle02pi[N][phi][1]*angle02pi[N][beta][1])
								C_matrix_moy[1][1] = C_matrix_moy[1][1] + ( (1./(8.*pow( pi,2)))*Pm[i][1]*Pm[j][1]*Pm[k][1]*Pm[l][1]*C[i][j][k][l]*sin(angle0pi[N][theta][0])*angle0pi[N][theta][1]*angle02pi[N][phi][1]*angle02pi[N][beta][1])
								C_matrix_moy[2][2] = C_matrix_moy[2][2] + ( (1./(8.*pow( pi,2)))*Pm[i][2]*Pm[j][2]*Pm[k][2]*Pm[l][2]*C[i][j][k][l]*sin(angle0pi[N][theta][0])*angle0pi[N][theta][1]*angle02pi[N][phi][1]*angle02pi[N][beta][1])
								C_matrix_moy[3][3] = C_matrix_moy[3][3] + 2.*( (1./(8.*pow( pi,2)))*Pm[i][1]*Pm[j][2]*Pm[k][1]*Pm[l][2]*C[i][j][k][l]*sin(angle0pi[N][theta][0])*angle0pi[N][theta][1]*angle02pi[N][phi][1]*angle02pi[N][beta][1])
								C_matrix_moy[4][4] = C_matrix_moy[4][4] + 2.*( (1./(8.*pow( pi,2)))*Pm[i][2]*Pm[j][0]*Pm[k][2]*Pm[l][0]*C[i][j][k][l]*sin(angle0pi[N][theta][0])*angle0pi[N][theta][1]*angle02pi[N][phi][1]*angle02pi[N][beta][1])
								C_matrix_moy[5][5] = C_matrix_moy[5][5] + 2.*( (1./(8.*pow( pi,2)))*Pm[i][0]*Pm[j][1]*Pm[k][0]*Pm[l][1]*C[i][j][k][l]*sin(angle0pi[N][theta][0])*angle0pi[N][theta][1]*angle02pi[N][phi][1]*angle02pi[N][beta][1])
								C_matrix_moy[0][1] = C_matrix_moy[0][1] + ( (1./(8.*pow( pi,2)))*Pm[i][0]*Pm[j][0]*Pm[k][1]*Pm[l][1]*C[i][j][k][l]*sin(angle0pi[N][theta][0])*angle0pi[N][theta][1]*angle02pi[N][phi][1]*angle02pi[N][beta][1])
								C_matrix_moy[0][2] = C_matrix_moy[0][2] + ( (1./(8.*pow( pi,2)))*Pm[i][0]*Pm[j][0]*Pm[k][2]*Pm[l][2]*C[i][j][k][l]*sin(angle0pi[N][theta][0])*angle0pi[N][theta][1]*angle02pi[N][phi][1]*angle02pi[N][beta][1])
								C_matrix_moy[1][2] = C_matrix_moy[1][2] + ( (1./(8.*pow( pi,2)))*Pm[i][1]*Pm[j][1]*Pm[k][2]*Pm[l][2]*C[i][j][k][l]*sin(angle0pi[N][theta][0])*angle0pi[N][theta][1]*angle02pi[N][phi][1]*angle02pi[N][beta][1])
	#C_matrix_moy = tensor4_to_voigt4( C_tensor4_moy )
	for i in range(0, 6):
		for j in range((i+1), 6):
			C_matrix_moy[j][i] = C_matrix_moy[i][j]
			
	return C_matrix_moy
print
print "Importing angles data..."

zeta_csv = import_hmgnzt_quad( "zeta3_4points.csv" )
omega_csv = import_hmgnzt_quad( "omega_512points.csv" )

angle_0pi = []
angle_0pi.append( import_anglepi( "0pi_16points.csv" ) )
angle_0pi.append( import_anglepi( "0pi_32points.csv" ) )
angle_0pi.append( import_anglepi( "0pi_64points.csv" ) )
angle_0pi.append( import_anglepi( "0pi_128points.csv" ) )
angle_0pi.append( import_anglepi( "0pi_256points.csv" ) )
angle_0pi.append( import_anglepi( "0pi_512points.csv" ) )

angle_2pi = initTensor( 0., 6 )
angle_2pi[0] = import_anglepi( "02pi_16points.csv" )
angle_2pi[1] = import_anglepi( "02pi_32points.csv" )
angle_2pi[2] = import_anglepi( "02pi_64points.csv" )
angle_2pi[3] = import_anglepi( "02pi_128points.csv" )
angle_2pi[4] = import_anglepi( "02pi_256points.csv" )
angle_2pi[5] = import_anglepi( "02pi_512points.csv" )

C = [ 40.7, 39.3, 12.4, 0., 0., 0., 40.7, 12.4, 0., 0., 0., 625.7, 0., 0., 0., 2.44, 0., 0., 2.44, 0., 1.36 ]
C_NTC_matrix = generate_symmetric_matrix66_from_list( C )
print 
print "C_NTC_matrix="
for i in range( 0, len(C_NTC_matrix)):
	print C_NTC_matrix[i]
C_NTC_tensor4 = voigt4_to_tensor4(C_NTC_matrix)

N = 1
C_NTC_matrix_t = moyenne_orientation( C_NTC_matrix, angle_0pi, angle_2pi, N )
print
print "C_NTC_matrix_tilde:"
for i in range(0, len(C_NTC_matrix_t)):
	print C_NTC_matrix_t[i]
C_NTC_tensor4_t = voigt4_to_tensor4(C_NTC_matrix_t)

print 
print "---------------------------------------------------------------------"
print
print "5% NTCs aggregated with MT"

print
print "Getting matrix/CNT properties..."
E0 = 2.
nu0 = 0.3

v0 = 0.95
v1 = 1. - v0

a = [ 1., 1., 1. ]

J_tensor4 = generate_J_tensor4()
J_matrix = tensor4_to_voigt4( J_tensor4 )

K_tensor4 = generate_K_tensor4()
K_matrix = tensor4_to_voigt4( K_tensor4 )

k0 = E0/(3.*(1. - 2.*nu0)) 
mu0 = E0/(2.*(1. + nu0)) 
C0_tensor4 = dot( 3.*k0, J_tensor4 ) + dot( 2.*mu0, K_tensor4 )
C0_matrix = tensor4_to_voigt4( C0_tensor4 )
print 
print "Let's MoriTanaka..."
C_MT_matrix_aggregat = mori_tanaka( a, v0, C0_tensor4, C_NTC_tensor4_t, zeta_csv, omega_csv )
C_MT_tensor4_aggregat = voigt4_to_tensor4( C_MT_matrix_aggregat )
print "Done."
print
print "C_MT_matrix_aggregat:"
for i in range(0, len(C_MT_matrix_aggregat)):
	print C_MT_matrix_aggregat[i]

k_agg = tensor4_contract4_tensor4( J_tensor4, C_MT_tensor4_aggregat )/3.
mu_agg = tensor4_contract4_tensor4( K_tensor4, C_MT_tensor4_aggregat )/10.

print 
print "k_agg=", k_agg
print "mu_agg=", mu_agg


print 
print "---------------------------------------------------------------------"
print
print "5% NTCs separes et dsitribues aleatoirement"

a = [ 1., 1., 500.]
C_MT_matrix_ale = mori_tanaka( a, v0, C0_tensor4, C_NTC_tensor4_t, zeta_csv, omega_csv )
C_matrix_ale = moyenne_orientation( C_NTC_matrix, angle_0pi, angle_2pi, N )

C_tensor4_ale = voigt4_to_tensor4( C_matrix_ale )

k_ale= tensor4_contract4_tensor4( J_tensor4, C_tensor4_ale )/3.
mu_ale = tensor4_contract4_tensor4( K_tensor4, C_tensor4_ale )/10.


print
print "C_MT_matrix_ale:"
for i in range(0, len(C_matrix_ale)):
	print C_matrix_ale[i]

print 
print "k_ale=", k_ale
print "mu_ale=", mu_ale

print 
print "---------------------------------------------------------------------"
print
print "NTC alignes"

C_MT_matrix_ali = mori_tanaka( a, v0, C0_tensor4, C_NTC_tensor4_t, zeta_csv, omega_csv )
C_MT_tensor4_ali = voigt4_to_tensor4( C_MT_matrix_ali )
k_ali = tensor4_contract4_tensor4( J_tensor4, C_MT_tensor4_ali )/3.
mu_ali = tensor4_contract4_tensor4( K_tensor4, C_MT_tensor4_ali )/10.

print
print "C_MT_matrix_alignes:"
for i in range(0, len(C_MT_matrix_ali)):
	print C_MT_matrix_ali[i]

print 
print "k_ali=", k_ali
print "mu_ali=", mu_ali