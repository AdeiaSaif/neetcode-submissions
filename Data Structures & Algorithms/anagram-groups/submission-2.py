class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out=[]
        dic={}
        for i in strs:
            key=''.join(sorted(list(i)))
            if key in dic.keys():
                dic[key].extend([i])
            else:
                dic[key]=[i]
        return list(dic.values())