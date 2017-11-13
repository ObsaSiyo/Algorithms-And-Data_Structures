# O(n) using a hashtable
from collections import defaultdict

s1 = "AABBCC"
s2 = "AAABCCDDDD"

holder = defaultdict(int)
total = ""

for x in s2:
    holder[x] += 1

for y in holder:
    total.append( y + str(holder[y]))
    
print(total)
    
    
