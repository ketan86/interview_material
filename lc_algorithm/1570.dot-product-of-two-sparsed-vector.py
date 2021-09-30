"""
1570. Dot Product of Two Sparse Vectors
Medium

325

48

Add to List

Share
Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values, you should store the
sparse vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?

Example 1:

Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
Output: 8
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
Example 2:

Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
Output: 0
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0
Example 3:

Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
Output: 6
 

Constraints:

n == nums1.length == nums2.length
1 <= n <= 10^5
0 <= nums1[i], nums2[i] <= 100
Accepted
54,739
Submissions
60,199
Seen this question in a real interview before?

"""


class SparseVector:
    def __init__(self, nums):
        """Runtime: 2484 ms, faster than 10.73%

        Naive -> Store nums and calculate dot product by zipping elements and
        going through all the elements.

        Let N be the length of the input array 
        Time -> O(N) for both construction and dot product
        Space -> O(1) for both

        """
        self.non_zeros = {}
        # store non zero values by index
        for index, n in enumerate(nums):
            if n != 0:
                self.non_zeros[index] = n

    # Return the dotProduct of two sparse vectors

    def dotProduct(self, vec: 'SparseVector') -> int:
        """
        Store the non-zero values and their corresponding indices in a
        dictionary, with the index being the key. Any index that is not
        present corresponds to a value 0 in the input array.

        Let N be the length of the input array and L be the number of
        non-zero elements.

        Time -> O(N) for hashmap and O(L) for dot product
        Space -> O(L) for hashmap and O(1) for dot product

        """
        result = 0

        for index, n in vec.non_zeros.items():
            if index in self.non_zeros:
                result += n * self.non_zeros[index]
        return result

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
