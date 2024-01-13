def twoSum(nums, target):
        hashmap = {}
        for i in range(len(nums)): #use hashmap search O(1)
            complement = target - nums[i] # check for the difference value 
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
output = twoSum([2,3,4,1], 4)
print(output)