

from collections import defaultdict

s1 = "cool"
s2 = "oolc"

s3 = "foo"
s4 = "dfakdf"

s5 = ""
s6 = ""

# Time: O(nlogn) from the sort ->
#it is called Timsort( made with merge sort and
# insertion sort to work with many kinds of real-world data
# Space: O(n)  from the sort
if sorted(s1) == sorted(s2):
    print("True")
else:
    print("False")


# defaultdict sets a default int when creating a new entry
# Time: O(n) Faster than the sorting algorithms
# Space: O(n) same amount of space
holder1 = defaultdict(int)
holder2 = defaultdict(int)

for x in s1:
    holder1[x] += 1
for y in s2:
    holder2[y] += 1

if holder1 == holder2:
    print("True")
else:
    print("False")
       
        
