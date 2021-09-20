import os
import json


class config:
    def __init__(self):
        File = open(os.path.join(os.path.dirname(__file__), "config.txt"))
        self.JsonValues = json.loads('{}')
        for line in File.readlines():
            # remove the empty lines
            if(line.strip() == ""):
                continue
            if(line.startswith('#') == False):
                # Get the Key
                key = line.strip().split("=")[0]
                # Get the value and Remove the Comment
                value = line.strip().split("=")[1].split("#")[0]
                # Add new item
                self.JsonValues.update({key.strip(): value.strip()})
