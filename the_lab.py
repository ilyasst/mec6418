from import_data import *
import matplotlib.pyplot as plt


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
	for i in range(0, len(deformation2MPa)-1):
		deformation02_11.append( float(deformation2MPa[i][0]) ) 
		deformation02_22.append( float(deformation2MPa[i][1]) )
		deformation05_11.append( float(deformation5MPa[i][0]) ) 
		deformation05_22.append( float(deformation5MPa[i][1]) )

	print len(deformation02_11), len(time2MPa)
	
	#plt.plot(time2MPa, stress2MPa, 'r--', label = "Stress2MPa")
	plt.plot(time2MPa, deformation02_11, 'b--', label = "Def2Mpa_11")
	plt.plot(time2MPa, deformation02_22, 'g--', label = "Def2Mpa_22")
	plt.plot(time5MPa, deformation05_11, 'r--', label = "Def5Mpa_11")
	plt.plot(time5MPa, deformation05_22, 'y--', label = "Def5Mpa_22")
	plt.xlabel('time')
	plt.ylabel('stress')
	plt.legend( )
	plt.savefig('lab_stress_def_initial_data.png')
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


def 
	
determine_linearity()