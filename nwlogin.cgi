#!/usr/bin/python
import mysql.connector,cgi,cgitb
cgitb.enable()
print "content-type:text/html"
print ""

data=cgi.FieldStorage()
name=data.getvalue('uname')
password=data.getvalue('upass')
email=data.getvalue('uemail')
mobileno=data.getvalue('uphone')

connect=mysql.connector.connect(user='root',password='12345',database='jaiky')
cursor=connect.cursor()
check="select email from rockey where email='{}';".format(email)
cursor.execute(check)
cursor.fetchall()
sumit=cursor.rowcount
if sumit==1:
	print "Email Already Registered, Please try other "
	print "<meta HTTP-EQUIV='refresh' content='2;url=http://192.168.122.1/index.html'/>"
else:
	check="select name from rockey where name='{}';".format(name)
	cursor.execute(check)
	cursor.fetchall()
	sumit=cursor.rowcount

 if sumit == 1 :
	 print "Username Already Taken,Try Another"
 else:
	check=" insert into rockey set name='{}',email='{}',mobileno='{}',password='{}';".format(name,email,mobileno,password)
	cursor.execute(check)
	connect.commit()
	print "<meta HTTP-EQUIV='refresh' content='0;url=http://192.168.122.1/index.html'>" 

