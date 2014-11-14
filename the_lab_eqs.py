from math import *
from numpy import *
from tensor_personal_functions import *
from projectors_personal_functions import *

def heaviside(x):
	if x == 0.:
		return 0.5
	return 0. if x < 0 else 1.


def residuals( x, deformation_dagger, time, lambdas, sigma_m, car_times ):
	err = 0
	for j in range(0, len(sigma_m)):
		for i in range( 0, len(time)):
			err = err + pow( ( ( deformation_dagger[j][i] - deformation_dagger_theory( x, lambdas, time[i], sigma_m[j], car_times ) )/sigma_m[j] ), 2 )
			#print deformation_dagger[j][i], deformation_dagger_theory( x, lambdas, time[i], sigma_m[j], car_times )
	#print "ERR =", err
	return err


def deformation_dagger_theory( x, lambdas, time, sigma_m, car_times ):
	
	for i in range(0, len(lambdas)):
		if x[i] < 0.:
			x[i] = x[i]*x[i]
	
	y0 = 0
	y1 = 0
	y2 = 0
	y3 = 0
	
	y0 = x[0] * time * heaviside(time)
	for i in range(1, len(lambdas) ):
		y0 = y0  +  x[i] * ( time - ( (1. - exp(-lambdas[i-1]*time) )/lambdas[i-1]) ) * heaviside(time)
	eq1 = ( y0/car_times[0] ) * sigma_m
	
	y1 = x[0] * (time - car_times[0]) * heaviside( time - car_times[0] )
	for i in range( 1, len(lambdas) ):
		if time < car_times[0]:
			temp_time = car_times[0] - 1.
		else:
			temp_time = time
		y1 = y1 + x[i]*( (temp_time-car_times[0])-( (1.-exp(-lambdas[i-1]*(temp_time-car_times[0])))/lambdas[i-1])) * heaviside( temp_time - car_times[0] )
	eq2 = ( y1 / car_times[0] ) * sigma_m

	y2 = x[0]*(time-car_times[1])*heaviside(time-car_times[1])
	for i in range(1, len(lambdas)):
		if time < car_times[1]:
			temp_time = car_times[1] - 1.
		else:
			temp_time = time
		y2 = y2 + x[i] * ( (temp_time - car_times[1]) - ( (1.- exp( -lambdas[i-1]*(temp_time-car_times[1])))/lambdas[i-1])) * heaviside(temp_time-car_times[1])
	eq3 = (y2/(car_times[2]-car_times[1])) * sigma_m

	y3 = x[0]*(time-car_times[2])*heaviside(time-car_times[2])
	for i in range(1, len(lambdas)):
		if time < car_times[1]:
			temp_time = car_times[2] - 1.
		else:
			temp_time = time
		y3 = y3 + x[i]*( (temp_time-car_times[2]) - ( (1.- exp(-lambdas[i-1]*(temp_time-car_times[2])))/lambdas[i-1]))*heaviside(temp_time-car_times[2])
	eq4 = y3/(car_times[2]-car_times[1])*sigma_m
	
	y = eq1 - eq2 - eq3 + eq4
	
	return y
			
			
def determine_epstheorique( fmin_slsqp_alpha, fmin_slsqp_beta, lambdas, sigma_m_scalar, time, car_times):
	epstheorique = initTensor( 0., len(time), 6 )
	stress = []
	stress.append( sigma_m_scalar )
	for i in range(0, 5):
		stress.append( 0. )
	print "STRESS VECTOR:", stress
	
	for i in range(0, len(time) ):
		s = souplesse_fluage_def( fmin_slsqp_alpha, fmin_slsqp_beta, lambdas, time[i], car_times )
		epstheorique[i] = dot( s, stress )
	return epstheorique
		

def souplesse_fluage_def( fmin_slsqp_alpha, fmin_slsqp_beta, lambdas, time, car_times ):

	s = initTensor( 0., 6, 6 )

	J_tensor4 = generate_J_tensor4()
	J_matrix4 = tensor4_to_voigt4( J_tensor4 )
	
	K_tensor4 = generate_K_tensor4()
	K_matrix4 = tensor4_to_voigt4( K_tensor4 )
	
	y0 = ( dot(fmin_slsqp_alpha[0],J_matrix4) + dot(fmin_slsqp_beta[0],K_matrix4))* time * heaviside(time)
	for i in range(1, len(lambdas) ):
		y0 = y0  + ( dot(fmin_slsqp_alpha[i],J_matrix4) + dot(fmin_slsqp_beta[i],K_matrix4)) * ( time - ( (1. - exp(-lambdas[i-1]*time) )/lambdas[i-1]) ) * heaviside(time)
	eq1 = ( y0/car_times[0] ) 
	
	y1 = ( dot(fmin_slsqp_alpha[0],J_matrix4) + dot(fmin_slsqp_beta[0],K_matrix4)) * (time - car_times[0]) * heaviside( time - car_times[0] )
	for i in range( 1, len(lambdas) ):
		if time < car_times[0]:
			temp_time = car_times[0] - 1.
		else:
			temp_time = time
		y1 = y1 + ( dot(fmin_slsqp_alpha[i],J_matrix4) + dot(fmin_slsqp_beta[i],K_matrix4))*( (temp_time-car_times[0])-( (1.-exp(-lambdas[i-1]*(temp_time-car_times[0])))/lambdas[i-1])) * heaviside( temp_time - car_times[0] )
	eq2 = ( y1 / car_times[0] )

	y2 = ( dot(fmin_slsqp_alpha[0],J_matrix4) + dot(fmin_slsqp_beta[0],K_matrix4))*(time-car_times[1])*heaviside(time-car_times[1])
	for i in range(1, len(lambdas)):
		if time < car_times[1]:
			temp_time = car_times[1] - 1.
		else:
			temp_time = time
		y2 = y2 + ( dot(fmin_slsqp_alpha[i],J_matrix4) + dot(fmin_slsqp_beta[i],K_matrix4)) * ( (temp_time - car_times[1]) - ( (1.- exp( -lambdas[i-1]*(temp_time-car_times[1])))/lambdas[i-1])) * heaviside(temp_time-car_times[1])
	eq3 = (y2/(car_times[2]-car_times[1])) 

	y3 =( dot(fmin_slsqp_alpha[0],J_matrix4) + dot(fmin_slsqp_beta[0],K_matrix4))*(time-car_times[2])*heaviside(time-car_times[2])
	for i in range(1, len(lambdas)):
		if time < car_times[1]:
			temp_time = car_times[2] - 1.
		else:
			temp_time = time
		y3 = y3 + ( dot(fmin_slsqp_alpha[i],J_matrix4) + dot(fmin_slsqp_beta[i],K_matrix4))*( (temp_time-car_times[2]) - ( (1.- exp(-lambdas[i-1]*(temp_time-car_times[2])))/lambdas[i-1]))*heaviside(temp_time-car_times[2])
	eq4 = y3/(car_times[2]-car_times[1])
	
	y = eq1 - eq2 - eq3 + eq4

	return y
	