#!/usr/bin/python
import commands,cgitb,time,cgi
print "content-type:text/html"
print ""

data=cgi-FieldStorage()
web=data.getvalue('web')
os=data.getvalue('os')
off="sudo qrencode -s 16*16 -o {}.png 'http://192.168.122.1:{}'".format(os,web)
move="sudo mv /var/www/cgi-bin/{}.png /var/www/html/"
commands.getoutput(off)
commands.getoutput(move)
