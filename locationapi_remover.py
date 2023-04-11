import os
import subprocess
import psutil

with open("filepath.txt") as f:
     locationAPI_file_path = f.read()

def get_pid():
    PID = subprocess.run(["pgrep", "CrBrowserMain"], capture_output= True)
    PID = ((PID.stdout).decode("utf-8")).strip()
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
    check_file = os.path.isfile(file_path)
    return check_file

def delete_file():
        os.remove(locationAPI_file_path)
        return
   
def main():
    PID = get_pid()
    if PID == False:
         print("PID Error: pgrep could not find a battlenet instance")
         pass
    else:
        print(f"Battlenet is open: {check_pid(PID)}")
        print(f"LocationAPI.dll exists: {check_for_file(locationAPI_file_path)}")
        if check_for_file(locationAPI_file_path):
            delete_file()
            print("File Deleted")
        else:
            print("File doesn't exist, no action taken.")


if __name__ == "__main__":
    main()
