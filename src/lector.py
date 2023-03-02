import csv

def write_to_csv(filename, data):

    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)

        for row in data:
            writer.writerow(row)