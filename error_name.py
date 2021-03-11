import csv
def Error_Print(Error_ID):
    results = []
    file = open("Errorlist.csv" , "r")
    reader = csv.reader(file)
    for row in reader:
        results.append([int(row[0]),row[1]])
    x = 0
    for x in results.length:
        if(results[0] == Error_ID):
            print("Error ",row[0], " :", row[1])
