class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for i in strs:
            key = str(sorted(i))
            if key in hash_map.keys():
                hash_map[key].append(i)
            else:
                hash_map[key] =[i]
                        
        print(hash_map.items())
        return list(hash_map.values())