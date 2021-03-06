class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        ans = 0;
        prefix = 0;
        count = [0] * K;
        count[0] = 1
        for num in A:
            prefix = (prefix + num) % K;
            count[prefix] += 1;
            ans += count[prefix] - 1;
        return ans;


#let c[i] denotes the counts of prefix_sum % K init: c[0] = 1
#Whenever we end up with the same prefix sum (after modulo), which means there are 
#subarrys end with current element that is divisible by K (0 modulo).
#
#e.g. A = [4,5,0,-2,-3,1], K = 5
#[4,5] has prefix sum of 4, which happens at index 0 [4], and index 1, [4,5]
#[4,5,0] also has a prefix sum of 4, which means [4, {5,0}], [4,5, {0}] are divisible 
#by K.
#
#ans += (c[prefix_sum] – 1)
#i = 0, prefix_sum = 0, c[(0+4)%5] = c[4] = 1, ans = 0
#i = 1, prefix_sum = 4+5, c[(4+5)%5] = c[4] = 2, ans = 0+2-1=0 => [5]
#i = 2, prefix_sum = 4+0, c[(4+0)%5] = c[4] = 3, ans = 1+3-1=3 => [5], [5,0], [0]
#i = 3, prefix_sum = 4-2, c[(4-2)%5] = c[2] = 1, ans = 3
#i = 4, prefix_sum = 2-3, c[(2-3+5)%5] = c[4] = 4, ans = 3+4-1=6 => [5],[5,0],[0],
#[5,0,-2,-3], [0,-2,-3],[-2,-3]
#i = 5, prefix_sum = 4+1, c[(4+1)%5] = c[0] = 2, ans = 6 + 2 – 1 =>
#[5],[5,0],[0],[5,0,-2,-3], [0,-2,-3],[-2,-3], [4,5,0,-2,-3,1]