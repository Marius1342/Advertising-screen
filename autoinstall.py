import pathlib
import os
# install the software
path = os.getcwd()
if os.name != 'nt':
    os.system("sudo apt-get install python3-pip -y")
    os.system("sudo apt-get install chromium-chromedriver -y")
    if os.path.isdir('/home/pi/ad-screen/') == False:
        os.system("mkdir /home/pi/ad-screen")
    os.system("cp " + str(path) +
              "/*.* /home/pi/ad-screen/")
    os.system("cp " + str(path) +
              "/*.* /home/pi/ad-screen/")
    if os.path.isdir('/home/pi/.config/') == False:
        os.system("mkdir /home/pi/.config/")
    if os.path.isdir('/home/pi/.config/autostart') == False:
        os.system("mkdir /home/pi/.config/autostart")
    os.system(
        "cp "+path+"/LinuxScripts/autorunmyad2.desktop /home/pi/.config/autostart/autorunmyad.desktop")
    os.system("pip3 install -r "+str(path) +
              "/requirements.txt")
    print("Edit the config.txt in /home/pi/ad-screen/ then reboot ")
else:
    print("You are using windows. Download pip and the chromium driver\n And change the config.txt")
    os.system("pip3 install -r "+str(path) +
              "/requirements.txt")