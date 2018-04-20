#!/usr/bin/python3
import pymysql
import sys
import os

os.system("gunzip ../backups/UserDB.sql.gz")
os.system("mysql --user='root' --password='hedia' < ../backups/UserDB.sql")

db=pymysql.connect(host='localhost',user='root',password='hedia',db='UserDB')
cursor_uid=db.cursor()
cursor_gid=db.cursor()
cursor_home=db.cursor()
cursor_shell=db.cursor()
cursor_size=db.cursor()
cursor_date=db.cursor()
sql_uid='SELECT uid FROM Users WHERE user LIKE \''+sys.argv[1]+'\''
sql_gid='SELECT gid FROM Users WHERE user LIKE \''+sys.argv[1]+'\''
sql_home='SELECT home FROM Users WHERE user LIKE \''+sys.argv[1]+'\''
sql_shell='SELECT shell FROM Users WHERE user LIKE \''+sys.argv[1]+'\''
sql_size='SELECT size FROM Users WHERE user LIKE \''+sys.argv[1]+'\''
sql_date='SELECT date FROM Users WHERE user LIKE \''+sys.argv[1]+'\''
print(sql_uid)
print(sql_gid)
print(sql_home)
print(sql_shell)
print(sql_size)
print(sql_date)
cursor_uid.execute(sql_uid)
cursor_gid.execute(sql_gid)
cursor_home.execute(sql_home)
cursor_shell.execute(sql_shell)
cursor_size.execute(sql_size)
cursor_date.execute(sql_date)
data_uid=cursor_uid.fetchone()
data_gid=cursor_gid.fetchone()
data_home=cursor_home.fetchone()
data_shell=cursor_shell.fetchone()
data_size=cursor_size.fetchone()
data_date=cursor_date.fetchone()
print("%s" %sys.argv[1])
print("%i" %data_uid)
print("%i" %data_gid)
print("%s" %data_home)
print("%s" %data_shell)
print("%i" %data_size)
print("%s" %data_date)
cmd='addgroup '+sys.argv[1]+' --gid '+str(data_gid[0])
print ("%s" %cmd)
os.system(cmd)

cmd='adduser '+sys.argv[1]+' --uid '+str(data_uid[0])+' --gid '+str(data_gid[0])+' --home '+str(data_home[0])
print ("%s" %cmd)

os.system(cmd)
cmd='mv ../backups/'+sys.argv[1]+'.tgz /'
print ("%s" %cmd)
os.system(cmd)
cmd='cd /; tar xvzf '+sys.argv[1]+'.tgz'
print ("%s" %cmd)
os.system(cmd)
os.system("mv /*.tgz /root/backups")
os.system("cd /root/backups; gzip UserDB.sql")


