from sympy.integrals import laplace_transform, inverse_laplace_transform
import sympy as sy

def laplace_carson( f, t, s ):
	l = laplace_transform( f, t, s)
	l_c = sy.simplify( s*l[0] )
	
	return l_c

def inverse_laplace_carson( f, t, s):
	f = sy.simplify( f/s )
	f = sy.apart( f )
	print "apart(f) =", f
	f_c = inverse_laplace_transform( f, t, s )
	
	return f_c