class Solution:
   def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       dic={}
       for i in strs:
           l="".join(sorted(i))
           dic.setdefault(l,[]).append(i)
     
       return dic.values()
            

        

        