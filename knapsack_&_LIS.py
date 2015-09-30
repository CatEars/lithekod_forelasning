# Fungerar bara med python3
from functools import lru_cache

def solve_knapsack(C):
   # Löser problemet 'knapsack'
   vikter = list()
   värden = list()
   # Läs in värden och vikter	
   
   @lru_cache(None)
   def knapsack(i, w):
      if w < 0: return -float('inf')		
      elif i < 0 or w == 0: return 0
      else: return max(knapsack(i - 1, w), 
                 knapsack(i - 1, w-vikter[i]) + värden[i])

   return knapsack(len(värden)-1, C)


def solve_LIS():
   # Löser problemet 'longincsubseq'
   värde = list()
   NUM = list()
   # läs in värden och vikter

   NUM[0] = värde[0]

   @lru_cache(None)
   def LIS(i):
      if i == 0: return 1
      bästa = 0
      for x in range(i):
         if LIS(x) > bästa:
            bästa = LIS(x)
            num = NUM[x]
         if NUM[x] < värde[i] and LIS(x) + 1 > bästa:
            bästa = LIS(x) + 1
            num = värde[i]
      NUM[i] = num
      return bästa

   return LIS(len(värde)-1)

if __name__ == "__main__":
   print(solve_LIS())
