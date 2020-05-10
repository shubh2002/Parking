import csv
from datetime import date, time

columns = ['Date', 'Time', 'EmptySpot']

def write_csv(empty_spot, col):

    with open('parking_analytics.csv') as csvfile:
        csv_reader = csv.reader(csvfile, delimeter=',')
        if col:
            csv_reader.writerow(columns)
        else:
            csv_reader.writerow([f'{date.today()}', f'{time.now()}', f'{empty_spot}'])
