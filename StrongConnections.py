#root = Noneだと連結でないものと見てO(N^2)のdfsをする

#とぽそつき
class StrongConnection:
  def __init__(self, N):
    self.N = N + 1
    self.edges = []
  def csr(self):
    start = [0] * (self.N + 1)
    elist = [0] * len(self.edges)
    for e in self.edges:
      start[e[0] + 1] += 1
    for i in range(1, self.N + 1):
      start[i] += start[i - 1]
    counter = start[:]
    for e in self.edges:
      elist[counter[e[0]]] = e[1]
      counter[e[0]] += 1
    self.start = start
    self.elist = elist
  def add_edge(self, v, w): self.edges.append((v, w))
  def scc_ids(self):
    self.csr()
    N = self.N
    now_ord = group_num = 0
    visited = []
    low = [0] * N
    order = [-1] * N
    ids = [0] * N
    parent = [-1] * N
    stack = []
    for i in range(N):
      if order[i] == -1:
        stack.append(~i)
        stack.append(i)
        while stack:
          v = stack.pop()
          if v >= 0:
            if order[v] == -1:
              low[v] = order[v] = now_ord
              now_ord += 1
              visited.append(v)
              for i in range(self.start[v], self.start[v + 1]):
                to = self.elist[i]
                if order[to] == -1:
                  stack.append(~to)
                  stack.append(to)
                  parent[to] = v
                else:
                  low[v] = min(low[v], order[to])
          else:
            v = ~v
            if low[v] == order[v]:
              while True:
                u = visited.pop()
                order[u] = N
                ids[u] = group_num
                if u == v:
                  break
              group_num += 1
            if parent[v] != -1:
              low[parent[v]] = min(low[parent[v]], low[v])
    for i, x in enumerate(ids):
      ids[i] = group_num - 1 - x
    return group_num, ids
  def groups(self):
    group_num, ids = self.scc_ids()
    groups = [[] for _ in range(group_num)]
    for i, x in enumerate(ids):
      groups[x].append(i)
    return groups

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