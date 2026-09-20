class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[-1] = 1

        for i in range(1, n):
            pref[i] = pref[i - 1] * nums[i - 1]
        for i in range(n - 2, -1 , -1):
            suff[i] = suff[i + 1] * nums[i + 1]
        for i in range(n):
            res[i] = suff[i] * pref[i]

        return res

"""
- set n to be len of list
- create res, pref and suff lists preset with 0
- create loops for pref and suff
final loop to take sum of pref and suff
"""