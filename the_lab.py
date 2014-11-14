from import_data import *
import matplotlib.pyplot as plt
from the_lab_eqs import *
from numpy import *
from scipy.optimize import fmin_slsqp
from tensor_personal_functions import *
from CtoS_1D import *

print "LAMBDAS:"
lambdas = []
for i in range(0, 45, 5):
	lambdas.append( float( 1./pow(10, float(i)/10.) ) )
print lambdas
print "Len(lambas):", len(lambdas)

car_times = []
print
print "TEMPS CARACTERISTIQUES:"
car_times.append( 5.5 )
print "t1 = 5.5 s"
print "t2 = 905 s"
car_times.append( 905. )
print "t3 = 910.5 s"
car_times.append( 910.5 )
print 


def determine_lineartiy_ratio( time2MPa, stress02, deformation02, stress0x, deformation0x ):
	ratio11 = []
	ratio22 = []
	time = []
	deformation02_11 = []
	deformation02_22 = []
	deformation0x_11 = []
	deformation0x_22 = []
	stress_ratio_i = []
	#On prend que le debut sinon apres c'est proche de 0 ca donne des valeurs de fou
	for i in range(0, 70):
		deformation02_11.append( float(deformation02[i][0]) ) 
		deformation0x_11.append( float(deformation0x[i][0]) ) 
		deformation02_22.append( float(deformation02[i][1]) )
		deformation0x_22.append( float(deformation0x[i][1]) ) 
		time.append( float( time2MPa[i] ) )
		
	for i in range(0, 70 ):
		stress_ratio_i = float( stress0x[i] )/float( stress02[i] )
		def_ratio11_i = deformation0x_11[i] / deformation02_11[i]
		def_ratio22_i = deformation0x_22[i] / deformation02_22[i]
		ratio11.append( stress_ratio_i/def_ratio11_i )
		ratio22.append( stress_ratio_i/def_ratio22_i )
	return time, ratio11, ratio22



