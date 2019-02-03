#!/usr/bin/python
import mysql.connector,commands,cgi,cgitb,os,random
cgitb.enable()
print "content-type:text/html"
print ""
data=cgi.FieldStorage()
name=data.getvalue('uname')
password=data.getvalue('upass')
email=data.getvalue('uemail')
mobileno=data.getvalue('uphone')
x=random.randint(1,200)
conn=mysql.connector.connect(user='root',password='12345',database='jaiky')
cursor=conn.cursor()
my="select name,email from rockey where name='{}' and email='{}';".format(name,email)
cursor.execute(my)
res=cursor.fetchall()
res=cursor.rowcount
print res
if res == 1:
	print "</script>"
	print "alert('YOU'RE ALREADY REGISTERED..')"
	print "alert('PLEASE LOGIN ..')"
	print "</script>"
	print "<meta HTTP-EQUIV='refresh' content='0;url=http://192.168.122.1/index.html'/>"
else :
	he="insert into rockey SET name='{}',password='{}',email='{}',mobileno='{}',sno='{}';".format(name,password,email,mobileno,x)
	cursor.execute(he)
	conn.commit() 
	print "<meta HTTP-EQUIV='refresh' content='0;url=http://192.168.122.1/index.html'>"
