nums = list(
    map(int, str(
        input()
        ).split()
    )
)
for x in range(len(nums) / 2):
    for i in range(len(nums)):
        try:
            if nums[i] > nums[i + 1]:
                nums[i] = nums[i] ^ nums[i + 1]
                nums[i + 1] = nums[i] ^ nums[i + 1]
                nums[i] = nums[i] ^ nums[i + 1]
        except IndexError:
            pass
print(nums)