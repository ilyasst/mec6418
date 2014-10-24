from interconversion_personal_functions import *
import sympy as sy
from sympy.abc import t, s

mu0 = 10
mu1 = 2
mu2 = 5

lambda1 = 1
lambda2 = 10

print ""

mu = mu0 + mu1*sy.exp( -t*lambda1 ) + mu2*sy.exp( -t*lambda2 )
print "mu =", mu

print ""

mu_s = laplace_carson( mu, t, s )
print "mu_s=", mu_s

print ""

factor_mu_s = sy.factor( mu_s )
print "factor( mu_s ) =", factor_mu_s

print "factor(den):", sy.solve( sy.fraction(factor_mu_s)[0] )
print ""
print "ROOT0:", sy.solve( sy.fraction(factor_mu_s)[0] )[0]
print "ROOT1:", sy.solve( sy.fraction(factor_mu_s)[0] )[1]
print ""

gamma_s = ( s - sy.solve( sy.fraction(factor_mu_s)[0] )[0] )* (s - sy.solve( sy.fraction(factor_mu_s)[0] )[1] ) / sy.fraction(factor_mu_s)[1]

print "gamma_s =", gamma_s

print ""

print "apart( gamma_s ) =", sy.apart( gamma_s )

print ""
gamma_t = inverse_laplace_carson( gamma_s, t, s)
print "gamma_t:", gamma_t




