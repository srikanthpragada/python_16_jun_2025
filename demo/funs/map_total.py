st = "10,20,a,30,40"

#Using filter() and map()
nums = filter(str.isdigit, st.split(","))
print(sum(map(int, nums)))

# Using list comprehension
nums_list = [int(s) for s in st.split(",") if s.isdigit()]
print(sum(nums_list))

