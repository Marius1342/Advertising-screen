# Advertising-screen

*Show Websites at autostart in full screen. Works with an Raspberry Pi 3b.*
* Why this software
    * ✅  Compatible with an Rpi 3b
    * ✅  Auto Shutdown on Linux Systems via Website data
    * ✅  Autostart up script
    * ✅  Automatic login
    * ✅  Inexpensive

__Written in Python and use Selenium__

## Setup with an Raspberry 3b

*Installation about 1 hour 🕐 it depends on your internet connection*

* Needed things
    * Rpi3 or Rpi3b+
        * 📝  Minimum ram memory 1 gig
        * 📝  Raspberry Pi os with Desktop
        * 📝  Sd Card about 16 gig
    * Internet connection
    * An compatible screen compatible for you purpose
    * Keyboard and mouse
    * Website with your advertisements

## Installation 

### Auto Setup
__Only use this if you have no other programm__
- Install the Pi Os
- Install python via *sudo apt-get install python3.7 -y*
- Download the Files and run the script in the same directory *python3 autoinstall.py*
- Type top to find 🔎 your memory *Mib mem*
- Change the the Swap file if you have only 2 or 1 gig type *sudo nano etc/dphys-swapfile* and change the *CONF_SWAPSIZE* varibel to the value currentMemory*2 exampel 1024mib memory then your swap should be 2048
__WARNING only use intergers !!__
- Now you are ready change the *config.txt it is now in the folder /home/pi/ad-screen/config.txt*
- Install the Chromium driver *sudo apt-get install chromium-chromedriver -y*
- Dont forget to change the gpu memory in the settings it should be 256 or higer
- Edit the /boot/config.txt and type *hdmi_force_hotplug=1* this will force the pi to start without an monitor
- Then reboot and it is done 
- If it doen't work then type *pip3 install selenium*

### Full Setup
- Install the Rpi os
- Open Ternimal and type *sudo apt-get install nano -y* that installs nano if it isnt installed yet
- Type top to find 🔎 your memory *Mib mem*
- Change the the Swap file if you have only 2 or 1 gig type *sudo nano etc/dphys-swapfile* and change the *CONF_SWAPSIZE* varibel to the value currentMemory*2 exampel 1024mib memory then your swap should be 2048
__WARNING only use intergers !!__
- Then open the config panel from the pi and set the Video Memory or gpu memory to 256 or higer
- Open Chromium and clone all Files
- Type in the ternimal *sudo apt-get install python3.7 -y*
- Copy the downloaded files to a folder
- Type in the Ternimal *sudo apt-get install python3-pip -y*
- Open a Ternimal in your Folder with the Files
- The Type *pip3 install -r requirements.txt* if it dint work use pip instead of pip3
- Now you are ready change the *config.txt*
- Install the Chromium driver *sudo apt-get chromium-chromedwriver -y*
- Then rebot the Pi
- Open your and ternimal in your folder and type *python3 start.py*
- Now you can make a autostart up script just read the *Linux Script/howto.txt*
- Edit the /boot/config.txt and type *hdmi_force_hotplug=1* this will force the pi to start without an monitor
- You did it have fun

### Setup the Config.txt
__Sysntax:__

- shutdownurl=url
    * *shutdownrl* thi is the key
    * *=* this splits the key from the value
    * *url* this is the value pleas dont use a [SPACE] or =

#### All Keys
- *loginurl* this is the url for login
- *showurl* this is the url with the advertisment
- *shutdownurl* this is the url for the shutdown time use only a .txt file with this format HH:MM
- *password* the passowrd to login
- *username* the username to login
- *box-username* the name html tag of the username field
- *box-password* the name html tag of the password field
- *submite-button* the name of the submite button
- *Login* if set to True then the System Login in if it is False then it dont Login in 
- *Titel-Login* the Login titel of the site it must be static
- *Titel* set this to the advertisment site titel only set this if your site is static
- *refreshtime* this is the time to refresh the page set this like a float like 1.5 the format is hour
- *refresh* if the system should use the refresh
- *shutdown* if it set shutdown
- *cookie-banner* if you have a cookie banner set this to your name Tag
- *boot-delay* this delay is when your coonection is bad then the programm will wait (only intigers)
