from numpy import *
from tensor_personal_functions import *
from convenient_objects import *
from projectors_personal_functions import *
from import_data import *
import matplotlib.pyplot as plt
from convenient_objects import *
from scipy.optimize import fmin_slsqp
from scipy.optimize import leastsq


def determine_epstheorique( fmin_slsqp_alpha, fmin_slsqp_beta, lambdas, stress, time):
	epstheorique = initTensor( 0., len(time), 6 )
	for i in range(0, len(time) ):
		s = initTensor(0., 6, 6 )
		s = souplesse_fluage_iso( fmin_slsqp_alpha, fmin_slsqp_beta, lambdas, time[i] )


		epstheorique[i] =  dot(s, stress)
		print "Time: i", epstheorique[i]
	return epstheorique
		

def souplesse_fluage_iso( fmin_slsqp_alpha, fmin_slsqp_beta, lambdas, time_scalar ):

	s = initTensor( 0., 6, 6 )

	J_tensor4 = generate_J_tensor4()
	J_matrix4 = tensor4_to_voigt4( J_tensor4 )
	
	K_tensor4 = generate_K_tensor4()
	K_matrix4 = tensor4_to_voigt4( K_tensor4 )
	
	for i in range(0, len(s[0]) ):
		for j in range(0, len(s[0]) ):
			for k in range(0, len(fmin_slsqp_alpha) ):
				if k == 0:
					s[i][j] = fmin_slsqp_alpha[k]*J_matrix4[i][j] + fmin_slsqp_beta[k]*K_matrix4[i][j]
				else:
					s[i][j] = s[i][j] + ( (1 - exp( - lambdas[k]*time_scalar))*fmin_slsqp_alpha[k])*J_matrix4[i][j] + ( (1 - exp( - lambdas[k]*time_scalar))*fmin_slsqp_beta[k])*K_matrix4[i][j]

	return s


def residuals( x, deformation_dagger, time, stress, lambdas ):
	err = 0
	for i in range( 0, len(time) ):
		err = err + pow( ( deformation_dagger[i] - deformation_dagger_theory( stress, lambdas, time[i], x ) ), 2 )
	return err
	
def deformation_dagger_theory( stress, lambdas, time, x ):
	
	#lambdas = []
	#for i in range(0, 60, 5):
		#lambdas.append( float( 1./pow(10, float(i)/10.) ) )

	#stress = initTensor(0., 6)
	#stress[0] = 20.
	#print stress
	
	for i in range(0, len(lambdas)):
		if x[i] < 0.:
			x[i] = x[i]*x[i]
	
	for i in range(0, len(lambdas)):
		if i == 0:
			f = x[0]
		else:
			f = f + x[i] * (1. - exp( -lambdas[i]* time  ) )
	f = f * stress[0]
	
	return f


def exercice01():
	
	time5MPa = []
	deformation5MPa = []
	time5MPa, deformation5MPa = import_data_04_01( "04_01_donnees5MPa.csv" )
	
	time10MPa = []
	deformation10MPa = []
	time10MPa, deformation10MPa = import_data_04_01( "04_01_donnees10MPa.csv" )
	
	time15MPa = []
	deformation15MPa = []
	time15MPa, deformation15MPa = import_data_04_01( "04_01_donnees15MPa.csv" )
	
	time20MPa = []
	deformation20MPa = []
	time20MPa, deformation20MPa = import_data_04_01( "04_01_donnees20MPa.csv" )
	
	print "Linear means that f(lamba * deformation ) = lambda * stress, with lambda real value"
	print "And f( deformation1 + deformation2 ) = f(deformation1) + f(deformation2) = stress1 + stress2 "
	

	
	print "Let's check it for 5MPa and 10MPa"
	print "Let's sum deformation5MPa[i]+deformation5MPa[i]:"
	sum_deformations = []
	for i in range(0, len(time5MPa)):
		sum_deformations.append( deformation5MPa[i] + deformation5MPa[i] )
	print "Deformation 5MPa+5MPa", "Deformation10MPa", "Ratio"
	for i in range(0, len(time5MPa)):
		print sum_deformations[i], deformation10MPa[i], sum_deformations[i]/deformation10MPa[i]
		
	
	plt.plot(time5MPa, deformation5MPa, 'ro', label = "Def5MPa")
	plt.plot(time10MPa, deformation10MPa, 'bo', label = "Def10MPa")
	plt.plot(time15MPa, deformation15MPa, 'go', label = "Def15MPa")
	plt.plot(time20MPa, deformation20MPa, 'yo', label = "Def20MPa")
	plt.xlabel('time')
	plt.ylabel('deformation')
	plt.legend()
	plt.savefig('04-01_initial_data.png')
	plt.close()
	

