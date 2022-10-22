for a in range(2):
  for b in range(2):
    for c in range(2):
      if ((not(a and not(b)) or c) == a) == 0:
        print(a, b, c)
