import csv
from googlesearch import search

with open('refinedList.csv', newline='') as f:
    reader = csv.reader(f)
    your_list = list(reader)

domains = []

for x in your_list:
    domains.append(search(str(x), num_results=1))
    print(domains)

with open('finalized.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(domains)





