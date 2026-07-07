class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for i, string in enumerate(strs):
            sortedstr = "".join(sorted(string))
            if sortedstr not in hashmap: 
                hashmap[sortedstr] = [strs[i]]
            else: 
                hashmap[sortedstr].append(strs[i])
            
        anastrs = list(hashmap.values())
        return anastrs