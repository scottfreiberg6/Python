teamdict ={
    "Bronx": "Yankees",
    "Queens": "mets",
    "Boston": "Red Sox"
} 
# print (teamdict) 
# prints whole dictionary
# print(teamdict{1})

# Nfllist =["NYGiants","NYJets","TBBucs"]
# Nfllist[2]="MiaDolphins"
# print(Nfllist)


def searchdict (some_list):
    for i in teamdict:
        print (i+teamdict[i])
        
searchdict(teamdict)