#!/usr/bin/python
import cgi,cgitb,commands
cgitb.enable()

print "content-type:text/html"
print ""

data=cgi.FieldStorage()
check=data.getvalue('s')

if check == "python" :
	x=commands.getstatusoutput('sudo docker run -itd  jaiky')
	a=x[1]
	y=commands.getstatusoutput('sudo docker exec {} hostname -i'.format(a))
	b=y[1]
	print "<meta HTTP-EQUIV='refresh' content='0;url=http://{}:4200'>".format(b)
'''elif check == "ruby" :
	 x=commands.getstatusoutput('sudo docker run -itd  jaiky')
        a=x[1]
        y=commands.getstatusoutput('sudo docker exec {} hostname -i'.format(a))
        b=y[1]
        print "<meta HTTP-EQUIV='refresh' content='0;url=http://{}:4200'>".format(b)

else :
	print "exit"
'''
