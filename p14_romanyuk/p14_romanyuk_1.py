import csv
with open('StrayKids.csv', 'w', newline='') as csvfile:
    fieldnames = ['Composition', 'Year']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Composition': 'Christmas EveL',
                     'Year': '2021'})
    writer.writerow({'Composition': 'Red Lights',
                     'Year': '2021'})
    writer.writerow({'Composition': 'Wolfgang',
                     'Year': '2021'})
    writer.writerow({'Composition': 'Thunderous',
                     'Year': '2021'})
    writer.writerow({'Composition': 'Domino',
                     'Year': '2021'})
    writer.writerow({'Composition': "God's Menu",
                     'Year': '2020'})
    writer.writerow({'Composition': 'All in',
                     'Year': '2020'})
    writer.writerow({'Composition': 'Maknae on Top',
                     'Year': '2021'})
    writer.writerow({'Composition': 'Back Door',
                     'Year': '2020'})
    writer.writerow({'Composition': 'Miroh',
                     'Year': '2019'})

with open('StrayKids.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for heading in reader.fieldnames:
        print(heading, end=' ')
    print('\n', '-'*30, sep='')
    for row in reader:
        print(row['Composition'], row['Year'])