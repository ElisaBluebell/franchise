import sympy

a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q = sympy.symbols("a b c d e f g h i j k l m n o p q")

f1 = sympy.Eq(21*a+29*b+11*e+f+7*g+98*h+85*i+2359*j+9*k+1001*l+188*m+o+11*p+34*q, 1)
f2 = sympy.Eq(12*a+2*b+2*c+20*i+97*j+2*k+167*l+30*m+o+21*p+7*q, 1)
f3 = sympy.Eq(3*a+21*c+2*d+16*e+7*f+4*g+191*h+35*i+12059*j+16*k+1310*l+239*m+n+4*o+2*p+37*q, 4)
f4 = sympy.Eq(5*a+21*c+2*d+13*e+6*f+5*g+190*h+36*i+8822*j+12*k+1258*l+252*m+n+2*o+p+37*q, 3)
f5 = sympy.Eq(a+7*c+9*e+31*h+i+10372*j+7*k+233*l+36*m+p, 1)
f6 = sympy.Eq(2*b+7*c+2*e+12*h+8*i+407*j+176*l+18*m+o+p+k+6*q, 1)
f7 = sympy.Eq(a+26*l+10*m+n+9*p+q, 1)
f8 = sympy.Eq(7*a+38*c+11*e+8*f+14*g+97*h+8*c+i+5947*j+3*k+58*i+1195*l+210*m+p+8*k+20*q, 1)
f9 = sympy.Eq(m+2*g+h+40*l+12*m+n+3*o, 1)
f10 = sympy.Eq(e+4*f+h+2*i+51*l+20*m+2*n+13*p+5*q, 1)
f11 = sympy.Eq(2*a+22*c+14*e+f+10*g+67*h+4*c+i+4371*j+2*k+29*i+621*l+90*m+p+5*k+7*q, 1)
f12 = sympy.Eq(15*a+19*c+d+8*e+f+19*g+46*h+8*c+i+2119*j+4*k+70*i+870*l+177*m+4*o+p+7*k+20*q, 1)
f13 = sympy.Eq(16*a+b+4*c+2*e+f+12*h+3*c+30*i+510*j+4*i+k+277*l+49*m+2*n+o+33*p+2*k+12*q, 1)
f14 = sympy.Eq(2*a+7*c+d+4*e+5*g+18*h+c+i+3352*j+3*i+249*l+38*m+2*n+11*p+k+11*q, 1)
f15 = sympy.Eq(9*a+6*c+2*e+33*f+3*g+15*h+6*c+i+432*j+2*k+17*i+164*l+33*m+3*p+4*k+2*q, 0)
f16 = sympy.Eq(2*a+8*c+d+8*e+33*f+4*g+130*h+5900*j+i+4*k+5*i+677*l+87*m+n+o+2*p+9*k+7*q, 3)
f17 = sympy.Eq(47*m+i+3*f+c+12*c+i+21*h+q+4*e+14*p+6*i+301*l+2*k+k+c+4149*j, 1)

print(sympy.solve([f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17]))

