# 二乗の木 dp の補助クラス

class tree_sq_dp:
  def __init__(self, n):
    self.n = n
    self.table = [1] * n
  def gen(self, x, y):
    for i in range(self.table[x] - 1, -1, -1):
      for j in range(self.table[y] - 1, -1, -1): yield (i, j)
    self.table[x] += self.table[y] - 1