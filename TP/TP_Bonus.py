import random

def generer_list_random(n):
  result = []
  for i in range(n):
    x = random.randint(1,n)
    if x not in result:
      result.append(x)
  return result

import time

# Petit test
start = time.time()
generer_list_random(100)
test_time = (time.time() - start) * 1000
print(f"Le petit test à pris {test_time:.1f} ms")

# Grand test

start = time.time()
generer_list_random(20000)
test_time = (time.time() - start) * 1000
print(f"Le petit test à pris {test_time:.1f} ms")
assert test_time < 100, "Trop long"

