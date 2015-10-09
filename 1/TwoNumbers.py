#class Solution(object):
 #   def twoSum(self, nums, target):
  #      index1=0
   #     index2=0
    #    for i in xrange(len(nums)):
     #       for j in xrange(len(nums)):
      #          if nums[i]+nums[j]==target and i<j:
       #             index1=i+1
        #            index2=j+1
        #return [index1, index2]
            
# AddSum
class Solution(object):
    def twoSum(self, nums, target):
        record = {}
        for i in xrange(len(nums)):
            record[nums[i]] = i
        for i in xrange(len(nums)):
            if record.has_key(target-nums[i]) and record[target-nums[i]] > i:
                i, j = i, record[target-nums[i]]
                break

        return [i+1,j+1]
