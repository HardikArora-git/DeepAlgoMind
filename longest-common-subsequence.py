# Longest Common Subsequence using recursion geeks of geeks : https://www.geeksforgeeks.org/problems/longest-common-subsequence-1587115620/1
class Solution:
    def lcs(s1, s2):
        # code here
        def solve(m, n):
            if m == 0 or n == 0:
                return 0

            if s1[m - 1] == s2[n - 1]:
                return 1 + solve(m - 1, n - 1)

            return max(solve(m - 1, n), solve(m, n - 1))
        return solve(len(s1),len(s2))

s1 = 'abscewkdwef'
s2 = 'abcdewdjiwejfiw'
print(Solution.lcs(s1,s2))