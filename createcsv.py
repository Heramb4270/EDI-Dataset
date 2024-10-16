# create a csv file 800 lines in first column names file_name 

# fine name should go from 00001.png to 00800.png

import csv

with open('file.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(1, 801):
        writer.writerow([f'{str(i).zfill(5)}.png'])