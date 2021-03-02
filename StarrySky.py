#みかんせい　ばぐってる
class StarrySky:
  def segfunc(self, x, y):
    return min(x, y)
  def __init__(self, n, ide_ele, init_val):
    self.ide_ele = ide_ele
    self.num = 2 ** (n - 1).bit_length()
    self.seg = [self.ide_ele] * 2 * self.num
    for i in range(n):
      self.seg[i + self.num - 1] = init_val[i]
    for i in range(self.num - 2, -1, -1):
      self.seg[i] = self.segfunc(self.seg[2 * i + 1], self.seg[2 * i + 2]) 
    for i in range(self.num - 2, -1, -1):
      self.seg[i] = self.segfunc(self.seg[2 * i + 1], self.seg[2 * i + 2])
      self.seg[2 * i + 1] -= self.seg[i]
      self.seg[2 * i + 2] -= self.seg[i]
  def maintain(self, i):
    if i + 1 >= self.num: return
    while True:
      mx = self.segfunc(self.seg[2 * i + 1], self.seg[2 * i + 2])
      self.seg[2 * i + 1] -= mx
      self.seg[2 * i + 2] -= mx
      self.seg[i] += mx
      if i == 0: break
      i //= 2
  def get(self, i):
    x = self.seg[0]
    k = i
    while k > 0:
      x += self.seg[k]
      k -= 1
      k //= 2
    return x
  def update(self, l, r, x):
    #[l, r) + x
    if r <= l: return
    l += self.num - 1
    r += self.num - 2
    while r - l > 1:
      if l & 1 == 0:
        self.seg[l] += x
        if l // 2 >= 0: self.maintain(l // 2)
      if r & 1 == 1:
        self.seg[r] += x
        if r // 2 >= 0: self.maintain(r // 2)
        r -= 1
      l = l // 2
      r = (r - 1) // 2
    if l == r:
      self.seg[l] += x
      if l // 2 >= 0: self.maintain(l // 2)
    else:
      self.seg[l] += x
      self.seg[r] += x
      if l // 2 >= 0: self.maintain(l // 2)
      if r // 2 >= 0: self.maintain(r // 2)
  def query(self, l, r):
    #max([l, r))
    if l >= r:
      return self.ide_ele
    l += self.num - 1
    r += self.num - 2
    res = self.ide_ele
    while r - l > 1:
      if l & 1 == 0:
        res = self.segfunc(res, self.get(l))
      if r & 1 == 1:
        res = self.segfunc(res, self.get(r))
        r -= 1
      l = l // 2
      r = (r - 1) // 2
    if l == r:
      res = self.segfunc(res, self.get(l))
    else:
      res = self.segfunc(self.segfunc(res, self.get(l)), self.get(r))
    return res
star = StarrySky(N, 10 ** 10, [0] * N)
for _ in range(Q):
  t = list(map(int, input().split()))
  if t[0] == 0:
    star.update(t[1], t[2] + 1, t[3])
  else: print(star.query(t[1], t[2] + 1))