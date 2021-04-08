import os
import subprocess as sp
a=sp.getoutput("ifconfig enp0s3 | grep inet" )
b=str(a).split()
ip=(b[1])
print("Your Network Card IP is ",ip)


print("Hadoop Configuration")
#Ipadd=input("Please Enter Master Ip ")
#os.system("scp /root/jdk-8u171-linux-x64.rpm {}:/root".format(Ipadd))
#os.system("scp /root/hadoop-1.2.1-1.x86_64.rpm {}:/root".format(Ipadd))
#os.system("ssh {} rpm -ivh /root/jdk-8u171-linux-x64.rpm".format(Ipadd))
#os.system("ssh {} rpm -ivh --force /root/hadoop-1.2.1-1.x86_64.rpm".format(Ipadd))
#os.system("ssh {} ls /etc/hadoop".format(Ipadd))
print("Create a new folder to mount hadoop")
#dir=input("Enter directory name")
#os.system("ssh {} mkdir  /{}".format(ip,dir))
#os.system("ssh {} cat /etc/hadoop/hdfs-site.xml".format(Ipadd))
os.system("ssh {} cat /etc/hadoop/hdfs-site.xml".format(ip))
#os.system("ssh {} hadoop namenode -format /etc/hadoop".format(ip))
