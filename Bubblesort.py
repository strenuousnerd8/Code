nums = list(
    map(int, str(
        input()
        ).split()
    )
)
for j in range(len(nums)):
    for i in range(len(nums)):
        try:
            if nums[i] > nums[i + 1]:
                nums[i] = nums[i] ^ nums[i + 1]
                nums[i + 1] = nums[i] ^ nums[i + 1]
                nums[i] = nums[i] ^ nums[i + 1]
        except IndexError:
            pass
print(nums)