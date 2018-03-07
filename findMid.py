class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i = 0
        j = 0
        m = float(len(nums1))
        n = float(len(nums2))
        mid = int((m + n + 1) / 2 )
        j_o = (m + n) % 2

        if (m < n):
            temp = nums1
            nums1 = nums2
            nums2 = temp
            temp_num = n
            n = m
            m = temp_num

        i = mid
        j = 0
        print(mid,m,n)
        del_j = float(n)
        k = 0
        while (del_j > 1):
            k = k + 1
            del_j = int(n/pow(2,k) + 0.5)

            print("del_j!!!",del_j)
            if (nums1[i - del_j] > nums2[j + del_j - 1]):
                i = i - del_j
                j = j + del_j - 1
                print("xiao")

            print(i, j)

        if (j_o == 1):
            if nums1[i-1] > nums2[j]:
                return nums2[j]
            else:
                return nums1[i-1]
        else:
            print(i, j)
            if(j!=0):
                return (nums1[i] + nums2[j]) / 2
            else:
                return float(nums1[i] + nums1[i-1]) / 2
a = Solution()
b = a.findMedianSortedArrays([1,1,2],[6,7,8,9,10,11])
print(b)