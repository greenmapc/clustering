import os
from csv import DictWriter

COLUMNS = ['brand', 'model', 'year', 'price', 'owners_count',
           'mileage', 'doors_count', 'class_auto', 'body_type']


def write_to_csv(data):
    with open("data.csv", "w", newline='') as out_file:
        writer = DictWriter(out_file, delimiter=',', fieldnames=COLUMNS)
        writer.writeheader()
        for data_page in data:
            writer.writerow(data_page)


def write_pd_to_csv(new_data, name):
    new_data.to_csv(name, index=False)