def determine_linearity():

	time2MPa, stress2MPa, deformation2MPa = import_data_lab_fluage( "fluage-recouvrance-2MPa.csv" )
	time5MPa, stress5MPa, deformation5MPa = import_data_lab_fluage( "fluage-recouvrance-5MPa.csv" )
	time10MPa, stress10MPa, deformation10MPa = import_data_lab_fluage( "fluage-recouvrance-10MPa.csv" )
	time13MPa, stress13MPa, deformation13MPa = import_data_lab_fluage( "fluage-recouvrance-13MPa.csv" )
	time16MPa, stress16MPa, deformation16MPa = import_data_lab_fluage( "fluage-recouvrance-16MPa.csv" )
	time20MPa, stress20MPa, deformation20MPa = import_data_lab_fluage( "fluage-recouvrance-20MPa.csv" )
	time22MPa, stress22MPa, deformation22MPa = import_data_lab_fluage( "fluage-recouvrance-22MPa.csv" )
	time25MPa, stress25MPa, deformation25MPa = import_data_lab_fluage( "fluage-recouvrance-25MPa.csv" )
	time30MPa, stress30MPa, deformation30MPa = import_data_lab_fluage( "fluage-recouvrance-30MPa.csv" )
	time35MPa, stress35MPa, deformation35MPa = import_data_lab_fluage( "fluage-recouvrance-35MPa.csv" )
	
	print 
	print "Linear means that f(lamba * deformation ) = lambda * stress, with lambda real value"
	print "And f( deformation1 + deformation2 ) = f(deformation1) + f(deformation2) = stress1 + stress2 "
	print
	
	time2MPa_reduced, ratio11_2MPa, ratio22_2MPa = determine_lineartiy_ratio( time2MPa, stress2MPa, deformation2MPa, stress2MPa, deformation2MPa )
	time5MPa_reduced, ratio11_5MPa, ratio22_5MPa = determine_lineartiy_ratio( time5MPa, stress2MPa, deformation2MPa, stress5MPa, deformation5MPa )
	time10MPa_reduced, ratio11_10MPa, ratio22_10MPa = determine_lineartiy_ratio( time10MPa, stress2MPa, deformation2MPa, stress10MPa, deformation10MPa )
	time13MPa_reduced, ratio11_13MPa, ratio22_13MPa = determine_lineartiy_ratio( time13MPa, stress2MPa, deformation2MPa, stress13MPa, deformation13MPa )
	time16MPa_reduced, ratio11_16MPa, ratio22_16MPa = determine_lineartiy_ratio( time16MPa, stress2MPa, deformation2MPa, stress16MPa, deformation16MPa )
	
	deformation02_11 = []
	deformation02_22 = []
	deformation05_11 = []
	deformation05_22 = []
	time2MPa = []
	for i in range(0, 50):
	#len(deformation2MPa)-1
		deformation02_11.append( float(deformation2MPa[i][0]) ) 
		deformation02_22.append( float(deformation2MPa[i][1]) )
		deformation05_11.append( float(deformation5MPa[i][0]) ) 
		deformation05_22.append( float(deformation5MPa[i][1]) )
		time2MPa = time2MPa.append( time2MPa[i] )

	print len(deformation02_11), len(time2MPa)
	
	#plt.plot(time2MPa, stress2MPa, 'r--', label = "Stress2MPa")
	plt.plot(time2MPa, deformation02_11, 'b--', label = "Def2Mpa_11")
	plt.plot(time2MPa, deformation02_22, 'g--', label = "Def2Mpa_22")
	plt.plot(time5MPa, deformation05_11, 'r--', label = "Def5Mpa_11")
	plt.plot(time5MPa, deformation05_22, 'y--', label = "Def5Mpa_22")
	#plt.figure(figsize=(18, 12), dpi=400)
	plt.xlabel('time')
	plt.ylabel('stress')
	plt.legend( )
	plt.savefig('lab_stress_def_initial_data.png', dpi = 300)
	plt.close()
	

	plt.plot(time2MPa_reduced, ratio11_2MPa, 'ro', label = "Ratio2Mpa_11")
	plt.plot(time2MPa_reduced, ratio22_2MPa, 'bo', label = "Ratio2Mpa_22")
	plt.plot(time2MPa_reduced, ratio11_5MPa, 'rs', label = "Ratio5Mpa_11")
	plt.plot(time2MPa_reduced, ratio22_5MPa, 'bs', label = "Ratio5Mpa_22")
	plt.plot(time2MPa_reduced, ratio11_10MPa, 'g^', label = "Ratio10Mpa_11")
	plt.plot(time2MPa_reduced, ratio22_10MPa, 'y^', label = "Ratio10Mpa_22")
	plt.plot(time2MPa_reduced, ratio11_13MPa, 'm^', label = "Ratio13Mpa_11")
	plt.plot(time2MPa_reduced, ratio22_13MPa, 'c^', label = "Ratio13Mpa_22")
	plt.axhline(y=1.05)
	plt.axhline(y=0.95)
	plt.xlabel('time')
	plt.ylabel('ratio')
	plt.legend( )
	plt.savefig('lab_determination_lineaires.png')
	plt.close()


