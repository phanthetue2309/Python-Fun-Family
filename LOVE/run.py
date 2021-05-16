
import sys
import os
from time import sleep


start_loading = '\n\n\n\nLoading'
loading = '.' * 159 + '\n\n'
os.system('cls')
print(start_loading)
for c in loading:
    print(c, end='')
    sys.stdout.flush()
    sleep(0.0025)

import authenticate