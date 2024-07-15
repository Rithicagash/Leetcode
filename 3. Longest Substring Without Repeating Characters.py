class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        seen = set()
        max_length = 0

        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
                max_length = max(max_length, right - left)
            else:
                seen.remove(s[left])
                left += 1

        return max_length
