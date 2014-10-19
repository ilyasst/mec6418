from numpy import *
from tensor_personal_functions import *
from convenient_objects import *
from projectors_personal_functions import *
from import_data import *
import matplotlib.pyplot as plt
from convenient_objects import *

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
	
	print "Stress:"
	stress = initTensor(0., 6)
	stress[0] = 20
	print stress
	
	
	plt.plot(time, deformation11, 'ro', label = "Def11")
	plt.plot( time, deformation22, 'bs', label = "Def22")
	plt.xlabel('time')
	plt.title("Stress: 20MPa")
	plt.ylabel('deformations')
	plt.legend()
	plt.savefig('04-02_initial_data.png')
	plt.close()
	
	print "Check 04-02_initial_data.png for initial data plot"
	
	
	lambdas = []
	for i in range(0, 50, 5):
		lambdas.append( 1./pow(10, float(i)/10) )
		
	print "Determining list deformation dagger..."
	deformation_dagger = []
	for i in range(0, len(time)):
		deformation_dagger.append( deformation11[i] - deformation22[i] )
		
	print "Determining list deformation double dagger..."
	deformation_double_dagger = []
	for i in range(0, len(time)):
		deformation_double_dagger.append( deformation11[i] + 2*deformation22[i] )
		
	popt, pcov = curve_fit(deformation_dagger_theory, time, deformation_dagger)
		
	
	
	
	
#exercice01()
exercice02()