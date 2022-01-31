def main():
    infile = open('clients.txt','r')

    #client_file = infile.read()
    counter = 1
    for client in infile:
        print(counter,". ", client.rstrip('\n'),sep="")
        counter += 1
main()
        



