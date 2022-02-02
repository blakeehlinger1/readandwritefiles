import csv

customers = open('customers.csv','r')

customer_file = csv.reader(customers, delimiter=',')

#to skip a line if the file contains a header record
next(customer_file)

for record in customer_file:
    #print("Name:",record[1],record[2], "Country:",record[4])
    print("Name:","     ", "Country:")
    print(record[1],record[2],record[4])