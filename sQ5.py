nums = [4, 3, 1, 2]
mid = len(nums) // 2

first_half = sum(nums[:mid])
second_half = sum(nums[mid:])

if first_half > second_half:
    print("First half greater")
elif first_half == second_half:
    print("Equal halves")
else:
    print("Second half greater")
