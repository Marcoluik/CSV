
#Generators and lists
gen = (i for i in range(10))
print(gen)
for element in gen:
    print(f"først-{element}")
for element in gen:
    print(f"anden--{element}")
#Læg mærke til at når generatoren først er brugt er den tom. dermed printes nr 2 ikke.
#hvis man har en meget lang kode der kun skal bruges en gang er det smartere at bruge generator


liste = [i for i in range(10)]
print(liste)# Printer [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for element in liste:
    print(element) # printes som string

