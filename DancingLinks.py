#２次元平面で、x方向とy方向別々に連結を管理する連結リスト
#(a, b), (c, d)がx方向につながっているなら uf.isSameGroup(dn.findx(a, b), dn.findx(c, d))はTrueとなる
#存在しない点はfindで0を返す。
#DanceUniteは新たに追加する点に使う。上下左右に正しくUniteしてくれる。

class DancingNodes:
  def __init__(self, n):
    self.n = n
    self.p = 1
    self.table = dict()
  def add(self, x, y):
    self.table[y * self.n + x] = self.p
    self.p += 2
  def findx(self, x, y):
    if y * self.n + x in self.table: return self.table[y * self.n + x]
    else: return 0
  def findy(self, x, y):
    if y * self.n + x in self.table: return self.table[y * self.n + x] + 1
    else: return 0

dn = DancingNodes(len(S) + 1)
dn.add(0, 0)

def DanceUnite(u, v):
  global dn
  global uf
  px = dn.findx(u, v)
  py = dn.findy(u, v)
  q = dn.findy(u, v + 1)
  if q: uf.Unite(py, q)
  q = dn.findy(u, v - 1)
  if q: uf.Unite(py, q)
  q = dn.findx(u + 1, v)
  if q: uf.Unite(px, q)
  q = dn.findx(u - 1, v)
  if q: uf.Unite(px, q)