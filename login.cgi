#!/usr/bin/python
import os,commands,cgi,cgitb,mysql.connector
cgitb.enable()

print "content-type:text/html"
print ""

data=cgi.FieldStorage()
user=data.getvalue('u')
password=data.getvalue('p')
x1=commands.getoutput('sudo hostname -I')
ip=x1.split(' ')
conn=mysql.connector.connect(user='root',password='12345',database='jaiky')
cursor=conn.cursor()
my="select name,password from rockey where name='{}'and password='{}';".format(user,password)
cursor.execute(my)
cursor.fetchall()
papa=cursor.rowcount
print papa
if papa == 1:
	print "<script>"
	print "alert('click here to load')"
	print "ENJOY THE CLOUD SERVICES"
	print "</script>"
	print "<meta HTTP-EQUIV='refresh' content='0;url=http://{}/cloud.html'>".format(ip[0])
else :
	print "bad authentication redirecting to login page"
	print "<script>"
        print "alert('back on the initial page')"
        print "</script>"
        print "<meta HTTP-EQUIV='refresh' content='0;url=http://{}/index.html'>".format(ip[0])