def determine_alpha_beta():
	
	time2MPa, stress2MPa, deformation2MPa = import_data_lab_fluage( "fluage-recouvrance-2MPa.csv" )
	time5MPa, stress5MPa, deformation5MPa = import_data_lab_fluage( "fluage-recouvrance-5MPa.csv" )
	time10MPa, stress10MPa, deformation10MPa = import_data_lab_fluage( "fluage-recouvrance-10MPa.csv" )
	
	print
	print "Determining Deformation_Daggers for sets of data..."
	print 
	
	deformation_dag1_2MPa, deformation_dag2_2MPa =  determine_deformation_daggers(deformation2MPa)
	deformation_dag1_5MPa, deformation_dag2_5MPa = determine_deformation_daggers(deformation5MPa)
	deformation_dag1_10MPa, deformation_dag2_10MPa = determine_deformation_daggers(deformation10MPa)
	print "LEN(deformation_dag1_2MPa):", len(deformation_dag1_2MPa)
	
	print
	print "Determining sigma_max_exp for each linear experiment..."
	sigma_m = []
	sigma_m.append( determine_sigma_max( stress2MPa ) )
	sigma_m.append( determine_sigma_max( stress5MPa ) )
	sigma_m.append( determine_sigma_max( stress10MPa ) )
	
	print
	print "Creating Deformation Dag1 and Dag2 matrix for minimization..."	
	deformation_dag1 = []
	deformation_dag2 = []
	deformation_dag1.append( deformation_dag1_2MPa ) 
	deformation_dag2.append( deformation_dag2_2MPa ) 
	deformation_dag1.append( deformation_dag1_5MPa ) 
	deformation_dag2.append( deformation_dag2_5MPa ) 
	deformation_dag1.append( deformation_dag1_10MPa ) 
	deformation_dag2.append( deformation_dag2_10MPa ) 
	#deformation_dag1 and deformation_dag2 contain 3 columns which each contains data for 2MPa, 5MPa, 10MPA as lists
	
	print "Initial values betas:"
	betas = []
	for i in range(0, len(lambdas) ):
		betas.append( 1.e-5 )
	print betas
	betas = asarray(betas)
	
	print "Initial values alpha:"
	alphas = []
	for i in range(0, len(lambdas) ):
		alphas.append( 1.e-7 )
	print alphas
	alphas = asarray(alphas)
	
	print
	print "LEN( betas )", len(betas)
	print "LEN( alphas )", len(alphas)
	print "LEN( lambdas )", len(lambdas)
	print "LEN( sigma_m )", len(sigma_m)
	print "LEN( car_times )", len(car_times)
	print
	
	fmin_slsqp_beta = fmin_slsqp( residuals, betas, args = ( deformation_dag1, time2MPa, lambdas, sigma_m, car_times ), bounds = [[0., inf]]*len(betas), iprint =2, acc = 1.e-8, epsilon=1.e-15 )
	print "fmin_slsqp_beta:"
	for i in range(len(fmin_slsqp_beta)):
		print "beta", i, fmin_slsqp_beta[i]
	print "res(fmin_slsqp_beta):", len( fmin_slsqp_beta )
	
	fmin_slsqp_alpha = fmin_slsqp( residuals, alphas, args = ( deformation_dag2, time2MPa, lambdas, sigma_m, car_times ), bounds = [[0., inf]]*len(alphas), iprint =2, acc = 1.e-8 )
	print "fmin_slsqp_alpha:"
	for i in range(len(fmin_slsqp_alpha)):
		print "alpha", i, fmin_slsqp_alpha[i]
	print "res(fmin_slsqp_alpha):", len( fmin_slsqp_alpha )
	
	print 
	print "S to C interconversion 1D for alphas...."
	retour = StoC_interconversion1D( fmin_slsqp_alpha, lambdas )
	alpha_inv = retour[ "C" ]
	alpha_rho = retour[ "rho" ]
	print "alpha_inv is : %s \nalpha_rho is : %s" % ( alpha_inv, alpha_rho )
	print

	print 
	print "S to C interconversion 1D for betas...."
	retour = StoC_interconversion1D( fmin_slsqp_beta, lambdas )
	beta_inv = retour[ "C" ]
	beta_rho = retour[ "rho" ]
	print "beta_inv is : %s \nbeta_rho is : %s" % ( beta_inv, beta_rho )
	print
	
	print "Determining theory stress..."
	stress_theory_2MPa = []
	for i in range(0, len(time2MPa)):
		stress_theory_2MPa.append( stress_theory( car_times, sigma_m[0], time2MPa[i] ) )
	stress_theory_5MPa = []
	for i in range(0, len(time5MPa)):
		stress_theory_5MPa.append( stress_theory( car_times, sigma_m[1], time5MPa[i] ) )
	stress_theory_10MPa = []
	for i in range(0, len(time10MPa)):
		stress_theory_10MPa.append( stress_theory( car_times, sigma_m[2], time10MPa[i] ) )
	plt.plot(time2MPa, stress2MPa, 'r--', label = "Stress2MPa")
	plt.plot(time2MPa, stress_theory_2MPa, 'b--', label = "Stress2MPa_th")
	plt.plot(time5MPa, stress5MPa, 'g--', label = "Stress5MPa")
	plt.plot(time5MPa, stress_theory_5MPa, 'm--', label = "Stress5MPa_th")
	plt.plot(time10MPa, stress10MPa, 'y--', label = "Stress10MPa")
	plt.plot(time10MPa, stress_theory_10MPa, 'k--', label = "Stress10MPa_th")
	plt.xlabel('time')
	plt.ylabel('stress')
	plt.legend( )
	plt.savefig('lab_verifying_theory_stress.png')
	plt.close()
	print "Plot showing theory+exp stress available *lab_verifying_theory_stress.png*..."
	
	print 
	print "Determining deformatin_dagger and double-daggers..."
	def2MPa_dag1_theory = []
	def2MPa_dag2_theory = []
	def5MPa_dag1_theory = []
	def5MPa_dag2_theory = []
	def10MPa_dag1_theory = []
	def10MPa_dag2_theory = []
	for i in range(0, len(time2MPa)):
		def2MPa_dag1_theory.append( deformation_dagger_theory( fmin_slsqp_beta, lambdas, time2MPa[i], sigma_m[0], car_times ) )
		def2MPa_dag2_theory.append( deformation_dagger_theory( fmin_slsqp_alpha, lambdas, time2MPa[i], sigma_m[0], car_times ) )
		def5MPa_dag1_theory.append( deformation_dagger_theory( fmin_slsqp_beta, lambdas, time2MPa[i], sigma_m[1], car_times ) )
		def5MPa_dag2_theory.append( deformation_dagger_theory( fmin_slsqp_alpha, lambdas, time2MPa[i], sigma_m[1], car_times ) )
		def10MPa_dag1_theory.append( deformation_dagger_theory( fmin_slsqp_beta, lambdas, time2MPa[i], sigma_m[2], car_times ) )
		def10MPa_dag2_theory.append( deformation_dagger_theory( fmin_slsqp_alpha, lambdas, time2MPa[i], sigma_m[2], car_times ) )

	plt.plot(time2MPa, def2MPa_dag1_theory, 'ro', label = "Eps2MPa_dag1")
	plt.plot(time2MPa, deformation_dag1_2MPa, 'b--', label = "Eps2MPa_dag1_th")
	plt.plot(time2MPa, def2MPa_dag2_theory, 'go', label = "Eps2MPa_dag2")
	plt.plot(time2MPa, deformation_dag2_2MPa, 'k--', label = "Eps2MPa_dag2_th")
	plt.xlabel('time')
	plt.ylabel('def')
	plt.legend( )
	plt.savefig('lab_verifying_theory_daggers_2MPa.png')
	plt.close()
	
	plt.plot(time5MPa, def5MPa_dag1_theory, 'ro', label = "Eps5MPa_dag1")
	plt.plot(time5MPa, deformation_dag1_5MPa, 'b--', label = "Eps5MPa_dag1_th")
	plt.plot(time5MPa, def5MPa_dag2_theory, 'go', label = "Eps5MPa_dag2")
	plt.plot(time5MPa, deformation_dag2_5MPa, 'k--', label = "Eps5MPa_dag2_th")
	plt.xlabel('time')
	plt.ylabel('def')
	plt.legend( )
	plt.savefig('lab_verifying_theory_daggers_5MPa.png')
	plt.close()
	
	plt.plot(time10MPa, def10MPa_dag1_theory, 'ro', label = "Eps10MPa_dag1")
	plt.plot(time10MPa, deformation_dag1_10MPa, 'b--', label = "Eps10MPa_dag1_th")
	plt.plot(time10MPa, def10MPa_dag2_theory, 'go', label = "Eps10MPa_dag2")
	plt.plot(time10MPa, deformation_dag2_10MPa, 'k--', label = "Eps10MPa_dag2_th")
	plt.xlabel('time')
	plt.ylabel('def')
	plt.legend( )
	plt.savefig('lab_verifying_theory_daggers_10MPa.png')
	plt.close()

	print 
	print "Determining deformatins_theory..."
	def_theorique02MPa = determine_epstheorique( fmin_slsqp_alpha, fmin_slsqp_beta, lambdas, sigma_m[0] , time2MPa, car_times)
	def_theorique05MPa = determine_epstheorique( fmin_slsqp_alpha, fmin_slsqp_beta, lambdas, sigma_m[1] , time2MPa, car_times)
	def_theorique10MPa = determine_epstheorique( fmin_slsqp_alpha, fmin_slsqp_beta, lambdas, sigma_m[2] , time2MPa, car_times)
	
	def_theorique02MPa_1 = []
	def_theorique02MPa_2 = []
	def_exp02MPa_1 = []
	def_exp02MPa_2 = []
	def_theorique05MPa_1 = []
	def_theorique05MPa_2 = []
	def_exp05MPa_1 = []
	def_exp05MPa_2 = []
	def_theorique10MPa_1 = []
	def_theorique10MPa_2 = []
	def_exp10MPa_1 = []
	def_exp10MPa_2 = []
	for i in range(0, len(def_theorique02MPa)):
		def_theorique02MPa_1.append( def_theorique02MPa[i][0] )
		def_theorique02MPa_2.append( def_theorique02MPa[i][1] )
		def_theorique05MPa_1.append( def_theorique05MPa[i][0] )
		def_theorique05MPa_2.append( def_theorique05MPa[i][1] )
		def_theorique10MPa_1.append( def_theorique10MPa[i][0] )
		def_theorique10MPa_2.append( def_theorique10MPa[i][1] )
		def_exp02MPa_1.append( deformation2MPa[i][0] )
		def_exp02MPa_2.append( deformation2MPa[i][1] )
		def_exp05MPa_1.append( deformation5MPa[i][0] )
		def_exp05MPa_2.append( deformation5MPa[i][1] )
		def_exp10MPa_1.append( deformation10MPa[i][0] )
		def_exp10MPa_2.append( deformation10MPa[i][1] )

	print
	plt.plot(time2MPa, def_theorique02MPa_1, 'r--', label = "def2MPa1_th")
	plt.plot(time2MPa, def_exp02MPa_1, 'ro', label = "def2MPa1")
	plt.plot(time2MPa, def_theorique02MPa_2, 'b--', label = "def2MPa1_th")
	plt.plot(time2MPa, def_exp02MPa_2, 'bo', label = "def2MPa1")
	plt.xlabel('time')
	plt.ylabel('def')
	plt.legend( )
	plt.savefig('lab_verifying_deformation_theory_2MPa.png')
	plt.close()
	plt.plot(time5MPa, def_theorique05MPa_1, 'r--', label = "def5MPa1_th")
	plt.plot(time5MPa, def_exp05MPa_1, 'ro', label = "def5MPa1")
	plt.plot(time5MPa, def_theorique05MPa_2, 'b--', label = "def5MPa1_th")
	plt.plot(time5MPa, def_exp05MPa_2, 'bo', label = "def5MPa1")
	plt.xlabel('time')
	plt.ylabel('def')
	plt.legend( )
	plt.savefig('lab_verifying_deformation_theory_5MPa.png')
	plt.close()
	plt.plot(time10MPa, def_theorique10MPa_1, 'r--', label = "def10MPa1_th")
	plt.plot(time10MPa, def_exp10MPa_1, 'ro', label = "def10MPa1")
	plt.plot(time10MPa, def_theorique10MPa_2, 'b--', label = "def10MPa1_th")
	plt.plot(time10MPa, def_exp10MPa_2, 'bo', label = "def10MPa1")
	plt.xlabel('time')
	plt.ylabel('def')
	plt.legend( )
	plt.savefig('lab_verifying_deformation_theory_10MPa.png')
	plt.close()
	print "Plot showing theory+exp def available *lab_verifying_deformation_theory.png*..."


	
	#Division by 3 necessary because C(t) = 3*k(t)*J + 2*u(t)*K
	print "====================================================================="
	print "Determining parameters for FEM:"
	
	print
	tau_fem = []
	for i in range( 0, len(alpha_rho)):
		tau_fem.append( 1./alpha_rho[i] )
	print "tau for FEM:", tau_fem
	
	print
	u0_fem = sum( beta_inv )/ 2.
	print "u0_fem =", u0_fem
	
	print
	k0_fem = sum( alpha_inv )/ 3.
	print "k0_fem =", k0_fem
	
	print
	alpha_fem = []
	for i in range(0, len(alpha_inv)):
		alpha_fem.append( ( alpha_inv[i]/3. )/ k0_fem )
	print "alpha for FEM:", alpha_fem




