#!/usr/bin/env python3

import sys
import csv
import string

def get_application_data(csv_file_path):
    with open(csv_file_path, 'r') as csv_file:
        applications_csv = list(csv.reader(csv_file))
        if len(applications_csv) == 0:
            return {}
        first_row = applications_csv[0]
        
        applications = {k:[] for k in first_row}

        for row in applications_csv[1:]:
            for k, v in zip(first_row, row):
                applications[k].append(v)
        return applications
            
def load_animals():
    with open("animals.txt", 'r') as animals:
        return set(animals.read().split('\n'))
            

if len(sys.argv) < 2 :
    print("specify .csv file")
    exit(0)

csv_file_path = sys.argv[1]

applications = get_application_data(csv_file_path)

animal_database = load_animals()

animals = {}

for animal_answer in applications['Spirit Animal']:
    found = False
    for animal in animal_answer.split():
        animal = animal.lower().strip(string.punctuation)
        if len(animal) > 0 and animal in animal_database:
            animals.setdefault(animal, 0)
            animals[animal] += 1
            found = True
    if not found:
        # print(animal_answer)
        pass
    
total_animals = sum(animals.values())
sorted_animals = sorted(animals.items(), key=lambda x: x[1], reverse=True)

non_empty = sum([1 for ans in applications['Spirit Animal'] if len(ans)>0]) 


for a in sorted_animals:
    print("{}: {} ({:.2f}%)".format(a[0], a[1], 100*a[1]/total_animals))

print(total_animals)

