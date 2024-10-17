class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        l = 0
        r = len(words) - 1
        while(l < r):
            words[l], words[r] = words[r], words[l]

            # temp = words[l]
            # words[l] = words[r]
            # words[r] = temp

            l+=1
            r-=1
        
        return (" ").join(words)
        