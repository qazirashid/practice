
#/usr/bin/env python3
def runningSum(nums):
    acc=0
    output = [0] * len(nums)
    for i in range(len(nums)):
        acc += nums[i]
        output[i] = acc
    return output


l = [2,3,8,1,9,0,8,2,7,6,3,5,4,9]

print("input:", l)
print("output:", runningSum(l))




