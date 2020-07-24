class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        curMax = -1;
        for i in range(len(A) - 2):
            curMax = max(A[i], curMax);
            if curMax > A[i + 2]:
                return False;
        return True;

#这道题给了一个长度为n的数组，里面是0到n-1数字的任意排序。又定义了两种倒置方法，
#全局倒置和局部倒置。其中全局倒置说的是坐标小的值大，局部倒置说的是相邻的两个数，
#坐标小的值大。那么我们可以发现，其实局部倒置是全局倒置的一种特殊情况，即局部倒
#置一定是全局倒置，而全局倒置不一定是局部倒置，这是解这道题的关键点。题目让我们
#判断该数组的全局倒置和局部倒置的个数是否相同，那么我们想，什么情况下会不相同？
#如果所有的倒置都是局部倒置，那么由于局部倒置一定是全局倒置，则二者个数一定相等。
#如果出现某个全局倒置不是局部倒置的情况，那么二者的个数一定不会相等。所以问题的
#焦点就变成了是否能找出不是局部倒置的全局倒置。所以为了和局部倒置区别开来，我们
#不能比较相邻的两个，而是至少要隔一个来比较。
#
#我们可以从前往后遍历数组，遍历到倒数第三个数字停止，然后维护一个 [0, i] 范围内
#的最大值，每次和 A[i + 2] 比较，如果大于 A[i + 2]，说明这是个全局的倒置，并且
#不是局部倒置，那么我们直接返回false即可，参见代码如下：


#于原数组正常的顺序应该是 [0, 1, 2, 3, 4...] 这种，即数字和其下标是相同的，所以
#如果我们发现乱序数组中某个数字和其坐标差的绝对值大于1的话，那么一定是有非局部倒置
#的全局倒置的存在。猛然这么一说，可能你会问为啥啊？因为0到n-1中每个数字都是在数组
#中存在的，如果当前数字 A[i] 比起坐标 i 大1的话，比如 A[i] = 3, i = 1 的时候，那
#么数组的第二个数字是3了，前三个数字suppose是 0，1，2 的，但是由于第二个数字是3了，
#那么一定会有一个小于3的数字被挤出前三个数字，这个小于3的数字最多出现在下标为3的位
#置上，那么由于数字3出现在了下标为1的位置上，所以non-local的全局倒置就出现了。同理，
#如果当前数字 A[i] 比其坐标 i 小1的话，比如 A[i] = 1, i = 3 的时候，那么就是后 n-i 
#个数字中有一个大于 A[i] 的数字被挤到了前面去了，而且其跟 A[i] 的距离最小为2，所以n
#on-local的全局倒置就出现了，
#class Solution {
#public:
#    bool isIdealPermutation(vector<int>& A) {
#        for (int i = 0; i < A.size(); ++i) {
#            if (abs(A[i] - i) > 1) return false;
#        }
#        return true;
#    }
#};