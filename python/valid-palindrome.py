# tc: O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal = ""

        for c in s:
            if c.isalnum():
                pal += c
        pal = pal.lower()
        l, r = 0, len(pal) - 1

        while l <= r:
            if pal[l] != pal[r]:
                return False
            l += 1
            r -= 1

        return True
