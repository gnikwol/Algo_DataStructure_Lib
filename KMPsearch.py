class KmpSearch:
  def __init__(self, word):
    self.word = word
    self.table = [0] * (len(word) + 1)
    self.table[0] = -1
    i, j = 0, 1
    while j < len(self.word):
      matched = self.word[i] == self.word[j]
      if not matched and i > 0:
        i = self.table[i]
      else:
        if matched:
          i += 1
        j += 1
        self.table[j] = i
  def search(self, text):
    table = self.table
    word = self.word
    i, p = 0, 0
    res = []
    while i < len(text):
      if text[i] == word[p]:
        i += 1
        p += 1
      elif p == 0:
        i += 1
      else:
        p = table[p]
      if p == len(word):
        res.append(i - p)
        p = table[p]
    return res
  def period(self, i): return i + 1 - self.table[i + 1]