class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        index_m = 0
        index_n = 0
        lenOfn = len(nums1)
        lenOfm = len(nums2)
        new_list = []
        if lenOfn == 0:
            new_list = nums2
        elif lenOfm == 0:
            new_list = nums1
        else:
            for i in range(lenOfn + lenOfm):
                if nums1[index_n] <= nums2[index_m]:
                    new_list.append(nums1[index_n])
                    index_n += 1
                    if index_n == lenOfn:
                        new_list = new_list + nums2[index_m:]
                        break
                else:
                    new_list.append(nums2[index_m])
                    index_m += 1
                    if index_m == lenOfm:
                        new_list = new_list + nums1[index_n:]
                        break
        lenOfnew = len(new_list)
        return (new_list[int(lenOfnew/2)] + new_list[int(lenOfnew/2 - 1)]) / 2 if lenOfnew % 2 == 0 else new_list[int((lenOfnew - 1)/2)]
