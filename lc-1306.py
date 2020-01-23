class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        index = set([i for i,v in enumerate(arr) if v == 0])
        s = set()
        visited = set()
        if start + arr[start] in range(len(arr)):
            s.add(start + arr[start])
            visited.add(start + arr[start])
        if start - arr[start] in range(len(arr)):
            s.add(start - arr[start])
            visited.add(start - arr[start])
        while s:
            cur = s.pop()
            if cur in index:
                return True
            if cur + arr[cur] in range(len(arr)) and cur + arr[cur] not in visited:
                s.add(cur + arr[cur])
                visited.add(cur + arr[cur])
            if cur - arr[cur] in range(len(arr)) and cur-arr[cur] not in visited:
                s.add(cur - arr[cur])
                visited.add(cur - arr[cur])
        return False
