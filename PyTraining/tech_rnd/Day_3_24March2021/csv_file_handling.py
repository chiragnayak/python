import csv

# Create the CSV File
def create_csv_file(fname):
    with open(fname, 'w', newline='') as csv_fhandle:
        # Configure the CSV Writer Object
        csv_writer = csv.writer(csv_fhandle, delimiter=',')

        # Header
        header = ('id', 'name', 'location', 'salary', 'team')
        csv_writer.writerow(header)

        # Data
        lst_of_recs = [(1, 'justin', 'blr', 5000, 'testing'),
                       (2, 'clark', 'hyd', 6000, 'testing'),
                       (3, 'davies', 'noi', 7000, 'support'),
                       (4, 'tris', 'mum', 8000, 'support'),
                       (5, 'manual', 'pune', 9000, 'testing')]
        csv_writer.writerows(lst_of_recs)

# Read the CSV File using reader method
def read_csv_using_reader(fname):
    with open(fname) as csv_read:
        all_recs = [tuple(rec) for rec in csv.reader(csv_read)]

    return all_recs

# Read the CSV File using DictReader method
def read_csv_using_dictreader(fname):
    with open(fname) as csv_read:
        all_recs = [dict(rec) for rec in csv.DictReader(csv_read)]

    return all_recs

print('-' * 75)

# Create the CSV File with contents
create_csv_file(r'files\data.csv')
print('CSV File Created')

print('-' * 75)

# Read the CSV File using reader method
recs = read_csv_using_reader(r'files\data.csv')
print('All Records -', recs)

# Parse the content from CSV File
print('Only 3rd Record -', recs[3])

# Index of team
idx_team = recs[0].index('team')
print('Team from 3rd Record -', recs[3][idx_team])

print('-' * 75)

# Read the CSV File using DictReader method
recs = read_csv_using_dictreader(r'files\data.csv')
print('All Records -', recs)

# Parse the content from CSV File
print('Only 3rd Record -', recs[2])
print('Team from 3rd Record -', recs[2]['team'])

print('-' * 75)