def exercice02():
	time = []
	deformation11 = []
	deformation22 = []
	time, deformation11, deformation22 = import_data_04_02( "04_02_donnees.csv" )
	time = asarray( time )
	
	print "Stress:"
	stress = initTensor(0., 6)
	stress[0] = 20.
	print stress
	
	print "LAMBDAS:"
	lambdas = []
	for i in range(0, 60, 5):
		lambdas.append( float( 1./pow(10, float(i)/10.) ) )
	print lambdas
	print "Len(lambas):", len(lambdas)
	
	

	plt.plot( time, deformation22, 'bs', label = "Def22")
	plt.plot(time, deformation11, 'ro', label = "Def11")
	plt.xlabel('time')
	plt.title("Stress: 20MPa")
	plt.ylabel('deformations')
	plt.legend()
	plt.savefig('04-02_initial_data.png')
	plt.close()
	
	print "Check 04-02_initial_data.png for initial data plot"

		
	print "Determining list deformation dagger..."
	deformation_dagger = []
	for i in range(0, len(time)):
		deformation_dagger.append( deformation11[i] - deformation22[i] )
	deformation_dagger = asarray(deformation_dagger )
		
	print "Determining list deformation double dagger..."
	deformation_double_dagger = []
	for i in range(0, len(time)):
		deformation_double_dagger.append( deformation11[i] + 2*deformation22[i] )
		
	#plt.plot( time, deformation_dagger, 'bs', label = "Def_dagger_exp")
	#plt.plot(time, deformation_double_dagger, 'ro', label = "Def_double_dagger_exp")
	#plt.xlabel('time')
	#plt.title("Stress: 20MPa")
	#plt.ylabel('deformations')
	#plt.legend()
	#plt.savefig('04_02_Def_daggers.png')
	#plt.close()
	
	print "Initial values betas:"
	betas = []
	for i in range(0, 60, 5):
		betas.append( 0.1 )
	print betas
	betas = asarray(betas)
	
	print "Initial values alpha:"
	alphas = []
	for i in range(0, 60, 5):
		alphas.append( 0.1 )
	print alphas
	alphas = asarray(alphas)

	
	#plsq_beta = leastsq( residuals_beta, betas, args = ( deformation_dagger, time ) )
	#print "PLSQ_Beta:", plsq_beta
	#print "len(PLSQ):", len( plsq_beta[0] )

	#res_beta = minimize( residuals_beta, betas, args = ( deformation_dagger, time ), method = 'SLSQP' )
	#print "res_Beta:", res
	#print "res_Beta_x:", res.x
	#print "res(PLSQ):", len( res )
	
	fmin_slsqp_beta = fmin_slsqp( residuals, betas, args = ( deformation_dagger, time, stress, lambdas ), bounds = [[0., inf]]*len(betas) )
	print "fmin_slsqp_beta:"
	for i in range(len(fmin_slsqp_beta)):
		print "beta", i, fmin_slsqp_beta[i]
	print "res(fmin_slsqp_beta):", len( fmin_slsqp_beta )
	
	
	fmin_slsqp_alpha = fmin_slsqp( residuals, alphas, args = ( deformation_double_dagger, time, stress, lambdas ), bounds = [[0., inf]]*len(alphas) )
	print "fmin_slsqp_alpha:"
	for i in range(len(fmin_slsqp_alpha)):
		print "alpha", i, fmin_slsqp_alpha[i]
	print "res(fmin_slsqp_alpha):", len( fmin_slsqp_alpha )
	
	#Unconstrained, no bounds optimization
	#plsq_alpha = leastsq( residuals_alpha, alphas, args = ( deformation_double_dagger, time ) )
	#print "PLSQ_Alpha:", plsq_alpha
	#print "len(PLSQ):", len( plsq_alpha[0] )
	
	deformation_dagger_theory_list = []
	for i in range(0, len(time)):
		#print deformation_dagger_theory( stress, lambdas, time[i], fmin_slsqp_beta ) - deformation_double_dagger[i]
		deformation_dagger_theory_list.append( deformation_dagger_theory( stress, lambdas, time[i], fmin_slsqp_beta ) )

		
	deformation_double_dagger_theory_list = []
	for i in range(0, len(time)):
		#print deformation_dagger_theory( stress, lambdas, time[i], fmin_slsqp_alpha ) - deformation_dagger[i]
		deformation_double_dagger_theory_list.append( deformation_dagger_theory( stress, lambdas, time[i], fmin_slsqp_alpha ) )
		
	plt.plot( time, deformation_dagger, 'bs', label = "Def_dagger_exp")
	plt.plot( time, deformation_dagger_theory_list, 'b--', label = "Def_dagger_theo")
	plt.plot( time, deformation_double_dagger, 'rs', label = "Def_double_dagger_exp")
	plt.plot( time, deformation_double_dagger_theory_list, 'r--', label = "Def_double_dagger_theo")
	plt.xlabel('time')
	plt.title("Stress: 20MPa")
	plt.ylabel('deformations')
	plt.legend()
	plt.savefig('04_02_Def_dagger_th_VS_exp.png')
	plt.close()
	
	epstheorique = initTensor(0., len(time), 6 ) 
	epstheorique = determine_epstheorique( fmin_slsqp_alpha, fmin_slsqp_beta, lambdas, stress, time)
	
	eps11_th = []
	eps22_th = []
	print "Eps_theorique11,", "Eps_theorique22,"
	for i in range(0, len(time)):
		eps11_th.append( epstheorique[i][0] )
		eps22_th.append( epstheorique[i][1] )
		print epstheorique[i][0]-deformation11[i], epstheorique[i][1]-deformation22[i]

	plt.plot( time, eps11_th, 'b--', label = "Def11_th")
	plt.plot( time, deformation11, 'bs', label = "Def11_exp")
	plt.plot( time, eps22_th, 'r--', label = "Def22_th")
	plt.plot( time, deformation22, 'rs', label = "Def22_exp")
	plt.xlabel('time')
	plt.title("Stress: 20MPa")
	plt.ylabel('deformations')
	plt.legend()
	plt.savefig('04_02_Eps_th_VS_exp.png')
	plt.close()
	
	poisson = []
	for i in range(0, len(eps11_th)):
		print -1. * eps22_th[i]/eps11_th[i]
		poisson.append( -1. * eps22_th[i]/eps11_th[i] )
	
	plt.plot( time, poisson, 'b--', label = "poisson")
	plt.xlabel('time')
	plt.title("Poisson ratio")
	plt.ylabel('-eps22/eps11')
	plt.legend()
	plt.savefig('poisson_ratio.png')
	plt.close()


	
	
#exercice01()
exercice02()
