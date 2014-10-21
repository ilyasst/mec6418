from numpy import *
from tensor_personal_functions import *
from convenient_objects import *
from projectors_personal_functions import *
from import_data import *
import matplotlib.pyplot as plt
from convenient_objects import *
from scipy.optimize import fmin_slsqp
from scipy.optimize import leastsq


	
def exercice02():
	time = []
	deformation11 = []
	deformation22 = []
	time, deformation11, deformation22 = import_data_04_02( "04_02_donnees.csv" )
	time = asarray( time )
	
	print "Stress:"
	stress = initTensor(0., 6)
	stress[0] = 20
	print stress
	
	

	plt.plot( time, deformation22, 'bs', label = "Def22")
	plt.xlabel('time')
	plt.title("Stress: 20MPa")
	plt.ylabel('deformations')
	plt.legend()
	plt.savefig('04-02_initial_data_E22.png')
	plt.close()
	
	plt.plot(time, deformation11, 'ro', label = "Def11")
	plt.xlabel('time')
	plt.title("Stress: 20MPa")
	plt.ylabel('deformations')
	plt.legend()
	plt.savefig('04-02_initial_data_E11.png')
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
		
	plt.plot( time, deformation_dagger, 'bs', label = "Def_dagger_exp")
	plt.plot(time, deformation_double_dagger, 'ro', label = "Def_double_dagger_exp")
	plt.xlabel('time')
	plt.title("Stress: 20MPa")
	plt.ylabel('deformations')
	plt.legend()
	plt.savefig('04_02_Def_daggers.png')
	plt.close()
	
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
	
	fmin_slsqp_beta = fmin_slsqp( residuals, betas, args = ( deformation_dagger, time ), bounds = [[0., inf]]*len(betas) )
	print "fmin_slsqp_beta:"
	for i in range(len(fmin_slsqp_beta)):
		print "beta", i, fmin_slsqp_beta[i]
	print "res(fmin_slsqp_beta):", len( fmin_slsqp_beta )
	
	
	fmin_slsqp_alpha = fmin_slsqp( residuals, alphas, args = ( deformation_double_dagger, time ), bounds = [[0., inf]]*len(alphas) )
	print "fmin_slsqp_alpha:"
	for i in range(len(fmin_slsqp_alpha)):
		print "alpha", i, fmin_slsqp_alpha[i]
	print "res(fmin_slsqp_alpha):", len( fmin_slsqp_alpha )
	
	#Unconstrained, no bounds optimization
	#plsq_alpha = leastsq( residuals_alpha, alphas, args = ( deformation_double_dagger, time ) )
	#print "PLSQ_Alpha:", plsq_alpha
	#print "len(PLSQ):", len( plsq_alpha[0] )

def residuals( x, deformation_dagger, time ):
	err = 0
	for i in range(0, len(time)):
		err = err + pow( ( deformation_dagger[i] - deformation_dagger_theory( time[i], x ) ), 2 )
	return err
	
def deformation_dagger_theory( time, x ):
	
	lambdas = []
	for i in range(0, 60, 5):
		lambdas.append( float( 1./pow(10, float(i)/10.) ) )

	stress = initTensor(0., 6)
	stress[0] = 20.
	#print stress
	
	for i in range(0, len(lambdas)):
		if x[i] < 0.:
			x[i] = 1000.
	
	for i in range(0, len(lambdas)):
		if i == 0:
			f = x[0]
		else:
			f = f + x[i] * (1. - exp( -lambdas[i-1]* time  ) )
	f = f * stress[0]
	
	return f
	
	
exercice02()