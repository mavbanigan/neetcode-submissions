class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Outline the steps to finding the solution
        1. Check which words are anagrams.
        This can be done via the "valid anagram" algorithm used in the last question.
        2. Assign each word with an anagram to a hashmap, and have its key be a list of each of its anagrams
        3. Append the word in the hashmap to the key, and add that list to the output list
        4. return the output list


        """
        mapO = {}

        for s in strs:
            key = tuple(sorted(s))
            if key not in mapO:
                mapO[key] = []
            mapO[key].append(s)
        return list(mapO.values())
            


        