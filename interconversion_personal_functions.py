from sympy.integrals import laplace_transform
from sympy.abc import t, s
import sympy as sy

def laplace_carson( f, t, s ):
	l = laplace_transform( f, t, s)
	l_c = sy.simplify( s*l[0] )
	
	return l_c