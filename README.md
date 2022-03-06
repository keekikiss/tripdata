# tripdata
How to run python file for Assignment

1. Run file "setting_db.py"
	- In this file have Create Database 'mytestlab' Table transaction and Table user
	-  Get data from File CSV "transaction.csv" and "user.csv" ,Import to Table in Database 'mytestlab'
	
2. After success, Run file "tripdata.py"
	- Get data to answer 1 and 2
		Q1: What is the total number of trips?
		A1: **10,830 trips**
		Q2: How many provinces are there in the trip with the most number of provinces?
		A2: **17 province**
	- export data to File CSV "province.csv" to "fpgrowth" folder
	
3. Go to folder "fpgrowth" and run file "fpgrowth.py" for answer 3
	Q3: Which province pairs most often appear together in a trip?
	A3: [{'Chanthaburi'}, {'Saraburi'}, {'Lampang'}, {'Chachoengsao'}, {'Ratchaburi'}, **{'Ratchaburi', 'Samut Sakhon'}**, {'Suphan Buri'}, {'Phra Nakhon Si Ayutthaya'}, **{'Phra Nakhon Si Ayutthaya', 'Pathum Thani'}**, {'Samut Prakan'}, {'Samut Sakhon'}, **{'Bangkok', 'Samut Sakhon'}**, **{'Nakhon Pathom', 'Samut Sakhon'}**, {'Nonthaburi'}, **{'Nonthaburi', 'Bangkok'}**, **{'Nonthaburi', 'Pathum Thani'}**, {'Bangkok'}, **{'Bangkok', 'Nakhon Pathom'}**, **{'Bangkok', 'Pathum Thani'}**, {'Nakhon Pathom'}, {'Pathum Thani'}]
freqItemSet, rules = **fpgrowth(output, minSupRatio=0.05, minConf=0.5)**
