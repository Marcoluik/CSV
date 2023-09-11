import csv # importering af csv modukletf
from statistics import mean
fandango_scores=[]
with open ("files/fandango_scrape.csv") as Moviecomp:
    csv_laeser = csv.reader(Moviecomp,delimiter=",")
    next(csv_laeser)
    #next(csv_laeser)  #ville springe førte linje over
    firstrow = next(csv_laeser)
    next(csv_laeser)
    clmns = len(firstrow)
    print(clmns)
    for linje in csv_laeser:
        fandango = float(linje[2])
        ofrating = float(linje[1])
        fandango_scores.append = fandango
        #print(linje)
mean_fandango = mean(fandango_scores)
print(mean_fandango)