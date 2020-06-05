

async def listMods(self,c,n,m):
  await self.message(c,'[\x036modulemanager\x0f] currently loaded mods: {}'.format(list(self.modules.keys())))

async def init(self):
  self.help['modules'] = ['modules - list the modules',':o']
  self.cmd['modules'] = listMods