def determine_sigma_max( stress2MPa ):
	temp_sum = 0.
	for i in range(14, 58):
		temp_sum = temp_sum + float( stress2MPa[i] )
	sigma2MPa_max = temp_sum / (58.-14.)
	print "SigmaMax:", sigma2MPa_max
	return sigma2MPa_max

def determine_deformation_daggers(deformation):
	deformation_dag1 = []
	deformation_dag2 = []
	for i in range(0, len( deformation )):
		deformation_dag1.append( deformation[i][0] - deformation[i][1] )
		deformation_dag2.append( deformation[i][0] + 2.*deformation[i][1] )
	return deformation_dag1, deformation_dag2


def stress_theory( car_times, sigma_m, time ):
	
	eq0 = ( sigma_m/car_times[0] ) * time * heaviside(time)
	eq1 = ( sigma_m/car_times[0] ) * ( time - car_times[0] ) * heaviside(time-car_times[0])
	eq2 = (sigma_m/(car_times[2] - car_times[1])) * (time-car_times[1]) * heaviside( time - car_times[1] )
	eq3 = (sigma_m/(car_times[2] - car_times[1])) * (time-car_times[2]) * heaviside( time - car_times[2] )

	stress_at_t = eq0 - eq1 - eq2 + eq3
	return stress_at_t
	
	
	
determine_alpha_beta()
	
#determine_linearity()