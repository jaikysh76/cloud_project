#!/usr/bin/python
import os,commands,cgitb,cgi,time
cgitb.enable()
print "content-type:text/html"
print ""

data=cgi.FieldStorage()
name=data.getvalue('osn')
off="sudo virsh destroy {}".format(name)
commands.getoutput(off)
print name
print "is shuting down"
if 5>3:
	print "<script>"
	print "alert('os is shutdown')"
	print "</script>"
	print"<meta HTTP-EQUIV='refresh' content='0;url=http://127.0.0.1/iaas.html'>"                         
'''else:
	print "<script>"
        print "alert('os is none exists')"
        print "</script>"
        print"<meta HTTP-EQUIV='refresh' content='0;url=http://127.0.0.1/iaas.html'>"'''
