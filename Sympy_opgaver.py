import sympy as sp
#import af symbols
a, b, c, d, e, x, y = sp.symbols("a b c d e x y")
#Udtryk
def saml_udtryk():
    udtryk = (-(5/7)-2)/(3*(3+a))
    sp.pprint(udtryk)
    sp.pprint(sp.cancel(udtryk))

    udtryk_b = ((4*a)/b) / ((b)/c)
    sp.pprint(udtryk_b)
    sp.pprint(sp.cancel(udtryk_b))
def expand_udtryk():
    udtryk_c = (5*b+a)**2
    sp.pprint(udtryk_c)
    sp.pprint(sp.expand(udtryk_c))

    udtryk_d = (1+(a/b))*(1+a)
    sp.pprint(udtryk_d)
    sp.pprint(sp.expand(udtryk_d))

    udtryk_e = ((b/a)-(a/b))**2
    sp.pprint(udtryk_e)
    sp.pprint(sp.expand(udtryk_e))
def udvid_log():
    udtryk_f = sp.log(x*y)
    sp.pprint(udtryk_f)
    sp.pprint(sp.expand_log(udtryk_f, force=True))

    udtryk_g = sp.log((3*x**1.5/y))
    sp.pprint(udtryk_g)
    sp.pprint(sp.expand_log(udtryk_g,force=True))

# LIGNINGER
def ligningløs():
    ligning_1 = sp.Eq(1/(x-1),2*x-3)
    sp.pprint(sp.solve(
ligning_1,x))
#ligningløs()

#funktioner
def funktioner():
    x_værdier = 2, 6, 14, 20, 26
    funktion_1 = sp.log(x ** 3 + 2) * sp.sqrt(x)
    funktionsvaerdier = [funktion_1.subs(x, x_vaerdi) for x_vaerdi in x_værdier]
    ez_values = [funktion_1.subs(x, x_val).evalf() for x_val in x_værdier]
    sp.plot(funktion_1, (x, 1, 20), yscale='log')
    sp.pprint(ez_values)
    sp.pprint(funktionsvaerdier)
#funktioner()

def diff_eksempel():

    f = (3 * x ** 2 - sp.sqrt(x)) / (2 + x)
    print("Med funktionen sp.diff")
    sp.pprint(sp.diff(f, x, 1))  # læg mærke til x og 1 som de sidste argumenter.
    print("Med metoden .diff")
    sp.pprint(f.diff(x, 1))  # Læg mærke til x og 1 som de sidste argumenter.
def diffopgaver1():
    f = ((8 * x**4 + 4)*(3*x**3-2*x+7))
    g = ((-3*x**2-5*x-6)/(x-7))
    h = (sp.sqrt(9*x)-4/x)

    fm = sp.Derivative(f,x)
    fg = sp.Derivative(g, x)
    fh = sp.Derivative(h, x)
    #Skrive dem op ved derivative og bagefter
    #do it funktion for at differentiere dem
    #sp.pprint(fm)
    #sp.pprint(fg)
    #sp.pprint(fh)
    #sp.pprint(fm.doit())
    #sp.pprint(fg.doit())
    #sp.pprint(fh.doit())
    #Man kan også bare udregne dem med det samme
    sp.pprint(sp.diff(f,x,1)) # func, var, gange
    sp.pprint(sp.expand(sp.diff(f,x,1)))
    sp.pprint(sp.diff(g, x, 1))
    sp.pprint(sp.expand(sp.diff(g, x, 1)))
    sp.pprint(sp.diff(h, x, 1))
    sp.pprint(sp.expand(sp.diff(h, x, 1)))

def diffopgaver2():
    f = ((8 * x**4 + 4)*(3*x**3-2*x+7))
    g = ((-3*x**2-5*x-6)/(x-7))
    h = (sp.sqrt(9*x)-4/x)

    fm = sp.Derivative(f,x)
    fg = sp.Derivative(g, x)
    fh = sp.Derivative(h, x)
    #Skrive dem op ved derivative og bagefter
    #do it funktion for at differentiere dem
    sp.pprint(fm)
    sp.pprint(fg)
    sp.pprint(fh)
    sp.pprint(fm.doit())
    sp.pprint(fg.doit())
    sp.pprint(fh.doit())
#diffopgaver1()
#diffopgaver2()

def intergral():
    f = (3*x**-8)-1/x+8
    sp.pprint(sp.Integral(f,x))
    sp.pprint(sp.Integral(f,x).doit())
    g = sp.E**x-x**sp.E
    sp.pprint(sp.Integral(g, x))
    sp.pprint(sp.Integral(g, x).doit())

    h = ((x**2-x)/x)
    sp.pprint(sp.Integral(h,(x,1,2)))
    sp.pprint(sp.Integral(g, x).doit())

    j = (x**2 +1)
    sp.pprint(sp.Integral(j,(x,0,1)))
    sp.pprint(sp.Integral(j,(x)).doit())
intergral()

def intergralbosslevel():
    boss = sp.Eq(x**a)
    sp.pprint(sp.Integral(boss,(-a,10,)))
    solution = sp.nsolve(sp.Eq(boss, 1, 1))
intergralbosslevel()
