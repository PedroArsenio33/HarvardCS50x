import sys
import csv
import dna2

# inicialize variables
args = sys.argv
lenArgs = len(args)
dicts = []

# take 2 command line arguments, else exit and print error
if lenArgs != 3:
    print("Error, incorrect number or arguments:", lenArgs - 1)
    sys.exit()

# open csv
with open(args[1]) as file:
    reader = csv.DictReader(file)
    for row in reader:
        dicts.append(row)

# open the DNA sequence and read its contents into memory
with open(args[2]) as file:
    seq = file.readline()

# for each STR run longest_match
strs = list(dicts[0].keys())[1:]
strCount = []
newDict = {}

list(dicts[0].keys())[1:]
for i in strs:
    strCount.append(dna2.longest_match(seq, i))

for i in range(len(strCount)):
    newDict[strs[i]] = strCount[i]

# if STR count matches to person print name, otherwise no match
count = len(newDict)
for dict in dicts:
    for key in dict:
        if key != "name" and dict[key] == str(newDict[key]):
            count -= 1
    if count == 0:
        print(dict["name"])
        sys.exit()
    count = len(newDict)

print("No match")
