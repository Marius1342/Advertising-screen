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
__Only use this if you have no other programs__
- Install the Pi Os
- Install python via *sudo apt-get install python3.7 -y*
- Download the Files and run the script in the same directory *python3 autoinstall.py*
- Type top to find 🔎 your memory *Mib mem*
- Change the the Swap file if you have only 2 or 1 gig type *sudo nano etc/dphys-swapfile* and change the *CONF_SWAPSIZE* varibel to the value currentMemory*2 example 1024mib memory then your swap should be 2048
__WARNING only use integers !!__
- Now you are ready change the *config.txt it is now in the folder /home/pi/ad-screen/config.txt*
- Install the Chromium driver *sudo apt-get chromium-chromedriver -y*
- Don't forget to change the gpu memory in the settings it should be 256 or higher
- Edit the /boot/config.txt and type *hdmi_force_hotplug=1* this will force the pi to start without an monitor
- Then reboot and it is done 
- If it doesn't work then type pip3 install selenium

### Full Setup
- Install the Rpi os
- Open terminal and type *sudo apt-get install nano -y* that installs nano if it isn't installed yet
- Type top to find 🔎 your memory *Mib mem*
- Change the the Swap file if you have only 2 or 1 gig type *sudo nano etc/dphys-swapfile* and change the *CONF_SWAPSIZE* varibel to the value currentMemory*2 example 1024mib memory then your swap should be 2048
__WARNING only use intergers !!__
- Then open the config panel from the pi and set the Video Memory or gpu memory to 256 or higher
- Open Chromium and clone all Files
- Type in the terminal *sudo apt-get install python3.7 -y*
- Copy the downloaded files to a folder
- Type in the terminal *sudo apt-get install python3-pip -y*
- Open a terminal in your Folder with the Files
- The Type *pip3 install -r requirements.txt* if it dint work use pip instead of pip3
- Now you are ready change the *config.txt*
- Install the Chromium driver *sudo apt-get chromium-chromedwriver -y*
- Then reboot the Pi
- Open your and terminal in your folder and type *python3 start.py*
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
- *showurl* this is the url with the advertisements
- *shutdownurl* this is the url for the shutdown time use only a .txt file with this format HH:MM
- *password* the password to login
- *username* the username to login
- *box-username* the name html tag of the username field
- *box-password* the name html tag of the password field
- *submite-button* the name of the submit button
- *Login* if set to True then the System Login in if it is False then it don't Login in 
- *Titel-Login* the Login title of the site it must be static
- *Titel* set this to the advertisement site title only set this if your site is static
- *refreshtime* this is the time to refresh the page set this like a float like 1.5 the format is hour
- *refresh* if the system should use the refresh
- *shutdown* if it set shutdown
- *cookie-banner* if you have a cookie banner set this to your name Tag
- *boot-delay* this delay is when your connection is bad then the program will wait (only integers)
