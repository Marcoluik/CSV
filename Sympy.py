import sympy as sp

#SYMPFY COMMANDS
def udtryk():
    # a defineres til at være et symbol
    a = sp.Symbol("a")

    # Nu oprettes et udtryk
    # Læg mærke til at alle gangetegn skal skrives ind.
    udtryk_b = (1+a)/(3*(2+1))*2/a
    # Nedenfor printes udtrykket ud på en "pæn" måde
    sp.pprint(udtryk_b)
def udvid():
    x = sp.Symbol("x")
    udtryk = (x + 1) ** 2
    print("Oprindeligt udtryk")
    sp.pprint(udtryk)
    print("Udviddet udtryk")
    sp.pprint(sp.expand(udtryk))
def faktorisering():

    x = sp.Symbol("x")
    udtryk = x ** 3 - x ** 2 + x - 1
    print("Oprindeligt udtryk")
    sp.pprint(udtryk)
    print("Faktoriseret udtryk")
    sp.pprint(sp.factor(udtryk))
def samle_ledene():

    x, y, z = sp.symbols("x, y, z")
    udtryk = x * y + x - 3 + 2 * x ** 2 - z * x ** 2 + x ** 3
    print("Oprindeligt udtryk")
    sp.pprint(udtryk)
    print("Samlede led")
    sp.pprint(sp.collect(udtryk, x))
def saml_brøk():
    x = sp.Symbol("x")
    udtryk = (3 * x / 2 - 2) / (x - 4) + 1 / x
    print("Oprindeligt udtryk")
    sp.pprint(udtryk)
    print("Udtryk på én brøkstreg")
    sp.pprint(sp.cancel(udtryk))

def opdel_brøK():
    x = sp.Symbol("x")
    udtryk = (4 * x ** 3 + 21 * x ** 2 + 10 * x + 12) / (x ** 4 + 5 * x ** 3 + 5 * x ** 2 + 4 * x)
    print("Oprindeligt udtryk")
    sp.pprint(udtryk)
    print("Opdeling i flere mindre brøker")
    sp.pprint(sp.apart(udtryk))

def simplificering():
    x = sp.Symbol("x")
    udtryk = (x ** 3 + x ** 2 - x - 1) / (x ** 2 + 2 * x + 1)
    print("Oprindeligt udtryk")
    sp.pprint(udtryk)
    print("Simplificeret udtryk")
    sp.pprint(sp.simplify(udtryk))

def others():
    #https://docs.sympy.org/latest/tutorials/intro-tutorial/simplification.html
    sp.trigsimp
    sp.expand_trig
    sp.powsimp
    sp.expand_power_exp
    sp.expand_power_base
    sp.powdenest
    sp.expand_log
    sp.logcombine

udtryk()
udvid()
faktorisering()
samle_ledene()
saml_brøk()
opdel_brøK()
simplificering()