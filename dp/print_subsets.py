Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        combo = [[None]*(target+1) for i in range(n+1)]
        
        
        for i in range(n+1):
            for j in range(target+1):
                if i==0 and j==0:
                    combo[i][j] =True
                elif i==0:
                    combo[i][j] = False
                elif j==0:
                    combo[i][j] = True
                elif candidates[i-1] <= j:
                    combo[i][j] = combo[i-1][j] or combo[i-1][j-candidates[i-1]]
                else:
                    combo[i][j] = combo[i-1][j]
        l=[]
        if not combo[n][target]:
            return l
        f =[]
        self.print_subset(combo, target, candidates, n, l,f)
        return self.remove_duplicates(f)
    
    def remove_duplicates(self,k):
        new_k = []
        for elem in k:
            elem.sort()
            if elem not in new_k:
                new_k.append(elem)
        return new_k
    def print_subset(self, combo, target, candidates, n, l,f):
        # print(l)
        if n==0:
            if target!=0:
                l.append(candidates[n])
            f.append(l)
            return l
        # True by not considering the value
        if combo[n-1][target]:
            # print(candidates[n-1])
            b = []
            b.extend(l)
            self.print_subset(combo,target,candidates,n-1,b,f)
        if target>= candidates[n-1] and combo[n-1][target-candidates[n-1]]:
            # considering the current element
            l.append(candidates[n-1])
            self.print_subset(combo,target-candidates[n-1],candidates,n-1,l,f)
