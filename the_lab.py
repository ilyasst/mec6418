from import_data import *


def determine_lineartiy_ratio( stress02, deformation02, stress0x, deformation0x ):
	ratio11 = []
	ratio22 = []
	deformation11 = []
	deformation22 = []
	for i in range(0, len(deformation02)):
		deformation11.append( defromation02[i][0] )
		deformation22.append( defromation02[i][1] )
		
	for i in range(0, len(stress) ):
		stress_ratio_i = float( stress02[i] )/float( stress0c[i] )
		def_ratio11_i = float( deformation11[i] )/float( deformation0x[i] )
		def_ratio22_i = float( deformation22[i] )/float( deformation0x[i] )
		ratio11.append(stress_ratio11_i/def_ratio_i)
		ratio.append(stress_ratio22_i/def_ratio_i)
	return ratio11, ratio22

def determine_linearity():

	time2MPa, stress2MPa, deformation2MPa = import_data_lab_fluage( "fluage-recouvrance-2MPa.csv" )
	time5MPa, stress5MPa, deformation5MPa = import_data_lab_fluage( "fluage-recouvrance-5MPa.csv" )
	time10MPa, stress10MPa, deformation10MPa = import_data_lab_fluage( "fluage-recouvrance-10MPa.csv" )
	tim13MPa, stres13MPa, deformatio13MPa = import_data_lab_fluage( "fluage-recouvrance-13MPa.csv" )
	time16MPa, stress16MPa, deformation16MPa = import_data_lab_fluage( "fluage-recouvrance-16MPa.csv" )
	time20MPa, stress20MPa, deformation20MPa = import_data_lab_fluage( "fluage-recouvrance-20MPa.csv" )
	time22MPa, stress22MPa, deformation22MPa = import_data_lab_fluage( "fluage-recouvrance-22MPa.csv" )
	time25MPa, stress25MPa, deformation25MPa = import_data_lab_fluage( "fluage-recouvrance-25MPa.csv" )
	time30MPa, stress30MPa, deformation30MPa = import_data_lab_fluage( "fluage-recouvrance-30MPa.csv" )
	time35MPa, stress35MPa, deformation35MPa = import_data_lab_fluage( "fluage-recouvrance-35MPa.csv" )
	
	print "Linear means that f(lamba * deformation ) = lambda * stress, with lambda real value"
	print "And f( deformation1 + deformation2 ) = f(deformation1) + f(deformation2) = stress1 + stress2 "
	
	
	ratio11_2MPa = determine_lineartiy_ratio( stress2MPa, deformation2MPa, stress2MPa, deformation2MPa )

	
determine_linearity()