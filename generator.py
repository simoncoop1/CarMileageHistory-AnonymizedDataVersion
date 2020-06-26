import os
import csv
import argparse

##iterate all records in the data
def dGenerateCars():
    current = 0
    fileno = 0
    filescsv = []
    filestxt = []

    ##get list of files
    for f in os.listdir('.'):
        if(f.endswith(".txt")& f.startswith("test")):
            filestxt.append(f)
        if f.endswith(".csv"):
            filescsv.append(f)



    for f in filestxt:


        with open(f, newline='') as txtfile:
            areader = csv.reader(txtfile, delimiter='|')

            for row in areader:
                yield row

        #count = 0

    for f in filescsv:
        with open(f, newline='') as csvfile:
            areader = csv.reader(csvfile, delimiter=',',doublequote=False)
            #print(f)

            for row in areader:
                #count+=1
                #print(count)
                yield row

if __name__ == "__main__":
    # this won't be run when imported

    #parse arguments
    parser = argparse.ArgumentParser(description='comparing books for unique words')
    parser.add_argument('carid',nargs=1,
                   help='search all records for all occurences of specified car_id')

    args = parser.parse_args()

    #print(args.carid)

                   
    theid = args.carid.pop()

    help = ""
    for c in dGenerateCars():
        #if len(c)<2:
        #    print("??")
        #    print(c)
        #    continue
        #if c[1]=='591469624':
        if c[1]==theid:
            print(c)
        
        #if len(c)>14:
        #    help+=("\""+c[0]+"\",")

    print(help)
        
        
