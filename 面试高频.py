# 查找字符串中最长的不重复字符串的长度


class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        strArr = []
        lengthArr = []
        length = len(s)
        sArr = list(s)
        sArr.append('occupy')
        for index, characters in enumerate(sArr):
            if index == length:
                lengthArr.append(len(strArr))
            if not(characters in strArr):
                strArr.append(characters)
            else:
                lengthArr.append(len(strArr))
                strArr.append(characters)
                # 下一次从当前最后一个不重复的字符开始
                lastIndex = strArr.index(characters)
                strArr = strArr[lastIndex+1:]
        result = (lengthArr and [max(lengthArr)] or [0])[0]
        return result

# 查找元素出现在列表中的第一个位置跟最后一个 没找到返回-1 二分查找


class Solution:
    def searchRange(nums, target):
        length = len(nums)
        left, mid, right, pos, min, max = 0, math.floor(
            length/2), length-1, -1, -1, -1
        # 注意边界条件
        if(length == 0):
            return [-1, -1]
        if(length == 1):
            min = max = 0 if nums[0] == target else -1
            return [min, max]
        # 当不在范围内的时候直接返回-1
        if(nums[left] > target or nums[right] < target):
            return [-1, -1]
        while(nums[mid] != target and left <= right):
            if nums[mid] < target:
                left = mid+1
                mid = math.floor((left+right)/2)
            elif nums[mid] > target:
                right = mid-1
                mid = math.floor((left+right)/2)
        # 找不到返回-1
        pos = mid if left <= right and nums[mid] == target else -1
        min = max = pos
        if(min == max == -1):
            return[-1, -1]
        flag = flag1 = False
        while(nums[min] == target):
            if(min > 0):
                flag = True
                min -= 1
            else:
                flag = False
                break
        while(nums[max] == target and max != -1):
            if(max < length-1):
                flag1 = True
                max += 1
            else:
                flag1 = False
                break
        print(min, max)
        minPos = (not flag and [min] or [min+1])[0]
        maxPos = (not flag1 and [max] or [max-1])[0]
        return [minPos, maxPos]


class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        first = l1
        second = l2
        sum = index = 0
        while(first != None or second != None):
            num1 = num2 = 0
            if first != None:
                num1 = first.val
                first = first.next
            if second != None:
                num2 = second.val
                second = second.next
            sum += 10**index*(num1+num2)
            index += 1
        l = list(str(sum))
        l.reverse()
        l3 = []
        for i in l:
            l3.append(int(i))
        return l3

# 电话号码 字母组合


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        result = []
        zeroCount = int((nums.count(0))/3)
        i = 0
        while i < zeroCount:
            zeroArr = [0, 0, 0]
            result.append(zeroArr)
            print(result, 8)
            i += 1

        def findNegativeOrPositive(num: int, sign: int):
            return sign*num < 0
        negativeArr = list(
            filter(lambda num: findNegativeOrPositive(num, 1), nums))
        positiveArr = list(
            filter(lambda num: findNegativeOrPositive(num, -1), nums))
        # filter返回的是filter对象 没有len方法 需要list（）
        if(len(negativeArr) == 0 and zeroCount == 0):
            return []
        if nums.count(0) > 0:
            for i in nums:
                for j in negativeArr:
                    if i > 0 and i == abs(j):
                        l = [i, j, 0]
                        if not result.count(l):
                            result.append(l)
        for index, x in enumerate(negativeArr):
            for y in negativeArr[index+1:]:
                # if x == y and negativeArr.count(y) == 1:
                #     continue
                    # 注意sum的参数是一个列表或者是元组
                negativeSum = abs(sum([x, y]))
                if(positiveArr.count(negativeSum) > 0):
                    l1 = [x, y, negativeSum]
                    if not result.count(l1):
                        result.append(l1)
        for index, m in enumerate(positiveArr):
            for n in positiveArr[index+1:]:
                if m == n and positiveArr.count(m) == 1:
                    continue
                positiveSum = 0-sum([m, n])
                if(negativeArr.count(positiveSum) > 0):
                    l2 = [m, n, positiveSum]
                    if not result.count(l2):
                        result.append(l2)
        return result
