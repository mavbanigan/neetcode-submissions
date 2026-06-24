class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Outline the steps to finding the solution
        1. Check which words are anagrams.
         - This can be done via an algorithm using sorted strings
        2. Assign each word to a hashmap, and have its key be a list of each of its anagrams
         - If the key already exists, then the string is skipped
        3. return the output list


        """
        mapO = {}

        for s in strs:
            key = tuple(sorted(s))
            if key not in mapO:
                mapO[key] = []
            mapO[key].append(s)
        return list(mapO.values())
            


        