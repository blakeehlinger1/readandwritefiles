import csv

def main():

    customers = open('customers.csv','r')
    #outfile = open("customer_country.csv",'w')

    customer_file = csv.reader(customers, delimiter=',')

    #to skip a line if the file contains a header record
    next(customer_file)

    outfile = open("customer_country.csv",'w')

    outfile.write("FirstName"+ "," + "LastName"+ ","+"Country""\n")

    for record in customer_file:
        firstname = record[1]
        lastname = record[2]
        country = record[4]

        outfile.write(firstname + ',' + lastname + ',' + country+ "\n")
    customers.close()
    outfile.close()
main()