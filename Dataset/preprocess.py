""" prune dataset """
import csv
import random

# out_file = '../backup/NYCtree1.csv'
out_file = "food_inspections_1.csv"
current_out_writer = csv.writer(open(out_file, 'w'), delimiter=',')
row_limit = 4000

rand_idx = random.sample(range(220866), row_limit)

with open('Food_Inspections.csv', 'r')as f:
    reader = csv.reader(f, delimiter=',')
    header, *data = list(reader)
    current_out_writer.writerow(header)
    for idx in rand_idx:
        current_out_writer.writerow(data[idx])
    # for i, row in enumerate(data):
        # if i+1 > row_limit:
        #     break
        # current_out_writer.writerow(row)

