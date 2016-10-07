import random 
import os 
import sys
import time 


def sleep_convert(swap_time):
   if swap_time[-1] == 'm':
      time_r = int(swap_time[:-1]) 
      real = 0 
      for it in range(1,time_r):
         real += 60 
      return real 
   elif swap_time[-1] == 'h':
      time_r = int(swap_time[:-1])
      real = 0
      for it in range(1,time_r):
         real += (60 * 60)
      return real
   elif swap_time[-1] == 'd':
      time_r = int(swap_time[:-1])
      real = 0
      for it in range(1,time_r):
         real += ((24 * 60) * 60)
      return real

   else:
      print('you fucked up: your swap time needs to be formatted like 30m, 5h, or 8d')
      sys.exit()
	



if len(sys.argv) < 2:
   print("yokyu_wheel.py path/to/resolvers.csv [resolver_swap_out_time(10m,3h,2d)]")
   sys.exit() 

swap = sleep_convert('8h') 

if len(sys.argv) == 3:
   swap = sleep_convert(sys.argv[2])
   
try:
   resolver = open(sys.argv[1]).readlines() 
except Exception as e:
   print('CANNOT LOAD RESOLVER:{0}\n\nBAILING'.format(e))
   sys.exit() 

resolver.pop(0)

wheel = [x.split(',')[0] for x in resolver] 


while True: 
   os.system('pkill dnscrypt-proxy') 
   os.system('service named stop') 
   random.seed() 
   sel = wheel[random.randint(0,len(wheel))]
   os.system('dnscrypt-proxy -d -R {0} -l /root/dnslog'.format(sel))
   time.sleep(swap)  
