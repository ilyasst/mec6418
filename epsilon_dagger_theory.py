

def heaviside(x):
	if x == 0.:
		return 0.5

	return 0. if x < 0 else 1.

def residuals():
	print 

#def residuals( x, deformation_dagger, time, stress, lambdas ):
	#err = 0
	#for i in range( 0, len(time) ):
		#err = err + pow( ( deformation_dagger[i] - deformation_dagger_theory( stress, lambdas, time[i], x ) ), 2 )
	#return err

def deformation_dag_theory( x, lambdas, time, sigma_m, car_times ):
	
	y0 = 0
	y1 = 0
	y2 = 0
	y3 = 0
	
	y0 = x[0] * time * heaviside(time)
	for i in range(1, len(lambdas) ):
		y0 = y0  +  x[i] * ( time - ( (1 - exp(-lambdas[i-1]*time) )/lambdas[i-1]) ) * heaviside(time)
	eq1 = ( y0/car_times[0] ) * sigma_m
	
	y1 = x[0] * (time - car_times[0]) * heaviside( time - car_times[0] )
	for i in range( 1, len(lambdas) ):
		if time < car_times[0]:
			temp_time = car_times[0] - 1.
		else:
			temp_time = time
		y1 = y1 + x[i]*( (temp_time-car_times[0])-( (1-exp(-lambdas[i-1]*(temp_time-car_times[0])))/lambdas[k-1]))
	eq2 = ( y1 / car_times[0] ) * sigma_m

	y2 = x[0]*(time-car_times[1])*heaviside(time-car_times[1])
	for i in range(1, len(lambdas)):
		if time < car_times[1]:
			temp_time = car_times[1] - 1.
		else:
			temp_time = time
		y2 = y2 + x[i] * ( (temp_time - car_times[1]) - ( (1- exp( -lambdas[i-1]*(temp_time-car_times[1])))/lambdas[k-1])) * heaviside(temp_time-car_times[1])
	eq3 = (y2/(car_time[2]-car_time[1])) * sigma_m

	y3 = x[0]*(time-car_time[2])*heaviside(time-car_time[2])
	for i in range(1, len(lambdas)):
		if time < car_times[1]:
			temp_time = car_times[2] - 1.
		else:
			temp_time = time
		y3 = x[i]*( (temp_time-car_times[2]) - ( (1- exp(-lambdas[k-1]*(temp_time-car_times[2])))/lambdas[k-1]))*heaviside(temp_time-car_time[2])
	eq4 = y3/(car_times[2]-car_times[1])*sigma_m
	
	y = eq1 + eq2 + eq3 + eq4
	
	return y
			
			
	