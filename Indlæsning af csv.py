import csv
with open("files/Afkoeling_af_kaffe_nul_grader_udenfor.csv") as datafil:
    csv_laeser = csv.reader(datafil, delimiter=",") # delimiter = "," indikere at linjer skilles m komma
    for linje in csv_laeser:
        print(linje)