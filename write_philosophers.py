def main():
    #open file
    outfile = open('philosophers.txt','w')

    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')
    #close file
    outfile.close()

def add_my_name():
    outfile = open('philosophers.txt','a')
    outfile.write('Blake Ehlinger\n')

    outfile.close()   

main()
add_my_name()
