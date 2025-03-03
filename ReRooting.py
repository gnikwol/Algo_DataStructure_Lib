# elemは単位元
# opup はボトムアップdfsの集計 x→p
# opdown はトップダウンの集計 p→x ただし、pvalにはすでにp側の集計結果が入っている
# merge dpのマージ
class ReRooting:
  def elem(self): return 1

  def opup(self, p, x):
    return (self.udp[x] + 1) % P

  def opdown(self, pval, xval):
    return (pval + 1) % P

  def merge(self, xval, yval):
    return xval * yval % P

  def __init__(self, n, e):
    self.n = n
    self.e = e
    self.vis = [0] * (n + 1)
    self.order = []
    self.parent = [-1] * (n + 1)
    self.ddp = [self.elem()] * (n + 1)
    self.udp = [self.elem()] * (n + 1)
    self._dfs()
    self.size = [1] * (n + 1)
    self.order.reverse()
    for x in self.order[: -1]: self.size[self.parent[x]] += self.size[x]
    self.res = [self.elem()] * (n + 1)
    

    for x in self.order:
      for y in e[x]:
        if self.parent[x] == y: continue
        self.udp[x] = self.merge(self.udp[x], self.opup(x, y))

    self.order.reverse()
    for x in self.order:
      edp = [self.elem()]
      for y in e[x]:
        if self.parent[x] == y:
          edp.append(edp[-1])
          continue
        edp.append(self.merge(edp[-1], self.opup(x, y)))

      edprev = [self.elem()]
      for y in e[x][: : -1]:
        if self.parent[x] == y:
          edprev.append(edprev[-1])
          continue
        edprev.append(self.merge(edprev[-1], self.opup(x, y)))


      for i in range(len(e[x])):
        y = e[x][i]
        if self.parent[x] == y: continue
        xval = self.merge(edp[i], edprev[len(e[x]) - i - 1])
        xval = self.merge(self.ddp[x], xval)
        self.ddp[y] = self.opdown(xval, self.ddp[y])

    for x in self.order: self.res[x] = self.merge(self.ddp[x], self.udp[x])


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