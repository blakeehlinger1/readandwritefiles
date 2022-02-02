import csv

def main():

    infile = open("Student_Scores.csv",'r')

    score_file = csv.reader(infile, delimiter = ',')

    next(score_file)

    outfile = open("student_avg.csv",'w')

    for record in score_file:
       name = record[0]
       score1 = record[1]
       score2 = record[2]
       score3 = record[3]
       avg = (float(record[1]) + float(record[2]) + float(record[3]))/3
       outfile.write(name + "," + score1 + "," + score2 + "," + score3 + "," + format(round(avg,2)) + "\n") 
    
    infile.close()
    outfile.close()
    
main()