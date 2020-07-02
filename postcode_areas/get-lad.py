import csv


#for extract data linking postcode to local authorities
#download this data and this script in same folder 
#https://ons.maps.arcgis.com/home/item.html?id=c4aeb11ff5b045018b7340e807d645cb


lads = []

with open("pcd11_par11_wd11_lad11_ew_lu.csv", newline='',encoding = "ISO-8859-1") as txtfile:
    areader = csv.reader(txtfile, delimiter=',')

    for row in areader:
        if row[10] in lads:
            continue
        else:
            lads.append(row[10])
print("This is the local authorities")
print(lads)


##postcode first digits to lad

pc = []

with open("pcd11_par11_wd11_lad11_ew_lu.csv", newline='',encoding = "ISO-8859-1") as txtfile:
    areader = csv.reader(txtfile, delimiter=',')

    for row in areader:
        if row[0]=="pcd7":
            continue

        if row[0][1].isalpha():
            if row[0][0:2] in pc:
                continue
            else:
                pc.append(row[0][0:2])
        else:
            if row[0][0:1] in pc:
                continue
            else:
                pc.append(row[0][0:1])


print(pc)



pc_dic = {}

for a in pc:
    pc_dic[a]=[]


with open("pcd11_par11_wd11_lad11_ew_lu.csv", newline='',encoding = "ISO-8859-1") as txtfile:
    areader = csv.reader(txtfile, delimiter=',')



    for row in areader:
        if row[0]=="pcd7":
                continue
        if row[0][1].isalpha():
            if row[10] not in pc_dic[row[0][0:2]]:
                pc_dic[row[0][0:2]].append(row[10])
        else:
            if row[10] not in pc_dic[row[0][0:1]]:
                pc_dic[row[0][0:1]].append(row[10])



##make double dictionary 
pc_dic2= {}

for a in pc_dic.keys():
    pc_dic2[a]={}
    for b in pc_dic[a]:
        pc_dic2[a][b]=0


##now add the count
#dictionary of postcode area -----> dictionary of local distrricts ----> number of postcodes
# in that local district with that post code area
with open("pcd11_par11_wd11_lad11_ew_lu.csv", newline='',encoding = "ISO-8859-1") as txtfile:
    areader = csv.reader(txtfile, delimiter=',')

    for row in areader:
        if row[0]=="pcd7":
            continue

        if row[0][1].isalpha():
            pc_dic2[row[0][0:2]][row[10]]+=1
        else:
            pc_dic2[row[0][0:1]][row[10]]+=1
                

print(pc_dic2)


LADcount = {}
##a dictionary LAD name ---> overall count. non post code area specific
with open("pcd11_par11_wd11_lad11_ew_lu.csv", newline='',encoding = "ISO-8859-1") as txtfile:
    areader = csv.reader(txtfile, delimiter=',')

    for row in areader:
        if row[0]=="pcd7":
            continue

        if row[10] not in LADcount.keys():
            LADcount[row[10]] = 1    
        else:
            LADcount[row[10]] += 1 

print(LADcount)     


##pc_dic3 should store for a post code area each LAD and the proportion of postcodes under that postcode area
pc_dic3 = {}

for a in pc_dic2.keys():
    pc_dic3[a]= {}

for a in pc_dic2.keys():
    for b in pc_dic2[a].keys():
        pc_dic3[a][b]=pc_dic2[a][b]/float(LADcount[b])

print(pc_dic3)


##now need to import literal for the population plus lad
pops = [530094,106803,93663,140980,322434,137150,197348,202055,302820,207913,150976,277705,149696,139446,384152,343071,129410,210014,97761,67049,108678,68183,53253,105088,287550,190990,552858,237110,222412,258834,293423,226493,237354,328662,88920,118216,80780,81043,146038,92112,143135,60888,71482,110788,114306,112091,150862,498042,276410,180585,324011,341173,259778,159563,172292,210618,57142,91594,160831,53730,55380,108757,90620,246866,311890,265411,584853,539776,211455,439787,793139,348312,257302,354224,332900,39927,128147,80562,104900,72325,115371,92666,101462,107261,101526,185851,93807,113136,51209,103611,57015,70173,141727,99299,116915,95019,142424,95667,72218,85950,94527,101776,224610,94490,79707,127918,117459,114033,117896,109313,122421,119184,192801,323136,256375,179854,100762,119754,104756,129441,112436,137280,98435,76696,65264,129883,108935,130098,143753,1141816,371521,321596,328450,216374,285478,263357,99881,78698,85261,101222,129433,101291,173292,288648,213052,202259,183125,174341,124798,89840,101850,177963,159086,187199,152604,77021,90376,178388,194706,131689,87067,64926,87368,146561,91284,97279,154763,149748,104919,133570,148452,87845,93323,96577,123043,139968,130783,99336,151383,104837,140573,140880,92036,249461,136913,103895,179045,270029,9721,281120,185143,268647,242467,156129,326034,305842,353134,318830,324745,329677,261317,212906,395869,248287,329771,332336,386710,341806,333794,287942,251160,259552,306870,271523,177507,206548,305222,198019,206349,276983,122549,290885,141771,278556,269457,214905,161780,149539,252520,158450,151422,171119,543973,103745,92661,103268,96080,161475,176582,122308,133584,116233,84838,97073,126220,180086,94599,126160,124859,130032,165394,112606,118131,112996,106939,171826,120750,150082,141922,132153,118724,150503,152457,142057,136007,110643,136795,80627,148998,87245,148748,89424,99844,89305,88129,126328,100793,64301,160758,121129,112409,143791,151022,110570,193282,395331,463377,569578,378508,2224,215052,262100,285093,222193,136264,500024,146284,131405,82311,97145,87004,134163,68267,55796,116306,89862,86791,129128,119964,95019,115587,123178,155115,168345,70043,124560,117203,95696,156100,135957,132435,72695,125818,188771,246993,143315,147049,133587,366903,241264,60326,181075,69862,93961,94590,154676,228670,261210,116200,85870,524930,51540,148860,149320,122010,108640,107090,95530,160890,373550,633120,235830,77800,92460,95820,26720,134740,341370,22270,151950,179100,115510,22920,112610,320530,94210,88930,183100,143504,161725,216205,343542,144838,151284,117397,146002,139274,148528,181368]
with open("LADpops") as f:
    LADpops = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
LADpops = [x.strip() for x in LADpops]
print(len(LADpops))
print(len(pops))

    



