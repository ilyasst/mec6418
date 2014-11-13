from import_data import *
import matplotlib.pyplot as plt
from the_lab_eqs import *
from numpy import *
from scipy.optimize import fmin_slsqp
from tensor_personal_functions import *


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
	
	deformation_dag1_2MPa, deformation_dag2_2MPa = determine_deformation_daggers(deformation2MPa)
	deformation_dag1_5MPa, deformation_dag2_5MPa = determine_deformation_daggers(deformation5MPa)
	deformation_dag1_10MPa, deformation_dag2_10MPa = determine_deformation_daggers(deformation10MPa)
	
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
		betas.append( 1.e-3 )
	print betas
	betas = asarray(betas)
	
	print "Initial values alpha:"
	alphas = []
	for i in range(0, len(lambdas) ):
		alphas.append( 1.e-5 )
	print alphas
	alphas = asarray(alphas)
	
	print
	print "LEN( betas )", len(betas)
	print "LEN( alphas )", len(alphas)
	print "LEN( lambdas )", len(lambdas)
	print "LEN( sigma_m )", len(sigma_m)
	print "LEN( car_times )", len(car_times)
	print
	
	fmin_slsqp_beta = fmin_slsqp( residuals, betas, args = ( deformation_dag1, time2MPa, lambdas, sigma_m, car_times ), bounds = [[0., inf]]*len(betas), iprint =2 )
	print "fmin_slsqp_beta:"
	for i in range(len(fmin_slsqp_beta)):
		print "beta", i, fmin_slsqp_beta[i]
	print "res(fmin_slsqp_beta):", len( fmin_slsqp_beta )
	
	fmin_slsqp_alpha = fmin_slsqp( residuals, alphas, args = ( deformation_dag2, time2MPa, lambdas, sigma_m, car_times ), bounds = [[0., inf]]*len(alphas), iprint =2 )
	print "fmin_slsqp_alpha:"
	for i in range(len(fmin_slsqp_alpha)):
		print "alpha", i, fmin_slsqp_alpha[i]
	print "res(fmin_slsqp_alpha):", len( fmin_slsqp_alpha )


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

determine_alpha_beta()
	
#determine_linearity()