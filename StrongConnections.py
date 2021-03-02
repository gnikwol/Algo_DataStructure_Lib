#root = Noneだと連結でないものと見てO(N^2)のdfsをする

#非再帰, ddなし, 検証してなし
class StrongConnections:
  def __init__(self, n, e, re, root = None):
    self.n = n
    self.e = e
    self.re = re
    self.stop = [0] * (n + 1)
    self.contv = []
    self.conttable = [0] * (n + 1)
    self.vis = [0] * (n + 1)
    self.z = 0
    if root == None:
      for i in range(1, n + 1):
        if self.vis[i]: continue
        self._dfs(i)
    else:
      self._dfs(root)

    t = [(self.stop[i], i) for i in range(1, n + 1)]
    t.sort()
    self.vis = [0] * (n + 1)
    while len(t):
      _, i = t.pop()
      if self.vis[i]: continue
      self.contv.append([])
      self.contv[-1] += self._contractdfs(i)
    for i in range(len(self.contv)):
      a = self.contv[i]
      for x in a:
        self.conttable[x] = i
  def _dfs(self, x):
    self.vis[x] = 1
    s = [x]
    order = []
    while len(s):
      p = s.pop()
      order.append(p)
      for q in self.e[p]:
        if self.vis[q]: continue
        s.append(q)
        self.vis[q] = 1
    order.reverse()
    for q in order:
      self.stop[q] = self.z + 1
      self.z += 1
  def _contractdfs(self, x):
    self.vis[x] = 1
    res = []
    s = [x]
    order = []
    while len(s):
      p = s.pop()
      order.append(p)
      for q in self.re[x]:
        if self.vis[q]: continue
        s.append(q)
        self.vis[q] = 1
    order.reverse()
    for q in order: res.append(q)
    return res
  def contract(self): return self.contv
  def contractedTo(self, x): return self.conttable[x]
  def contractEdges(self):
    res = [set() for _ in range(max(self.conttable) + 1)]
    for x in range(1, N + 1):
      xx = self.contractedTo(x)
      for y in self.e[x]:
        yy = self.contractedTo(y)
        if xx != yy: res[xx].add(yy)
    return res


class StrongConnections:
  def __init__(self, n, e, re, root = None):
    self.n = n
    self.e = e
    self.re = re
    self.stop = [0] * (n + 1)
    self.contv = []
    self.conttable = [0] * (n + 1)
    self.vis = [0] * (n + 1)
    self.z = 0
    if root == None:
      for i in range(1, n + 1):
        if self.vis[i]: continue
        self._dfs(i)
    else:
      self._dfs(root)

    t = [(self.stop[i], i) for i in range(1, n + 1)]
    t.sort()
    self.vis = [0] * (n + 1)
    while len(t):
      _, i = t.pop()
      if self.vis[i]: continue
      self.contv.append([])
      self.contv[-1] += self._contractdfs(i)
    for i in range(len(self.contv)):
      a = self.contv[i]
      for x in a:
        self.conttable[x] = i

  def _dfs(self, x):
    self.vis[x] = 1
    for y in self.e[x]:
      if self.vis[y]: continue
      self._dfs(y)
    self.stop[x] = self.z + 1
    self.z += 1

  def _contractdfs(self, x):
    self.vis[x] = 1
    res = [x]
    for y in self.re[x]:
      if self.vis[y]: continue
      res += self._contractdfs(y)
    return res

  def contract(self):
    return self.contv

  def contractedTo(self, x):
    return self.conttable[x]

  def contractEdges(self):
    res = dd(set)
    for x in range(1, N + 1):
      for y in self.e[x]:
        res[self.contractedTo(x)].add(self.contractedTo(y))
    return res

sc = StrongConnections(N, e, re)
scv = sc.contract()
sce = sc.contractEdges()