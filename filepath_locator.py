#   WIP, DO NOT COMMIT CHANGES
#   GOAL: Use subprocess.run to get LocationAPI.dll directory, then write this directory to the "filepath.txt"
#   Remember to call locationapi_remover.py after running, or create new main file to call all functions in a single script


import os
import subprocess


x = (subprocess.run(["find", ". -name test"], capture_output= True).stdout).decode("utf-8").strip()

print(x)