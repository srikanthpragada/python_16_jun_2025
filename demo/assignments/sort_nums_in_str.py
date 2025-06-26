st = "10 9 300 13 45 5"

nums = st.split(" ")
print(nums)

numbers = [int(n) for n in nums]

print(sorted(numbers))