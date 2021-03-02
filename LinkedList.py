class LinkedList:
  def __init__(self, n, a):
    self.a = a[: ]
    self.l = [i - 1 for i in range(n)]
    self.r = [i + 1 for i in range(n)]
    self.r[-1] = -1
  def erase(self, i):
    self.a[i] = None
    li = self.l[i]
    ri = self.r[i]
    if li != -1: self.r[li] = ri
    if ri != -1: self.l[ri] = li
    self.l[i] = -1
    self.r[i] = -1
  def getleft(self, i):
    if self.l[i] == -1: return None
    return self.a[self.l[i]]
  def getright(self, i):
    if self.r[i] == -1: return None
    return self.a[self.r[i]]