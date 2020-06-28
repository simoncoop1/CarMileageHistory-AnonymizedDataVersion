import os
import csv
import argparse
import sys
import plot

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

def plotit(car_id):

    thelist= []

    for c in dGenerateCars():

        if c[1]==theid:
            thelist.append(c)   


    thelist =sorted(thelist, key=lambda r: r[2])
    print(thelist)

    milages = []
    dates = []
    for a in thelist:
        milages.append(int(a[6]))
        dates.append(a[2])

    plot.plotIt(dates,milages)

#your car of interest needs to be de-anonymised before anything interesting can be done
#this is done but taking key pieces of information about the history of your car. This
#can be obtained from https://www.gov.uk/check-mot-history and entering you registration
# number.
def GetCarID(first_registered,amot_date,amot_mileage):
    for c in dGenerateCars():
        if c[13]==first_registered and  c[2]==amot_date and c[6]==str(amot_mileage):
            print("the carid is: " + c[1])
            return c[1]


if __name__ == "__main__":
    # this won't be run when imported

    #parse arguments
    parser = argparse.ArgumentParser(description='comparing books for unique words')
    parser.add_argument('carid',nargs=1,
                   help='search all records for all occurences of specified car_id')
    parser.add_argument('--plot', dest='plot', action='store_true',
               help='plot it')

    args = parser.parse_args()

    #print(args.carid)

                   
    theid = args.carid.pop()

    if args.plot:
        plotit(theid)
        sys.exit()

    #for c in dGenerateCars():
        #if len(c)<2:
        #    print("??")
        #    print(c)
        #    continue
    #    if c[1]=='1103092882':
    #        print(c)


    theid = GetCarID("2007-05-01","2017-04-04","69646")
    plotit(theid)
       

    print(help)
        
        
