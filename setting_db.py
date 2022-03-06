import csv
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS mytestlab CHARACTER SET utf8 COLLATE utf8_general_ci")
mycursor.execute("SHOW DATABASES")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mytestlab"
)
mycursor = mydb.cursor()

file_user = open("user.csv")
csvreader_user = csv.reader(file_user)
header_user = next(csvreader_user)
# Create Table user
mycursor.execute('CREATE TABLE IF NOT EXISTS user (user_id varchar(100), hometown varchar(100))')
for row_user in csvreader_user:
    sql = "INSERT INTO user (user_id, hometown) VALUES (%s, %s)"
    val = (row_user[0], row_user[1])
    mycursor.execute(sql, val)
file_user.close()

file_tran = open("transaction.csv")
csvreader_tran = csv.reader(file_tran)
header_tran = next(csvreader_tran)
# Create Table transaction
mycursor.execute('CREATE TABLE IF NOT EXISTS transaction (date varchar(100), hour varchar(100), user_id varchar(100), province varchar(100))')
for row_tran in csvreader_tran:
    sql = "INSERT INTO transaction (date, hour, user_id, province) VALUES (%s, %s, %s, %s)"
    val = (str(row_tran[0]), row_tran[1], row_tran[2], row_tran[3])
    mycursor.execute(sql, val)
file_tran.close()