class Trie:
  def __init__(self, alphabets = 26):
    self.d = alphabets
    self.e = [[-1] * alphabets]
    self.n = 0
    self.parent = [-1]
    self.c = [0]

  def add(self, s):
    x = 0
    for c in s:
      if self.e[x][c] == -1:
        self.n += 1
        self.e[x][c] = self.n
        self.parent.append(x)
        self.e.append([-1] * self.d)
        self.c.append(0)
      x = self.e[x][c]
    self.c[x] += 1

  def query(self, s):
    x = 0
    for c in s:
      for i in range(self.alphabets):
        if self.e[z][i] != -1: pass
        x = self.e[x][c]
    return