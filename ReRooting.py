class ReRooting:
  def ReRfunc(self, x):
    y = self.parent[x]
    return self.res[y] * self.size[x] % mod * pow(self.n - self.size[x], mod - 2, mod) % mod

  def __init__(self, n, e):
    self.n = n
    self.e = e
    self.vis = [0] * (n + 1)
    self.order = []
    self.parent = [-1] * (n + 1)
    self.ddp = [0] * (n + 1)
    self.udp = [0] * (n + 1)
    self._dfs()
    self.size = [1] * (n + 1)
    self.order.reverse()
    for x in self.order[: -1]: self.size[self.parent[x]] += self.size[x]
    self.res = [0] * (n + 1)
    #初期化の値
    self.res[1] = f.factorial(N)
    for x in range(1, N + 1): self.res[1] = self.res[1] * pow(self.size[x], mod - 2, mod) % mod

    self.order.reverse()
    for x in self.order[1: ]: self.res[x] = self.ReRfunc(x)

  def _dfs(self):
    s = [1]
    while len(s):
      x = s.pop()
      self.vis[x] = 1
      self.order.append(x)
      for y in self.e[x]:
        if self.vis[y]: continue
        s.append(y)
        self.parent[y] = x

  def Size(self, x):
    return self.size[x]

  def Query(self, x):
    return self.res[x]