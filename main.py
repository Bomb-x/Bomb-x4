bgreen="\033[1;32m"       # Green
bblack="\033[1;30m"       # Black
r="\033[1;31m"         # Red
bgreen="\033[1;32m"       # Green
y="\033[1;33m"      # Yellow
bblue="\033[1;34m"        # Blue
p="\033[1;35m"      # Purple
c="\033[1;36m"        # Cyan
bwhite="\033[1;37m"       # White
logo=bgreen+str("""
$$$$$$$\                          $$\                        
$$  __$$\                         $$ |                       
$$ |  $$ | $$$$$$\  $$$$$$\$$$$\  $$$$$$$\         $$\   $$\ 
$$$$$$$\ |$$  __$$\ $$  _$$  _$$\ $$  __$$\ $$$$$$\\$$\ $$  |
$$  __$$\ $$ /  $$ |$$ / $$ / $$ |$$ |  $$ |\______|\$$$$  / 
$$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |        $$  $$<  
$$$$$$$  |\$$$$$$  |$$ | $$ | $$ |$$$$$$$  |       $$  /\$$\ 
\_______/  \______/ \__| \__| \__|\_______/        \__/  \__|
=================================================================
     ***[✓] Devoloper : Mishkat Zaman***
=================================================================
            Version : 2.1.0
""")
import os
while True:
	os.system("clear")
	print(logo)
	print(r+""" [1] Sms bomber\n [2] E-Mail bomber\n [3] Mask phishlink\n [4] DDos attack ©hammer \n [5] Termux banner ©chb\n [6] Exit """)
	a=str(input(c+""" 
[✓] Select your option : """+y))
	if a=="1":
		os.system("python3 01.py")
		a=input()
	elif a=="2":
		os.system("python3 02.py")
		a=input()
	elif a=="3":
		os.system("python3 03.py")
		a=input()
	elif a=="4":
		os.system("python3 04.py")
		a=input()
	elif a=="5":
		os.system("python3 05.py")
		a=input()
	elif a=="6":
		print(c+""" 
		Thanks for using 
		★★★Bomb-x★★★       
		""")
		quit()
		a=input()
	else:
		print(p+"Wrong Value Enterd")
		a=input()