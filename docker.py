import os
import getpass


os.system("clear")

print("---------------------------------------------------------------------------------------------------------------------------------------")
print("                                               Welcome in the Devops World... !!!")
print("---------------------------------------------------------------------------------------------------------------------------------------")



passwd = getpass.getpass("Enter your Password : ")

if passwd != "docker":
  print("Password Incorrect ...")
  print("Please Login again")
  exit()

awskey=raw_input("Enter your AWS Key location : ")
instanceIP=raw_input("Enter the IP of your Instance : ")
osname1=raw_input("Enter your OS name : ")
r = raw_input("\nEnter yes to Continue : ")


while True:
  os.system("clear")
  os.system("tput setaf 5")
  print("                        ------------------------------------------------------------------")
  print("                       |               Enjoy this Menu Driven Program                     |")
  print("                        ------------------------------------------------------------------")   
  os.system("tput setaf 7")  
  

  print("""
  \n
  Press 1  : to configure the docker. 
  Press 2  : to start the docker services.
  Press 3  : to pull the image.
  Press 4  : to launch the container.
  Press 5  : to configure apache webserver on the top of container.
  Press 6  : to get code in the document root.
  Press 7  : to start the webserver .
  Press 8  : to deploy webpage.
  Press 9  : to setup Python Interpreter.
  Press 10 : to run python code.
  Press 11 : to exit.
  
  """)


  choice = input("Enter Your Choice : ")
  
  if r=="yes":
    
    if int(choice) == 1:
      os.system("tput setaf 2")
      
      os.system("tput setaf 1")
      print("\n                                 Docker Engine is going to configure on the top of AWS instance.......\n") 
      os.system("tput setaf 2")   
      os.system("ssh -i {} root@{} sudo yum install docker-ce --nobest -y".format(awskey,instanceIP))
      os.system("tput setaf 7")
      print("\n                                 Docker Engine has been configured")
     
    elif int(choice) == 2:
      os.system("tput setaf 1")
      print("                                   Docker Services is going to start...\n")    
      os.system("ssh -i {} root@{} systemctl start docker".format(awskey,instanceIP))
      os.system("tput setaf 7")
      print("\n                                 Docker Services have been started")
      
      
    elif int(choice) == 3:
      os.system("tput setaf 3")
      image=raw_input("Enter the Docker image name: ")
      version=raw_input("Enter the Docker version name: ")
      os.system("tput setaf 1")
      print("\n                                {} image is going to launch with {} version...\n".format(image,version))
      os.system("tput setaf 3")    
      os.system("ssh -i {} root@{} docker pull {}:{}".format(awskey,instanceIP,image,version))
      os.system("tput setaf 7")
      print("\n                                {} image has been launched with {} version".format(image,version))
      
      

    elif int(choice) == 4:
      os.system("tput setaf 4")   
      osname = raw_input("Enter Container Name : ")
      osimage= raw_input("Enter image name : ")
      osversion=raw_input("Enter image version : ")
      os.system("tput setaf 1")
      print("\n                                {} containter is going to launch...\n".format(osname))
      os.system("tput setaf 4")
      os.system("ssh -i {} root@{} docker run -dit --name {} {}:{}".format(awskey,instanceIP,osname,osimage,osversion))
      os.system("tput setaf 7")
      print("\n                                {} containter has been launched".format(osname) )
      
      
    elif int(choice) == 5:    
      os.system("tput setaf 5")   
      os.system("ssh -i {} root@{} docker exec -dit {} yum install httpd -y".format(awskey,instanceIP,osname1))
      print("apache webserver is now configured")
      os.system("tput setaf 7")

          
      

    elif int(choice) == 6:
      os.system("tput setaf 6")    
      os.system("ssh -i {} root@{} docker exec -dit {} yum install git -y".format(awskey,instanceIP,osname1))
      os.system("ssh -i {} root@{} docker exec -dit {} git clone https://github.com/aaditya2801/menu.git".format(awskey,instanceIP,osname1))
      os.system("ssh -i {} root@{} docker exec -dit {} mv menu/index.html /var/www/html/".format(awskey,instanceIP,osname1))
      print("code is deployed")
      os.system("tput setaf 7")


    elif int(choice) == 7:
      os.system("tput setaf 2")    
      os.system("ssh -i {} root@{} docker exec -dit {} /usr/sbin/httpd".format(awskey,instanceIP,osname1))
      print("service started")
      os.system("tput setaf 7")


    elif int(choice) == 8:
      print("webpage deploying")


    elif int(choice) == 9:
      os.system("tput setaf 4")    
      os.system("ssh -i {} root@{} docker exec -dit {} yum install python3 -y".format(awskey,instanceIP,osname1))
      print("python interpreter setup is done")
      os.system("tput setaf 7")


    elif int(choice) == 10:
      os.system("ssh -i {} root@{} docker exec -dit {} git clone https://github.com/aaditya2801/calculator.git".format(awskey,instanceIP,osname1))
      print()
      os.system("ssh -i {} root@{} docker exec -dit {} python3 /calculator/cal.py".format(awskey,instanceIP,osname1))


    elif int(choice) == 11:
      print("see you soon , have a nice day")
      exit()
    else: 
      print("not supported")
  
  raw_input("\n Press Enter to continue....")
