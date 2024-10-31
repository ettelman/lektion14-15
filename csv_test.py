import csv

# data = [
#     ['name', 'age', 'city'],
#     ['Bobbo', '37', 'Linköping'],
#     ['Karl', '25', 'Stockholm']
# ]

# with open('output.csv', 'w', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)

data = [
    {"name": "Bobbo", "age": 37, "city": "Linköping"},
    {"name": "Karl", "age": 25, "city": "Stockholm"}
]

with open('output.csv', 'w', encoding='utf-8') as file:
    headers = ["name", "age", "city"]
    writer = csv.DictWriter(file, fieldnames=headers)
    
    writer.writeheader()
    for row in data:
        writer.writerow(row)