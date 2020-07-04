import os
import csv
import argparse
import sys
import plot

import matplotlib.pyplot as plt

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

    title = ""

    for c in dGenerateCars():


        if c[1]==theid:
            thelist.append(c)
            if len(title)==0:
                fuel = c[11].replace("DI","Diesel").replace("PE","Petrol")
                title = c[8]+ " " + c[9]+ " " + c[10]+ " " + fuel+ " " + c[12]+ "cc First-Registered:" + c[13]


    thelist =sorted(thelist, key=lambda r: r[2])
    print(thelist)

    milages = []
    dates = []
    for a in thelist:
        milages.append(int(a[6]))
        dates.append(a[2])

    plot.plotIt(dates,milages,title)

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
    parser.add_argument('--question1', dest='question1', action='store_true',
               help="""For model  Octavia,Golf,Focus,Astra in 2019, for cars over 200k
                     how many are diesel and how many petrol""")
    parser.add_argument('--question2', dest='question2', action='store_true',
               help="""See if the average age of a vehicle changed between 2009 and 2019,
                       based on the date vehicle first registered and mots for 2009 and 
                        2019""")
    parser.add_argument('--question3', dest='question3', action='store_true',
               help="""make a scatter chart of mileage-category vs frequency for 1896cc 
                       Diesel Golf first registered 2008, using 2019 MOT data""")
    parser.add_argument('--question4', dest='question4', action='store_true',
               help="""Which county mots the most and least Rolls Royce""")    

    args = parser.parse_args()


    if args.question1 is True:
        ##work out the question and give an answer
        ## these models of cars in 2019 how many diesel and petrols are there with over
        # 200k mileage.
        GolfDi = 0
        GolfPe = 0
        AstraPe = 0
        AstraDi = 0
        OctaviaDi = 0
        OctaviaPe = 0
        FocusDi = 0
        FocusPe = 0
        i30Di = 0
        i30Pe = 0
        for c in dGenerateCars():
            
            try:
                mileage=int(c[6])
            except ValueError:
                continue


            if c[11]=="DI" and c[9]=="GOLF" and int(c[6])>=200000 and c[2].startswith("2019"):
                GolfDi+=1
            elif c[11]=="PE" and c[9]=="GOLF" and int(c[6])>=200000 and c[2].startswith("2019"):
                GolfPe+=1
            elif c[11]=="DI" and c[9]=="ASTRA" and int(c[6])>=200000 and c[2].startswith("2019"):
                AstraDi+=1
            elif c[11]=="PE" and c[9]=="ASTRA" and int(c[6])>=200000 and c[2].startswith("2019"):
                AstraPe+=1
            elif c[11]=="DI" and c[9]=="OCTAVIA" and int(c[6])>=200000 and c[2].startswith("2019"):
                OctaviaDi+=1
            elif c[11]=="PE" and c[9]=="OCTAVIA" and int(c[6])>=200000 and c[2].startswith("2019"):
                OctaviaPe+=1
            elif c[11]=="DI" and c[9]=="FOCUS" and int(c[6])>=200000 and c[2].startswith("2019"):
                FocusDi+=1
            elif c[11]=="PE" and c[9]=="FOCUS" and int(c[6])>=200000 and c[2].startswith("2019"):
                FocusPe+=1
            elif c[11]=="DI" and c[9]=="I30" and int(c[6])>=200000 and c[2].startswith("2019"):
                i30Di+=1
            elif c[11]=="PE" and c[9]=="I30" and int(c[6])>=200000 and c[2].startswith("2019"):
                i30Pe+=1

        print("---- Over 200k, 2019 ----")
        print("Golf Di:",GolfDi)
        print("Golf Pe:",GolfPe)
        print("Astra Di:",AstraDi)
        print("Astra Pe:",AstraPe)
        print("Octavia Di:",OctaviaDi)
        print("Octavia Pe:",OctaviaPe)
        print("Focus Di:",FocusDi)
        print("Focus Pe:",FocusPe)
        print("i30 Di:",i30Di)
        print("i30 Pe:",i30Pe)

        sys.exit()

    if args.question2 is True:
        ##work out the question and give an answer
        #the average age of a vehicle in 2009 compared to 2019
        count2009=0
        count2019=0
        fig2009=0
        fig2019=0

        for c in dGenerateCars():
            
            try:
                int(c[13][0:4])
            except ValueError:
                continue


            if c[2].startswith("2009"):
                fig2009=fig2009+(2009-(int(c[13][0:4])))
                count2009+=1
    
            elif c[2].startswith("2019"):
                fig2019=fig2019+(2019-(int(c[13][0:4])))
                count2019+=1

        fig2009 = fig2009/float(count2009)
        fig2019 = fig2019/float(count2019)

        print("---- Average age of vehicle 2009/2019 ----")
        print("2009:",fig2009)
        print("2019:",fig2019)

        sys.exit()

    if args.question3 is True:
        ##work out the question and give an answer
        #the average age of a vehicle in 2009 compared to 2019

        frequency = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        #plt.scatter([3,4,2,1,3],[1,3,3,1,6])
        #plt.show()


        for c in dGenerateCars():
            
            #try:
            #    int(c[13][0:4])
            #except ValueError:
            #    continue

            try:
                mileage = (int)(c[6])
            except ValueError:
                continue

            if mileage > 300000:
                continue

            if c[13].startswith("2008") and c[9]=="GOLF" and c[11]=="DI" and c[12]=="1896"and c[2].startswith("2019"):

                category=mileage/15000
                frequency[int(category)] +=1

                
        xd = []
        for a in range(20):
            xd.append((a)*15)

        print("---- mileage category vs frequency for 2008 GOLF Diesel 1896, from 2019 MOT data ----")
        plt.scatter(xd,frequency)
        plt.show()

        sys.exit()

    if args.question4 is True:
        #which county has most rolls royce per captita
        #work out rols royce per capita for all post code areas
        p_pcode_area = {'AL': 271312.57846788695, 'B': 2001645.1792515158, 'BA': 441125.7384486151, 'BB': 489583.61069465044, 'BD': 589832.7940888732, 'BH': 567003.6375206348, 'BL': 404752.5838243801, 'BN': 856361.6458174149, 'BR': 311822.7817972954, 'BS': 948801.9088444001, 'CA': 319452.60448446753, 'CB': 198194.72290071796, 'CF': 1043600.7984997848, 'CH': 658413.216432643, 'CM': 630161.25542235, 'CO': 455150.1055115506, 'CR': 417625.8281461846, 'CT': 511626.66187961947, 'CV': 788146.3801269259, 'CW': 299039.1080764709, 'DA': 461028.36693536275, 'DE': 470358.7156893601, 'DG': 207.40076335877862, 'DH': 301470.18549289874, 'DL': 394387.23258673307, 'DN': 718020.5254177209, 'DT': 226322.9644683427, 'DY': 400473.2944185027, 'E': 1136572.1873367522, 'EC': 59389.21998017208, 'EN': 382172.15707005456, 'EX': 602125.4866535115, 'FY': 235327.8344431818, 'GL': 602687.7972449826, 'GU': 695787.1251048397, 'HA': 427189.21128425474, 'HD': 266243.3313040242, 'HG': 131495.87357721155, 'HP': 484089.7725321442, 'HR': 181703.84890670457, 'HU': 372709.21839671116, 'HX': 164198.88596978196, 'IG': 354145.75007775985, 'IP': 655494.8090906369, 'KT': 569383.5956525605, 'L': 912453.7903966847, 'LA': 338497.29197771655, 'LD': 48201.52058158851, 'LE': 952679.4592372143, 'LL': 543803.5107282264, 'LN': 262003.6080854539, 'LS': 832760.9278934912, 'LU': 270944.2902982057, 'M': 1249563.1764649397, 'ME': 646265.1255205923, 'MK': 436861.0087534517, 'N': 922025.7389422061, 'NE': 1198844.0213290032, 'NG': 1253685.2004739712, 'NN': 587817.9565670957, 'NP': 510912.79630932066, 'NR': 746466.0017211306, 'NW': 417812.11522074154, 'OL': 499783.9605653971, 'OX': 434983.75164908764, 'PE': 937825.1469105138, 'PL': 549974.0687446359, 'PO': 859597.2883548806, 'PR': 525098.9194726355, 'RG': 732455.3732176973, 'RH': 565090.9190336774, 'RM': 566845.7229417237, 'S': 1287349.8137038366, 'SA': 753997.9370042654, 'SE': 1092005.0394851856, 'SG': 374471.5614645335, 'SK': 619668.4363776982, 'SL': 419784.04820187285, 'SM': 230115.9787313939, 'SN': 498571.4154624558, 'SO': 687264.9108044809, 'SP': 263741.5414025115, 'SR': 249550.9831020527, 'SS': 553051.077132948, 'ST': 616174.3459627255, 'SW': 962814.9273024341, 'SY': 360998.8287945703, 'TA': 342386.23025779874, 'TD': 15905.568251926878, 'TF': 235629.77774098935, 'TN': 751106.6472950772, 'TQ': 295101.05693519517, 'TR': 321430.95550881734, 'TS': 571965.3529400739, 'TW': 509760.1917422045, 'UB': 366277.5801005688, 'W': 592391.2494658303, 'WA': 696991.6055345163, 'WC': 61714.0018509975, 'WD': 272812.3911275196, 'WF': 543908.0553234728, 'WN': 297706.61380219203, 'WR': 297710.73898024147, 'WS': 450718.4001089022, 'WV': 409518.0881036483, 'YO': 461690.0279718355}
        cict = {}
        for a in p_pcode_area.keys():
            cict[a] = 0

        for c in dGenerateCars():
            if len(c[7])==0:
                continue
            if c[7]=="EH": #for some reason my postcode data excludes EH postcode
                continue
            if c[7]=="ML": #for some reason my postcode data excludes ML postcode
                continue
            if c[7]=="G": #for some reason my postcode data excludes G postcode
                continue
            if c[7]=="KY": #for some reason my postcode data excludes KY postcode
                continue
            if c[7]=="PH": #for some reason my postcode data excludes PH postcode
                continue
            if c[7]=="KA": #for some reason my postcode data excludes PH postcode
                continue
            if c[7]=="FK": #for some reason my postcode data excludes FK postcode
                continue
            if c[7]=="DD": #for some reason my postcode data excludes FK postcode
                continue
            if c[8]=="ROLLS ROYCE" and c[2][0:4]=="2019":
                cict[c[7]]+=1
            
            

        print(cict)

        cict_pc = {}
        for a in cict.keys():
            cict_pc[a]=cict[a]/p_pcode_area[a]

        sorteed = sorted(cict_pc.keys(), key=lambda p: cict_pc[p])
        print(sorteed)

        sys.exit()
    
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
        
        
