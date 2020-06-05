
import json, requests


async def lookup(self,c,n,m):
  if len(m) < 1:
    await self.message(c, '[\x036ham\x0f] you need the callsign lol')
    return
  res = requests.get('https://callook.info/{}/json'.format(m))
  if res.status_code :
    js = res.json()
    if js['status'] == 'VALID':
      await self.message(c, '[\x036ham\x0f] {}, name: {} grid: {}, expires: {}'.format(js['current']['operClass'], js['name'], js['location']['gridsquare'], js['otherInfo']['expiryDate']))
      return
    await self.message(c, '[\x036ham\x0f] invalid callsign')
  else:
    await self.message(c, '[\x036ham\x0f] something went wrong...')


async def init(self):
  self.cmd['lookup'] = lookup
  self.help['lookup'] = ['lookup <callsign> - lookup a ham callsign','ROBERT']


