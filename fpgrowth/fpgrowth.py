from fpgrowth_py import fpgrowth
import csv

file_name = "province.csv"
output = []
with open(file_name, 'r') as f:
    content = csv.reader(f, delimiter=',')
    for line in content:
        output.append([i for i in line])

    for line in content:
    	if len(line) > 1 :
        	output.append([i for i in line])

freqItemSet, rules = fpgrowth(output, minSupRatio=0.05, minConf=0.5)
print(freqItemSet)
print(rules)