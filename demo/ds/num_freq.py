
nums = {}
while True:
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break

    count = nums.get(num, 0)
    nums[num] = count + 1

print(nums)



