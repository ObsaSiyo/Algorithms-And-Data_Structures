s1 = "abcd"
s2 = "abcde"

s3 = "aaabbcdd"
s4 = "abdbacade"

# find the unique characters in the string and put them in to a array
# O(n + m)
holder = []

for x in s3:
    if x not in holder:
        holder.append(x)

for y in s4:
    if y not in holder:
        print(y)
