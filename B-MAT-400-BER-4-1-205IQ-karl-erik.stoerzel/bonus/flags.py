import sys
import csv
import json
import math


def to_csv():
    u = float(sys.argv[1])
    s = float(sys.argv[2])
    with open("./data.csv", "w") as file:
        writer = csv.writer(file, delimiter=',')
        for i in range(201):
            res = (1 / (s * math.sqrt(2 * math.pi))) * (math.exp(-0.5 * math.pow((i - u) / s, 2)))
            res = round(res, 5)
            writer.writerow([i, res])


def to_json():
    u = float(sys.argv[1])
    s = float(sys.argv[2])
    data = {'values': []}
    for i in range(201):
        res = (1 / (s * math.sqrt(2 * math.pi))) * (math.exp(-0.5 * math.pow((i - u) / s, 2)))
        res = round(res, 5)
        data['values'].append({
            'X': i,
            'Y': res
        })
    with open("./data.json", "w") as file:
        json.dump(data, file)


def check_flag(flag):
    for i in range(1, len(sys.argv)):
        if sys.argv[i] == flag:
            return True
    return False
