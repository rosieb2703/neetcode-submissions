class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for str in strs:
            sorted_str = sorted(str)
            sorted_str = ''.join(sorted_str)
            hash_map[sorted_str].append(str)
            
        return list(hash_map.values())