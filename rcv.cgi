#!/usr/bin/python
import os,commands,cgi,cgitb
cgitb.enable()
 
print  "content-type:text/html"
print  ""
 
data=cgi.FieldStorage()
data1=data.getvalue('s')
name=data.getvalue('osn')
ram=data.getvalue('osr')
cpu=data.getvalue('osc')
hdd=data.getvalue('osh')
port=data.getvalue('port')
port1=data.getvalue('port1')


print name
print ram
print cpu
print hdd
print port
print port1

print  "<br><br>"

if data1 == 're':

	os_create="sudo virt-install  --name {} --ram {} --disk none  --cdrom=/var/lib/libvirt/images/rhel-server-7.3-x86_64-dvd.iso  --vcpu {} --graphics vnc,listen=0.0.0.0,port={},password=123  --noautoconsole".format(name,ram,cpu,port)

	print os_create
	run="sudo websockify -D --web=/usr/share/novnc {} 0.0.0.0:{}".format(port1,port)
	print run

	create="sudo virt-install  --name {} --ram {} --disk path=/var/lib/libvirt/images/jaiky.qcow2 --vcpu {} --graphics vnc,listen=0.0.0.0,port={},password=123 --import --noautoconsole".format(name,ram,cpu,port)

	print commands.getstatusoutput(os_create)
	print commands.getstatusoutput(run)
	print commands.getstatusoutput(run)
	print "<meta HTTP-EQUIV='refresh'  content='0;url=http://192.168.0.101/novnc/vnc_auto.html?ip=192.168.0.101&port={}&password=123'/>".format(port1)

else :

	myos_create="sudo virt-install  --name {} --ram {} --disk none  --cdrom=/var/lib/libvirt/images/Fedora.iso --vcpu {} --graphics vnc,listen=0.0.0.0,port={},password=123  --noautoconsole".format(name,ram,cpu,port)

	print myos_create
	myos_run="sudo websockify -D --web=/usr/share/novnc {} 0.0.0.0:{}".format(port1,port)
	print myos_run

	print commands.getstatusoutput(myos_create)
	print commands.getstatusoutput(myos_run)
	print "<meta HTTP-EQUIV='refresh'  content='0;url=http://192.168.0.101/novnc/vnc_auto.html?ip=192.168.0.101&port={}&password=123'/>".format(port1)









