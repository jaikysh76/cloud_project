#!/usr/bin/python
import socket,os,commands,cgitb,cgi,time
cgitb.enable()
print "content-type:text/html"
print ""

data=cgi.FieldStorage()
name=data.getvalue('osn')
off="sudo virsh undefine {}".format(name)
commands.getoutput(off)
print name
print "is deleted"
print"<meta HTTP-EQUIV='refresh' content='0;url=http://127.0.0.1/iaas.html'>"
