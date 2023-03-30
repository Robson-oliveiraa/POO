import sys
import time
def text(text):
  for i in list(text):
    print(i, end='')
    sys.stdout.flush()
    time.sleep(0.025)
  time.sleep(1.2)
  print(end = '\n') 