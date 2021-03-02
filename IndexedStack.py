class IndexedStack:
  def __init__(self):
    self.pushs = []
    self.pops = []
  def push(self, x): self.pushs.append(x)
  def popright(self):
    if len(self.pushs): return self.pushs.pop()
    while len(self.pops): self.pushs.append(self.pops.pop())
    return self.pushs.pop()
  def popleft(self):
    if len(self.pops): return self.pops.pop()
    while len(self.pushs): self.pops.append(self.pushs.pop())
    return self.pops.pop()
  def at(self, k):
    if k >= len(self.pushs) + len(self.pops): return None
    if k < len(self.pushs): return self.push[k]
    return self.pops[-1 - (k - len(self.pushs))]