#using prefix sum
def average_difference(nums, numsSize):
    return_index = 0
    left = 0
    right = sum(nums)
    min_value = float('inf')

    for i in range(numsSize):
        left += nums[i]
        right -= nums[i]

        left_average = left//(i + 1)
        
        if i + 1 == numsSize:
            right_average = 0
        else:
            right_average = right//(numsSize - (i + 1))
        
        result = abs(left_average - right_average)

        if result < min_value:
            min_value = result
            return_index = i

    return return_index

n = int(input())

for i in range(n):
    nums = list(map(int, input().split(" ")))
    numsSize = nums.pop(0)
    index = average_difference(nums, numsSize)
    print(index)