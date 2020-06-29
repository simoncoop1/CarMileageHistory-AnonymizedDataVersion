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
    parser.add_argument('regdate_motdate_motmileage',nargs=3,
                   help="""to de-anonymise data give the date vehicle was first 
                           registered, a date of an mot, and the mileage at that mot.
                            e.g "2008-04-01 2017-02-12 48901" would be the correct
                            parameter for first registered 1st April 2008, and MOT
                            on 12th Feb 2017, and an mileage at this MOT of 48901.""")
    parser.add_argument('--carid',dest='carid',
                   help='if you already know the carid you can provide it')
    parser.add_argument('--no_plot', dest='no_plot', action='store_true',
               help='if you just want just text data and no plot')

    args = parser.parse_args()

    #print(args.carid)

    if args.carid is not None:               
        theid = args.carid


    #theid = GetCarID("2007-05-01","2017-04-04","69646")
    #theid = GetCarID("2007-03-21","2017-06-30","114124")
    

    if args.carid is None:
        theid = GetCarID(args.regdate_motdate_motmileage[0],args.regdate_motdate_motmileage[1],args.regdate_motdate_motmileage[2])

    if args.no_plot:
        for c in dGenerateCars():
            if c[1]==carid:
              print(c)
        sys.exit()

    plotit(theid)
       

    print(help)
        
        
