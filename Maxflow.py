from collections import deque
class Dinic:
  def __init__(self, n):
    self.n = n
    self.links = [[] for _ in range(n)]
    
  def add_edge(self, from_, to, capacity):
    self.links[from_].append([capacity, to, len(self.links[to])])
    self.links[to].append([0, from_, len(self.links[from_]) - 1])
 
  def bfs(self, s):
    depth = [-1] * self.n
    depth[s] = 0
    q = deque([s])
    while q:
      v = q.popleft()
      for cap, to, rev in self.links[v]:
        if cap > 0 and depth[to] < 0:
          depth[to] = depth[v] + 1
          q.append(to)
    return depth
 
  def dfs(self, s, t, depth, progress, link_counts):
    links = self.links
    stack = [s]
 
    while stack:
      v = stack[-1]
      if v == t:
        break
      for i in range(progress[v], link_counts[v]):
        progress[v] = i
        cap, to, rev = links[v][i]
        if cap == 0 or depth[v] >= depth[to] or progress[to] >= link_counts[to]:
          continue
        stack.append(to)
        break
      else:
        progress[v] += 1
        stack.pop()
    else:
      return 0
 
    f = 1 << 60
    fwd_links = []
    bwd_links = []
    for v in stack[:-1]:
      cap, to, rev = link = links[v][progress[v]]
      f = min(f, cap)
      fwd_links.append(link)
      bwd_links.append(links[to][rev])
 
    for link in fwd_links:
      link[0] -= f
 
    for link in bwd_links:
      link[0] += f
 
    return f
 
  def max_flow(self, s, t):
    link_counts = list(map(len, self.links))
    flow = 0
    while True:
      depth = self.bfs(s)
      if depth[t] < 0:
        break
      progress = [0] * self.n
      current_flow = self.dfs(s, t, depth, progress, link_counts)
      while current_flow > 0:
        flow += current_flow
        current_flow = self.dfs(s, t, depth, progress, link_counts)
    return flow




class BipartiteMatching:
  def __init__(self, n, m):
    self._n = n
    self._m = m
    self._to = [[] for _ in range(n)]

  def add_edge(self, a, b):
    self._to[a].append(b)

  def solve(self):
    n, m, to = self._n, self._m, self._to
    pre = [-1] * n
    root = [-1] * n
    p = [-1] * n
    q = [-1] * m
    upd = True
    while upd:
      upd = False
      s = []
      s_front = 0
      for i in range(n):
        if p[i] == -1:
          root[i] = i
          s.append(i)
      while s_front < len(s):
        v = s[s_front]
        s_front += 1
        if p[root[v]] != -1: continue
        for u in to[v]:
          if q[u] == -1:
            while u != -1:
              q[u] = v
              p[v], u = u, p[v]
              v = pre[v]
            upd = True
            break
          u = q[u]
          if pre[u] != -1: continue
          pre[u] = v
          root[u] = root[v]
          s.append(u)
      if upd:
        for i in range(n):
          pre[i] = -1
          root[i] = -1
    return [(v, p[v]) for v in range(n) if p[v] != -1]

class maxflow_with_limit:
  def __init__(self, n):
    self.n = n + 2
    self.sml = 0
    self.S = n
    self.T = n + 1
  def gen_add_edge(self, u, v, l, r):
    self.sml += l
    if r - l - 1 > 0: yield (u, v, r - l - 1)
    if l:
      yield (self.S, v, l)
      yield (u, self.T, l)
  def gen_flow(self, s, t):
    yield (self.S, self.T)
    yield (s, self.T)
    yield (self.S, t)
    yield (s, t)
  def calc_flow(self, a, b, c, d):
    if a + c == a + b == self.sml: return b + d
    return -1