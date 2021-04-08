import os
import getpass
import webbrowser

print()
print("welcome to my menu !!!")
print("----------------------")

passwd = getpass.getpass("Enter your Password : ")

if passwd != "docker":
  print("password incorrect ...")
  exit()

print()

r = input("Enter yes to Continue : ")
print(r)


while True:
  os.system("clear")
  print("""
  \n
  Press 1 : to configure apache webserver on the top of container.
  Press 2 : to get code in the document root.
  Press 3 : to start the webserver .
  Press 4 : to deploy webpage.
  Press 5 : to setup Python Interpreter.
  Press 6 : to run python code.
  Press 7 : to exit.
  """)


  choice = input(" Enter Your Choice : ")
  print(choice)

  osname = input("Enter Container Name : ")

  if r == "yes":
    if int(choice) == 1:
      os.system("docker exec -it {} yum install httpd -y".format(osname))
      print("apache webserver is now configured")
    elif int(choice) == 2:
      os.system("docker exec -it {} yum install git -y".format(osname))
      os.system("docker exec -it {} git clone https://github.com/aaditya2801/menu.git".format(osname))
      os.system("docker exec -it {} mv menu/index.html /var/www/html/".format(osname))
      print("code is deployed")
    elif int(choice) == 3:
      os.system("docker exec -it {} /usr/sbin/httpd".format(osname))
      print("service started")
    elif int(choice) == 4:
      webbrowser.open("192.168.29.56:8080/index.html")
      print("webpage deploying")
    elif int(choice) == 5:
      os.system("docker exec -it {} yum install python3 -y".format(osname))
      print("python interpreter setup is done")
    elif int(choice) == 6:
      os.system("docker exec -it {} git clone https://github.com/aaditya2801/calculator.git".format(osname))
      print()
      os.system("docker exec -it {} python3 /calculator/cal.py".format(osname))
    elif int(choice) == 7:
      print("see you soon , have a nice day")
      exit()
    else:
      print("not supported")

  input("\n Press Enter to continue....")
