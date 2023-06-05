# rm-locationAPI-HS
Simple script fix to get Hearthstone working on Linux via Wine/Lutris

# Usage
Simply run the script on the same drive you have Heartstone installed on.
```bash
python3 locationapi_remover.py
```

# Why?
Game crashes when file is present and constantly redownloads it upon relaunch. This script checks if battlenet is open, and deletes the file if present, fixing the issue upon every launch.


