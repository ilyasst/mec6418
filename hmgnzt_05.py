from interconversion_personal_functions import *
import sympy as sy
from sympy.abc import t, s, X
from numpy.linalg import inv, solve, pinv
from tensor_personal_functions import *



v0 = 0.7
v1 = 1. - v0

### C0
# k0
k0_0 = 10.
k0_1 = 1.2
lambdak0_1 = 1.
k0_2 = 0.5 
lambdak0_2 = pow( 10, (-1.5) )
k0_f = k0_0 + k0_1*sy.exp(-t*lambdak0_1) + k0_2*sy.exp(-t*lambdak0_2)
k0_s = laplace_carson(k0_f, t, s) ;

#mu0
mu0_0 = 2.
mu0_1 = 0.1
lambdamu0_1 = 1.
mu0_2 = 0.5
lambdamu0_2 = pow( 10, (-1.5) )
mu0_f = mu0_0 + mu0_1*sy.exp(-t*lambdamu0_1) + mu0_2*sy.exp(-t*lambdamu0_2)
mu0_s =  laplace_carson(mu0_f, t, s)


### C1
# k1
k1_0 = 100.
k1_1 = 15.
lambdak1_1 = pow( 10, (-0.5) )
k1_2 = 8.
lambdak1_2 = pow( 10, (-1.5) )
k1_f = k1_0 + k1_1*sy.exp(-t*lambdak1_1) + k1_2*sy.exp(-t*lambdak1_2) ;
k1_s = laplace_carson(k1_f, t, s) ;

#mu1
mu1_0 = 34.
mu1_1 = 3.
lambdamu1_1 = pow( 10, (-0.9) )
mu1_2 = 12.
lambdamu1_2 = pow( 10, (-1.2) )
mu1_f = mu1_0 + mu1_1*sy.exp(-t*lambdamu1_1) + mu1_2*sy.exp(-t*lambdamu1_2)
mu1_s = laplace_carson(mu1_f, t, s) 

###Eshelby
alpha_eshelby_s = ((3.*k0_s/(3.*k0_s+4.*mu0_s)))
beta_eshelby_s = ((6.*(k0_s + 2.*mu0_s)/(5.*(3.*k0_s + 4.*mu0_s))))

###Mori-Tanaka
alphaT0_s = 1.
alphaT1_s = (1./( 1. + alpha_eshelby_s*(1./(3.*k0_s))*3.*(k1_s - k0_s) ))

alphaA0_s = (1./(v0*alphaT0_s + v1*alphaT1_s))
alphaA1_s = (alphaT1_s*alphaA0_s) ;

alphaMT_s = (3.*k0_s + v1*3.*(k1_s - k0_s)*alphaA1_s)
kMT_s = (alphaMT_s/3.)

betaT0_s = 1.
betaT1_s = (1./( 1. + beta_eshelby_s*(1./(2.*mu0_s))*2.*(mu1_s - mu0_s) )) 

betaA0_s = (1./(v0*betaT0_s + v1*betaT1_s))
betaA1_s = (betaT1_s*betaA0_s)

betaMT_s = (2.*mu0_s + v1*2.*(mu1_s - mu0_s)*betaA1_s)
muMT_s = (betaMT_s/2.)

### Collocation
n = 5

# to
to = []
for i in range(0, n):
	to.append( float( pow( 10, (-2 + 4*(i)/(n-1)) ) ) )

# C
C = initTensor( 0., n, n )
for i in range(0, n):
	for j in range(0, n):
		C[i][j] = to[i]/( to[i]+to[j] )

# Delta_s
delta_kMT_s = kMT_s - kMT_s.subs(s,0)
print
print "kMT_s.subs(s,0):", kMT_s.subs(s,0)
print
#print "delta_kMT_s:", delta_kMT_s
#print
delta_muMT_s = muMT_s - muMT_s.subs(s,0)
print "kMT_s.delta_muMT_s(s,0):", muMT_s.subs(s,0)
print

delta_kMT_s_list = []
phi_k = []
for i in range(0, n):
	delta_kMT_s_list.append( delta_kMT_s.subs(s, to[i]) )
#phi_k = solve(C, delta_kMT_s_list)	
phi_k = solve( C, delta_kMT_s_list )
print "phi_k:"
print phi_k


delta_muMT_s_list = []
phi_mu = []
for i in range(0, n):
	delta_muMT_s_list.append( delta_muMT_s.subs(s, to[i]) )
phi_mu = solve( C,delta_muMT_s_list )
print "phi_mu:"
print phi_mu

# Summations
sumsk = 0
for i in range(0, n):
	sumsk_int = ( phi_k[i]*sy.exp(-to[i]*t))
	sumsk = sumsk + sumsk_int
kMT = kMT_s.subs(s, 0) + sumsk
print
print "kMT_s:", kMT_s, "Type:", type(kMT_s)
print
print "sumsk:", sumsk, "Type:", type(sumsk)
kMT1_1 = kMT.subs( t, 1.5 )
print
print "kMT1_1:"
print kMT1_1


sumsmu = 0
for i in range(0, n):
	sumsmu_int = phi_mu[i]*sy.exp(- to[i]*t )
	sumsmu = sumsmu + sumsmu_int
muMT = muMT_s.subs(s, 0) + sumsmu
muMT_1 = muMT.subs( t, 1.5 )
print
print "muMT_1:"
print muMT_1
