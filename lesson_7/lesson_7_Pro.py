import csv
import pandas as pd
import json
import time

start = time.time()
car_data = []
# Считывание файла построчно
f = open('data_text')
for line in f:
    line = line.lstrip(' ').split("\n")[0]
    line = line.split(' ')
    for _ in range(5):
        try:
            line.remove('')
        except:
            pass
    car_data.append(line)
f.close()
print(car_data)
print()

DataFrame_from_csv = pd.read_csv('example_time.csv', sep=',')
print(type(DataFrame_from_csv))
print(DataFrame_from_csv)
print()

with open('example_time.csv', 'w') as f:
    writer = csv.writer(f, delimiter=',')
    car_data.append(['time_report_CSV', time.time() - start])
    writer.writerows(car_data)
print('Writing complete!')
print()

with open('car_data_json_time.txt', 'w') as f:
    car_data.append(['time_report_json', time.time() - start])
    json.dump(car_data, f)

dict_to_json = json.dumps(car_data)
print(type(car_data), car_data)

# load, loads
with open('car_data_json_time.txt') as f:
    data = json.load(f)
print(type(data), data)
print()

car_data_1 = json.loads(dict_to_json)
print(type(car_data_1), car_data_1)