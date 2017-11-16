# O(n) space: O(n)
# the brute force method is O(n^2)

nums = [1,3,2,-7,5]
holder = []
target = 3
for num in nums:
    target_holder = target - num
    if num in holder:
        print(str(holder.index(num)) + ' ' + str(nums.index(num)))
    else:
        holder.append(target_holder)
