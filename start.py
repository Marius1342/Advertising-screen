from browser import Browser
from Config import config
import os
import sys


def main():
    print("Pleas wait 60 seconds if you press SRTG+C")
    browser_ = Browser()
    try:
        browser_.Show()
    except KeyboardInterrupt:
        browser_.driver.close()
        browser_.driver.quit()
        print('Interrupted')
        sys.exit(0)


if __name__ == "__main__":
    argv = sys.argv[1:]
    if "-h" in argv:
        print("-h Help")
        exit()
    main()
