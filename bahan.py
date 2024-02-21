import os,sys
os.system("pkg update && pkg upgrade -y")
os.system("pkg install python -y")
os.system("pkg install openssh -y")
os.system("pip install flask")
os.system("pip install requests")
