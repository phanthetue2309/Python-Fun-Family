
import time
import sys
import os
from time import sleep
import turtle
from random import randint
from colorama import init,Fore,Back,Style

start_loading = '\n\n\n\nLoading'
loading = '.' * 159 + '\n\n'

item_one = 'x'
item_two = 'o'

items = item_one + \
    item_two

reversed_items = item_two + \
    item_one



print('\n' * 10 + ' ' * 75 + 'TRUY CẬP THÀNH CÔNG')
print('\n' + ' ' * 74 + 'Good day My Sister ')

print(start_loading)
for c in loading:
    print(c, end='')
    sys.stdout.flush()
    sleep(0.0025)

os.system('cls')
print(items * 79 + item_one + '\n' + items + ' ' * 155 + reversed_items)

localtime = time.asctime(time.localtime(time.time()))
print(items + ' ' * 66 + localtime + ' ' * 65 + reversed_items)

print(items + ' ' * 67 + 'Happy Birth\'s Day !' + ' ' * 69 + reversed_items)
print(items + ' ' * 49 + 'Wishing you a wonderful birthday filled with love joy and happiness !' + ' ' * 37 + reversed_items)

print(items + ' ' * 36 + items * 13 + 'x' + ' ' * 31 +
      items * 13 + 'x' + ' ' * 34 + reversed_items)

print(items + ' ' * 34 + items * 15 + 'x' + ' ' * 27 +
      items * 15 + 'x' + ' ' * 32 + reversed_items)

print(items + ' ' * 32 + items * 17 + 'x' + ' ' * 23 +
      items * 17 + 'x' + ' ' * 30 + reversed_items)

print(items + ' ' * 30 + items * 19 + 'x' + ' ' * 19 +
      items * 19 + 'x' + ' ' * 28 + reversed_items)

print(items + ' ' * 28 + items * 21 + 'x' + ' ' * 15 +
      items * 21 + 'x' + ' ' * 26 + reversed_items)

print(items + ' ' * 26 + items * 23 + 'x' + ' ' * 11 +
      items * 23 + 'x' + ' ' * 24 + reversed_items)

print(items + ' ' * 24 + items * 25 + 'x' + ' ' * 7 +
      items * 25 + 'x' + ' ' * 22 + reversed_items)

print(items + ' ' * 22 + items * 27 + 'x' + ' ' * 3 +
      items * 27 + 'x' + ' ' * 20 + reversed_items)

print(items + ' ' * 22 + items * 27 + 'x' + ' H ' +
      items * 27 + 'x' + ' ' * 20 + reversed_items)

print(items + ' ' * 22 + items * 27 + 'x' + ' P ' +
      items * 27 + 'x' + ' ' * 20 + reversed_items)

print(items + ' ' * 22 + items * 27 + 'x' + ' B ' +
      items * 27 + 'x' + ' ' * 20 + reversed_items)

print(items + ' ' * 22 + items * 27 + 'x' + ' D ' +
      items * 27 + 'x' + ' ' * 20 + reversed_items)

print(items + ' ' * 22 + items * 27 + 'x' + '   ' +
      items * 27 + 'x' + ' ' * 20 + reversed_items)

print(items + ' ' * 22 + items * 27 + 'x' + ' T ' +
      items * 27 + 'x' + ' ' * 20 + reversed_items)

print(items + ' ' * 22 + items * 27 + 'x' + ' U ' +
      items * 27 + 'x' + ' ' * 20 + reversed_items)

print(items + ' ' * 22 + items * 27 + 'x' + ' E ' +
      items * 27 + 'x' + ' ' * 20 + reversed_items)

print(items + ' ' * 22 + items * 27 + 'x' + ' T ' +
      items * 27 + 'x' + ' ' * 20 + reversed_items)

print(items + ' ' * 22 + items * 27 + 'x' + ' A ' +
      items * 27 + 'x' + ' ' * 20 + reversed_items)

print(items + ' ' * 22 + items * 27 + 'x' + ' M ' +
      items * 27 + 'x' + ' ' * 20 + reversed_items)

