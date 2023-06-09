import os
import subprocess
import psutil
import time
import glob
from pyfiglet import figlet_format

SLEEP_TIME = 5


"""with open("data/brad_local_path.txt") as f:
     locationAPI_file_path = f.read()

with open("data/bnet_local_path.txt") as g:
    bnet_location = g.read()
"""

# replaces above, no more manual path selection
global locationAPI_file_path
global bnet_location

def set_file_paths():
    bnet_location = glob.glob("**/Battle.net Launcher.exe", recursive=True)[0]
    locationAPI_file_path = glob.glob("**/LocationAPI.dll", recursive=True)[0]


def get_pid():
    PID = ((subprocess.run(["pgrep", "CrBrowserMain"],
           capture_output=True).stdout).decode("utf-8")).strip()
    if not PID:
        return False
    else:
        return int(PID)


def check_pid(PID):
    if psutil.pid_exists(PID):
        return True
    else:
        return False


def check_for_file(file_path):
    return (check_file := os.path.isfile(file_path))


def delete_file():
    os.remove(locationAPI_file_path)
    return

# open bnet if not open already


def open_battlenet():
    subprocess.call(f"wine {bnet_location}")
    time.sleep(SLEEP_TIME)


def main():
    set_file_paths()
    PID = get_pid()
    while check_pid(PID):
        if check_for_file(locationAPI_file_path) == False:
            print("File not found, restarting...")
            time.sleep(SLEEP_TIME)
            main()
        else:
            os.remove(locationAPI_file_path)
            print("File removed")
            exit()
    else:
        print("Battlenet process not running, attempting to open...")
        open_battlenet()
        main()


# add os.open function to open bnet in wine if process not found. reduce clicks


if __name__ == "__main__":
    print(figlet_format("rm-locationAPI-HS"))
    main()
