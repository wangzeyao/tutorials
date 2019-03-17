# class Solution:
#     def longestPalindrome(self, s):
#      maxstr = s[0] if len(s) > 0 else ''
#      curstr = ''
#      for i in range(len(s)):
#          curstr= s[i]
#          for l in range(i+1,len(s)):
#              curstr = curstr + s[l]
#              if curstr[0] == curstr[len(curstr)-1] and len(curstr)>1:
#                  j = 0
#                  k = len(curstr) - 1
#                  if len(curstr) % 2 != 0:
#                      while j != k:
#                          if curstr[j] != curstr[k]:
#                              break
#                          else:
#                              j += 1
#                              k -= 1
#                      if j == k:
#                          maxstr = curstr if len(maxstr) < len(curstr) else maxstr
#                  else:
#                      left = curstr[:int(len(curstr)/2)]
#                      right = curstr[int(len(curstr)/2):]
#                      right = right[::-1]
#                      if left == right:
#                          maxstr = curstr if len(maxstr) < len(curstr) else maxstr
#      return maxstr


class Solution:
    def subpalidromenlen(self,str,i):
        curStr = []
        curStr.append(str[i])
        k = 1
        while i+k < len(str) and i-k >= 0:
            if str[i-k] == str[i+k]:
             curStr.insert(0,str[i-k])
             curStr.append(str[i+k])
             k += 1
            else:
                break
        return curStr

    def longestPalindrome(self, s):
        if len(s) == 0:
            return ''
        strlist = []
        for i in range(len(s)):
            strlist.append('#')
            strlist.append(s[i])
        strlist.append('#')
        maxStr = []
        for i in range(len(strlist)):
            curStr = self.subpalidromenlen(strlist,i)
            maxStr = curStr if len(curStr)>len(maxStr) else maxStr
        while '#' in maxStr:
            maxStr.remove('#')
        return ''.join(maxStr)

sol = Solution()
a = 'a'
print(sol.longestPalindrome(a))