#staticな冪等性あるモノイドが乗ると思う。
#たぶんSegTreeよりはやい クエリはO(1)

import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
a = list(map(int, input().split()))

class SparseTable:
  def calc(self, x, y): return min(x, y)
  def __init__(self, n, init_val, ide_ele):
    self.n = n
    k = n.bit_length()
    self.k = k
    self.ide_ele = ide_ele
    self.log_table = [[ide_ele] * n for _ in range(k + 1)]
    for i in range(n): self.log_table[0][i] = init_val[i]
    for i in range(k):
      d = 1 << i
      for j in range(n):
        if j + d >= n: break
        self.log_table[i + 1][j] = self.calc(self.log_table[i][j], self.log_table[i][j + d])
  def query(self, l, r):
    d = r - l
    if d < 0: return self.ide_ele
    if d == 1: return self.log_table[0][l]
    m = d.bit_length() - 1
    return self.calc(self.log_table[m][l], self.log_table[m][r - (1 << m)])

st = SparseTable(N, a, 10 ** 10)
for _ in range(Q):
  l, r = map(int, input().split())
  print(st.query(l, r))