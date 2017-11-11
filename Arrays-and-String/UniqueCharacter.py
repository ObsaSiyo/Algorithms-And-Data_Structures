
string1 = "foo"
string2 = "bar"
string3 = "'"

hashTable1 = []

for x in string3:
    if x in hashTable1:
        print("False")
    else:
        hashTable1.append(x)
print("True")
