import csv
import json
import pandas as pd
csvfile = "example.csv"

df = pd.read_csv(csvfile)

for index, row in df.items():
    print(row)


# for row in csv_read:
#     print(type(row))

# for row in csv_read[1:]:
#     temp = {}
#     for index, col in enumerate(cols):
#         temp[col] = row[index]
#     res.append(temp)

# print(res)