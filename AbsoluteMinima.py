import heapq
hpush = heapq.heappush
hpop = heapq.heappop
class AbsoluteMinima:
  def __init__(self):
    self.L = []
    self.R = []
    self.bias = 0
    self.res = 0
  def addall(self, x): self.bias += x
  def appendline(self, a):
    # + |x-a|
    if len(self.L) == 0 or a <= -self.L[0]:
      hpush(self.L, -a)
      self.res += -self.L[0] - a
    else:
      hpush(self.R, a)
      self.res += a + self.L[0]
    if len(self.R) > len(self.L):
      self.res -= self.R[0] + self.L[0]
      hpush(self.L, -hpop(self.R))
    elif len(self.L) - len(self.R) >= 2: hpush(self.R, -hpop(self.L))
  def minleft(self):
    # (x, f(x))
    return -self.L[0], self.res + self.bias