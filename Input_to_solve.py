import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
import matplotlib.pyplot as plt
import csv
x = sp.Symbol("x")

def funktionsplotteren():
    """
    Funktionsplotteren tager som input en funktionsstreng, som skal plottes, og to tal, som er de nedre og de øverste grænser for plottet på x-aksen.
    """
    print("Velkommen til funktionsplotteren!")
    funktionsstreng = input("Skriv den funktion, som du gerne vil plotte. Husk at opløftet hedder **, og at x er den uafhængige variabel> ")
    minimum = float(input("Indtast den nedre grænse for plottet på x-aksen> "))
    maximum = float(input("Indtast den øvre grænse for plottet på x-aksen> "))
    funktion = parse_expr(funktionsstreng)
    sp.plot(funktion, (x, minimum, maximum))

def Differentiate():
    print("Velkommen til Differentieringsmaskinen 3000!")
    Diff = input(
        "Skriv den ligning der skal differentieres ")
    var = input("Skriv variablen > ")
    diff_tjek = parse_expr(Diff)
    var = parse_expr(var)
    diff_opskrevet = sp.Derivative(diff_tjek, var)
    sp.pprint(diff_opskrevet)
    sp.pprint(diff_opskrevet.doit())

def Integrate():
    print("Velkommen til Integrationsmaskinen 3000!")
    Integral = input(
        "Skriv den ligning der skal integreres ")
    var = input("Skriv variablen > ")
    yesno = input("Vil du bruge en grænse? y eller n > ")
    if yesno == "y":
        grænse1 = input("Indtast den nedre grænse for plottet på x-aksen> ")
        grænse2 = input("Indtast den øvre grænse for plottet på x-aksen> ")
        integral_tjek = parse_expr(Integral)
        parse_expr(grænse1)
        parse_expr(grænse2)
        var = parse_expr(var)
        integral_opskrevet = sp.Integral(integral_tjek, (var, grænse1, grænse2))
        sp.pprint(integral_opskrevet)
        sp.pprint(integral_opskrevet.doit())
        sp.plot(integral_opskrevet.doit())
    if yesno == "n":
        integral_tjek = parse_expr(Integral)

        var = parse_expr(var)
        integral_opskrevet = sp.Integral(integral_tjek, var)
        sp.pprint(integral_opskrevet)
        sp.pprint(integral_opskrevet.doit())

def ligning():
    print("Velkommen til logaritme-maskinen 3000!")
    log = input("Skriv ligningen > ")
    var = input("Skriv variablen > ")
    andenside = input("Skriv Andne side af lighedstegnet > ")
    sp.pprint(sp.N(sp.solveset(sp.Eq(log, andenside),var)))

def billag():
    X = []
    Y = []
    with open ("files/Bilag_Haardhed.csv") as datafil:
        csv_laeser = csv.reader(datafil, delimiter=",")
        next(csv_laeser)
        for linje in csv_laeser:
            #til float
            x, y = [float(element) for element in linje]
            X.append(x)
            Y.append(y)
    plt.plot(X, Y, label='Plot', color='blue')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Plot')
    plt.legend()
    plt.show()

def main():
    valg = input("Velkommen til altmulig-udregner-3000, vælg mellem func,   diff,   int,    ligning,    log,    billag")
    if valg == "func":
        funktionsplotteren()
    if valg == "diff":
        Differentiate()
    if valg == "int":
        Integrate()
    if valg == "ligning":
        ligning()
    if valg == "billag":
        billag()

if __name__ == "__main__":
    main()