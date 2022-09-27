import csv


rows = []

with open(input("Enter file name: "), "r") as file:
    alumni = csv.reader(file)
    header = next(alumni)
    for row in alumni:
        rows.append(row)

print(header)

