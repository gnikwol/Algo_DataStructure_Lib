#unionfindを使って二辺連結成分分解する
#非連結グラフなら始点を増やした方がいいかも

uf = UnionFind(N)

s = [1]
vis = [0] * (N + 1)
parent = [0] * (N + 1)
order = []
xord = [0] * (N + 1)
while len(s):
  x = s.pop()
  if vis[x]: continue
  xord[x] = len(order)
  order.append(x)
  vis[x] = 1
  for y in e[x]:
    if vis[y]: continue
    parent[y] = x
    s.append(y)

order.reverse()
lowlink = [0] * (N + 1)
for x in order:
  lowlink[x] = xord[x]
  for y in e[x]:
    if parent[x] == y: continue
    lowlink[x] = min(lowlink[x], xord[y])
    if xord[x] < xord[y]: lowlink[x] = min(lowlink[x], lowlink[y])

for x in order:
  for y in e[x]:
    if xord[x] < xord[y] and xord[x] >= lowlink[y]: uf.Unite(x, y)

gr = [[] for _ in range(N + 1)]
for x in range(1, N + 1): gr[uf.Find_Root(x)].append(x)