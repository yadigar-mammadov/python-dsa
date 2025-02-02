from collections import defaultdict
from typing import List

class GroupAnagrams:

    def __init__(self, strings: List[str]):
        """Strings """
        self.strings = strings

    def group_anagrams_by_sorting(self) -> List[List[str]]:
        results = defaultdict(list)
        for s in self.strings:
            results[tuple(sorted(s))].append(s)
        return list(results.values())

    def group_anagrams_by_count_using_array(self)-> List[List[str]]:
        results = defaultdict(list)
        for s in self.strings:
            ords = [0] * 26
            for v in s:
                ords[ord(v) - ord('a')] += 1
            results[tuple(ords)].append(s)
        return list(results.values())

    def group_anagrams_by_count_using_dictionary(self)-> List[List[str]]:
        results = defaultdict(list)
        for s in self.strings:
            d = {}
            for v in s:
                d[v] = d.get(v, 0) + 1
            results[frozenset(d.items())].append(s)
        return list(results.values())



