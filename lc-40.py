class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        ans = []
        def sequence(i, arr, ans):
            for j in range(i+1,len(candidates)):
                if sum(arr) + candidates[j] < target:
                    sequence(j, arr+[candidates[j]], ans)
                elif sum(arr) + candidates[j] == target:
                    temp = [arr + [candidates[j]]]
                    if not temp[0] in ans:
                        ans += temp
                else:
                    break
        for i in range(len(candidates)):
            if candidates[i] < target:
                sequence(i, [candidates[i]], ans)
            elif candidates[i] == target:
                if [candidates[i]] not in ans:
                    ans += [[candidates[i]]]
        return ans
