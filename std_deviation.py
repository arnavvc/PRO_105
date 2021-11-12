import math
import csv
with open("data.csv", newline="")as f:
    reader = csv.reader(f)
    file_data = list(reader)

    data = file_data[0]
    def mean(data):
        n = len(data)
        total = 0
        for x in data:
            total += int(x)
            mean = total/n
            return mean
            
            squaredList = []
            for number in data:
                e = int(number) - mean(data)
                a = a** 2
                squared_list.append(a)
                print(std_deviation)
