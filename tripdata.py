import csv
import mysql.connector
from collections import defaultdict
import pprint

pp = pprint.PrettyPrinter(indent=0, width=100)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mytestlab"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT *, IF(t.province = u.hometown, '0', '1') AS check_ht FROM user u INNER JOIN transaction t ON t.user_id = u.user_id ORDER BY u.user_id ASC, t.date ASC, t.hour ASC")

def getNextKey(dict, key):
    keys = iter(dict)
    key in keys
    return next(keys, "")

transaction = mycursor.fetchall()

ishometown = {}
samedate = {}
for key, value in enumerate(transaction):
  if value[6] == '0':
    ishometown[key] = key

ishometownarr = defaultdict(list)

for key, value in enumerate(ishometown):
  nextkey = getNextKey(ishometown, value)
  if nextkey != "":
    for i in range(value, nextkey, 1):
      if i != value:
        ishometownarr[value].append(transaction[i])

final = defaultdict(list)
for key, value in enumerate(ishometownarr):
  lenValue = len(ishometownarr[value])
  if lenValue > 1:
    for sub_key, sub_value in enumerate(ishometownarr[value]):
      if sub_value not in final:
        final[0].append(sub_value)


province = defaultdict(list)
for key, value in enumerate(final):
  for sub_key, sub_value in enumerate(final[value]):
    province[0].append(sub_value[5])

seen = set()
uniq = []
uniqKey = defaultdict(list)
def get_unique_numbers(lists):
  for key, value in enumerate(lists):
    if value in seen:
      uniq.append(value)
      uniqKey[key].append(value)
    else:
      seen.add(value)
  return uniq

duplicates = get_unique_numbers(province[0])

def find_key(dic, val):
  for key, value in enumerate(dic):
    if value == val:
      return key

dupKeyProvince = []
dupKeyProvinceKey = []
if len(duplicates) > 0:
  for key, value in enumerate(province[0]):
    if value in duplicates:
      dupKeyProvince.append(value) # value
      dupKeyProvinceKey.append(key) # key

  # value
  myLastElement = int(dupKeyProvinceKey[-1])
  # key
  beforeLastElement = len(dupKeyProvinceKey)-1 # get last key of element
  prevKeyOrg = beforeLastElement-1
  preKeyDupKey = len(dupKeyProvinceKey)-1
  firstDupKey = find_key(province[0], uniqKey[myLastElement][0])

  pre_pro = ""
  cur_pro = ""
  merge_date = defaultdict(list)
  for i in range(0, len(dupKeyProvince), 1):
    if i == prevKeyOrg:
      pre_pro = final[0][dupKeyProvinceKey[prevKeyOrg]]
      merge_date[dupKeyProvince[prevKeyOrg]].append(final[0][dupKeyProvinceKey[prevKeyOrg]][2])

    if dupKeyProvinceKey[i] == myLastElement:
      cur_pro = final[0][myLastElement][5]
      merge_date[myLastElement].append(final[0][myLastElement][2])

  if pre_pro == cur_pro :
    maxdate = merge_date[dupKeyProvince[prevKeyOrg]]
    for key, value in enumerate(final):
      if key == myLastElement:
        del ishometownarr[dupKeyProvinceKey[beforeLastElement]][firstDupKey]
        del ishometownarr[dupKeyProvinceKey[beforeLastElement]][key-1]
        ishometownarr[key].append(final[value][0])

tempdata = defaultdict(list)
for key, value in enumerate(ishometownarr):
  count = 0
  if len(ishometownarr[value]) > 1:
    user_id = ""
    province_list = ""
    pushdate = []
    
    for sub_key, sub_value in enumerate(ishometownarr[value]):
      user_id = sub_value[0]
      province_list += sub_value[5]+', '
      pushdate.append(sub_value[2])
      count = count+1

    tempdata[key].extend([user_id, min(pushdate), max(pushdate), province_list[0:-2], 'count: '+str(count)])
    
  else:
    for sub_key, sub_value in enumerate(ishometownarr[value]):
      tempdata[key].extend([sub_value[0], sub_value[2], sub_value[2], sub_value[5], 'count: 1'])

pp.pprint(tempdata)      
      
# open the file in the write mode
with open('./fpgrowth/province.csv', 'w', encoding='UTF8', newline='') as f:
  # create the csv writer
  writer = csv.writer(f)
  # write a row to the csv file
  for sub_list in tempdata:
    s = tempdata[sub_list][3]
    writer.writerow([element.strip("'") for element in s.split(', ')])
