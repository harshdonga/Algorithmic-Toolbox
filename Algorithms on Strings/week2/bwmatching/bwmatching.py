# python3
import sys

def InverseBWT(bwt):
    front = {'A': {}, 'C': {}, 'T': {}, 'G': {}}
    back = {'A': {}, 'C': {}, 'T': {}, 'G': {}}
    bwt_sorted = sorted(bwt)

    count = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
    for idx, letter in enumerate(bwt):
        if letter == '$':
            continue
        front[letter][idx] = count[letter]
        count[letter] += 1

    count = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
    for idx, letter in enumerate(bwt_sorted):
        if letter == '$':
            continue
        back[letter][count[letter]] = idx
        count[letter] += 1

    i = 0
    output = [""] * (len(bwt)+1)
    output[-1] = '$'
    count = 2
    while bwt[i] != '$':
        letter = bwt[i]
        output[~count] = letter

        c = front[letter][i]
        i = back[letter][c]
        count += 1

    return ''.join(output)

def counter(pattern, text):
  count = 0
  pattlen = len(pattern)
  textlen = len(text)
  inital = pattern[0]
  ilist = [x for x in range(textlen) if text[x] == inital]
  for j in ilist:
    if j + pattlen <= textlen:
      if pattern == text[j:j+pattlen]:
        count += 1
  return count

if __name__ == '__main__':
  bwt = input().strip()
  pattern_count = int(input().strip())
  patterns = input().strip().split()
  text = InverseBWT(bwt)
  out = []
  for i in patterns:
    out.append(counter(i,text))
  print(*out)