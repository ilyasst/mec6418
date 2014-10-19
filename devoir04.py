from numpy import *
from tensor_personal_functions import *
from convenient_objects import *
from projectors_personal_functions import *
from import_data import *
import matplotlib.pyplot as plt

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
		
	
	plt.plot(time5MPa, deformation5MPa, 'ro', time10MPa, deformation10MPa, 'bs')
	plt.xlabel('time5MPa')
	plt.ylabel('deformation5MPa')
	plt.savefig('5MPa.png')
	
exercice01()