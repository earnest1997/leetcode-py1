#  给定target，数组，找到组合数
class Solution:
    def combinationSum(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
        candidates.sort()
        # print(candidates)
        return self.combinationSum_helper(candidates, 0, target)

    def combinationSum_helper(self, candidates, idx, target):
        if target == 0:
            return [[]]
        cur_res = []
        for i in range(idx, len(candidates)):
            if target < candidates[i]:
                break
            nxt_res = self.combinationSum_helper(
                candidates, i, target - candidates[i])
            if nxt_res != []:
                for s in nxt_res:
                    cur_res.append(s + [candidates[i]])
        return cur_res


print(Solution().combinationSum([1, 2, 2, 3], 6))
# 找到最小的没有出现在nums中的正数


class Solution:
    def firstMissingPositive(self, nums) -> int:
        if len(nums) == 0:
            return 1
        maxNum = 1 if max(nums) < 0 else max(nums)+1
        for i in range(1, maxNum+1):
            print(i, 99)
            if(nums.count(i) == 0):
                return i
# 删除倒数第n个节点


class Solution:
    def removeNthFromEnd(self, head: 'ListNode', n: 'int') -> 'ListNode':
        def getLen(head):
            len = 0
            while(head != None):
                len += 1
                head = head.next
            return len
        length = getLen(head)
        if(length == 0 or index+1 > length):
            return None
        index = length-n
        if(index == 0 and length == 1):
            return []
    # 考虑要删除的是头节点的情况
        if(index == 0):
            head = head.next
            return head
        i = 0
        qianpu = head
        while(i <= index-1 and qianpu):
            if(i == index-1):
                removenode = qianpu.next
                if(not removenode):
                    houji = None
                    return head
                houji = removenode.next
    # 要删除的是最后一个节点的情况
                if(houji == None):
                    qianpu.next = None
                    return head
                qianpu.next = houji
            # qianpu具有对head的引用 所以返回head就好 但是不能返回qianpu 因为qianpu已经移动到后面了
                return head
            i += 1
            qianpu = qianpu.next
        return head
