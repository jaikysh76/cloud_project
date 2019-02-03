#!/usr/bin/python
import cgi,os,commands,time,cgitb
cgitb.enable()
print "content-type:text/html"
print ""
data=cgi.FieldStorage()
dn=data.getvalue('dn')
ds=data.getvalue('ds')
print dn
print ds

x1=commands.getoutput('hostname -I')
ip=x1.split(' ')

commands.getoutput('sudo lvcreate --name {}   --size {} M adhoccloud'.format(dn,ds))
commands.getoutput('sudo mkfs.fat /dev/adhoccloud/{}'.format(dn))
commands.getoutput('sudo mkdir  /mnt/{}'.format(dn))
commands.getoutput('sudo mount /dev/adhoccloud/{}    /mnt/{}'.format(dn,dn))

nfs_write="/mnt/{}    *(rw,no_root_squash)\n".format(dn)
x=open('/etc/exports','a')
x.write(nfs_write)
x.close()
commands.getoutput('sudo exportfs -r')
commands.getoutput('sudo touch /mnt/myproject/{} > {}.sh'.format(dn,dn)) 
m="{}.sh".format(dn)

commands.getstatusoutput("echo 'mkdir /mnt/{}' > {}.sh".format(dn,dn))
commands.getstatusoutput("echo mount {}:/mnt/{} /mnt/{} >> {}.sh".format(ip[0],dn,dn,dn))

commands.getstatusoutput('sudo chmod o+w {}'.format(m))
commands.getstatusoutput('sudo chmod +x {}.sh'.format(dn))
print commands.getoutput('sudo tar cvf ../html/{}.tar {}.sh'.format(dn,dn))
print "<script>"
print "alert('extract to mount your storage:')"
print "</script>"
m1= "<meta HTTP-EQUIV='refresh' content='0;url=http:///{}/{}.tar'/>".format(ip[0],dn)
print m1

