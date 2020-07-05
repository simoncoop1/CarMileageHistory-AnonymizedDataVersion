import csv


#for extract data linking postcode to local authorities
#download this data and this script in same folder 
#https://ons.maps.arcgis.com/home/item.html?id=c4aeb11ff5b045018b7340e807d645cb



lads = []

with open("somefile.txt", newline='',encoding = "ISO-8859-1") as txtfile:
    areader = csv.reader(txtfile, delimiter=',')

    for row in areader:
        if row[10] in lads:
            continue
        elif row[10] == "lad11nm": #get rid header
            continue
        else:
            lads.append(row[10])
print("This is the local authorities")
print(lads)


##postcode first digits to lad

pc = []

with open("somefile.txt", newline='',encoding = "ISO-8859-1") as txtfile:
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


with open("somefile.txt", newline='',encoding = "ISO-8859-1") as txtfile:
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
with open("somefile.txt", newline='',encoding = "ISO-8859-1") as txtfile:
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
with open("somefile.txt", newline='',encoding = "ISO-8859-1") as txtfile:
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

with open("LADpops.txt") as f:
    LADpops = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
LADpops = [x.strip() for x in LADpops]

with open("pops.txt") as f:
    pops = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
pops = [x.strip() for x in pops]

print("pops",len(LADpops),len(pops))

matchedExact = []
matchedPartial = []
notmached = []

for a in LADpops:
    if a in lads:
        matchedExact.append(a)

for a in lads:
    if a in matchedExact:
        continue    
    for b in LADpops:
        if (a in b) or (b in a):
            matchedPartial.append(a)

for a in lads:
    if (a not in matchedExact) and (a not in matchedPartial):
        notmached.append(a)

print("matched exact",matchedExact)
print("matched partial",matchedPartial)
print("not matched exact",notmached)

##for the postcode data work out for each lad how much each
#example I have 12 rols royce in CV post code. To get rolls royce pet capita
# 12 / CVpopulation if cv population is 24 the rolls royce per capita is 0.5
#if I know the total population of every post code lad plus for each post code
#area the amount of postcodes from each lad. If for each lad in a postcode area
#I do "(postcodes in this postcode area for this lad /total postcodes in lad)*
#totol pop of the postcode lad=population estimate for the post code area"
#to work out the the population of each post code lad, each popLad should contain
#1 or more postcode lads. If its just 1 then the post code lad population is the
#pop lad population. A post code lad can only belong to 1 pop lad since this accounts
#for entire UK pop.If there are 2 post code lads to a pop lad then the population
#of each post code lad is split from the pop lad based on the number of post codes
#each post code lad has. e.g is the lad pop is 100, and each postcode lad has 20
#post codes the population of each post code lad would be 50. This is based of a 
#postcode having an average population. Not perfect but pretty good.

#poplad : list of tuples postcode lad and a num which will be a population
poplad_postlad = {}
for a in LADpops:
    poplad_postlad[a]=[]

added = [] #keep a store of what is alredy added to the dic
for a in poplad_postlad.keys():
    for b in lads:
        if (a == b) and (b not in added):
            poplad_postlad[a].append([b,0])
            added.append(b)             
        elif ((a in b) or (b in a)) and (b not in added):
            poplad_postlad[a].append([b,0])
            added.append(b)
        elif (b not in added) and (b =="Purbeck" and a=="Dorset"): ##start placing the non fitters
            poplad_postlad[a].append([b,0])
            added.append(b)
        elif (b not in added) and (b =="Forest Heath" and a=="West Suffolk"):
            poplad_postlad[a].append([b,0])
            added.append(b)
        elif (b not in added) and (b =="St Edmundsbury" and a=="West Suffolk"):
            poplad_postlad[a].append([b,0])
            added.append(b)
        elif (b not in added) and (b =="Shepway" and a=="Folkestone and Hythe"):
            poplad_postlad[a].append([b,0])
            added.append(b)
        elif (b not in added) and (b =="Weymouth and Portland" and a=="Dorset"):
            poplad_postlad[a].append([b,0])
            added.append(b)
        elif (b not in added) and (b =="Taunton Deane" and a=="Somerset West and Taunton"):
            poplad_postlad[a].append([b,0])
            added.append(b)
        elif (b not in added) and (b =="West Somerset" and a=="Somerset West and Taunton"):
            poplad_postlad[a].append([b,0])
            added.append(b)
        elif (b not in added) and (b =="Wycombe" and a=="Buckinghamshire"):
            poplad_postlad[a].append([b,0])
            added.append(b)
        elif (b not in added) and (b =="South Bucks" and a=="Buckinghamshire"):
            poplad_postlad[a].append([b,0])
            added.append(b)
        elif (b not in added) and (b =="Chiltern" and a=="Buckinghamshire"):
            poplad_postlad[a].append([b,0])
            added.append(b)
        elif (b not in added) and (b =="Aylesbury Vale" and a=="Buckinghamshire"):
            poplad_postlad[a].append([b,0])
            added.append(b)
        elif (b not in added) and (b =="Suffolk Coastal" and a=="East Suffolk"):
            poplad_postlad[a].append([b,0])
            added.append(b)
        elif (b not in added) and (b =="Waveney" and a=="East Suffolk"):
            poplad_postlad[a].append([b,0])
            added.append(b)

cc1=0
for a in poplad_postlad.keys():
    cc1 +=len(poplad_postlad[a])

print("verify:",cc1,len(lads))#the  dictionary of post lads should all occur once in the poplad dictonary

for a in poplad_postlad.keys():
    this_pop = pops[LADpops.index(a)]

    if not poplad_postlad[a]:
        continue

    allpc = 0
    for b in poplad_postlad[a]:#its a tupple
        allpc += LADcount[b[0]]

    for b in poplad_postlad[a]:
        #print(LADcount[b[0]],float(allpc),this_pop,b[0],LADcount[b[0]]/float(allpc),(LADcount[b[0]]/float(allpc)) * float(this_pop) )

        b[1] = (LADcount[b[0]]/float(allpc)) * float(this_pop)

print(poplad_postlad)


#post code area: population #the final goal
pcapop = {}

for a in pc:
    runnngtot = 0
    for b in pc_dic3[a].keys():
        #get this post code lad pop
        for c in poplad_postlad.keys():
            for d in poplad_postlad[c]:
                if d[0] == b:
                    runnngtot += (d[1] * pc_dic3[a][b]) #is the pop for the lad time mulitplier for its occurence in this post code area

    pcapop[a]=runnngtot

print(pcapop)

sorteed = sorted(pcapop.keys(), key=lambda p: pcapop[p])

for a in sorteed:
    print(a,pcapop[a])   


