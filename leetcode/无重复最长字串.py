# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         maxCount = 0
#         for i in range(len(s)):
#             current = [s[i]]
#             for j in range(i+1,len(s)):
#                 if s[j] not in current:
#                     current.append(s[j])
#                 else:
#                     break
#             maxCount = max(maxCount,len(current))
#         return maxCount
class Solution:
    def lengthOfLongestSubstring(self, s):
        mapSet = {}
        start, result = 0, 0
        for end in range(len(s)):
            if s[end] in mapSet:
                start = max(mapSet[s[end]], start)
            result = max(result, end - start + 1)
            mapSet[s[end]] = end + 1


#
#         return result
s = "abcdcbcbbe"

sol = Solution()

print(sol.lengthOfLongestSubstring(s))