class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq_nums1 = Counter(nums1)
        result = []
        for num in nums2:
            if num in freq_nums1 and freq_nums1[num] > 0:
                result.append(num)
                freq_nums1[num] -= 1
        return result
