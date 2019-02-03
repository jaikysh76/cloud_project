#!/usr/bin/python
import commands,cgi,cgitb
cgitb.enable()
print "content-type:text/html"
print ""
data=cgi.FieldStorage()
python=data.getvalue('s')

commands.getstatusoutput('sudo docker run -itd  -p 7774:4200 jaiky1')
print 
'''
l="<meta HTTP-EQUIV='refresh' content='0; URL=http://192.168.10.132:7774'/>"
	print l
'''
