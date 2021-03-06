#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt

################################ HELP
def help():
  print 'Usage:', sys.argv[0], '[input_file]'
  print '''\
    Draw curves for series of 2D coordinates like:
    x00 y00 x01 y01 ...
    x10 y10 x11 y11 ...
    Curve from the same line will be in the same color.

    <input_file>    File that contains lines of numbers. STDIN will be used if
                    not specified.'''
  exit()

if len(sys.argv) == 2 and (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
  help()

################################ PROCESS
Base = int(sys.argv[1])
series_no = 1
for line in sys.stdin:
  numbers = [float(num) for num in line.split()]
  count = len(numbers)
  x = [numbers[i] for i in range(0, count, 2)]
  y = [numbers[i] for i in range(1, count, 2)]
  series_label = 'Series %d, from(%.2f, %.2f) to (%.2f, %.2f)' % (series_no, x[0], y[0], x[-1], y[-1])
  series_no += 1
  plt.semilogx(x, y, label = series_label, basex = Base)

plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.grid(True)
plt.legend(loc = 'lower right')
plt.show()

