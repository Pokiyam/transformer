import math
import matplotlib.pyplot as plt

n = 4  # the number of words
dim = 9  # the dimension of the word embedding

def get_angles(pos, i, dim):
  angles = 1 / math.pow(10000, 2 * (i // 2) / dim)
  return pos * angles

def get_positional_encoding(pos, i, dim):
  if i % 2 == 0:  # apply only to even indices
    return math.sin(get_angles(pos, i, dim))
  # apply only to odd indices
  return math.cos(get_angles(pos, i, dim))

result = [ㅔㅈㅇ[0] * dim for _ in range(n)]

for i in range(n):
  for j in range(dim):
    result[i][j] = get_positional_encoding(i, j, dim)