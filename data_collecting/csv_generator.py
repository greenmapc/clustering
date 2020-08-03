import os
from csv import DictWriter

COLUMNS = ['brand', 'model', 'year', 'color', 'price', 'owners_count', 'region',
           'mileage', 'doors_count', 'class_auto', 'name_auto', 'trunk_volume']


# df = pd.DataFrame(, columns = COLUMNS)
# df.to_csv(r'/path/to/cartridge_accounting.csv')

def write_to_csv(data):
    with open("data.csv", "w", newline='') as out_file:
        print(os.path.abspath("/"))
        writer = DictWriter(out_file, delimiter=',', fieldnames=COLUMNS)
        writer.writeheader()
        for data_page in data:
            writer.writerow(data_page)
