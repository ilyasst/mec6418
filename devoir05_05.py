from interconversion_personal_functions import *

mu0 = 10.
mu1 = 2.
mu2 = 5.

lambda1 = 1.
lambda2 = 10.

mu = mu0 + mu1*sy.exp( -t*lambda1 ) + mu2*sy.exp( -t*lambda2 )
mu_s = laplace_carson( mu, t, s )

print mu_s




