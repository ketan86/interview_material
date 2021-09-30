#
# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#

# @lc code=start
class Solution:
    def canPartitionKSubsets(self, nums, k: int) -> bool:
        """
        To qualify for equal sum partition, the total sum of the array
        values should be divisible by k.
            9 % 3 == 0 : partition possible else return false

        We can process elements from left to right and put each element in
        the one partition, and until the sum of the each partition 
        exhaust the k value and then put element in next partition.

        Because we don't need return partition list, we can just use k partition
        as array of three values and use those as sum.


        nums = [1,1,3,2,2]
        0 0 0 if k == 3

        0,0,0 : 1
            - 1,0,0 :1
                - 2,0,0: 3
                    - 2,3,0:2
                        - 2,3,2: 2
                            x
                    - 2,0,3:2
                        - 2,2,3: 2
                            x
                - 1,1,0: 3
                    - 1,1,3 : 2
                        - 3,1,3: 2
                            - 3,3,3 *
        """
        sum_ = sum(nums)

        # if can't divide, we can not partition
        if sum_ % k != 0:
            return False

        target = sum_ // k

        # sort the nums 
        nums.sort()

        # if last number is greater than target, it can not be put in any
        # partition and hence return False
        if nums[-1] > target:
            return False

        partitions = [0] * k

        def search():
            if not nums:
                return True

            value = nums.pop()

            for i, curr_sum in enumerate(partitions):
                if curr_sum + value <= target:
                    partitions[i] += value
                    if search():
                        return True
                    partitions[i] -= value

            nums.append(value)

            return False

        return search()

print(Solution().canPartitionKSubsets([1,1,3,2,2], k=3))
print(Solution().canPartitionKSubsets([1,1,3,2,1], k=3))
# @lc code=end

