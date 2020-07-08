import os
import csv
import argparse
import sys
import plot
import  json

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

##calculate per capita, and count per pcode for all make an model.
#{make : {model:[{pcodearea:percap},{pcodearea:count}]}
def Getgkp():
  

    p_pcode_area = {'pc': 0, 'AB': 533950.8817646004, 'AL': 269738.17571000225, 'B': 1991073.057345411, 'BA': 423807.9909564766, 'BB': 495689.08093591925, 'BD': 587095.3642845196, 'BH': 559099.3527650888, 'BL': 380872.9611814539, 'BN': 857079.7927516169, 'BR': 307362.5492488172, 'BS': 968932.412706771, 'BT': 1893667.0, 'CA': 323799.8125014299, 'CB': 210616.86297197975, 'CF': 1037681.386420321, 'CH': 480165.3952346568, 'CM': 642444.3080168071, 'CO': 447064.1610122909, 'CR': 430925.1156062462, 'CT': 514088.21861251927, 'CV': 786701.4545968267, 'CW': 299948.2753186591, 'DA': 464740.73301721073, 'DD': 279142.4598993904, 'DE': 490098.7113398885, 'DG': 146355.51817132343, 'DH': 308478.781088173, 'DL': 387755.67623796564, 'DN': 699747.3769466791, 'DT': 220768.0267760806, 'DY': 389260.99044594564, 'E': 1119234.672264762, 'EC': 133221.2997810118, 'EH': 939644.6603634906, 'EN': 362288.2218389178, 'EX': 597943.441391508, 'FK': 283758.7354659648, 'FY': 234952.7794216419, 'G': 1181513.5725514372, 'GL': 589244.106014495, 'GU': 697870.717283279, 'HA': 408366.34827458265, 'HD': 284751.9199649316, 'HG': 128614.0084220901, 'HP': 506134.6107135518, 'HR': 183913.0011400514, 'HS': 14544.13620430646, 'HU': 340277.96157760813, 'HX': 164959.15831571055, 'IG': 381573.6543259759, 'IP': 661504.0919179018, 'IV': 218756.14384431014, 'KA': 367098.47915853723, 'KT': 554763.8963340883, 'KW': 51740.01382989233, 'KY': 378074.3489868345, 'L': 1108332.1981691574, 'LA': 336673.29405858513, 'LD': 49203.966229357015, 'LE': 961880.8604996909, 'LL': 543980.2086851299, 'LN': 269764.3191595417, 'LS': 835613.4330083781, 'LU': 275247.95855747827, 'M': 1292764.4279642196, 'ME': 648798.3491079231, 'MK': 420074.4994829539, 'ML': 385882.59785766416, 'N': 835609.21570022, 'NE': 1198420.831242167, 'NG': 1237977.4291670364, 'NN': 603556.4922857445, 'NP': 520252.5975986275, 'NR': 728213.7707923241, 'NW': 402507.0838701482, 'OL': 496694.2240033805, 'OX': 435400.3182146322, 'PA': 215111.11302522206, 'PE': 936948.9687222829, 'PH': 164557.40302336126, 'PL': 542975.3088715959, 'PO': 848881.4882557077, 'PR': 525127.417398752, 'RG': 744876.4295915223, 'RH': 560065.122925983, 'RM': 557175.6798677116, 'S': 1286313.9705775506, 'SA': 752679.0497433741, 'SE': 1080603.70042657, 'SG': 362730.04196034675, 'SK': 609981.7095787606, 'SL': 406966.4332642214, 'SM': 223227.2367348285, 'SN': 500631.016987324, 'SO': 733031.7925245425, 'SP': 245930.11979584885, 'SR': 249242.44838776445, 'SS': 546250.2626453729, 'ST': 611587.90434149, 'SW': 943604.7887399129, 'SY': 356282.39542570163, 'TA': 341618.90271312697, 'TD': 114906.08665934893, 'TF': 218438.3171026652, 'TN': 743591.3674664351, 'TQ': 300273.17710272997, 'TR': 328282.37027171016, 'TS': 553014.2886462638, 'TW': 541032.4083310588, 'UB': 340395.6334744352, 'W': 643151.3069980209, 'WA': 671518.1500460687, 'WC': 102596.88463750099, 'WD': 280728.4095256867, 'WF': 519310.62808433414, 'WN': 293698.0223223254, 'WR': 304796.4367139767, 'WS': 468716.67819454387, 'WV': 422266.1678966084, 'XX' : 0, 'YO': 526262.0220911006, 'ZE': 22920.0}


    # first get the make and models
    make_mdl = {}
    for c in dGenerateCars():
        if c[8] == "make":
            continue
        if len(c) != 14:
            continue
        if c[2][0:4] != "2019":
            continue
        if c[8] in make_mdl.keys():
            if c[9] not in make_mdl[c[8]]:
                make_mdl[c[8]].append(c[9])
        else:
            make_mdl[c[8]] = [c[9],]

    #initialise the structure of dicts and lists
    ff = {}
    for a in make_mdl.keys():
        ff[a] = {}
        for b in make_mdl[a]:            
            ff[a][b]= [{},{}]
            for c in p_pcode_area.keys():
                ff[a][b][0][c] = 0
                

    #count the number of cars in each post code area
    for c in dGenerateCars():
        if c[8] == "make":
            continue
        if len(c) != 14:
            continue
        if c[2][0:4] != "2019":
            continue
        ff[c[8]][c[9]][0][c[7]] += 1

    ##the file is far too big so calculate in javascript at last moment or db
    if False:
        #now make iterate the structure to calculate percapita
        for a in ff.keys():
            for b in ff[a]:
                for c in ff[a][b][0].keys():  ##pcodes
                    if p_pcode_area[c] == 0:
                        continue
                    ff[a][b][1][c] = ff[a][b][0][c] / p_pcode_area[c]#count / pcode population

    ##may as well print this hope it works
    #dump to a json file 2 item list, [0]dictionary per capita,[1]sorted list of pcode area(performance reasons)[2] dictiony count per pcode area[3] sorted list pcode area
    #j = [cict,sorteed1,cict_pc,sorteed2]

    with open('all.json', 'w', encoding='utf-8') as f:
        json.dump(ff, f, ensure_ascii=False, indent=4)
        

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
               help="""Which post code area mots the most and least Rolls Royce, and per capita""")    
    parser.add_argument('--question5', dest='question5', action='store_true',
               help="""Which post code area mots the most and least Skoda Octavia, and per capita""") 
    parser.add_argument('--question6', dest='question6', action='store_true',
               help="""Which post code area mots the most and least Volkswagen Golf, and per capita""")
    parser.add_argument('--question7', dest='question7', action='store_true',
               help="""Which post code area mots the most and least Skoda Citigo, and per capita""")
    parser.add_argument('--question8', dest='question8', action='store_true',
               help="""Which post code area mots the most and least Land Rover Range Rover, and per capita""")
    parser.add_argument('--cAll', dest='cAll', action='store_true',
               help="""construct a json dictionary of counts and counts for capita in post code area for all makes and all models""")
    parser.add_argument('--question9', dest='question9', action='store_true',
               help="""construct a json dictionary of counts and counts for capita in post code area for all makes and all models""")

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
        p_pcode_area = {'pc': 0, 'AB': 533950.8817646004, 'AL': 269738.17571000225, 'B': 1991073.057345411, 'BA': 423807.9909564766, 'BB': 495689.08093591925, 'BD': 587095.3642845196, 'BH': 559099.3527650888, 'BL': 380872.9611814539, 'BN': 857079.7927516169, 'BR': 307362.5492488172, 'BS': 968932.412706771, 'BT': 1893667.0, 'CA': 323799.8125014299, 'CB': 210616.86297197975, 'CF': 1037681.386420321, 'CH': 480165.3952346568, 'CM': 642444.3080168071, 'CO': 447064.1610122909, 'CR': 430925.1156062462, 'CT': 514088.21861251927, 'CV': 786701.4545968267, 'CW': 299948.2753186591, 'DA': 464740.73301721073, 'DD': 279142.4598993904, 'DE': 490098.7113398885, 'DG': 146355.51817132343, 'DH': 308478.781088173, 'DL': 387755.67623796564, 'DN': 699747.3769466791, 'DT': 220768.0267760806, 'DY': 389260.99044594564, 'E': 1119234.672264762, 'EC': 133221.2997810118, 'EH': 939644.6603634906, 'EN': 362288.2218389178, 'EX': 597943.441391508, 'FK': 283758.7354659648, 'FY': 234952.7794216419, 'G': 1181513.5725514372, 'GL': 589244.106014495, 'GU': 697870.717283279, 'HA': 408366.34827458265, 'HD': 284751.9199649316, 'HG': 128614.0084220901, 'HP': 506134.6107135518, 'HR': 183913.0011400514, 'HS': 14544.13620430646, 'HU': 340277.96157760813, 'HX': 164959.15831571055, 'IG': 381573.6543259759, 'IP': 661504.0919179018, 'IV': 218756.14384431014, 'KA': 367098.47915853723, 'KT': 554763.8963340883, 'KW': 51740.01382989233, 'KY': 378074.3489868345, 'L': 1108332.1981691574, 'LA': 336673.29405858513, 'LD': 49203.966229357015, 'LE': 961880.8604996909, 'LL': 543980.2086851299, 'LN': 269764.3191595417, 'LS': 835613.4330083781, 'LU': 275247.95855747827, 'M': 1292764.4279642196, 'ME': 648798.3491079231, 'MK': 420074.4994829539, 'ML': 385882.59785766416, 'N': 835609.21570022, 'NE': 1198420.831242167, 'NG': 1237977.4291670364, 'NN': 603556.4922857445, 'NP': 520252.5975986275, 'NR': 728213.7707923241, 'NW': 402507.0838701482, 'OL': 496694.2240033805, 'OX': 435400.3182146322, 'PA': 215111.11302522206, 'PE': 936948.9687222829, 'PH': 164557.40302336126, 'PL': 542975.3088715959, 'PO': 848881.4882557077, 'PR': 525127.417398752, 'RG': 744876.4295915223, 'RH': 560065.122925983, 'RM': 557175.6798677116, 'S': 1286313.9705775506, 'SA': 752679.0497433741, 'SE': 1080603.70042657, 'SG': 362730.04196034675, 'SK': 609981.7095787606, 'SL': 406966.4332642214, 'SM': 223227.2367348285, 'SN': 500631.016987324, 'SO': 733031.7925245425, 'SP': 245930.11979584885, 'SR': 249242.44838776445, 'SS': 546250.2626453729, 'ST': 611587.90434149, 'SW': 943604.7887399129, 'SY': 356282.39542570163, 'TA': 341618.90271312697, 'TD': 114906.08665934893, 'TF': 218438.3171026652, 'TN': 743591.3674664351, 'TQ': 300273.17710272997, 'TR': 328282.37027171016, 'TS': 553014.2886462638, 'TW': 541032.4083310588, 'UB': 340395.6334744352, 'W': 643151.3069980209, 'WA': 671518.1500460687, 'WC': 102596.88463750099, 'WD': 280728.4095256867, 'WF': 519310.62808433414, 'WN': 293698.0223223254, 'WR': 304796.4367139767, 'WS': 468716.67819454387, 'WV': 422266.1678966084, 'XX' : 0, 'YO': 526262.0220911006, 'ZE': 22920.0}


        #temp does mot data cover this postal code this exist
        #test11 = { "pc" : 0, "BT" : 0, "EC" : 0 , "GI" : 0 , "GY": 0 , "HS" : 0 , "WC" : 0 , "ZE" : 0 }
        #for c in dGenerateCars():
        #    if c[7] in test11.keys():
        #        test11[c[7]] += 1


        cict = {}
        for a in p_pcode_area.keys():
            cict[a] = 0

        for c in dGenerateCars():
            if len(c[7])==0:
                continue
            #if c[7]=="EH": #for some reason my postcode data excludes EH postcode
            #    continue
            #if c[7]=="ML": #for some reason my postcode data excludes ML postcode
            #    continue
            #if c[7]=="G": #for some reason my postcode data excludes G postcode
            #    continue
            #if c[7]=="KY": #for some reason my postcode data excludes KY postcode
            #    continue
            #if c[7]=="PH": #for some reason my postcode data excludes PH postcode
            #    continue
            #if c[7]=="KA": #for some reason my postcode data excludes PH postcode
            #    continue
            #if c[7]=="FK": #for some reason my postcode data excludes FK postcode
            #    continue
            #if c[7]=="DD": #for some reason my postcode data excludes DD postcode
            #    continue
            if c[8]=="ROLLS ROYCE" and c[2][0:4]=="2019":
                cict[c[7]]+=1

        #print(cict)
        sorteed1 = sorted(cict.keys(), key=lambda p: int(cict[p]))        
        print("2019 Rolls Royce MOT by Post Code area")
        for a in sorteed1:
            print(a,cict[a])

        cict_pc = {}
        for a in cict.keys():
            #dont use 0 population p area code
            if p_pcode_area[a] == 0:
                continue
            cict_pc[a]=cict[a]/p_pcode_area[a]

        sorteed2 = sorted(cict_pc.keys(), key=lambda p: cict_pc[p])
        print("2019 Rolls Royce MOT by Post Code area, Per Capita")
        for a in sorteed2:
            print(a,cict_pc[a])

        sys.exit()

    if args.question5 is True:
        #which county has most rolls royce per captita
        #work out rols royce per capita for all post code areas
        p_pcode_area = {'pc': 0, 'AB': 533950.8817646004, 'AL': 269738.17571000225, 'B': 1991073.057345411, 'BA': 423807.9909564766, 'BB': 495689.08093591925, 'BD': 587095.3642845196, 'BH': 559099.3527650888, 'BL': 380872.9611814539, 'BN': 857079.7927516169, 'BR': 307362.5492488172, 'BS': 968932.412706771, 'BT': 1893667.0, 'CA': 323799.8125014299, 'CB': 210616.86297197975, 'CF': 1037681.386420321, 'CH': 480165.3952346568, 'CM': 642444.3080168071, 'CO': 447064.1610122909, 'CR': 430925.1156062462, 'CT': 514088.21861251927, 'CV': 786701.4545968267, 'CW': 299948.2753186591, 'DA': 464740.73301721073, 'DD': 279142.4598993904, 'DE': 490098.7113398885, 'DG': 146355.51817132343, 'DH': 308478.781088173, 'DL': 387755.67623796564, 'DN': 699747.3769466791, 'DT': 220768.0267760806, 'DY': 389260.99044594564, 'E': 1119234.672264762, 'EC': 133221.2997810118, 'EH': 939644.6603634906, 'EN': 362288.2218389178, 'EX': 597943.441391508, 'FK': 283758.7354659648, 'FY': 234952.7794216419, 'G': 1181513.5725514372, 'GL': 589244.106014495, 'GU': 697870.717283279, 'HA': 408366.34827458265, 'HD': 284751.9199649316, 'HG': 128614.0084220901, 'HP': 506134.6107135518, 'HR': 183913.0011400514, 'HS': 14544.13620430646, 'HU': 340277.96157760813, 'HX': 164959.15831571055, 'IG': 381573.6543259759, 'IP': 661504.0919179018, 'IV': 218756.14384431014, 'KA': 367098.47915853723, 'KT': 554763.8963340883, 'KW': 51740.01382989233, 'KY': 378074.3489868345, 'L': 1108332.1981691574, 'LA': 336673.29405858513, 'LD': 49203.966229357015, 'LE': 961880.8604996909, 'LL': 543980.2086851299, 'LN': 269764.3191595417, 'LS': 835613.4330083781, 'LU': 275247.95855747827, 'M': 1292764.4279642196, 'ME': 648798.3491079231, 'MK': 420074.4994829539, 'ML': 385882.59785766416, 'N': 835609.21570022, 'NE': 1198420.831242167, 'NG': 1237977.4291670364, 'NN': 603556.4922857445, 'NP': 520252.5975986275, 'NR': 728213.7707923241, 'NW': 402507.0838701482, 'OL': 496694.2240033805, 'OX': 435400.3182146322, 'PA': 215111.11302522206, 'PE': 936948.9687222829, 'PH': 164557.40302336126, 'PL': 542975.3088715959, 'PO': 848881.4882557077, 'PR': 525127.417398752, 'RG': 744876.4295915223, 'RH': 560065.122925983, 'RM': 557175.6798677116, 'S': 1286313.9705775506, 'SA': 752679.0497433741, 'SE': 1080603.70042657, 'SG': 362730.04196034675, 'SK': 609981.7095787606, 'SL': 406966.4332642214, 'SM': 223227.2367348285, 'SN': 500631.016987324, 'SO': 733031.7925245425, 'SP': 245930.11979584885, 'SR': 249242.44838776445, 'SS': 546250.2626453729, 'ST': 611587.90434149, 'SW': 943604.7887399129, 'SY': 356282.39542570163, 'TA': 341618.90271312697, 'TD': 114906.08665934893, 'TF': 218438.3171026652, 'TN': 743591.3674664351, 'TQ': 300273.17710272997, 'TR': 328282.37027171016, 'TS': 553014.2886462638, 'TW': 541032.4083310588, 'UB': 340395.6334744352, 'W': 643151.3069980209, 'WA': 671518.1500460687, 'WC': 102596.88463750099, 'WD': 280728.4095256867, 'WF': 519310.62808433414, 'WN': 293698.0223223254, 'WR': 304796.4367139767, 'WS': 468716.67819454387, 'WV': 422266.1678966084, 'XX' : 0, 'YO': 526262.0220911006, 'ZE': 22920.0}


        #temp does mot data cover this postal code this exist
        #test11 = { "pc" : 0, "BT" : 0, "EC" : 0 , "GI" : 0 , "GY": 0 , "HS" : 0 , "WC" : 0 , "ZE" : 0 }
        #for c in dGenerateCars():
        #    if c[7] in test11.keys():
        #        test11[c[7]] += 1


        cict = {}
        for a in p_pcode_area.keys():
            cict[a] = 0

        for c in dGenerateCars():
            if len(c[7])==0:
                continue
            #if c[7]=="EH": #for some reason my postcode data excludes EH postcode
            #    continue
            #if c[7]=="ML": #for some reason my postcode data excludes ML postcode
            #    continue
            #if c[7]=="G": #for some reason my postcode data excludes G postcode
            #    continue
            #if c[7]=="KY": #for some reason my postcode data excludes KY postcode
            #    continue
            #if c[7]=="PH": #for some reason my postcode data excludes PH postcode
            #    continue
            #if c[7]=="KA": #for some reason my postcode data excludes PH postcode
            #    continue
            #if c[7]=="FK": #for some reason my postcode data excludes FK postcode
            #    continue
            #if c[7]=="DD": #for some reason my postcode data excludes DD postcode
            #    continue
            if c[8]=="SKODA" and c[9]=="OCTAVIA" and c[2][0:4]=="2019":
                cict[c[7]]+=1

        #print(cict)
        sorteed1 = sorted(cict.keys(), key=lambda p: int(cict[p]))        
        print("2019 Skoda Octavia MOT by Post Code area")
        for a in sorteed1:
            print(a,cict[a])

        cict_pc = {}
        for a in cict.keys():
            #dont use 0 population p area code
            if p_pcode_area[a] == 0:
                continue
            cict_pc[a]=cict[a]/p_pcode_area[a]

        sorteed2 = sorted(cict_pc.keys(), key=lambda p: cict_pc[p])
        print("2019 Skoda Octavia MOT by Post Code area, Per Capita")
        for a in sorteed2:
            print(a,cict_pc[a])

        sys.exit()

    if args.question6 is True:
        #which county has most rolls royce per captita
        #work out rols royce per capita for all post code areas
        p_pcode_area = {'pc': 0, 'AB': 533950.8817646004, 'AL': 269738.17571000225, 'B': 1991073.057345411, 'BA': 423807.9909564766, 'BB': 495689.08093591925, 'BD': 587095.3642845196, 'BH': 559099.3527650888, 'BL': 380872.9611814539, 'BN': 857079.7927516169, 'BR': 307362.5492488172, 'BS': 968932.412706771, 'BT': 1893667.0, 'CA': 323799.8125014299, 'CB': 210616.86297197975, 'CF': 1037681.386420321, 'CH': 480165.3952346568, 'CM': 642444.3080168071, 'CO': 447064.1610122909, 'CR': 430925.1156062462, 'CT': 514088.21861251927, 'CV': 786701.4545968267, 'CW': 299948.2753186591, 'DA': 464740.73301721073, 'DD': 279142.4598993904, 'DE': 490098.7113398885, 'DG': 146355.51817132343, 'DH': 308478.781088173, 'DL': 387755.67623796564, 'DN': 699747.3769466791, 'DT': 220768.0267760806, 'DY': 389260.99044594564, 'E': 1119234.672264762, 'EC': 133221.2997810118, 'EH': 939644.6603634906, 'EN': 362288.2218389178, 'EX': 597943.441391508, 'FK': 283758.7354659648, 'FY': 234952.7794216419, 'G': 1181513.5725514372, 'GL': 589244.106014495, 'GU': 697870.717283279, 'HA': 408366.34827458265, 'HD': 284751.9199649316, 'HG': 128614.0084220901, 'HP': 506134.6107135518, 'HR': 183913.0011400514, 'HS': 14544.13620430646, 'HU': 340277.96157760813, 'HX': 164959.15831571055, 'IG': 381573.6543259759, 'IP': 661504.0919179018, 'IV': 218756.14384431014, 'KA': 367098.47915853723, 'KT': 554763.8963340883, 'KW': 51740.01382989233, 'KY': 378074.3489868345, 'L': 1108332.1981691574, 'LA': 336673.29405858513, 'LD': 49203.966229357015, 'LE': 961880.8604996909, 'LL': 543980.2086851299, 'LN': 269764.3191595417, 'LS': 835613.4330083781, 'LU': 275247.95855747827, 'M': 1292764.4279642196, 'ME': 648798.3491079231, 'MK': 420074.4994829539, 'ML': 385882.59785766416, 'N': 835609.21570022, 'NE': 1198420.831242167, 'NG': 1237977.4291670364, 'NN': 603556.4922857445, 'NP': 520252.5975986275, 'NR': 728213.7707923241, 'NW': 402507.0838701482, 'OL': 496694.2240033805, 'OX': 435400.3182146322, 'PA': 215111.11302522206, 'PE': 936948.9687222829, 'PH': 164557.40302336126, 'PL': 542975.3088715959, 'PO': 848881.4882557077, 'PR': 525127.417398752, 'RG': 744876.4295915223, 'RH': 560065.122925983, 'RM': 557175.6798677116, 'S': 1286313.9705775506, 'SA': 752679.0497433741, 'SE': 1080603.70042657, 'SG': 362730.04196034675, 'SK': 609981.7095787606, 'SL': 406966.4332642214, 'SM': 223227.2367348285, 'SN': 500631.016987324, 'SO': 733031.7925245425, 'SP': 245930.11979584885, 'SR': 249242.44838776445, 'SS': 546250.2626453729, 'ST': 611587.90434149, 'SW': 943604.7887399129, 'SY': 356282.39542570163, 'TA': 341618.90271312697, 'TD': 114906.08665934893, 'TF': 218438.3171026652, 'TN': 743591.3674664351, 'TQ': 300273.17710272997, 'TR': 328282.37027171016, 'TS': 553014.2886462638, 'TW': 541032.4083310588, 'UB': 340395.6334744352, 'W': 643151.3069980209, 'WA': 671518.1500460687, 'WC': 102596.88463750099, 'WD': 280728.4095256867, 'WF': 519310.62808433414, 'WN': 293698.0223223254, 'WR': 304796.4367139767, 'WS': 468716.67819454387, 'WV': 422266.1678966084, 'XX' : 0, 'YO': 526262.0220911006, 'ZE': 22920.0}


        #temp does mot data cover this postal code this exist
        #test11 = { "pc" : 0, "BT" : 0, "EC" : 0 , "GI" : 0 , "GY": 0 , "HS" : 0 , "WC" : 0 , "ZE" : 0 }
        #for c in dGenerateCars():
        #    if c[7] in test11.keys():
        #        test11[c[7]] += 1


        cict = {}
        for a in p_pcode_area.keys():
            cict[a] = 0

        for c in dGenerateCars():
            if len(c[7])==0:
                continue
            #if c[7]=="EH": #for some reason my postcode data excludes EH postcode
            #    continue
            #if c[7]=="ML": #for some reason my postcode data excludes ML postcode
            #    continue
            #if c[7]=="G": #for some reason my postcode data excludes G postcode
            #    continue
            #if c[7]=="KY": #for some reason my postcode data excludes KY postcode
            #    continue
            #if c[7]=="PH": #for some reason my postcode data excludes PH postcode
            #    continue
            #if c[7]=="KA": #for some reason my postcode data excludes PH postcode
            #    continue
            #if c[7]=="FK": #for some reason my postcode data excludes FK postcode
            #    continue
            #if c[7]=="DD": #for some reason my postcode data excludes DD postcode
            #    continue
            if c[8]=="VOLKSWAGEN" and c[9]=="GOLF" and c[2][0:4]=="2019":
                cict[c[7]]+=1

        #print(cict)
        sorteed1 = sorted(cict.keys(), key=lambda p: int(cict[p]))        
        print("2019 Volkswagen Golf MOT by Post Code area")
        for a in sorteed1:
            print(a,cict[a])

        cict_pc = {}
        for a in cict.keys():
            #dont use 0 population p area code
            if p_pcode_area[a] == 0:
                continue
            cict_pc[a]=cict[a]/p_pcode_area[a]

        sorteed2 = sorted(cict_pc.keys(), key=lambda p: cict_pc[p])
        print("2019 Volkswagen Golf MOT by Post Code area, Per Capita")
        for a in sorteed2:
            print(a,cict_pc[a])

        sys.exit()
    if args.question7 is True:
        #which county has most rolls royce per captita
        #work out rols royce per capita for all post code areas
        p_pcode_area = {'pc': 0, 'AB': 533950.8817646004, 'AL': 269738.17571000225, 'B': 1991073.057345411, 'BA': 423807.9909564766, 'BB': 495689.08093591925, 'BD': 587095.3642845196, 'BH': 559099.3527650888, 'BL': 380872.9611814539, 'BN': 857079.7927516169, 'BR': 307362.5492488172, 'BS': 968932.412706771, 'BT': 1893667.0, 'CA': 323799.8125014299, 'CB': 210616.86297197975, 'CF': 1037681.386420321, 'CH': 480165.3952346568, 'CM': 642444.3080168071, 'CO': 447064.1610122909, 'CR': 430925.1156062462, 'CT': 514088.21861251927, 'CV': 786701.4545968267, 'CW': 299948.2753186591, 'DA': 464740.73301721073, 'DD': 279142.4598993904, 'DE': 490098.7113398885, 'DG': 146355.51817132343, 'DH': 308478.781088173, 'DL': 387755.67623796564, 'DN': 699747.3769466791, 'DT': 220768.0267760806, 'DY': 389260.99044594564, 'E': 1119234.672264762, 'EC': 133221.2997810118, 'EH': 939644.6603634906, 'EN': 362288.2218389178, 'EX': 597943.441391508, 'FK': 283758.7354659648, 'FY': 234952.7794216419, 'G': 1181513.5725514372, 'GL': 589244.106014495, 'GU': 697870.717283279, 'HA': 408366.34827458265, 'HD': 284751.9199649316, 'HG': 128614.0084220901, 'HP': 506134.6107135518, 'HR': 183913.0011400514, 'HS': 14544.13620430646, 'HU': 340277.96157760813, 'HX': 164959.15831571055, 'IG': 381573.6543259759, 'IP': 661504.0919179018, 'IV': 218756.14384431014, 'KA': 367098.47915853723, 'KT': 554763.8963340883, 'KW': 51740.01382989233, 'KY': 378074.3489868345, 'L': 1108332.1981691574, 'LA': 336673.29405858513, 'LD': 49203.966229357015, 'LE': 961880.8604996909, 'LL': 543980.2086851299, 'LN': 269764.3191595417, 'LS': 835613.4330083781, 'LU': 275247.95855747827, 'M': 1292764.4279642196, 'ME': 648798.3491079231, 'MK': 420074.4994829539, 'ML': 385882.59785766416, 'N': 835609.21570022, 'NE': 1198420.831242167, 'NG': 1237977.4291670364, 'NN': 603556.4922857445, 'NP': 520252.5975986275, 'NR': 728213.7707923241, 'NW': 402507.0838701482, 'OL': 496694.2240033805, 'OX': 435400.3182146322, 'PA': 215111.11302522206, 'PE': 936948.9687222829, 'PH': 164557.40302336126, 'PL': 542975.3088715959, 'PO': 848881.4882557077, 'PR': 525127.417398752, 'RG': 744876.4295915223, 'RH': 560065.122925983, 'RM': 557175.6798677116, 'S': 1286313.9705775506, 'SA': 752679.0497433741, 'SE': 1080603.70042657, 'SG': 362730.04196034675, 'SK': 609981.7095787606, 'SL': 406966.4332642214, 'SM': 223227.2367348285, 'SN': 500631.016987324, 'SO': 733031.7925245425, 'SP': 245930.11979584885, 'SR': 249242.44838776445, 'SS': 546250.2626453729, 'ST': 611587.90434149, 'SW': 943604.7887399129, 'SY': 356282.39542570163, 'TA': 341618.90271312697, 'TD': 114906.08665934893, 'TF': 218438.3171026652, 'TN': 743591.3674664351, 'TQ': 300273.17710272997, 'TR': 328282.37027171016, 'TS': 553014.2886462638, 'TW': 541032.4083310588, 'UB': 340395.6334744352, 'W': 643151.3069980209, 'WA': 671518.1500460687, 'WC': 102596.88463750099, 'WD': 280728.4095256867, 'WF': 519310.62808433414, 'WN': 293698.0223223254, 'WR': 304796.4367139767, 'WS': 468716.67819454387, 'WV': 422266.1678966084, 'XX' : 0, 'YO': 526262.0220911006, 'ZE': 22920.0}


        #temp does mot data cover this postal code this exist
        #test11 = { "pc" : 0, "BT" : 0, "EC" : 0 , "GI" : 0 , "GY": 0 , "HS" : 0 , "WC" : 0 , "ZE" : 0 }
        #for c in dGenerateCars():
        #    if c[7] in test11.keys():
        #        test11[c[7]] += 1


        cict = {}
        for a in p_pcode_area.keys():
            cict[a] = 0

        for c in dGenerateCars():
            if len(c[7])==0:
                continue
            #if c[7]=="EH": #for some reason my postcode data excludes EH postcode
            #    continue
            #if c[7]=="ML": #for some reason my postcode data excludes ML postcode
            #    continue
            #if c[7]=="G": #for some reason my postcode data excludes G postcode
            #    continue
            #if c[7]=="KY": #for some reason my postcode data excludes KY postcode
            #    continue
            #if c[7]=="PH": #for some reason my postcode data excludes PH postcode
            #    continue
            #if c[7]=="KA": #for some reason my postcode data excludes PH postcode
            #    continue
            #if c[7]=="FK": #for some reason my postcode data excludes FK postcode
            #    continue
            #if c[7]=="DD": #for some reason my postcode data excludes DD postcode
            #    continue
            if c[8]=="SKODA" and c[9]=="CITIGO" and c[2][0:4]=="2019":
                cict[c[7]]+=1

        #print(cict)
        sorteed1 = sorted(cict.keys(), key=lambda p: int(cict[p]))        
        print("2019 Skoda Citigo MOT by Post Code area")
        for a in sorteed1:
            print(a,cict[a])

        cict_pc = {}
        for a in cict.keys():
            #dont use 0 population p area code
            if p_pcode_area[a] == 0:
                continue
            cict_pc[a]=cict[a]/p_pcode_area[a]

        sorteed2 = sorted(cict_pc.keys(), key=lambda p: cict_pc[p])
        print("2019 Skoda Citigo MOT by Post Code area, Per Capita")
        for a in sorteed2:
            print(a,cict_pc[a])

        sys.exit()

    if args.question8 is True:
        #which county has most rolls royce per captita
        #work out rols royce per capita for all post code areas
        p_pcode_area = {'pc': 0, 'AB': 533950.8817646004, 'AL': 269738.17571000225, 'B': 1991073.057345411, 'BA': 423807.9909564766, 'BB': 495689.08093591925, 'BD': 587095.3642845196, 'BH': 559099.3527650888, 'BL': 380872.9611814539, 'BN': 857079.7927516169, 'BR': 307362.5492488172, 'BS': 968932.412706771, 'BT': 1893667.0, 'CA': 323799.8125014299, 'CB': 210616.86297197975, 'CF': 1037681.386420321, 'CH': 480165.3952346568, 'CM': 642444.3080168071, 'CO': 447064.1610122909, 'CR': 430925.1156062462, 'CT': 514088.21861251927, 'CV': 786701.4545968267, 'CW': 299948.2753186591, 'DA': 464740.73301721073, 'DD': 279142.4598993904, 'DE': 490098.7113398885, 'DG': 146355.51817132343, 'DH': 308478.781088173, 'DL': 387755.67623796564, 'DN': 699747.3769466791, 'DT': 220768.0267760806, 'DY': 389260.99044594564, 'E': 1119234.672264762, 'EC': 133221.2997810118, 'EH': 939644.6603634906, 'EN': 362288.2218389178, 'EX': 597943.441391508, 'FK': 283758.7354659648, 'FY': 234952.7794216419, 'G': 1181513.5725514372, 'GL': 589244.106014495, 'GU': 697870.717283279, 'HA': 408366.34827458265, 'HD': 284751.9199649316, 'HG': 128614.0084220901, 'HP': 506134.6107135518, 'HR': 183913.0011400514, 'HS': 14544.13620430646, 'HU': 340277.96157760813, 'HX': 164959.15831571055, 'IG': 381573.6543259759, 'IP': 661504.0919179018, 'IV': 218756.14384431014, 'KA': 367098.47915853723, 'KT': 554763.8963340883, 'KW': 51740.01382989233, 'KY': 378074.3489868345, 'L': 1108332.1981691574, 'LA': 336673.29405858513, 'LD': 49203.966229357015, 'LE': 961880.8604996909, 'LL': 543980.2086851299, 'LN': 269764.3191595417, 'LS': 835613.4330083781, 'LU': 275247.95855747827, 'M': 1292764.4279642196, 'ME': 648798.3491079231, 'MK': 420074.4994829539, 'ML': 385882.59785766416, 'N': 835609.21570022, 'NE': 1198420.831242167, 'NG': 1237977.4291670364, 'NN': 603556.4922857445, 'NP': 520252.5975986275, 'NR': 728213.7707923241, 'NW': 402507.0838701482, 'OL': 496694.2240033805, 'OX': 435400.3182146322, 'PA': 215111.11302522206, 'PE': 936948.9687222829, 'PH': 164557.40302336126, 'PL': 542975.3088715959, 'PO': 848881.4882557077, 'PR': 525127.417398752, 'RG': 744876.4295915223, 'RH': 560065.122925983, 'RM': 557175.6798677116, 'S': 1286313.9705775506, 'SA': 752679.0497433741, 'SE': 1080603.70042657, 'SG': 362730.04196034675, 'SK': 609981.7095787606, 'SL': 406966.4332642214, 'SM': 223227.2367348285, 'SN': 500631.016987324, 'SO': 733031.7925245425, 'SP': 245930.11979584885, 'SR': 249242.44838776445, 'SS': 546250.2626453729, 'ST': 611587.90434149, 'SW': 943604.7887399129, 'SY': 356282.39542570163, 'TA': 341618.90271312697, 'TD': 114906.08665934893, 'TF': 218438.3171026652, 'TN': 743591.3674664351, 'TQ': 300273.17710272997, 'TR': 328282.37027171016, 'TS': 553014.2886462638, 'TW': 541032.4083310588, 'UB': 340395.6334744352, 'W': 643151.3069980209, 'WA': 671518.1500460687, 'WC': 102596.88463750099, 'WD': 280728.4095256867, 'WF': 519310.62808433414, 'WN': 293698.0223223254, 'WR': 304796.4367139767, 'WS': 468716.67819454387, 'WV': 422266.1678966084, 'XX' : 0, 'YO': 526262.0220911006, 'ZE': 22920.0}


        #temp does mot data cover this postal code this exist
        #test11 = { "pc" : 0, "BT" : 0, "EC" : 0 , "GI" : 0 , "GY": 0 , "HS" : 0 , "WC" : 0 , "ZE" : 0 }
        #for c in dGenerateCars():
        #    if c[7] in test11.keys():
        #        test11[c[7]] += 1


        cict = {}
        for a in p_pcode_area.keys():
            cict[a] = 0

        for c in dGenerateCars():
            if len(c[7])==0:
                continue
            if c[8]=="LAND ROVER" and c[9]=="RANGE ROVER" and c[2][0:4]=="2019":
                cict[c[7]]+=1

        #print(cict)
        sorteed1 = sorted(cict.keys(), key=lambda p: int(cict[p]))        
        print("2019 Land Rover Range Rover MOT by Post Code area")
        for a in sorteed1:
            print(a,cict[a])

        cict_pc = {}
        for a in cict.keys():
            #dont use 0 population p area code
            if p_pcode_area[a] == 0:
                continue
            cict_pc[a]=cict[a]/p_pcode_area[a]

        sorteed2 = sorted(cict_pc.keys(), key=lambda p: cict_pc[p])
        print("2019 Land Rover Range Rover MOT by Post Code area, Per Capita")
        for a in sorteed2:
            print(a,cict_pc[a])

        #dump to a json file 2 item list, [0]dictionary per capita,[1]sorted list of pcode area(performance reasons)[2] dictiony count per pcode area[3] sorted list pcode area
        #j = [cict,sorteed1,cict_pc,sorteed2]

        #with open('LAND ROVER RANGE ROVER.json', 'w', encoding='utf-8') as f:
        #    json.dump(j, f, ensure_ascii=False, indent=4)

        sys.exit()
    if args.cAll is True:
        Getgkp()

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
        
        


