#!/usr/bin/python
import os,commands,cgi,cgitb
cgitb.enable()

print "content-type:text/html"
print ""



data=cgi.FieldStorage()
check=data.getvalue('s')
x1=commands.getoutput('hostname -I')
ip=x1.split(' ')

if check == 'saas' :

	print "welcome to saas"
	print "<meta HTTP-EQUIV='refresh' content='0;url=http://{}/saas.html'>" .format(ip[0])

if check == 'staas' :

	print "welcome to staas"
	print "<meta HTTP-EQUIV='refresh' content='0;url=http://{}/staas.html'>".format(ip[0])


if check == 'iaas' :
	print "welcome to iaas"
 	print "<meta HTTP-EQUIV='refresh' content='0;url=http://{}/iaas.html'>".format(ip[0])
if check == 'paas' :
	print "welcome to iaas"
 	print "<meta HTTP-EQUIV='refresh' content='0;url=http://{}/paas.html'>".format(ip[0])
