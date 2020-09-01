import random
import os
#colours
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'
#Code
os.system("apt-get update")
os.system("apt-get upgrade")
os.system("clear")
print("\033[96m ----Scripting start---- $ \033[93mPassword Creater Tool")                              
os.system("toilet -f mono12 -F border P-GEN")

print('\033[93m'""" <<<<<----------\033[96m[( Coded by \033[92mMandeep )]\033[93m--------->>>>>""")
length=int(input("\033[1;37m""Enter The length of The \033[1;33mPassword: ""\033[1;31m"))
print("\033[93m""<----------\033[1;31mPassword Generated\033[93m---------->")
print(" ")
char="abcdefghijklmnopqrstuvwxyz1234567890#$%&*=!"
password = ("\033[1;91m" "\033[1;92m")
for i in range(length):
                                                          password+=random.choice(char)


print(password)
print(" ")
print("\033[90m"">>>>>>>-----\033[94mgrab your password\033[90m-----<<<<<<<")
print(" ")


