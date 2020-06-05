
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
  del self.rpnhist[chan][15:]
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
    try:
      self.rpnhist[chan][0] =  self.rpnhist[chan].pop(1)/self.rpnhist[chan][0]
    except ZeroDivisionError:
      self.rpnhist[chan][0] = float('NaN')

  elif msg == '^' or msg == 'e':
    self.rpnhist[chan][0] =  self.rpnhist[chan].pop(1)**self.rpnhist[chan][0]

  elif msg == 'p':
    pass # just dont do anything lol
  elif msg == 'r':
    await self.message(chan, '[\x036rpn\x0f] {}'.format(str(self.rpnhist[chan])))
    return
  else:
    return
  await self.message(chan, '[\x036rpn\x0f] '+str(self.rpnhist[chan][0]))
    

async def init(self):
  self.help['rpn'] = ['rpn <inp> - simple reverse polish notation calculator (more)', 'it has an alias of . so you can just do {}. <inp>, and if enabled it will also parse floats and functions as input. there are 4 functions, add (+|a), subtract (-|s), multiply (*|x|m), and devide (/|d), and p to print register 0'.format(self.prefix)]
  self.cmd['rpn'] = rpninp
  self.cmd['.'] = rpninp
  self.raw['rpn'] = rpninp

  self.rpnhist = {}
  
