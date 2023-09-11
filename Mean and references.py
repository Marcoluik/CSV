import csv # importering af csv modukletf
from statistics import mean
fandango_lst=[]
rating_lst=[]
with open ("files/fandango_scrape.csv") as Moviecomp:
    csv_laeser = csv.reader(Moviecomp,delimiter=",")
    firstrow = next(csv_laeser)
    clmns = len(firstrow)
    print(f"Længden af rækkerne er {clmns}")
    for linje in csv_laeser:
        Titel, rating, fandango,votes = linje
        fandango_lst.append(float(fandango))
        rating_lst.append(float(rating))
print(f"Gennemsnittet af fandangos stemmmer på film er: {mean(fandango_lst)}")
print(f"Gennemsnittet af Andres stemmmer på film er: {mean(rating_lst)}")

