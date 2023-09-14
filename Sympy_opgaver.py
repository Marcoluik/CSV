import sympy as sp
a = sp.Symbol("a")

udtryk = (5/-7)-2/3(3+a)
sp.pprint(udtryk)
sp.pprint(sp.cancel(udtryk))