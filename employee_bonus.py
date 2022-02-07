import csv

def main():

    infile = open("EmployeePay.csv",'r')

    emp_file = csv.reader(infile, delimiter = ',')

    next(emp_file)

    outfile = open("Employee_Bonus.csv", 'w')

    outfile.write("ID" + "," + "FirstName" + "," + "LastName" + "," + "Salary" + "," + "bonus" + "," + "TotalPay" + "\n")

    for record in emp_file:
        id_num = record[0]
        firstname = record[1]
        lastname = record[2]
        salary = record[3]
        bonus = record[4]
        totalpay = float(record[3]) + (float(record[3])*float(record[4]))
        outfile.write(id_num +","+firstname + "," + lastname + "," + salary + "," + bonus + "," + format(totalpay) + "\n") 

    infile.close()
    outfile.close()
main()



