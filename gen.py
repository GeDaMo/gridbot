def f():
  for i in range(0, 256):
    n = ((i & 128) == 128) + ((i & 64) == 64) + ((i & 1) == 1)
    e = ((i & 64) == 64) + ((i & 32) == 32) + ((i & 16) == 16)
    w = ((i & 2) == 2) + ((i & 4) == 4) + ((i & 1) == 1)
    s = ((i & 16) == 16) + ((i & 4) == 4) + ((i & 8) == 8)
    c = n
    d = "@NORTH"
    if e > c:
      c = e
      d = "@EAST"
    if w > c:
      c = w
      d = "@WEST"
    if s > c:
      c = s
      d = "@SOUTH"
    #print "  movetable[%d] = %s;" % (i, d)
    print "  PUSH " + d

f()
