import pathlib
import os
# install the software
path = os.getcwd()
if os.name != 'nt':
    os.system("sudo apt-get install python3-pip -y")
    os.system("sudo apt-get install chromium-chromedriver -y")
    os.system("sudo apt-get install chromium-driver -y")
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
    os.system("pip3 install -U -r "+str(path) +
              "/requirements.txt")
    try:
        from selenium import webdriver
    except:
        os.system("pip3 install --user -r "+str(path) +
                  "/requirements.txt")
    try:
        from selenium import webdriver
    except:
        os.system("pip3 install selenium")
    print("Edit the config.txt in /home/pi/ad-screen/ then reboot \n if it doesn't work then type pip3 install selenium")
else:
    print("You are using windows. Download pip and the chromium driver\n And change the config.txt")
    os.system("pip3 install -U -r "+str(path) +
              "/requirements.txt")
