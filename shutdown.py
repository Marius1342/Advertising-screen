import os
import re
import requests


class Shutdown:

    def __init__(self, time):
        time = requests.get(time, verify=False).text
        if re.match('^[\d:]{2}:[\d]{2}', time) != None and len(time) == 6:
            os.system("shutdown -h " + time)
        else:
            print("No matching in the time: " +
                  time + " Vaild Time pattern hh:mm")
