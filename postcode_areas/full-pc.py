import csv

LAD19CD = {}

with open("LA_UA names and codes UK as at 12_19.csv", newline='',encoding = "ISO-8859-1") as txtfile:
    areader = csv.reader(txtfile, delimiter=',')

    for row in areader:
        if row[1] == "LAD19NM": #get rid header
            continue

        LAD19CD[row[0]]=row[1]
        print(row)
print("LAD19CD->LAD19NM")
print(LAD19CD)

with open('somefile.txt', 'a') as the_file:
    with open("ONSPD_AUG_2019_UK.csv", newline='',encoding = "ISO-8859-1") as txtfile:
        areader = csv.reader(txtfile, delimiter=',')

        for row in areader:

            
            skipped = 0

            if row[7]=="oslaua":
                la = "lad11nm"
            #elif row[0][0]=="G":
            #    la = "Glasgow City"
            #elif row[0][0:2]=="FY":
            #    la = "Blackpool"
            #elif row[0][0:2]=="BS":
            #    la = "Bristol, City of"
            elif row[7]=='' or (row[7] not in LAD19CD.keys()): #some of the post code data is lacking local authority data or any other data for that matter, maybe a very new postcode
                skipped+=1
                continue
            else:
                la = LAD19CD[row[7]]

            the_file.write(row[0]+","+row[1]+","+row[2]+",,,,,,,,"+la+"\n")

    #print("This is the local authorities")
    #print(lads)




#with open('somefile.txt', 'a') as the_file:
#    the_file.write('Hello\n')
