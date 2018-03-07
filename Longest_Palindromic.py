class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_len = len(s)
        target_set = ([])
        target_set_2 = ([])
        search_k = 1
        search_k_2 = 0.5
        last_target = 0
        last_target_2 = 0

        if str_len == 1:
            return s

        if str_len == 2:
            if(s[0]==s[1]):
                return s
            else:
                return s[0]

        if str_len >= 3:
            for i in range(1, str_len - 1):
                if (s[i-1] == s[i+1]):
                    target_set.append(i)
                    last_target = target_set[0]
            while (len(target_set) != 0):
                search_k = search_k + 1
                target_set_fix = target_set[:]
                for j in target_set_fix:
                    if ((j - search_k >= 0) and (j + search_k <= str_len - 1)):
                        if (s[j - search_k] != s[j + search_k]):
                            target_set.remove(j)
                    else:
                        target_set.remove(j)
                if (len(target_set) != 0):
                    last_target = target_set[0]

            search_k = search_k - 1
            result_str = s[last_target - search_k:last_target+search_k+1]

        if str_len >= 3:
            i = 0.5
            while(i<=str_len - 1.5):
                if (s[int(i-0.5)] == s[int(i+0.5)]):
                    target_set_2.append(i)
                    last_target_2 = target_set_2[0]
                i = i + 1

            while (len(target_set_2) != 0):
                search_k_2 = search_k_2 + 1
                target_set_fix_2 = target_set_2[:]
                for j in target_set_fix_2:
                    if ((j - search_k_2 >= 0) and (j + search_k_2 <= str_len - 1)):
                        if (s[int(j - search_k_2)] != s[int(j + search_k_2)]):
                            target_set_2.remove(j)
                    else:
                        target_set_2.remove(j)
                if (len(target_set_2) != 0):
                    last_target_2 = target_set_2[0]

            search_k_2 = search_k_2 - 1
            result_str_2 = s[int(last_target_2-search_k_2):int(last_target_2+search_k_2+1)]

        print(search_k,search_k_2)
        if(search_k>search_k_2):
            return result_str
        else:
            return result_str_2

a = Solution()
b = a.longestPalindrome('abb')
print(b)