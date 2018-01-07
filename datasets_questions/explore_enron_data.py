#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("/Users/winson/PycharmProjects/ud120-projects/final_project/final_project_dataset.pkl", "r"))

# print enron_data.items()
# print enron_data.keys()
print enron_data['METTS MARK'].keys()
num_poi = 0

for name in enron_data.keys():
    if enron_data[name]["poi"] == 1:
        num_poi += 1
        print name

print num_poi

name = "Prentice James"
print enron_data[name.upper()]["total_stock_value"]
name = "Colwell Wesley"
print enron_data[name.upper()]["from_this_person_to_poi"]
name = "Skilling Jeffrey K"
print enron_data[name.upper()]
name = "Lay Kenneth l"
print enron_data[name.upper()]
name = "FASTOW ANDREW S"
print enron_data[name.upper()]