print(items + ' ' * 22 + items * 27 + 'x' + ' ' * 3 +
      items * 27 + 'x' + ' ' * 20 + reversed_items)

print(items + ' ' * 24 + items * 54 + item_one + ' ' * 22 + reversed_items)
print(items + ' ' * 26 + items * 52 + item_one + ' ' * 24 + reversed_items)
print(items + ' ' * 28 + items * 50 + item_one + ' ' * 26 + reversed_items)
print(items + ' ' * 30 + items * 48 + item_one + ' ' * 28 + reversed_items)
print(items + ' ' * 32 + items * 46 + item_one + ' ' * 30 + reversed_items)
print(items + ' ' * 34 + items * 44 + item_one + ' ' * 32 + reversed_items)
print(items + ' ' * 36 + items * 42 + item_one + ' ' * 34 + reversed_items)
print(items + ' ' * 38 + items * 40 + item_one + ' ' * 36 + reversed_items)
print(items + ' ' * 40 + items * 38 + item_one + ' ' * 38 + reversed_items)
print(items + ' ' * 42 + items * 36 + item_one + ' ' * 40 + reversed_items)
print(items + ' ' * 44 + items * 34 + item_one + ' ' * 42 + reversed_items)
print(items + ' ' * 46 + items * 32 + item_one + ' ' * 44 + reversed_items)
print(items + ' ' * 48 + items * 30 + item_one + ' ' * 46 + reversed_items)
print(items + ' ' * 50 + items * 28 + item_one + ' ' * 48 + reversed_items)
print(items + ' ' * 52 + items * 26 + item_one + ' ' * 50 + reversed_items)
print(items + ' ' * 54 + items * 24 + item_one + ' ' * 52 + reversed_items)
print(items + ' ' * 56 + items * 22 + item_one + ' ' * 54 + reversed_items)
print(items + ' ' * 58 + items * 20 + item_one + ' ' * 56 + reversed_items)
print(items + ' ' * 60 + items * 18 + item_one + ' ' * 58 + reversed_items)
print(items + ' ' * 62 + items * 16 + item_one + ' ' * 60 + reversed_items)
print(items + ' ' * 64 + items * 14 + item_one + ' ' * 62 + reversed_items)
print(items + ' ' * 66 + items * 12 + item_one + ' ' * 64 + reversed_items)
print(items + ' ' * 68 + items * 10 + item_one + ' ' * 66 + reversed_items)
print(items + ' ' * 70 + items * 8 + item_one + ' ' * 68 + reversed_items)
print(items + ' ' * 72 + items * 6 + item_one + ' ' * 70 + reversed_items)
print(items + ' ' * 74 + items * 4 + item_one + ' ' * 72 + reversed_items)
print(items + ' ' * 76 + items * 2 + item_one + ' ' * 74 + reversed_items)
print(items + ' ' * 77 + items * 1 + item_one + ' ' * 75 + reversed_items)
print(items + ' ' * 155 + reversed_items)
print(items * 79 + item_one)


a = input("Continue ? Y or N ")

init(convert=True)
for i in range(1,5):
      print('')
play = 0 
while play == 0:
      Left_Space = randint(8,80)
      Loves = 8
      for i in range(1,17):
            count = Left_Space
            while count > 0:
                  print(' ',end = '')
                  count -= 1
            count = Loves
            while count > 0:
                  if i == 1 and count == 4:
                        print('  ',end='')
                  elif i < 3 and count == 5:
                        print('  ',end='')
                  else :
                        print(Fore.RED + Style.BRIGHT +'HPBD',end='')
                  count -=1 
            if i < 5:
                  Left_Space -=  2
                  Loves += 1
            else :
                  Left_Space += 2
                  Loves -= 1
            
            time.sleep(0.3)
            print("\n",end ='')
      print("\n",end ='')
      time.sleep(0.3)
      count = randint(8,80)
      
      while count > 0:
            print(" ",end ='')
            count -= 1
      print(Fore.LIGHTRED_EX + Style.BRIGHT +'H a p p y B i r t h D a y ! ! !')
      time.sleep(0.3)
      print("\n",end ='')
      time.sleep(0.3)