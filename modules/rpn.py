
import subprocess


def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False


async def rpninp(self, chan, nick, msg):
  if chan not in self.rpnhist:
    self.rpnhist[chan] = [0]
  self.rpnhist[chan].append(0)
  del self.rpnhist[chan][100:]
  if isfloat(msg):
    self.rpnhist[chan].insert(0, float(msg))
    return
  elif msg == '+' or msg == 'a':
    self.rpnhist[chan][0] = self.rpnhist[chan][0]+self.rpnhist[chan].pop(1)
  elif msg == '-' or msg == 's':
    self.rpnhist[chan][0] =  self.rpnhist[chan].pop(1)-self.rpnhist[chan][0]
  elif msg == '*' or msg == 'x' or msg == 'm':
    self.rpnhist[chan][0] =  self.rpnhist[chan].pop(1)*self.rpnhist[chan][0]
  elif msg == '/' or msg == 'd':
    self.rpnhist[chan][0] =  self.rpnhist[chan].pop(1)/self.rpnhist[chan][0]
  elif msg == 'p':
    pass # just dont do anything lol
  else:
    self.rpnhist[chan].insert(0, self.rpnhist[chan][0])
  await self.message(chan, '[\x036rpn\x0f] '+str(self.rpnhist[chan][0]))
    

async def init(self):
  self.help['rpn'] = ['rpn <inp> - simple reverse polish notation calculator (more)', 'it has an alias of . so you can just do {}. <inp> and also there are 4 f8jct90js (+|a) (-|s) (*|x|m) (/|d) and p to print register 0'.format(self.prefix)]
  self.cmd['rpn'] = rpninp
  self.cmd['.'] = rpninp
  
  self.rpnhist = {}
  
